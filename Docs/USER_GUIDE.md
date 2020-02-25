# MySQL With Vault - User Guide v0.1

This user guide speaks to running the services and application locally on MacOS Catalina. Basic familiarity with the CLI and MacOS development tools is assumed.


## Requirements:

To run the project locally and demonstrate app functionality, you will need:

1. This Git Repo, cloned to your machine with relevant configuration files.

2. Python 2.7 installed - the standard-issue MacOS bin will do fine.
3. Virtual Environment created, with package requirements installed via PIP.

4. MySQL 5.7 installed, with client running locally.

5. Consul installed, with agent running in -dev mode.
6. Vault installed, agent running in production mode, back-end storage with Consul.
7. EnvConsul installed, configured to work with Consul & Vault.


## 1. Clone Git Repository to Your Machine via CLI:

To download from GitHub with the CLI, navigate to your projects directory and run:

`git checkout https://github.com/SamNiechcial/MySQL-With-Vault.git`

If your Git isn't working from the CLI, beware the stealth Xcode update - it gets me every time.

Run this in your shell to popup the update the command line tools: `xcode-select --install`


## 2. Run Python 2.7:

Check which version of Python you are running with: `which python`

If you get: `/usr/bin/python` back, which you should do, assuming you aren't already running a different virtual environment, no further action should be required.


## 3. Create Virtual Environment with Package Requirements Installed via PIP:

Navigate to root directory of the newly-cloned project, and create a Python 2.7 virtual environment for the project with: `python -m virtualenv *NAME*`

Where *NAME* denotes whatever you want to call the virtual environment, e.g. `python -m virtualenv sql_env`

Remaining in the project root directory, activate the virtual environment using: `source sql_env/bin/activate`

Finally, install the package requirements with PIP: `pip install -r requirements.txt`

Your virtual environment should now be ready to run the project scripts.


## 4. Install MYSQL and MYSQL client with Homebrew, Run Client Locally:

# Install Homebrew:

If you don't already have Homebrew, why on earth not? If you do, beware the automatic updates, they always seem to break something. Anyway, enter;

`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

# Install MySQL 5.7 and Client with Homebrew:

We are going to need Brew Services to run MySQL - install with: `brew tap homebrew/services`

Check the standard MySQL 5.7 distribution is available as a stable build..
The latest version of MySQL is 8 - as a result we will need to append a tag to the default package key: `brew info mysql@5.7`

As long as the output contains the word stable, install MySQL 5.7 and client with: `brew install mysql@5.7` and `brew install mysql-client@5.7`

# Run MySQL Locally - Configuration:

Force link version 5.7: `brew link mysql@5.7 --force`

Load and start the MySQL service: `brew services start mysql@5.7.`
Hopefully, the output looks like this: `Successfully started mysql (label: homebrew.mxcl.mysql)`

Check if the MySQL service has been loaded: `brew services list`

Verify the installed MySQL instance: `mysql -V`
Hopefully, the output looks like this: `Ver 14.14 Distrib 5.7.22, for osx10.13 (x86_64)`

To make your MySQL installation a little more secure, notably by setting root credentials: `mysql_secure_installation`

Important : Use the single ‘quotes’ to surround the password and make sure to select a strong password!


## Useful Documentation:

[Consul Local Deployment Guide](https://learn.hashicorp.com/consul/getting-started/agent)

[Consul Production Deployment Guide](https://learn.hashicorp.com/consul/datacenter-deploy/deployment-guide)
