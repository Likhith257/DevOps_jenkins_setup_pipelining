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

### Installation of Jenkins
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
Download the Jenkins installer from the official Jenkins website. https://www.jenkins.io/download/