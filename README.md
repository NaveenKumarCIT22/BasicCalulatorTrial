# Git Setup and Pushing Code to GitHub: A Step-by-Step Guide

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Setting Up Git](#setting-up-git)
    - [Windows](#windows)
    - [Linux](#linux)
3. [Creating a GitHub Account](#creating-a-github-account)
4. [Pushing Code to GitHub](#pushing-code-to-github)

## Prerequisites
- Basic knowledge of command line operations.
- A code editor (optional but recommended).

## Setting Up Git

### Windows
1. **Download Git:**
   - Visit the official Git website: [Git for Windows](https://git-scm.com/download/win).
   - Download the installer and run it.

2. **Install Git:**
   - Follow the installation steps, choosing the default options.
   - During installation, ensure the option "Git Bash Here" is selected.

3. **Verify Installation:**
   - Open **Git Bash** or **Command Prompt** and run:
     ```bash
     git --version
     ```

### Linux
1. **Install Git:**
   - Open a terminal and run the following command based on your distribution:
     - **Ubuntu/Debian:**
       ```bash
       sudo apt update
       sudo apt install git
       ```
     - **Fedora:**
       ```bash
       sudo dnf install git
       ```
     - **Arch Linux:**
       ```bash
       sudo pacman -S git
       ```

2. **Verify Installation:**
   - Run the following command in your terminal:
     ```bash
     git --version
     ```

## Creating a GitHub Account
1. **Sign Up:**
   - Go to [GitHub](https://github.com) and click on "Sign up".
   - Follow the instructions to create your account.

2. **Configure Git with GitHub:**
   - Set your username and email (used in your GitHub account) in Git:
     ```bash
     git config --global user.name "Your Name"
     git config --global user.email "your-email@example.com"
     ```

## Pushing Code to GitHub
1. **Create a Repository on GitHub:**
   - Log in to your GitHub account.
   - Click on the "+" icon in the top-right corner and select "New repository".
   - Name your repository, add a description, and click "Create repository".

2. **Initialize a Local Repository:**
   - Navigate to your project directory in the terminal:
     ```bash
     cd /path/to/your/project
     ```
   - Initialize Git:
     ```bash
     git init
     ```
   - Add your files to the staging area:
     ```bash
     git add .
     ```
   - Commit your changes:
     ```bash
     git commit -m "Initial commit"
     ```

3. **Connect to GitHub and Push Code:**
   - Add the GitHub repository as a remote:
     ```bash
     git remote add origin https://github.com/your-username/your-repository.git
     ```
   - Push your code to GitHub:
     ```bash
     git push -u origin master
     ```

4. **Verify Your Code on GitHub:**
   - Go to your GitHub repository URL to see your pushed code.

## Conclusion
You've successfully set up Git on your system, created a GitHub account, and pushed your code to GitHub! You're now ready to collaborate on projects and manage your code efficiently.

--- 

This README is designed to guide beginners through the process of setting up Git and pushing their first code to GitHub.
