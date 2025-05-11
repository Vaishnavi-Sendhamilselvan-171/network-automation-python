# Network Automation with Python and Netmiko

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://www.python.org/)
[![Netmiko](https://img.shields.io/badge/Library-Netmiko-brightgreen)](https://github.com/ktbyers/netmiko)
[![Automation](https://img.shields.io/badge/Use%20Case-Network%20Automation-orange)]()


A simple and extensible network automation script using Python and Netmiko for automating configuration tasks on Cisco routers/switches.

## Table of Contents

- ## Overview
- ## Feature
- ## Project Structure
- ## Usage

## Overview

This project automates the process of connecting to multiple network devices via SSH and pushing common configuration commands using the *Netmiko* library.

It is ideal for:
- Networking beginners exploring Python
- Lab environments (e.g., GNS3, Packet Tracer)
- DevNet associate-level projects

## Features

- SSH login to multiple Cisco devices
- Execute and apply configuration from a file
- Modular and easy to update
- Clean logging/output

## Project Structure

- automate_config.py         # Main automation script
- device_list.txt            # List of devices (IP, type, username, password)
- config_commands.txt        # Cisco CLI commands to push
- README.md                  # Project documentation

## Usage

- Add devicedetails to device_list.txt 
- Add configuration commands in config_commands.txt
- ## How to Run
- 1. Clone this repository:
     ```bash
     git clone https://github.com/your-username/your-repo.git
     cd your-repo
- 2. Install required packages:
  pip install -r requirements.txt
- Run the script

You can run the python automate_config.py command in a terminal or command-line interface, depending on your operating system:

For Windows:
- Press Win + R, type cmd, and press Enter or open Command Prompt or PowerShell.
- Navigate to the directory containing automate_config.py using the cd command.
- Run the command:
python automate_config.py

For macOS / Linux:
- Open Terminal
- Navigate to the folder containing your script:
cd /path/to/your/script
- Run the command:
python automate_config.py

- Requirements:
Make sure Python is installed. You can check by running:
python --version 
or
python3 --version
