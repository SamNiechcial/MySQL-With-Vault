import os

def getFromEnv():

    # Extracts the MYSQL Credential Variables from the EnvConsul Sub-shell:

    username = str(os.environ.get("DATABASE_CREDS_LEGACY_MYSQL_ROLE_USERNAME"))
    password = str(os.environ.get("DATABASE_CREDS_LEGACY_MYSQL_ROLE_PASSWORD"))

    # Error handling at it's most rudimentary:

    if password == "None":
        print "Script has failed to obtain variables from the environment with EnvConsul"
        print "Please ensure you call this script using the envconsul command via CLI as specified in the readme"

    # Interpolate MySQL credentials from Vault API via EnvConsul and serve to STDOUT:
    
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
