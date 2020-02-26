# MySQL With Vault
A learning project to explore dynamic secrets and encryption as a service, using the Hashicorp suite of technologies with MySQL.

## Requirements:
The eventual aim is to enable minimally technical end users to automate the initiation and configuration of a MySQL database service, in the cloud, with dynamic secrets, to a best practices production standard of security and service delivery.


The current aim is to configure and run all services locally as a learning exercise.

## Achievements To Date:
In the 16 hours I have devoted to the project so far, I have configured and run a minimally configured service:


* [MySQL 5.7](https://formulae.brew.sh/formula/mysql@5.7) server, locally, with HomeBrew - providing the database for the credentials to service
* [Consul](https://www.consul.io/), locally, in -dev mode - serving as data storage for Vault
* [Vault](https://www.vaultproject.io/), locally, in production mode - serving dynamic secrets securely, integrated with MySQL 5.7 and Consul
* [EnvConsul](https://github.com/hashicorp/envconsul/), locally - to serve MySQL credentials from Vault to my Python 2.7 scripts


I have included a video to demonstrate that the scripts I have written are working locally for me, *working.mov*.


I have also included detailed step-by-step instructions for installing and configuring the services to run locally at */Docs/USER_GUIDE.md*

## App Testing:
I have not yet started work on initiating and configuring this architecture with Terraform, nor do I have a live web service to hit for requests running in the cloud.
As a result, the Python scripts provided will not work unless you configure these back-end services to run locally on your own machine first.


**To test the app for yourself, please configure the services locally from the CLI, following instructions in Docs/USER_GUIDE.md**


Future iterations of this application will use Terraform to automate spinning up the architecture and services.


## Next steps:
1. The scripts I have created so far are essentially scratches - they refactoring for security, separation of concerns etc.

2. Use Hashicorp documentation to learn how to use Terraform to spin up architecture; MySql 5.7 Server and Client, Consul and Vault - this time with Ubuntu on AWS or Docker.

3. Write project Terraform configuration to spin up architecture; MySql 5.7 Server and client, Consul and Vault - Again, on Ubuntu.

4. Refactor Python 2.7 scripts for use with new Terraform architecture, above.

5. Refactor new Python 2.7 scripts for security, separation of concerns, etc.

6. Write Test suite:
Unit testing with PyTest,
Behavioural testing with Cucumber

7. Battle testing: Start anew, alter configuration files, and attempt to spin up all service clusters in production mode.

8. Create a version to work with modern services, MySQL 8 with Python 3

9. Maintain project, monitoring for security vulnerabilities, dependency issues etc.

## Readme Details:
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
