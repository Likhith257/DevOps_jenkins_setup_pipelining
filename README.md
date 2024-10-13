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
  ```bash
  sudo apt update
  sudo apt install openjdk-11-jdk or download jdk deb package in https://www.oracle.com/java/technologies/downloads/#jdk21-linux

  #### Install Java (Windows):
  Download and install Java from the official Oracle website. https://www.oracle.com/java/technologies/downloads/#jdk21-windows
  