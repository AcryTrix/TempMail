import requests
import random
import time
import string
import os

# API endpoint for 1secmail service
API = "https://www.1secmail.com/api/v1/"

# List of available domains for email generation
domain_list = [
    "1secmail.com",
    "1secmail.org",
    "1secmail.net"
]

# Randomly select a domain from the domain_list
domain = random.choice(domain_list)


def generate_username():
    """
    Generate a random username consisting of lowercase letters and digits.

    Returns:
        str: Randomly generated username
    """
    name = string.ascii_lowercase + string.digits
    username = ''.join(random.choice(name) for i in range(10))

    return username


def check_mail(mail=""):
    """
    Check for new messages in the mailbox associated with the provided email address.

    Args:
        mail (str): Email address to check for messages
    """
    req_link = f'{API}?action=getMessages&login={mail.split("@")[0]}&domain={mail.split("@")[1]}'
    r = requests.get(req_link).json()
    length = len(r)

    if length == 0:
        print(f"[?] На почте пока нет новый сообщений. Проверка происходит каждые 5 секунд!")
    else:
        id_list = []

        for i in r:
            for k, v in i.items():
                if k == 'id':
                    id_list.append(v)

        print(f"[+] На почте {length} сообщений.")

        # Create a directory to store mail files if it doesn't already exist
        current_dir = os.getcwd()
        final_dir = os.path.join(current_dir, 'all_mails')

        if not os.path.exists(final_dir):
            os.makedirs(final_dir)

        # Save each message to a separate text file
        for i in id_list:
            read_msg = f'{API}?action=readMessage&login={mail.split("@")[0]}&domain={mail.split("@")[1]}&id={i}'
            r = requests.get(read_msg).json()

            sender = r.get('from')
            subject = r.get('subject')
            date = r.get('date')
            content = r.get('textBody')

            mail_file_path = os.path.join(final_dir, f'{i}.txt')

            with open(mail_file_path, 'w') as f:
                f.write(f"Sender: {sender}\nTo: {mail}\nSubject: {subject}\nDate: {date}\n\n{content}")


def delete_mail(mail=''):
    """
    Delete the mailbox associated with the provided email address.

    Args:
        mail (str): Email address to delete the mailbox for
    """
    url = 'https://www.1secmail.com/mailbox'

    data = {
        'action': 'deleteMailbox',
        'login': mail.split("@")[0],
        'domain': mail.split("@")[1]
    }

    r = requests.post(url, data=data)
    print(f"[-] Ваш почтовый ящик {mail} был удален")


def main():
    """
    Main function to generate an email address, check for new messages, and handle interruptions.
    """
    try:
        # Generate a random username and create an email address
        username = generate_username()
        mail = f"{username}@{domain}"
        print(f"[+] Ваш электронный адрес: {mail}")

        # Check for new messages every 5 seconds
        while True:
            check_mail(mail=mail)
            time.sleep(5)
    except(KeyboardInterrupt):
        # Delete the mailbox if the program is interrupted
        delete_mail(mail=mail)
        print("\n[!] Программа прервана")


if __name__ == "__main__":
    main()