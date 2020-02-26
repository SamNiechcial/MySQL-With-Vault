# MySQL With Vault - README.md v0.1

A learning project to explore dynamic secrets and encryption as a service, using the Hashicorp suite of technologies with MySQL.

## Requirements:

The eventual aim is to enable minimally technical end users to automate the initiation and configuration of a MySQL database service, in the cloud, with dynamic secrets, to a best practices production standard of security and service delivery.


The current aim is to configure and run all services locally as proof of concept.

## Achievements To Date:

In the 12 hours I have devoted to the project so far, I have configured and run a minimal proof-of-concept service:


- [MySQL 5.7]("https://formulae.brew.sh/formula/mysql@5.7") server, locally, with HomeBrew - providing the database for the credentials to service
- [Consul]("https://www.consul.io/"), locally, in -dev mode - serving as data storage for Vault
- [Vault]("https://www.vaultproject.io/"), locally, in production mode - serving dynamic secrets securely, integrated with MySQL 5.7 and Consul
- [EnvConsul]("https://github.com/hashicorp/envconsul/"), locally - to serve MySQL credentials from Vault to my Python 2.7 scripts

I have not yet started work on initiating and configuring this architecture with Terraform, nor do I have a live web service to hit for requests running in the cloud.
As a result, the Python scripts provided will not work unless you configure these back-end services to run locally on your own machine first.


**To test the app for yourself, please configure the services manually following instructions in Docs/USER_GUIDE.md**


For now, I have included a video to demonstrate that the scripts I have written are working locally for me, *working.mov*.


Future iterations of this application will use Terraform to automate spinning up the architecture and services.


## Next step:

1. The scripts I have created so far are essentially scratches - they refactoring for security, separation of concerns etc.

## Further Steps:

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

## Tech:

This project currently uses open source projects from Hashicorp:

* [Consul](https://www.consul.io/) for Data Storage; Provide encrypted backend data storage for Vault.
* [EnvConsul](https://github.com/hashicorp/envconsul/) for Environment Variable Injection; Export MySQL secrets from Vault to shell subprocesses
* [Vault](https://www.vaultproject.io/) for Dynamic Secrets; Generate and configure MySQL secrets, with integrated restricted permissions and automatic expiry.

It will eventually also use Terraform:
* [Terraform](https://www.terraform.io/) for IaaS; Spin up architecture and configure services.

This project also uses a number of other cool open source software projects:

* [HomeBrew](https://brew.sh/) for MacOS package management; Install and run local MySQL service.
* [Python](https://www.python.org/) for Scripting; Run requests against services and generate user output.
* [Requests](https://pypi.org/project/requests/) for human-compliant Read/Write syntax for HTTP API requests in Python2.7; Process requests for credentials to and from the Vault API

And lastly, this project itself is open source and can be found at the public git repository:
* [Project Git Repo](https://github.com/SamNiechcial/MySQL-With-Vault)

## Readme Details:
README VERSION NUMBER: 0.1

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
