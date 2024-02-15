# Password Manager Bot - BotGenPass

This project is a Telegram bot for generating and storing passwords. The bot allows users to generate random passwords, store them securely, and view the history of created passwords.

## Functionality

- Generating random passwords of various lengths and complexities.
- Storing the last generated password and its creation date.
- Ability to view the history of created passwords.
- Encrypting passwords using a master key to ensure data security.

## Technologies

This project is implemented using the following technologies:

- Python 3.11
- [aiogram](https://github.com/aiogram/aiogram) - a framework for creating Telegram bots in Python.
- SQLite - for storing data about users and their passwords.
- [cryptography](https://github.com/pyca/cryptography) - for encrypting passwords.

## Setting Master Password

Before using the bot, you need to set the master password, which will be used to encrypt user password data. To do this, follow these steps:

1. Open the `main.py` file in your code editor.
2. Find the line where the master password is defined, for example: `password = b'Password'`.
3. Replace the value of the `password` variable with your master password. For example: `password = b'MyMasterPassword123'`.
4. Save the changes to the file.

Now the bot will use your master password to encrypt data, and you can start using it to generate and store passwords.

## Usage

To run the bot, follow these steps:

1. Install all dependencies by running `pip install -r requirements.txt`.
2. In the `connect.py` module, fill in the API_TOKEN obtained from [@BotFather](https://t.me/BotFather). 
3. Start the bot by running `python main.py`.

## Additional Information

This project was created as part of learning and can be further developed and extended to meet user needs. If you have any questions or suggestions for improving the project, feel free to contact! [@m1_leu](https://t.me/m1_leu)
