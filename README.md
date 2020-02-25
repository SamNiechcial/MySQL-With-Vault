# MySQL With Vault - Read Me

A learning project to explore dynamic secrets and encryption as a service with MySQL, using the Hashicorp suite of technologies.

### Tech:

This project currently uses open source projects from Hashicorp:

* [Consul](https://www.consul.io/) for Service Networking; Provide encrypted backend data storage for Vault.
* [EnvConsul] for Environment Management; Export MySQL secrets from Vault to shell subprocesses
* [Vault] for Dynamic Secrets; Generate and configure MySQL secrets, with integrated restricted permissions and automatic expiry.

It will eventually also use Terraform:
* [Terraform] for IaaC; Spin up architecture and configure services.

This project also uses a number of other cool open source software projects:

* [HomeBrew] for MacOS package management; Install and run local MySQL service.
* [Python] for Scripting; Run requests against services and generate user output.
* [Requests] for human-compliant Read/Write syntax for HTTP API requests in Python2.7; Process requests for credentials to and from the Vault API

And lastly, this project itself is open source and can be found at the public git repository:
* [Project Git Repo]

### Project Goals:

The eventual aim is to enable minimally technical end users to automate the initiation and configuration of a MySQL database service, in the cloud, with dynamic secrets, to a best practices production standard of security and service delivery.

### Current Project State:

The project is in a very early state and is currently unlikely to be of use to anyone else.
In the 12 hours I have devoted to it so far, I have configured and run a proof-of-concept service locally;

 - MySQL 5.7 server and client (locally, with HomeBrew) - providing the database for the credentials to service
 - Consul (locally, in -dev mode) - serving as encrypted data storage for Vault
 - Vault (locally, in production mode) - serving dynamic secrets securely, integrated with MySQL 5.7 and Consul
 - EnvConsul locally - to serve MySQL credentials from Vault to my Python 2.7 scripts

I have not yet started work on initiating and configuring this architecture with Terraform, nor do I have a live web service to hit for requests running in the cloud.

As a result, the Python scripts provided will *not* work unless you configure thes back-end services to run locally on your own machine *first*.

### Demonstrating Working Initial Proof of Concept:

For now, I have included a video to demonstrate that the scripts I have written are working locally for me, *working.mp4*. It can be found in the root directory of the project.

### Next steps:

1. The scripts I have included are essentially scratches - they need immediate refactoring for security, separation of concerns, portability etc.

2. After that, I need to upload configuration files and documentation to enable users to spin up and run architecture locally to demonstrate Python scripts themselves.

### Further Steps:

3. Use Hashicorp documentation to learn how to use Terraform to spin up architecture; MySql 5.7 Server and Client, Consul and Vault - this time on Ubuntu, or something else I can eventually configure to run in production on AWS.

4. Write project Terraform configuration to spin up architecture; MySql 5.7 Server and client, Consul and Vault - Again, on Ubuntu.

5. Refactor Python 2.7 scripts for use with new Terraform architecture, above.

6. Refactor new Python 2.7 scripts for security, separation of concerns, etc.

7. Write Test suite:
Unit testing with PyTest
Behavioural testing with Cucumber (Potentially - for Product Owners etc)

8. Real world testing: Start anew, alter configuration files, and attempt to spin up the entire service in production mode - If this works a few times, I would then consider version 1.0 and package distribution, with public key cryptography etc.

9. Create a version to work with modern services, MySQL 8 with Python 3

10. Maintain project, monitoring for security vulnerabilities, dependency issues etc.

### Readme Details:

This project was written by Sam Niechcial:
* [My Git Profile] - Find me on Github

Readme written with Atom and checked with Dillinger:

* [Atom] - A hackable text editor for the 21st Century
* [Dillinger] - Online Markdown Editor

So long and thanks for all the free software! :-)

[//]:

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
