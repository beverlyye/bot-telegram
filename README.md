## Telegram Bot with python-telegram-bot

This Python script implements a Telegram bot using the python-telegram-bot library. The bot handles various commands (start, help, custom, upset, happy) and responds to messages based on predefined keywords. Threading is utilized for concurrent control, and the bot polls for updates every 3 seconds.


## Dependencies

python-telegram-bot


## Installation

Make sure you have the following installed:

- Python (version 3.6 or higher)
- `pip` (Python package installer)

1. Clone the Repository:

    ```bash
    git clone https://github.com/beverlyye/bot-telegram.git
    cd 
    ```

2. Install Dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Configure Bot Token:

    - Open the `main.py` file.
    - Replace the placeholder `6581449693:AAEIpCBITfHLgqgDTTH8mr71ucD3gCzaGpU` with this token

## Running the Bot

    ```bash
    python3 main.py
    ```

    The bot will start running, and you should see a message indicating that the bot is running with the provided token.


## Features

Command Handling: The bot responds to various commands, including start, help, custom, upset, and happy.
Keyword-based Responses: The bot responds to messages containing predefined keywords.
Threading: Threading is employed for concurrent control, allowing the bot to handle multiple tasks simultaneously.
Polling: The bot polls for updates every 3 seconds using the polling method.

## Bot Commands

The bot responds to the following commands:

- `/start`: Begin the conversation.
- `/help`: Get information about the bot.
- `/custom`: Use a custom command.
- `/upset`: Express what makes you sad.
- `/happy`: Share what makes you happy.

## Conversations and Responses

- The bot responds to messages with keywords such as "sad," "happy," "thank," etc.
- Customize responses based on keywords in the `take_response` function.

## Usage

- In a private chat, simply type your message, and the bot will respond.
- In a group chat, mention the bot's username (`@talk2m3bot`) followed by your message to receive a response.

## Error Handling

The bot includes error handling for unexpected issues. If you encounter any problems, check the console for error messages.

## Contributions

Feel free to contribute to the project by forking the repository, making improvements, and creating pull requests. If you encounter bugs or have suggestions, please open an issue.

## Stop the Bot

Press `Ctrl + C` in the terminal where the bot is running to stop it.


## Contributors

Beverly Adrien Octavianto

## Acknowledgments

Special thanks to the developers of python-telegram-bot for providing a powerful and easy-to-use library for Telegram bot development, and also the inspo and tutorial i got from the web freecode camp and the youtube channel Indently.