# Chatbot

## Overview
This chatbot provides answers to questions related to specific procedures. It's designed to help users get quick information without needing to search through documents or wait for human assistance. Built with Python and Flask, this chatbot is easy to deploy and customize.

## Features
- **Case Insensitive Matching**: Users can ask questions in any case.
- **Flexible Question Phrasing**: The chatbot can understand questions even if they're not phrased exactly as stored in the knowledge base.
- **Easy Customization**: Add, remove, or update questions and answers in the chatbot's knowledge base with minimal effort.

## Getting Started

### Prerequisites
- Python 3.6 or later
- Flask

### Installation
1. Clone the repository to your local machine:
`git clone https://yourrepositorylink.com/path/to/repo.git`
2. Navigate to the project directory: `Navigate to the project directory:`
3. Install the required Python packages: `pip install -r requirements.txt`


### Running the Chatbot
1. Start the Flask application: `python chatbot_app.py`
2. Open a web browser and navigate to `http://127.0.0.1:5000/` to start interacting with the chatbot.

## Customizing the Chatbot
To customize the chatbot's knowledge base, edit the `ProcedureChatbot` class in `chatbot_app.py`. Add or modify entries in the `knowledge_base` dictionary, where each key is a question and each value is the corresponding answer.

## Deployment
For instructions on deploying the chatbot to a web server, see the deployment section above. The process involves selecting a hosting service, setting up the environment, and deploying the Flask application.
