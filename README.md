# Temporary Email Generator

This Python script interacts with the 1secmail service API to generate a temporary email address, check for new messages, save them to text files, and delete the mailbox upon interruption.

## Setup

1. Install the necessary dependencies by running:
  pip install requests

2. Update the `domain_list` variable in the script with the desired domain names for email generation.

3. Run the script.


## Functionality

- `generate_username()`: Generates a random username consisting of lowercase letters and digits.
- `check_mail(mail)`: Checks for new messages in the mailbox associated with the provided email address.
- `delete_mail(mail)`: Deletes the mailbox associated with the provided email address.

## Usage

1. Run the script to generate a temporary email address and start checking for messages.
2. Press `Ctrl + C` to interrupt the program and delete the mailbox.

## Note

- The script saves each message to a separate text file in the `all_mails` directory.
- Ensure proper permissions and handling of sensitive information when using temporary email addresses.
