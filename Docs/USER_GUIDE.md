# MySQL With Vault - USER_GUIDE.md v0.1
This user guide speaks to running the services and application locally on MacOS Catalina.


Basic familiarity with the CLI and MacOS development tools is assumed.


It is recommended that you use the **secret_note_template.txt** file included to record important credentials as you go.


Once you have everything configured, it is strongly recommended that you save this secret_note in a secure location, such as with a password manager like 1password, and **destroy** the original file.

## Requirements:
To run the project locally and demonstrate app functionality, you will need:


1. This Git Repo, cloned to your machine with relevant configuration files.
2. Python 2.7 installed - the standard-issue MacOS bin will do fine.
3. Virtual Environment created, with package requirements installed via PIP.
4. MySQL 5.7 installed, with client running locally.
5. Consul installed, with agent running in -dev mode.
6. Vault installed, with agent running locally in production mode.
7. Vault configured to provide Dynamic Secrets for MySQL Database via HTTP API
8. EnvConsul installed and working on the CLI.
9. EnvConsul configured to Serve Dynamic Secrets via Subprocess.
10. App script configured with correct vault policy token information.

## 1. Clone Git Repository to Your Machine via CLI:
To download from GitHub with the CLI, navigate to your projects directory and run:


```shell
git checkout https://github.com/SamNiechcial/MySQL-With-Vault.git
```

If your Git isn't working from the CLI, beware the stealth Xcode update - it gets me every time. Run this in your shell to popup the update the command line tools:


```shell
xcode-select --install
```
## 2. Check Default Python 2.7 Installation:
Check which version of Python you are running with:


```shell
which python
```


If you aren't already running a different virtual environment, you get should get:


```Shell
/usr/bin/python
```

If so, no further action should be required.

## 3. Create Virtual Environment with VirtualEnv and PIP:

Navigate to root directory of the newly-cloned project, and create a Python 2.7 virtual environment for the project with:


```shell
python -m virtualenv sql_env
```


Remaining in the project root directory, activate the virtual environment using:


```shell
source sql_env/bin/activate
```


Finally, install the package requirements with PIP:


```shell
pip install -r requirements.txt
```


Your virtual environment should now be ready to run the project scripts.

## 4. Install MYSQL and MYSQL client with Homebrew and Run MySQL Server Locally:
If you don't already have Homebrew, enter:


```shell
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```


If you do, beware the automatic updates, they always seem to break something for me. Anyway, enter:

```shell
brew -update
```


It may also be a good idea to run the doctor and fix anything important:


```shell
brew -doctor
```


#### Install MySQL 5.7 and Client with Homebrew:
Install MySQL 5.7 with:


```shell
brew install mysql@5.7
```


and client with:


```shell
brew install mysql-client@5.7
```


#### Start MySQL Running Locally:
Force link version 5.7:


```shell
brew link mysql@5.7 --force
```


Load and start the MySQL service:


```shell
brew services start mysql@5.7
```


Check if the MySQL service has been loaded:


```shell
brew services list
```


To make your MySQL installation a little more secure, notably by setting root credentials immediately:


**IMPORTANT: Make sure to select a strong password!**



```shell
mysql_secure_installation
```


**IMPORTANT: Copy the secret_note_template from the project directory into a secure location, for example a secret note in 1Password. Add the MySQL Root Credentials to the secret note. Ensure this note is properly saved before continuing.**

## 5. Install Consul and Run Consul Agent Locally (in Development Mode):
Download latest version of Consul:


```shell
curl --remote-name https://releases.hashicorp.com/consul/1.7.0/consul_1.7.0_darwin_amd64.zip
```


Unzip the supplied archive:


```shell
unzip consul_1.7.0_darwin_amd64.zip
```


Add supplied binary to path, for example by moving to /usr/local/bin:


```shell
mv consul /usr/local/bin/
```


Check consul is now available on path by running:


```shell
consul --version
```


If not available, restart your terminal window and try again.


#### Start Consul running locally in Development Mode:
Start your local consul agent and node by running:

```shell
consul agent -dev -node NAME
```


**IMPORTANT: Never run a Consul agent in Development mode in production. This guide is strictly for a proof-of concept and testing implementation.**


Where NAME indicates the name you want for your agent, e.g.


```shell
consul agent -dev -node 'legacy_sql_node'
```


**Note: DNS queries against local consul nodes won't work if the Node name contains full stops. Consul uses the Mac machine hostname for the Node name by default. As my Mac machine hostname default does contain full stops, I thought it safer to specify a node name with the node flag.**


If everything is working, Consul should stream you quite a bit of log data to STDOUT.
This terminal window is now running your local consul server. Open another.


**IMPORTANT: Forcibly killing the Consul agent process is not a good idea. Nodes should be stopped, when finished, using:**


```shell
consul leave
```

## 6. Install Vault and Run Local Server in Production Mode:
Download the latest version of Vault and Unzip:

```shell
curl --remote-name https://releases.hashicorp.com/vault/1.3.2/vault_1.3.2_darwin_amd64.zip
unzip vault_1.3.2_darwin_amd64.zip
```

Add vault to path:


```shell
mv vault /usr/local/bin/
```


Install Vault Command Line Completion:


```shell
vault -autocomplete-install
```


Start a new terminal window, and use it to start a local Vault Server, specifying the project configuration file with the config flag:


```shell
vault server -config=*/Config/Vault/vault_server_config.hcl
```


