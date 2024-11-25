# Project Title

This is an part of the sarr-mal api process that involves getting OAuth from google to load gemini.
You can read more about this OAuth Authenication process here https://developers.google.com/identity/protocols/oauth2


---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Usage](#usage)

---


## Prerequisites

List the tools, libraries, and versions required to run the code.

- Python 3.x
- Required libraries: `example-library`, `another-library`

---

## Installation

Step-by-step guide to install the dependencies and set up the environment.

```bash
# Clone the repository
git clone https://github.com/your-username/your-project.git

# Navigate to the project directory
cd your-project

# Install dependencies
pip install -r requirements.txt
```

## Usage

1. Go to [Google Cloud Console](https://console.cloud.google.com) and create a new project.
2. Set up your OAuth credentials with the type set to **Desktop Application**.
3. Download the `client.json` file and place it in your project folder.
4. Open `testing-gemini.py` and update the model link to point to your own Gemini model.
   ```python
   # Example:
   model_link = "your_gemini_model_link_here"
5. The setup is complete! You can now test your Gemini model by running the script.