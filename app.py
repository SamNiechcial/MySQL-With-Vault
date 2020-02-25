import json
import requests
import subprocess

def getFromAPI():

    # Hard-coding credentials is NOT advisable in production applications.
    # It is my intention to serve this from a config file in future versions!

    mysql_vault_token = # Insert Token for Authenticating for legacy-mysql-role here!

    # Make API request to Vault and assign response to locally-scoped variable:

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
        print "THE HTTP API CALL TO VAULT HAS FAILED"
        print "-----------------------------------------------" + "\n"
        print "Please ensure Vault is configured correctly"
        print "-----------------------------------------------" + "\n"

def getFromEnv():

    # Hard-coding credentials is NOT advisable in production applications.
    # It is my intention to serve this from a config file in future versions!

    # Generate shell subprocess populated with MySQL credentials from Vault via EnvConsul CLI Tool:
    token = # Insert Token for Authenticating for envconsul role here!
    address = 'http://127.0.0.1:8200'
    vault_cred_path = 'database/creds/legacy_mysql_role'
    cmd = "VAULT_TOKEN='{}' VAULT_ADDR='{}' envconsul -upcase -secret {} env"

    # Extract environment variables from shell subprocess and convert to dictionary:
    output = subprocess.check_output(cmd.format(token, address, vault_cred_path), shell=True)
    output_by_line = output.split('\n')

    env_vars = {}
    for line in output_by_line:
        key_value = line.split('=')
        env_vars[key_value[0]] = key_value[1] if len(key_value) > 1 else None

    # Extract MySQL username and password from Subprocess Environment Variables Dictionary:
    username = env_vars.get('DATABASE_CREDS_LEGACY_MYSQL_ROLE_USERNAME')
    password = env_vars.get('DATABASE_CREDS_LEGACY_MYSQL_ROLE_PASSWORD')

    # Error handling at it's most rudimentary:
    if password == "None":
        print "-----------------------------------------------"
        print "VARIABLE POPULATION WITH ENVCONSUL HAS FAILED"
        print "-----------------------------------------------" + "\n"
        print "Please ensure services are configured correctly" + "\n"
        print "-----------------------------------------------"
        print "-----------------------------------------------" + "\n"

    # Much Success! Print Username and Password Credentials to STDOUT for user:
    else:
        print ""
        print "-----------------------------------------------"
        print "VARIABLES POPULATED SUCCESSFULLY WITH ENVCONSUL"
        print "-----------------------------------------------" + "\n"
        print "Your credentials are:"
        print "Username = " + username
        print "Password = " + password                          + "\n"
        print "These credentials will expire after 1hr"         + "\n"
        print "-----------------------------------------------"
        print "-----------------------------------------------" + "\n"

getFromEnv()
getFromAPI()
