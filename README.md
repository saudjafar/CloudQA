# Selenium Automation Script

This Python script utilizes Selenium to automate interactions with a web page. It performs certain actions on the web page specified in the script.

## Setup Instructions

Before running the script, please ensure that you have the following set up:

### 1. Python Installation

Make sure you have Python installed on your system. You can download the latest version of Python from the official website: [python.org/downloads](https://www.python.org/downloads/)

### 2. Chrome WebDriver Installation

The script uses Chrome WebDriver to interface with the Chrome browser. Follow these steps to set it up:

1. Check the version of your Chrome browser by opening Chrome and navigating to **Settings > About Google Chrome**.
2. Download the corresponding version of Chrome WebDriver from the official website: [chromedriver.chromium.org/downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads)
3. Extract the downloaded WebDriver executable.
4. Choose a location to store the WebDriver executable file. For example, you can create a directory named `C:/SeleniumDrvers`.
5. Update the `os.environ['PATH']` line in the script to point to the directory where the Chrome WebDriver executable is stored. For example:

   ```python
   os.environ['PATH'] += r"C:/SeleniumDrvers"

### 3. Install Dependencies

The script relies on the `selenium` package. Install it using the following command:

```bash
pip install selenium

## Running the Script

1. Open a command-line interface or terminal.
2. Navigate to the directory containing the Python script.
3. Execute the script using the following command:

   ```bash
   python test.py