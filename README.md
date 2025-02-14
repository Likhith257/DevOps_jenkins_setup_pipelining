# Jenkins with Pipeline Project Integration

This repository demonstrates how to set up Jenkins, configure it to pull a Python project from GitHub, and execute a Python script in a CI/CD pipeline.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation of Jenkins](#installation-of-jenkins)
- [Setting Up Jenkins for Pipeline Projects](#setting-up-jenkins-for-pipeline-projects)
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

- **Git**:  Jenkins uses Git to clone the repository. Install Git from [here](https://git-scm.com/downloads).

- **Java**: Jenkins requires Java to run. Install Java 8 or higher.
  
  #### Install Java (Linux):
  ```
  sudo apt update
  sudo apt install openjdk-21-jdk 
  ```

  #### Install Java (Windows):
  Download and install Java from the official Oracle website [here](https://www.oracle.com/java/technologies/downloads/#jdk21-windows).

- **Python**:  Jenkins will use Python to run your Python scripts. Install Python 3.8 or higher.

  #### Install Python (Linux):
  ```
  sudo apt update
  sudo apt install python3
  ```
  
  #### Install Python (Windows):
  Download and install Python from official Python website [here](https://www.python.org/downloads/).

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
Download the Jenkins installer from the official Jenkins website [here](https://www.jenkins.io/download).

## Setting Up Jenkins for Pipeline Projects
#### Install Jenkins Plugins

- **Plugins**: 
Go to Manage Jenkins > Manage Plugins > Available.
Search for Git Plugin and install it.
Search for Pipeline Plugin and install it
Similarly, search for Python Plugin and install it.

- **Configure Jenkins Job**:
Go to Jenkins Dashboard and click on New Item.
Enter a name for your job (e.g., "Pipelining GitHub Project") and select Pipeline project. Click Ok
Scroll down  to the Pipeline section and click on the "Pipeline script" dropdown menu and select "Pipeline script"
Click on Try Sample Pipeline "Hello World" to check and edit and paste the following code into the script editor:
```
pipeline {
    agent any

    environment {
        PYTHON_HOME = 'C:\\Users\\likhi\\AppData\\Local\\Programs\\Python\\Python312'  // Path to your Python installation
        PATH = "${PYTHON_HOME};${PATH}"   // Add Python to the system PATH

    }

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: '8cc37c72-394e-4d31-97f0-05b40a4a4f87', url: 'https://github.com/Likhithv257/DevOps_jenkins_setup_pipelining']]) //  Replace with your GitHub repository URL and credentials ID

            }
        }
        stage('Build') {
            steps {
                git branch: 'main', changelog: false, credentialsId: '8cc37c72-394e-4d31-97f0-05b40a4a4f87', poll: false, url: 'https://github.com/Likhithv257/DevOps_jenkins_setup_pipelining.git' //  Replace with your GitHub repository URL and credentials ID
                bat 'python sort.py' // or  use sh 'python3 sort.py' for Linux
            }
        }
        stage('Test') {
            steps {
                echo "Testing is done"
            }
        }
    }
}
```
This script will clone the repository, run the Python script, and then test the code. You can Save the job configuration.

## Running Python Script from GitHub Repo

Once you've set up the job:

Navigate to the job's page on Jenkins.

Click Build Now to manually trigger a build.

Jenkins will: Clone your GitHub repository.

Run the Python script specified in the pipeline configuration.

You can monitor the build progress and see detailed logs by clicking on Console Output after the build starts.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See LICENSE.txt for details.
