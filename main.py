import csv
from email.message import EmailMessage
import smtplib

# Caching the credentials at a script-level to avoid reading file each time
# Function to get email address and password from file
def get_credentials(filepath):
    with open(filepath, "r") as f:
        email_address = f.readline().strip()  # strip to remove unnecessary newlines
        email_pass = f.readline().strip()
    return email_address, email_pass

# Global variables for email credentials
email_address, email_pass = get_credentials("./credentials.txt")

# Function to login to the SMTP server
def login(s):
    s.ehlo()
    # start TLS for security
    s.starttls()
    s.ehlo()
    # Authentication
    s.login(email_address, email_pass)
    print("Logged in")

# Function to prepare and send email
def send_mail():
    # Initializing the SMTP server
    s = smtplib.SMTP("smtp.gmail.com", 587)
    login(s)
    # message to be sent
    subject = "Weekly Project Update"
    body = """
    Dear Team,

    Please find the updates for our ongoing projects this week:

    1. Project X: ...
    2. Project Y: ...
    3. Project Z: ...

    Please do not hesitate to reach out if you have any questions or concerns. 

    Best,
    [Your Name]
    """
    message = EmailMessage()
    message.set_content(body)
    message['Subject'] = subject
    message['From'] = email_address

    # Open the csv file with email addresses
    with open("emails.csv", newline="") as csvfile:
        # Read emails one by one
        email_reader = csv.reader(csvfile, delimiter=" ", quotechar="|")
        for email in email_reader:
            message['To'] = email[0]
            # Send the email
            s.send_message(message)
            print("Sent to " + email[0])

    # terminating the session
    s.quit()
    print("Emails sent")

if __name__ == "__main__":
    send_mail()