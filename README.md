# MySQL With Vault
A learning project to explore Dynamic Secrets and Encryption as a Service, using the Hashicorp suite of technologies and MySQL.

## Requirements: MVP
The initial aim was to explore a couple of options for injecting Dynamic Secrets, in order to learn which I prefer, while also demonstrating a minimum viable product.
In order to achieve this, I needed to be able to:

1. Set up Vault (in non-dev mode), using a config.hcl that I would have created beforehand. Use Consul as a storage backend.
2. Initialise the Vault and authenticate as root.
3. Understand how to read and write secrets
4. Mount the MySQL Secret Engine and find a way to generate readonly credentials for MYSQL
5. Create a policy that only authorises to “generate readonly credentials for MYSQL” and assign it to a new token. Confirm this new token can’t do anything else.
6. Use a Vault API Call to inject MySQL credentials into Python scripts dynamically.
7. Use EnvConsul to inject secrets into the script and read from getFromEnv()


To meet this aim in a reasonable timeframe, I configured and ran all services locally, as a learning exercise.
## Progress: MVP Demonstrated
In the 16 hours I have devoted to the project so far, I have configured, run and demonstrated a Minimum Viable Product service:


* [MySQL 5.7](https://formulae.brew.sh/formula/mysql@5.7) server, locally, with HomeBrew - Providing the database to use with the Dynamic Secrets.
* [Consul](https://www.consul.io/), locally, in -dev mode - Serving as data storage for Vault.
* [Vault](https://www.vaultproject.io/), locally, in production mode - serving Dynamic Secrets, integrated with MySQL 5.7 and Consul.
* [EnvConsul](https://github.com/hashicorp/envconsul/), locally - Serving MySQL credentials from Vault to my Python 2.7 scripts.


I have included a video to demonstrate that the MVP is functional locally for me, *working.mov*.
In the video, you will see Vault serving Dynamic Secrets to my app.py script, and the corresponding users appearing in the SQL database.


I have also included detailed step-by-step instructions for installing and configuring the services to run locally at */Docs/USER_GUIDE.md*
## Configuration for Local App Testing
I have not yet started work on initiating and configuring this architecture with Terraform, nor do I have a live web service to hit for requests running in the cloud.
As a result, the Python scripts provided will not currently work unless you configure these back-end services to run locally on your own machine first.


**To test the app for yourself, please configure the services locally from the CLI, following instructions in Docs/USER_GUIDE.md**


Future iterations of this application will use Terraform to automate spinning up the architecture and services.
## Requirements - Short Term: Automate Service Architecture
Learn Terraform, then use it to automate the configuration of the back-end services for other users. This will enable other users to easily run and test a "live" application locally, without need to resort to the User Guide.
## Next Steps: Terraform
1. Use Hashicorp documentation to learn how to use Terraform to spin up architecture; MySql 5.7 Server and Client, Consul and Vault - this time with Ubuntu on AWS or Docker.
2. Write project Terraform configuration to spin up architecture; MySql 5.7 Server and client, Consul and Vault - Again, on Ubuntu.



## Requirements - Long Term: Develop a Project that's Actually Useful
The eventual aim is to enable minimally technical end users to automate the initiation and configuration of a MySQL database service, in the cloud, with dynamic secrets, to a best practices production standard of security and service delivery. This may take some time.
## Further Steps: Refactoring and Testing - Unit, Integration and Battle
3. The scripts I have created so far are essentially scratches - they refactoring for security, separation of concerns etc.
4. Refactor Python 2.7 scripts for use with new Terraform architecture, security, separation of concerns, etc.
6. Write Test suite:
Unit testing with PyTest,
Behavioural testing with Cucumber
7. Battle testing: Start anew, alter configuration files, and attempt to spin up all service clusters in production mode.
8. Create a version to work with modern services, MySQL 8 with Python 3
9. Maintain project, monitoring for security vulnerabilities, dependency issues etc.

## Readme Details
README_VERSION_NUMBER: 0.1

[My Git Profile]: <"https://github.com/SamNiechcial">
[Project Git Repo]: <"https://github.com/SamNiechcial/MySQL-With-Vault">

[Atom]: <"https://atom.io/">
[Consul]: <"https://www.consul.io/">
[Dillinger]: <"https://dillinger.io/">
[EnvConsul]: <"https://github.com/hashicorp/envconsul/">
[HomeBrew]: <"https://brew.sh/">
[Python]: <"https://www.python.org/">
[Requests]: <"https://pypi.org/project/requests/">
[Terraform]: <"https://www.terraform.io/">
[Vault]: <"https://www.vaultproject.io/">