Where the * indicates your specific path to your Projects directory. This terminal window is now running your Vault server. Open a new one.


#### Initialise and Unseal the Vault Server:
Initialise the vault:


```shell
vault operator init
```


This will provide you with a set of 5 unseal keys and an initial root token, and a lot of useful information about vault keys. Save all the keys provided in your Secret Note.


Now, the Vault server is running, and has access to the backend storage in Consul, but is unable to decrypt that backend storage.  Next, we need to unseal the vault, using the 5 unseal keys provided:


```shell
vault operator unseal
```


This will ask you for an unseal key from the list of 5 Vault provided. Enter one. Repeat this process twice more. That should be your Vault Server unsealed. Now, all that remains is to log in. Pass the root token provided by the `vault login` command, for example (Not real credentials):


```shell
vault login s.9jazDIV2i7yjKw5f4DdLnP8n
```


Great Success! You have now initiated a Vault server in production mode, unsealed the server, and **authenticated** as the root user. Now it's time to configure the vault server to serve us some dynamic secrets for our MySQL database.  We are going to do this using the **database secrets engine** in Vault.

## 7. Configure Vault to Serve Dynamic Secrets for MySQL:
Start the pre-installed database Vault secrets service with:


```shell
vault secrets enable database
```


Next, to configure vault with the proper connect and plugin information.


4 MySQL plugins are available for the database secrets engine
- mysql-database-plugin
- mysql-aurora-database-plugin
- mysql-rds-database-plugin
- mysql-legacy-database-plugin


As we are running a MySQL 5.7 database at present, we want the legacy plugin.
Connect Vault to the local MySQL service by passing arguments on the CLI, like so:


```shell
vault write database/config/legacy_mysql \
    plugin_name=mysql-legacy-database-plugin \
    connection_url="{{username}}:{{password}}@tcp(127.0.0.1:3306)/" \
    allowed_roles="legacy_mysql_role" \
    username="root" \
    password="god"
```


Wherein the supplied connection url is the default for MySQL running locally, the username and password are replaced with the MySQL root information from your secret note, and the allowed_roles includes only the name of the role we are about to write next.


**NOTE: As we will be passing MySQL credentials to shell environment variables later on with EnvConsul, and the names of these variables will be determined by the role name, it is inadvisable to include any characters in the role name which are not allowable in shell environment variable names.**


Next, we need to write a Vault role with permissions to access the MySQL database and generate new users dynamically:


```shell
vault write database/roles/legacy_mysql_role \
    db_name=legacy_mysql \
    creation_statements="CREATE USER '{{name}}'@'%' IDENTIFIED BY '{{password}}';GRANT SELECT ON *.* TO '{{name}}'@'%';" \
    default_ttl="1h" \
    max_ttl="24h"
```


We should now be able to generate new users, with working username and password, on the command line with Vault, using


```shell
vault read database/creds/legacy_mysql_role
```


**NOTE: The Credentials are different every time you run this command. A new user is being generated in the MySQL database every time.**


For security reasons, we do not want our legacy mysql dynamic secrets application to have root access to Vault. Now, we need to control the **authorization** the token we generate for our application to use has, with Vault Policies.


To configure a policy which will **only** allow the user holding the token to generate and read MySQL credentials, and nothing more, load the policy provided in the project Config folder:


```shell
vault policy write mysql_policy */Config/Vault/mysql_policy.hcl
```


**NOTE: Vault is inherently secure. The config file need only contain minimum necessary permissions for the role. All other abilities will be disabled by default.**

Create a Vault token for the mysql_role using the mysql_policy:


```shell
vault token create -policy=mysql_policy
```


The "token" Value from the output is the Vault token we will be needing for our Python Script.
We will be using it to make calls to the Vault HTTP API.
Save it in your secret note for now.

## 8. Install EnvConsul:
Contrary to what you may think, EnvConsul is not a feature of Consul, but is in fact an entirely separate binary file. It will have to be installed as per the two other hashicorp binaries above. Download and unzip with:

```shell
curl --remote-name https://releases.hashicorp.com/envconsul/0.9.2/envconsul_0.9.2_SHA256SUMS
unzip envconsul_0.9.2_darwin_amd64.zip
```


Put EnvConsul on path using:


```shell
mv envconsul /usr/local/bin/
```


Restart your terminal window.

## 9. Configure EnvConsul to Serve MySQL Credentials from Vault to Python:
Set the EnvConsul policy using the policy provided in the Vault Config folder:


```shell
vault policy write envconsul_policy /Config/Vault/envconsul_policy.hcl
```

Create the token for the envconsul_policy:


```shell
vault token create -policy=envconsul_policy
```


Again, the token value is the information you need for the EnvConsul method in the app.py script. Save it for now in your secret note.

## 10. Configure App Script with Vault Policy Token Information:
Simply take the two policy tokens from your secret list, paste them into the relevant lines in app.py, and run from the CLI with:

```shell
python app.py
```

Note you are served different credentials via the environment and via the Vault HTTP API, every time you run the script.

This means you now have a bare-bones local Vault service, serving credentials live to a Python application, via both the Vault HTTP API and EnvConsul.

## Useful Documentation:
[Consul Local Deployment Guide](https://learn.hashicorp.com/consul/getting-started/agent)

[Consul Configuration Documentation](https://www.consul.io/docs/agent/options.html)

[Consul Production Deployment Guide](https://learn.hashicorp.com/consul/datacenter-deploy/deployment-guide)
