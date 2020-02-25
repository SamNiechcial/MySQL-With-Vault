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
6. EnvConsul installed
7. Vault installed, with agent running locally in production mode.
8. Vault configured to provide Dynamic Secrets for MySQL Database.

 configured to work with Consul & Vault.

Vault installed, agent running in production mode, back-end storage with Consul.
## 1. Clone Git Repository to Your Machine via CLI:


To download from GitHub with the CLI, navigate to your projects directory and run:


```shell
git checkout https://github.com/SamNiechcial/MySQL-With-Vault.git
```

If your Git isn't working from the CLI, beware the stealth Xcode update - it gets me every time.


Run this in your shell to popup the update the command line tools:


```shell
xcode-select --install
```

## 2. Check Default Python 2.7 Installation:


Check which version of Python you are running with:


```shell
which python
```


If you get:


```Shell
/usr/bin/python
```

back, which you should do, assuming you aren't already running a different virtual environment, no further action should be required.


## 3. Create Virtual Environment with Package Requirements Installed via PIP:


Navigate to root directory of the newly-cloned project, and create a Python 2.7 virtual environment for the project with:


```shell
python -m virtualenv *NAME*
```


Where *NAME* denotes whatever you want to call the virtual environment, e.g.


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


## 4. Install MYSQL and MYSQL client with Homebrew, Run Client Locally:


### Install Homebrew:


If you don't already have Homebrew, why not? Anyway, enter:


```shell
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```


If you do, beware the automatic updates, they always seem to break something. Anyway, enter:

```shell
brew -update
```


It may also be a good idea to run the doctor and fix anything important:


```shell
brew -doctor
```


### Install MySQL 5.7 and Client with Homebrew:


Check the standard MySQL 5.7 distribution is available as a stable build..
The latest version of MySQL is 8 - as a result we will need to append a tag to the default package key:


```shell
brew info mysql@5.7
````

As long as the output contains the word stable, install MySQL 5.7 with:


```shell
brew install mysql@5.7
```


and client with:


```shell
brew install mysql-client@5.7
```


### Start MySQL Running Locally:


Verify the installed MySQL instance:


```shell
mysql -V
```


Hopefully, the output looks like this:


```shell
Ver 14.14 Distrib 5.7.22, for osx10.13 (x86_64)
```


Force link version 5.7:


```shell
brew link mysql@5.7 --force
```


Load and start the MySQL service:


```shell
brew services start mysql@5.7
```


Hopefully, the output looks like this:


```shell
Successfully started mysql (label: homebrew.mxcl.mysql)
```


Check if the MySQL service has been loaded:


```shell
brew services list
```


To make your MySQL installation a little more secure, notably by setting root credentials immediately:


```shell
mysql_secure_installation
```


**IMPORTANT: Make sure to select a strong password!**


**IMPORTANT: Copy the secret_note_template from the project directory into a secure location, for example a secret note in 1Password. Add the MySQL Root Credentials to the secret note. Ensure this note is properly saved before continuing.**


## 5. Install Consul, Run Consul Agent Locally (in Development Mode):


### Install Consul:


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


### Start Consul running locally in Development Mode:


**IMPORTANT: Never run a Consul agent in Development mode in production. This guide is strictly for a proof-of concept and testing implementation.**


Start your local consul agent and node by running:

```shell
consul agent -dev -node *NAME*
```


Where *NAME* indicated the name you want for your node, e.g.


```shell
consul agent -dev -node 'legacy_sql_node'
```


**Note: DNS queries against local consul nodes won't work if the Node name contains full stops. Consul uses the Mac machine hostname for the Node name by default.**


As my Mac machine hostname default does contain full stops, I thought it safer to specify a node name with the node flag.


If everything is working, Consul should stream you quite a bit of log data to STDOUT.


**IMPORTANT: Add the Node ID, Node Name and Client Address to your secret note. You will need them all later.**


### Consul - Basic Service Discovery:


There are various ways to obtain details about the running Consul service.


Nodes running on the local Consul Agent can be inspected with:


```shell
consul members -detailed
```

This runs against the client, which is getting data via the Gossip Protocl.


For a more strongly consistent view, query the HTTP API, which returns JSON:


```shell
curl localhost:8500/v1/catalog/nodes
```


Lastly, there is also a DNS interface, by which to discover nodes via the consul server. This runs on port 8600 by default.


```shell
dig @127.0.0.1 -p 8600 sql_node.node.consul
```


This will all become much more important when we are configuring the production application. For now, it just may be handy to know if you need it.


### Consul - Correct Shutdown:


**IMPORTANT: Forcibly killing the Consul agent process is not a good idea. Nodes should be stopped, when finished, using:**


```shell
consul leave
```


### Further Reading for Consul Configuration:


[Consul Local Deployment Guide](https://learn.hashicorp.com/consul/getting-started/agent)


[Consul Configuration Documentation](https://www.consul.io/docs/agent/options.html)


[Consul Production Deployment Guide](https://learn.hashicorp.com/consul/datacenter-deploy/deployment-guide)


## Install EnvConsul


Contrary to what you may think, EnvConsul is not a feature of Consul, but is in fact an entirely separate binary file.


## Install Vault, Run Locally in Production Mode:

Download the latest version of Vault:
`curl --remote-name https://releases.hashicorp.com/vault/1.3.2/vault_1.3.2_darwin_amd64.zip`


## Useful Documentation:

[Consul Local Deployment Guide](https://learn.hashicorp.com/consul/getting-started/agent)

[Consul Configuration Documentation](https://www.consul.io/docs/agent/options.html)

[Consul Production Deployment Guide](https://learn.hashicorp.com/consul/datacenter-deploy/deployment-guide)

**TO BE CONTINUED**
