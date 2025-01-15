import smtplib

my_email = "100dopython@gmail.com"
gmail_password = "plkkkflgqyxpntxx"
# yahoo_password = "100DaysofPythonTest"

# connection = smtplib.SMTP("smtp.gmail.com")
# # connection = smtplib.SMTP("smtp.mail.yahoo.com")
#
# connection.starttls() # Encrypts message
# # TLS = Transport Layer Security
#
# connection.login(user=my_email, password=gmail_password)
# connection.sendmail(
#     from_addr=my_email,
#     to_addrs="dopython@yahoo.com",
#     msg="Subject:Hello\n\nThis is the body of my email."
# )
# connection.close()

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls() # Encrypts message
#     connection.login(user=my_email, password=gmail_password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="dopython@yahoo.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )

import datetime as dt
import random

now = dt.datetime.now()
year = now.year
month = now.month
weekday = now.weekday()

with open("quotes.txt", "r") as quotes:
    list_of_quotes = quotes.readlines()

if weekday == 4:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() # Encrypts message
        connection.login(user=my_email, password=gmail_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="dopython@yahoo.com",
            msg=f"Subject:{weekday}\n\n{random.choice(list_of_quotes)}"
        )
