# This is my new Project2 Repo !!!!

[![CI](https://github.com/xxxpegaxxx/p2_cicd/actions/workflows/main.yml/badge.svg)](https://github.com/xxxpegaxxx/p2_cicd/actions/workflows/main.yml)


# Overview

A roject on how to set up a Microsoft Azure CI/CD Pipeline. We will be discussing how to clone and build your flask appication in Azure Shell setup Github Actions for Continuous Integrations. We will also be showing how to set up a Azure DevOps pipeline for Continuous Delivery.

## Project Plan
<TODO: Project Plan

* Trello board for the P2_CICD Project - https://trello.com/b/qDuO5AoQ/project-2-ci-cd-pipeline#
* Project Plan - https://github.com/xxxpegaxxx/p2_cicd/blob/0a2d67250ef19b5182be12edab68419c11084621/Project%20Plan%20-%20P2_CICD.xlsx

## Instructions

<TODO:  
* Architectural Diagram (Shows how key parts of the system work)>

<TODO:  Instructions for running the Python project.  How could a user with no context run this project without asking you for any help.  Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots:

## Continuous Integration
* Create a Github Repo (if not created) with the below options
	*  Public
	*  Initialize with README
	*  .gitignore - Python
* Upload the following files
	*  Upload hello.py and test_hello.py
* Open Azure Cloud Shell
* Create ssh-keys in Azure Cloud Shell
	*  Use the ssh-keygen -t rsa to create keys
	*  Print out the .pub (public key) - cat /home/odl_user/.ssh/id_rsa.pub
	* Copy ssh key (ssh-rsa) to place in the azure portal
* Upload ssh-keys to Github
	*  Go to Settings in your Github profile --> SSH and GPG Keys
	*  Select New SSH Keys and paste the copied keys and click on Add Keys
* Create scaffolding for the project (if not created)
	* Go to Github Repo and copy Clone with SSH address
	*  In the Azure terminal clone the repo using the following command - git clone git@github.com:xxxpegaxxx/testrepo.git 
	   * Results should look like this
	   
		![image](https://user-images.githubusercontent.com/101995184/196294981-11db30ae-9a76-4325-af1e-cb4d5bf9de6e.png)

	*  Change directory to project directory - cd cicd_p2/
* Create Makefile and requirements.txt
	* Run the touch command to create Makefile file
	* Insert in the Makefile the following commands
		* install:
			pip install --upgrade pip &&\
				pip install -r requirements.txt	
			
		* test:
			python -m pytest -vv test_hello.py
		
		* lint:
			pylint --disable=R,C hello.py
		
		* all: install lint test
	
	* Run the touch command to create requirements.txt file	
	* Insert in the requirements.txt the following modules
		* pytest
		* pylint
* Push changes into Github Repo		
	*  run the git status command to see the changes
	*  run the git add . command to add all the updated anew files 
	*  run the git commit -m "Adding a change to the README" command
	*  The folowing commands are only requireed if pushing for the first time
	 	* git config --global user.email "spackpega@aol.com
	  	* git config --global user.name "Carlos J Viera"
	*  run the Git push command to push the changes up to the repo
* Setting up Github Actions
	*  Go to the Actions Tab in your Github repo
	*  Select - Setup Workflow for ourselves
	*  Commit the main.yml file.
	*  Workflows should now be enabled

## Continuous Delivery

* Create a new repo (If non exist)
	*  Clone repo to shell using git clone command
* Create a virtual environment in terminal
	*  cd in to project
	*  run the floowing 2 commands
		* python3 -m venv ~/.p2_cicd
		* source ~/.p2_cicd/bin/activate
	*  Install modules by running the Run make all commans
	*  Results should look like this
	
		![image](https://user-images.githubusercontent.com/101995184/196295119-25b0843c-705f-466a-8a24-00e784199daa.png)

* Create app service in shell
	*  Run the following command - az webapp up -n cjvp2app to create the app service
	
	 	![image](https://user-images.githubusercontent.com/101995184/196295163-483eba87-1fe7-477e-b4fc-18ac5e5db12f.png)
	*  Verify that the app works - https://cjvp2app.azurewebsites.net	
	
		![image](https://user-images.githubusercontent.com/101995184/196295217-84786710-5901-40e5-98f6-77331c25adbc.png)
* Perform the prediction that returns back a JSON payload
	*  Update the following line in the make_predict_azure_app.sh to 
		-X POST https://cjvp2app.azurewebsites.net:$PORT/predict
	*  Run the prediction - 
		./make_predict_azure_app.sh
	*  If you get an access denied then run the following command to change the security
		chmod +x make_predict_azure_app.sh
	*  Retry running bash file again
	*  	./make_predict_azure_app.sh

* Got to Azure DevOps Organization
* Create a new project with the follwoing options
	*  Private
	*  Git
	*  Basic
* Create a new service connection
	*  Go to Project settings
	*  Go to Azure Resource Manager and Pipeline
	*  It should look like the below screenshot
	
	 	![image](https://user-images.githubusercontent.com/101995184/196294326-556b7c32-d5cf-48c2-a25f-bb013034bc66.png)


* Go to Pipelines in Project
	*  Create a new Pipeline
	*  Select your Github repository
	*  Pick Python to Linux WeApp on Azure
	*  Confirm that the YAML file has been created in your repository
	*  Pipeline should now Build and Deploy
	
		![image](https://user-images.githubusercontent.com/101995184/196295287-d7663126-de89-4e79-9120-fa21fd3b4e4c.png)

	* Here is the application running against a load test with locust
	
		![image](https://user-images.githubusercontent.com/101995184/196315362-3bb05004-67ce-44d0-b822-9f7c5bc5c526.png)



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
