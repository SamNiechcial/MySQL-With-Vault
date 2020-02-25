import json
import requests

def getFromAPI():

    # Hard-coding credentials is NOT advisable in production applications.
    # It is my intention to serve this from a config file in future versions!

    mysql_vault_token = # Insert Token for Authenticating for legacy-mysql-role here!

    # Make API request to Vault and assign response to locally-scoped variable

    resp = requests.get("http://localhost:8200" +
                        "/v1/database/creds/legacy-mysql-role",
                        headers = {"X-Vault-Token": mysql_vault_token})

    # Convert JSON response from API to a dictionary using JSON package:

    resp_dict = json.loads(resp.text)
    resp_data = resp_dict.get("data")

    # If Much Success:
    # Interpolate MySQL credentials from Vault API request and serve to STDOUT:

    if(resp.ok):
        print ""
        print "-----------------------------------------------"
        print "HTTP API CALL MADE SUCCESSFULLY TO VAULT"
        print "-----------------------------------------------" + "\n"
        print "Your credentials are:\n"
        print "Username = " + resp_data.get("username")
        print "Password = " + resp_data.get("password")         + "\n"
        print "These credentials will expire after 1hr"
        print "-----------------------------------------------"
        print "-----------------------------------------------" + "\n"

    # Or, if not;
    # Error handling at it's most rudimentary:

    else:
        resp.raise_for_status()
        print ""
        print "-----------------------------------------------" + "\n"
        print "THE HTTP API CALL TO VAULT HAS FAILED"           + "\n"
        print "-----------------------------------------------"
        print "-----------------------------------------------" + "\n"


getFromAPI()
