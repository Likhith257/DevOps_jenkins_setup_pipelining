# Jenkins with Python Project Integration

This repository explains how to set up Jenkins, configure it to pull a Python project from GitHub, and execute a Python script.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation of Jenkins](#installation-of-jenkins)
- [Setting Up Jenkins for Python Projects](#setting-up-jenkins-for-python-projects)
- [Running Python Script from GitHub Repo](#running-python-script-from-github-repo)
- [Contributing](#contributing)
- [License](#license)

## Introduction
[Jenkins](https://www.jenkins.io/) is an open-source automation server used for Continuous Integration (CI) and Continuous Delivery (CD). This guide covers the installation of Jenkins and how to set it up to run a Python script stored in a GitHub repository.

## Features
- Jenkins installation on various OS
- Setup for running Python scripts
- GitHub repository integration with Jenkins
- Automation for continuous integration

## Installation of Jenkins

### Prerequisites
Before you install Jenkins, ensure that you have the following:
- **Java**: Jenkins requires Java to run. Install Java 8 or higher.
  
  #### Install Java (Linux):
  ```
  sudo apt update
  sudo apt install openjdk-21-jdk 
  ```

  #### Install Java (Windows):
  Download and install Java from the official Oracle website. https://www.oracle.com/java/technologies/downloads/#jdk21-windows

- **Python**:  Jenkins will use Python to run your Python scripts. Install Python 3.8 or higher.

  #### Install Python (Linux):
  ```
  sudo apt update
  sudo apt install python3
  ```
  
  #### Install Python (Windows):
  Download and install Python from official Python website. https://www.python.org/downloads/

### Install Jenkins
- **Linux** (Ubuntu/Debian):
```
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc \
    https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]" \
    https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
    /etc/apt/sources.list.d/jenkins.list > /dev/null  
sudo apt update
sudo apt install jenkins
```

- **Windows**:
Download the Jenkins installer from the official Jenkins website. https://www.jenkins.io/download

## Setting Up Jenkins for Python Projects
#### Install Jenkins Plugins
- **Git Plugin**: This allows Jenkins to pull code from a GitHub repository.
Go to Manage Jenkins > Manage Plugins > Available.
Search for Git Plugin and install it.
Python Plugin: This allows Jenkins to run Python scripts.
Similarly, search for Python Plugin and install it.

- **Configure Jenkins Job**:
Go to Jenkins Dashboard and click on New Item.
Enter a name for your job (e.g., "Python GitHub Project") and select Freestyle project.
Under Source Code Management, choose Git and enter your GitHub repository URL:

https://github.com/yourusername/your-repo.git
Add a Build Step:

For Linux: Execute Shell

bash
Copy code
python3 your_script.py
For Windows: Execute Windows batch command

bash
Copy code
python your_script.py
Save the job configuration.