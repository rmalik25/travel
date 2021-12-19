# TODO: Add the LaunchDarkly SDK to this so we can flag new features
import os
from flask import Flask, render_template
import ldclient
from ldclient.config import Config
import json



# Paste your SDK key below
ldclient.set_config(Config("sdk-4f0ff5b2-9c06-463f-9ac7-ab24588b1a84"))
client = ldclient.get()




app = Flask(__name__, static_folder='public', template_folder='views')

    
@app.route('/')
def pricing():
    """Displays the pricing page."""

    # Since this page doesn't require a logged in user,
    # tell LaunchDarkly that this is an anonymous user.
    f = open('user.json')
    data = json.load(f)

    user = {
      "key": data['key'],
      "anonymous": False,
      "country": data['country'],
      "firstName": data['firstName']
    }
    is_tier_3_enabled = client.variation('firstflag', user, False) #update feature flag name here
    print("Flag: " + str(is_tier_3_enabled))
    return render_template('pricing.html', is_tier_3_enabled=is_tier_3_enabled)


  
if __name__ == '__main__':
    app.run()
