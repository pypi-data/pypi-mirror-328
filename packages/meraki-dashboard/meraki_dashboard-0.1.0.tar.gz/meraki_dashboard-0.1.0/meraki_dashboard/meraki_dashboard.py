import requests, ast, sqlite3, dataclasses
from copy import deepcopy
from pathlib import Path
from urllib.parse import urlparse
from collections import namedtuple
from html.parser import HTMLParser

python_to_sqlite = {
    type(False): "INT",
    type(""): "TEXT",
    type(1): "INT",
    type(1.0): "REAL",
    type(b""): "BLOB",
    type(None): "TEXT",
}


@dataclasses.dataclass(eq=True, frozen=True)
class Organization:
    id: str = ""
    eid: str = ""
    uid: str = ""
    org_admin_type: str = ""
    name: str = ""
    num_networks: int = 0
    num_visible_networks: int = 0
    shard_id: int = 0
    licensed_product_edition_name: str = ""
    license_expires_on: int = 0
    block_meraki_admins: bool = False
    licensing_mode: int = 0
    is_demo: bool = False


@dataclasses.dataclass(eq=True, frozen=True)
class Locale:
    id: str = ""
    name: str = ""
    org_id: str = ""
    shard_id: int = 0
    is_config_template: bool = False
    cellular_gateway: str = ""
    switch: str = ""
    wired: str = ""
    wireless: str = ""
    tag: str = ""
    is_template_child: bool = False


@dataclasses.dataclass(eq=True, frozen=True)
class Node_group:
    id: str = ""
    n: str = ""
    t: str = ""
    eid: str = ""
    org_id: str = ""
    shard_id: int = 0
    locale_id: str = ""
    config_template_ng_id: str = ""
    network_type: str = ""
    network_tags: str = ""
    time_zone: str = ""
    node_group_mtime: int = 0
    node_group_ctime: int = 0
    can_read: bool = False
    can_write: bool = False
    has_wireless: bool = False
    has_wired: bool = False
    has_vm_concentrator: bool = False
    has_pcc: bool = False
    has_switch: bool = False
    has_phone: bool = False
    is_virtual: bool = False
    is_config_template: bool = False
    has_sensor: bool = False
    has_cellular_gateway: bool = False
    is_template_child: bool = False


### known issue: locales does not contain a column for MT or phone type devices as I don't have an example to get the right key name
db_schemas = {
    "organizations": tuple([key for key in Organization.__dataclass_fields__.keys()]),
    "node_groups": tuple([key for key in Node_group.__dataclass_fields__.keys()]),
    "locales": tuple([key for key in Locale.__dataclass_fields__.keys()]),
}

db_tuples = {
    "organizations": Organization,
    "node_groups": Node_group,
    "locales": Locale,
}


def organizations_factory(cursor, row):
    return db_tuples["organizations"](row)


def locales_factory(cursor, row):
    return db_tuples["locales"](row)


def node_groups_factory(cursor, row):
    return db_tuples["node_groups"](row)


db_factories = {
    "organizations": organizations_factory,
    "node_groups": node_groups_factory,
    "locales": locales_factory,
}


def find_value(content: str, seek_string: str):
    value_start = content.find(seek_string) + len(seek_string)
    value_end = content.find(";", value_start)
    return content[value_start:value_end]


class MerakiOverviewParser(HTMLParser):
    def __init__(self, *, convert_charrefs=True):
        self.authenticity_token = ""
        self.pageload_request_id = ""
        self._mkiconf_semaphore = False
        super().__init__(convert_charrefs=convert_charrefs)

    def handle_starttag(self, tag, attrs):
        if (
            attrs == [("type", "text/javascript"), ("charset", "utf-8")]
            and tag == "script"
        ):
            self._mkiconf_semaphore = True
        return super().handle_starttag(tag, attrs)

    def handle_data(self, data):
        if self._mkiconf_semaphore:
            self.authenticity_token = (
                find_value(data, "Mkiconf.authenticity_token = ")
                .replace('"', "")
                .replace("'", "")
            )
            self.pageload_request_id = (
                find_value(data, "Mkiconf.pageload_request_id || ")
                .replace('"', "")
                .replace("'", "")
            )
        return super().handle_data(data)

    def handle_endtag(self, tag):
        if self._mkiconf_semaphore:
            if tag == "script":
                self._mkiconf_semaphore = False
        return super().handle_endtag(tag)


