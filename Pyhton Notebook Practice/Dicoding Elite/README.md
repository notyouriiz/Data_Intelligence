# Sleep Health Dashboard

This repository contains a Streamlit dashboard application designed to provide insightful visualizations and data analysis from [sleep health dataset](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset/). Follow the instructions below to set up and run the application.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setting Up the Environment](#setting-up-the-environment)
  - [Clone the Repository](#clone-the-repository)
  - [Create a Virtual Environment](#create-a-virtual-environment)
  - [Activate the Virtual Environment](#activate-the-virtual-environment)
  - [Install Required Packages](#install-required-packages)
- [Running the Streamlit Application](#running-the-streamlit-application)
  - [Run the Streamlit Application](#run-the-streamlit-application)
  - [Stopping the Application](#stopping-the-application)
- [Additional Notes](#additional-notes)

## Prerequisites

Make sure you have the following installed on your system:

- Python 3.10 or higher
- pip (Python package installer)

## Setting Up the Environment

### Clone the Repository

Start by cloning this repository to your local machine. Open your terminal and run:

```bash
git clone https://github.com/ivandrian11/sleep-health-dashboard.git
cd sleep-health-dashboard
```

### Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies for your project. You can create a virtual environment using the following command:

```bash
python -m venv venv
```

This command creates a directory named `venv` in your project folder, which will contain the virtual environment.

### Activate the Virtual Environment

Activate the virtual environment using the appropriate command for your operating system:

- On Windows:

  ```bash
  venv\Scripts\activate
  ```

- On macOS and Linux:

  ```bash
  source venv/bin/activate
  ```

After activation, your terminal prompt will change to indicate that the virtual environment is active.

### Install Required Packages

Once the virtual environment is activated, install the required packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

This will install all the necessary dependencies for the Streamlit application.

## Running the Streamlit Application

### Navigate to the Dashboard Directory

Ensure you are in the directory where `main.py` is located. If you are not already there, use the following command:

```bash
cd dashboard
```

### Run the Streamlit Application

Start the Streamlit application by executing the following command:

```bash
streamlit run main.py
```

This command will start the Streamlit server and provide you with a local URL (usually `http://localhost:8501`) to view the dashboard in your web browser.

### Stopping the Application

To stop the Streamlit application, you can use `Ctrl + C` in the terminal where the server is running.

## Additional Notes

- Make sure to deactivate the virtual environment when you're done working by running:

  ```bash
  deactivate
  ```

- If you make changes to the code or install new packages, you might need to restart the Streamlit server to see the changes reflected.

- For more information on Streamlit features and functions, refer to the [Streamlit Cheat Sheet](https://docs.streamlit.io/develop/quick-reference/cheat-sheet).

- To learn how to deploy your Streamlit application, check the instructions at [Deploying Streamlit Apps](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app).
