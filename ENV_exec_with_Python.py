import subprocess

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
