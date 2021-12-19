Requirements before getting started"
- Phython 3 installed
- Github CLI/Desktop
- Launch Darkly account with Server side SDK installation


Application Setup and Installation:
1. Clone repository: git clone repo https://github.com/rmalik25/travel.git
2. Edit server.py, and update SDK key value in line 11: _ldclient.set_config(Config(_**SDK Key value**_))_
3. Update the name of the feature flag in Line 35: _is_tier_3_enabled = client.variation(**flag-name**, user, False)_
4. Run Python and Launch server: pip3 install -r requirements && python3 server.py
5. Open up browser and browse to http://127.0.0.1:5000/
6. Update user.json with new values e.g. change country to "Australia" and refresh browser to see changes.
  
  
