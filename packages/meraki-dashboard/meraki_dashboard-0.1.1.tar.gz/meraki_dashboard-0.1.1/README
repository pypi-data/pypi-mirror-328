# meraki_dashboard (module for easier access to hidden apis such as [delete umbrella](https://documentation.meraki.com/MR/Other_Topics/Automatically_Integrating_Cisco_Umbrella_with_Meraki_Networks#Disabling_Automatic_Umbrella_Integration_on_an_SSID))

This module is specifically for gathering relevant data from the meraki dashboard UI that is necessary for automating configurations that are not available via the public [Meraki API](https://developer.cisco.com/meraki/api-v1/api-index/). There is a lot more data necessary for some of these calls, the simplest I have used this module for is removing an umbrella integration on an SSID which only requires a couple parameters to execute, [example here](https://github.com/llucas-sb/delete_umbrella_ssid)

# Quick Start

1. Install via preferred method
2. Import into your script `import meraki_dashboard`
3. Create and instance of the MerakiDashboardAPI() class `dashboard = meraki_dashboard.MerakiDashboardAPI(username=xxxx,password=xxxx)`
4. Get your dashboard data via one of the 2 available methods `dashboard.get_org_data()` or `dashboard.get_orgs_data()`
5. Parse the data received `dashboard.parse_values()`
6. Gather the locale or node_group or organization you need for your calls e.g. `[local for locale in dashboard.locales if locale.name in ['networkname1','networkname2']]
7. Start making API calls.
8. Watch your token expiration, this is not automatic yet, but a call to `dashboard.refresh_token(shard_id)` will refresh the values you need for subsequent calls
9. If you want to store your dashboard data for importing later, make a call to `dashboard.use_sqlite(db_filename)` and next time you instantiate your object, you can call `use.sqlite(db_filename)` before `get_orgs_data()` and it will import all of the previous data, you will still need to perform a `meraki_login()` to get the necessary `dash_auth` cookie for authentication to shard(s) and `refresh_token()` to get the relevant token(s) for your shard(s)


**Note:**
I recommend using the `dashboard.session` object for calls as it will maintain the session_id cookie and dash_auth cookie as needed for you. It is up to you to ensure you pass in the shard specific headers for your calls.
