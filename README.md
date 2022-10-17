# This is my new Project2 Repo !!!!

[![CI](https://github.com/xxxpegaxxx/p2_cicd/actions/workflows/main.yml/badge.svg)](https://github.com/xxxpegaxxx/p2_cicd/actions/workflows/main.yml)


# Overview

A roject on how to set up a Microsoft Azure CI/CD Pipeline. We will be discussing how to clone and build your flask appication in Azure Shell setup Github Actions for Continuous Integrations. We will also be showing how to set up a Azure DevOps pipeline for Continuous Delivery.

## Project Plan
<TODO: Project Plan

* A link to a Trello board for the project - https://trello.com/b/qDuO5AoQ/project-2-ci-cd-pipeline#
* A link to a spreadsheet that includes the original and final project plan>

## Instructions

<TODO:  
* Architectural Diagram (Shows how key parts of the system work)>

<TODO:  Instructions for running the Python project.  How could a user with no context run this project without asking you for any help.  Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots:

Continuous Integration
1. Create a Github Repo (if not created)
	• Public
	• Initialize with README
	• .gitignore - Python
	• Upload hello.py and test_hello.py
2. Open Azure Cloud Shell
3. Create ssh-keys in Azure Cloud Shell
	• ssh-keygen -t rsa
	• Print out the .pub (public key) - cat /home/odl_user/.ssh/id_rsa.pub
	• Copy ssh key ( ssh-rsa) and place in azure portal
4. Upload ssh-keys to Github
	• Settings --> SSH and GPG Keys
	• New SSH Keys
5. Create scaffolding for the project (if not created)
	1. Github Repo - copy Clone with SSH 
	• git clone git@github.com:xxxpegaxxx/testrepo.git
	• cd cicd_p2/
	• git status
	• Git add README.md
	• Git commit -m "Adding a change to the README"
	• git config --global user.email "spackpega@aol.com
	• cicd_p2$ git config --global user.name "Carlos J Viera"
	• Git push
6. Create Makeflie and requirements.txt
	• Touch Makefile
	
	• Touch requirements.txt
	install:
		pip install --upgrade pip &&\
			pip install -r requirements.txt
	
	test:
		#python -m pytest -vv test_hello.py
	
	
	lint:
		pylint --disable=R,C hello.py
	
	all: install lint test
	
7. Github Actions
	• Setup Workflow for ourselves
	• Remove from main.yml
		○ Remove Comments


Continuous Delivery

1. Create a new repo
	• Clone repo to shell
2. Create virtual env
	• cd in to project
	• python3 -m venv ~/.p2_cicd
	source ~/.p2_cicd/bin/activate
	• Run make install
3. Create app service in shell
	• az webapp up -n cjvp2app
	• Verify it works - 
		https://cjvp2app.azurewebsites.net
4. Perform prediction
	• Change line in make_predict_azure_app.sh to 
		-X POST https://cjvp2app.azurewebsites.net:$PORT/predict
	• Change security on file 
		chmod +x make_predict_azure_app.sh
	• Run prediction - 
		./make_predict_azure_app.sh
5. Got to Azure DevOps Organization
6. Create new project
	• Private
	• Git
	• Basic
7. Create a new service connection
	1. Project settings
	2. Go to Azure Resource Manager and Pipeline
	3. ![image](https://user-images.githubusercontent.com/101995184/196294326-556b7c32-d5cf-48c2-a25f-bb013034bc66.png)

  
  
8. Go to Pipelines
	• Create Pipeline
	• Select Github
	• Python to Linux WeApp on Azure
	• Confirm YAML file created.



* Project running on Azure App Service

* Project cloned into Azure Cloud Shell

* Passing tests that are displayed after running the `make all` command from the `Makefile`

* Output of a test run

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

* Running Azure App Service from Azure Pipelines automatic deployment

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

* Output of streamed log files from deployed application

> 

## Enhancements

<TODO: A short description of how to improve the project in the future>

## Demo 

<TODO: Add link Screencast on YouTube>
