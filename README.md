# Email Sending Script

## Description

This is a Python script designed to automatically send email updates about project status to a list of recipients. The email content and the list of recipients are customizable.

## Requirements

-   Python 3.6 or higher.
-   The smtplib and csv libraries, which are part of the Python Standard Library.

## Setup

1.  Ensure that Python and necessary libraries are installed on your system.
2.  Replace the contents of the "credentials.txt" file with your Gmail address on the first line and your Gmail password on the second line. Make sure this file is in the same directory as the script.
3.  In the "emails.csv" file, add the email addresses of the recipients. Each email address should be on a new line. This file should also be in the same directory as the script.
4.  Customize the subject and body variables in the script with your preferred subject line and body text.

## Usage

To run the script, use the following command in your terminal:

shCopy code

`python email_script.py` 

The script logs into the SMTP server with the provided credentials, composes an email with the provided subject and body, then sends the email to each recipient in the "emails.csv" file.

## Note

The script uses an unencrypted connection. It is advised not to use your main email for this, as your password is stored in plaintext. Instead, consider creating a new, separate Gmail account for this task.

This script is designed for Gmail SMTP servers. If you are using a different email provider, you may need to adjust the SMTP server and port.