class MerakiDashboardAPI:
    """
    A class to contain Meraki Dashboard data necessary for accessing and using the backend (non-public/REST) APIs.

    ...

    Attributes
    ----------
    username : str
        email address of authorized meraki dashboard account
    password : str
        password of authorized meraki dashboard account
    dash_auth : str
        contents of the "dash_auth" cookie from a web-session (unused currently)
    session_id : str
        contents of the "_session_id_for_nXXX" cookie from a web-session (unused currently)
    administered_orgs : dict
        raw output of the /manage/organization/administered_orgs api call
    organizations: set
        parsed output from administered_orgs (or sqlite db) creating an Organization object for each
    locales: set
        parsed output from administered_orgs (or sqlite db) creating a Locale object for each and adding org_id and shard_id
    node_groups: set
        parsed output from administered_orgs (or sqlite db) creating a Node_groups object for each and adding org_id and shard_id
    shard_headers: dict
        keyed entries of the csrf_token and pageload_id used for many of the API calls, shard specific and not automatically added to calls
    _session: requests.session
        long-lived session with all cookies necessary when using the meraki_login() method

    Methods
    -------
    meraki_login():
        Perform a web-based login to the meraki dashboard (must use a password based username) and store necessary cookies in _session
    refresh_token(shard_id):
        scrape a page from the specified shard_id organization and update the csrf_token and pageload_id in the shard_headers attribute
        required for long running automation as these keys eventually expire in some configurations.
    get_org(name, id, eid):
        return an Organization object based on the requested name, id or eid. Must have data in administered_orgs from get_org_data()
    get_org_data(name, id, eid):
        populate adminsitered_orgs with data from /manage/organization/administered_orgs api call, attempting to use the passed parameters
        to find the organization. Note: at least one call to your default org must be made as a bootstrap for the data, you may have to call
        this function twice unless you have already called get_orgs_data()
    get_orgs_data():
        starting with the default org (landing page shard) loop through all returned organization shard_id and eids and populate administered_orgs
        with the information
    parse_values():
        loop through administered_orgs data and generate the organizations, locales, and node_groups attribute sets
    use_sqlite(db_filename, overwrite):
        import data from sqlite database or create one if it doesn't exist, overwrite file data if overwrite is True
    """

    def __init__(
        self,
        username: str = "",
        password: str = "",
        dash_auth: str = "",
        session_id: str = "",
    ):
        if not (username and password) and not (dash_auth and session_id):
            print(
                "You much provide some authentication data, either dash_auth or uname/pw combo. exiting."
            )
            return
        if not dash_auth:
            self._login_required = True
        else:
            self._login_required = False
        # if dash_auth, pop into cookies of _session along with session_id for shard
        if session_id and dash_auth:
            self.session_id = ast.literal_eval(session_id)
            self.dash_auth = dash_auth
        self.administered_orgs = {}
        self.organizations = set()
        self.node_groups = set()
        self.locales = set()
        self.shard_headers = {}
        self._username = username
        self._password = password
        self._netloc = "dashboard.meraki.com"
        self._scheme = "https:"
        self._last_uri = ""
        self._token = ""
        # using a shared session across our calls makes the cookies for _session_for_shard handled automatically
        self.session = requests.session()
        self._basic_headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Priority": "u=0, i",
            "Referer": self._last_uri,
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-site",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:134.0) Gecko/20100101 Firefox/134.0",
        }
        self._json_headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Priority": "u=0",
            "Referer": self._last_uri,
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:134.0) Gecko/20100101 Firefox/134.0",
        }

    def refresh_token(self, shard_id: int):
        path = "/manage/overviews"
        uri = self._scheme + "//n" + str(shard_id) + ".meraki.com" + path
        result = self.session.get(uri, headers=self._basic_headers)
        if result.status_code != 200:
            result.raise_for_status()
            raise RuntimeError(
                f"Request to {uri} returned status code {result.status_code}"
            )
            return
        dashboard_page = result.text
        last_url = result.url
        self._netloc = urlparse(last_url).netloc
        self._last_uri = last_url
        dashboard_parser = MerakiOverviewParser()
        dashboard_parser.feed(dashboard_page)
        self.shard_headers[shard_id] = {
            "csrf_token": dashboard_parser.authenticity_token,
            "pageload_id": dashboard_parser.pageload_request_id,
        }

    def get_org(self, name: str = "", id: str = "", eid: str = ""):
        return_org = Organization()
        if self.administered_orgs == {}:
            print("No organization data yet, call get_org_data or get_orgs_data")
            return return_org
        elif len(self.organizations) + len(self.node_groups) + len(self.locales) == 0:
            self.parse_values(self.administered_orgs, "organizations", "", 0)
        for org in self.organizations:
            if org.name == name or org.id == id or org.eid == eid:
                return_org = org
                break
        return return_org

    def get_org_data(self, name: str = "", id: str = "", eid: str = ""):
        if (not (name or id or eid)) or self.administered_orgs == {}:
            print("No organization selected...gathering default organization.")
            shard_id = int(self._netloc.split(".")[0][1:])
            selected_org = Organization()
        else:
            selected_org = self.get_org(name, id, eid)
            if selected_org.id == "":
                print("Organization not found...check for typos.")
                return
            else:
                shard_id = selected_org.shard_id
        self.refresh_token(shard_id)
        path = "/manage/organization/administered_orgs"
        headers = deepcopy(self._json_headers)
        headers["Accept"] = "application/json, text/javascript, */*, q=0.01"
        headers["Referer"] = self._last_uri
        headers["X-CSRF-TOKEN"] = self.shard_headers[shard_id]["csrf_token"]
        headers["X-Pageload-Request-Id"] = self.shard_headers[shard_id]["pageload_id"]
        headers["X-Requested-With"] = "XMLHttpRequest"

        if selected_org.id != "":
            uri = "{scheme}//n{org.shard_id}.meraki.com/o/{org.eid}{path}".format(
                org=selected_org, scheme=self._scheme, path=path
            )
        else:
            uri = self._scheme + "//n" + str(shard_id) + ".meraki.com" + path
        result = self.session.get(uri, headers=headers)
        if result.status_code != 200:
            result.raise_for_status()
            raise RuntimeError(
                f"Request to {uri} returned status code {result.status_code}"
            )
        else:
            if selected_org.id == "":
                self.administered_orgs = result.json()
            else:
                self.administered_orgs[selected_org.id] = result.json()[selected_org.id]

    def get_orgs_data(self):
        if len(self.administered_orgs.keys()) == 0:
            self.get_org_data()
        shard_id = int(self._netloc.split(".")[0][1:])
        for key, value in self.administered_orgs.items():
            if value["shard_id"] == shard_id:
                continue
            self.get_org_data(id=key)

    def _get_csrf_token(self):
        path = "/csrf/token"
        uri = self._scheme + "//" + self._netloc + path

        result = self.session.get(uri, headers=self._json_headers)
        if result.status_code != 200:
            result.raise_for_status()
            raise RuntimeError(
                f"Request to {uri} returned status code {result.status_code}"
            )
            token = ""
        else:
            token = result.json().get("csrf_token")
            self._last_uri = uri
        return token

    def _get_login_type(self):
        path = "/login/email_lookup?email=" + self._username
        uri = self._scheme + "//" + self._netloc + path
        headers = deepcopy(self._json_headers)
        headers["Accept"] = "application/json"
        headers["Referer"] = self._scheme + "//" + self._netloc + "/login/"

        result = self.session.get(
            uri, headers={**headers, "X-CSRF-TOKEN": self._token}
        )
        if result.status_code != 200:
            result.raise_for_status()
            raise RuntimeError(
                f"Request to {uri} returned status code {result.status_code}"
            )
            login_type = ""
        else:
            login_type = result.json()["auth_method"]

        return login_type

    def _post_login(self):
        path = "/login/login"
        uri = self._scheme + "//" + self._netloc + path
        headers = deepcopy(self._json_headers)
        headers["Accept"] = "application/json"
        headers["Referer"] = self._scheme + "//" + self._netloc + "/login/local"
        login_data = {"email": self._username, "password": self._password, "go": ""}
        result = self.session.post(
            uri,
            json=login_data,
            headers={
                **self._json_headers,
                "content-type": "application/json",
                "X-CSRF-TOKEN": self._token,
            },
        )
        if result.status_code != 200:
            result.raise_for_status()
            raise RuntimeError(
                f"Request to {uri} returned status code {result.status_code}"
            )
            return "", ""
        else:
            return result.url, result.text

    def meraki_login(self):
        path = "/"
        uri = self._scheme + "//" + self._netloc + path

        result = self.session.get(uri, headers=self._basic_headers)
        if result.status_code != 200:
            result.raise_for_status()
            raise RuntimeError(
                f"Request to {uri} returned status code {result.status_code}"
            )
            return
        else:
            # we expect a 302 here, we want to grab the end of it, same for last url for referer
            self._netloc = urlparse(result.url).netloc
            self._last_uri = result.url

        self._token = self._get_csrf_token()
        if self._get_login_type().find("password") == -1:
            print(
                "username provided does not support password authentication, exiting."
            )
            return
        # get another token for our login post
        self._token = self._get_csrf_token()
        last_url, dashboard_page = self._post_login()
        self._netloc = urlparse(last_url).netloc
        self._last_uri = last_url
        shard_id = int(self._netloc.split(".")[0][1:])
        dashboard_parser = MerakiOverviewParser()
        dashboard_parser.feed(dashboard_page)
        self.shard_headers[shard_id] = {
            "csrf_token": dashboard_parser.authenticity_token,
            "pageload_id": dashboard_parser.pageload_request_id,
        }

    def _process_row(self, table_name: str, data: dict):
        insertion_tuple = db_tuples[table_name]
        columns = db_schemas[table_name]
        insertion_data = {k: v for k, v in data.items() if k in columns}
        return insertion_tuple(**insertion_data)

    def parse_values(
        self,
        value_data: dict = {},
        table_name: str = "organizations",
        organization_id: str = "",
        shard_id: int = 0,
    ):
        if (value_data == {}) and (table_name == "organizations"):
            # build the default structure so users don't have to pass things in, but allow for override for recursive calls.
            value_data = self.administered_orgs
            # empty our organization set as shard specific calls return extra data that is not available otherwise
            # this way we will always only have a set of organizations for which we have the best data
            self.organizations = set()
        for key, value in value_data.items():
            if type(value) != type({}):
                continue
            if key == "node_groups":
                self.parse_values(value, "node_groups", organization_id, shard_id)
            elif key == "locales":
                self.parse_values(value, "locales", organization_id, shard_id)
            elif table_name == "organizations":
                self.parse_values(value, "organizations", key, value["shard_id"])
            if not (
                (table_name == "organizations") and (key in ["node_groups", "locales"])
            ):
                if "shard_id" in value.keys():
                    insertion_tuple = self._process_row(
                        table_name, {**value, "org_id": organization_id}
                    )
                else:
                    insertion_tuple = self._process_row(
                        table_name,
                        {**value, "org_id": organization_id, "shard_id": shard_id},
                    )
                getattr(self, table_name).add(insertion_tuple)
        return

    def _build_sql_schema(self, schema: tuple, table_name: str):
        columns = ""
        for column in schema:
            column_type = type(getattr(db_tuples[table_name], column))
            primary = ""
            if column == "id":
                primary = " PRIMARY KEY"
            if len(columns) != 0:
                columns += ","
            columns += column + " " + python_to_sqlite[column_type] + primary
        if table_name in ["node_groups", "locales"]:
            columns += ", FOREIGN KEY (org_id) REFERENCES organizations (id)"
        if table_name == "node_groups":
            columns += ", FOREIGN KEY (locale_id) REFERENCES locales (id)"
        table_schema = "CREATE TABLE {table_name} ({columns})".format(
            table_name=table_name, columns=columns
        )
        return table_schema

    def use_sqlite(self, db_filename: str, overwrite: bool = False):
        if not overwrite:
            if Path(db_filename).is_file():
                print("DB exists, attempting data import...")
                con = sqlite3.connect(db_filename)
                for table in db_schemas.keys():
                    con.row_factory = db_factories[table]
                    cur = con.execute("SELECT * FROM {}".format(table))
                    setattr(self, table, cur.fetchall())
                con.close()
                return
        if len(self.organizations) + len(self.node_groups) + len(self.locales) == 0:
            self.parse_values(self.administered_orgs, "organizations", "", 0)
        con = sqlite3.connect(db_filename)
        for table, schema_def in db_schemas.items():
            schema = self._build_sql_schema(schema_def, table)
            con.execute("DROP TABLE IF EXISTS {}".format(table))
            con.execute(schema)
            value_bind = "?" + ", ?" * (len(schema_def) - 1)
            script = "INSERT INTO {} VALUES({})".format(table, value_bind)
            # list comprehension to return a plain tuple for our dataclass entries in each table
            insertion_list = [dataclasses.astuple(t) for t in getattr(self, table)]
            con.executemany(script, insertion_list)
        con.commit()
        con.close()
