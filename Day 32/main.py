# import smtplib

# my_email = "eduard.kmet1@gmail.com"
# password = "itdm zorz jtpx uncp"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user = my_email, password=password)
#     connection.sendmail(from_addr=my_email, 
#                         to_addrs="eduard.kmet3@gmail.com", 
#                         msg="Subject:Hello\n\nThis is the body of my email."
#                         )

 

import smtplib
import datetime as dt
import random


MY_EMAIL = "eduard.kmet1@gmail.com"
PASSWORD = "itdm zorz jtpx uncp"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 5:
    with open("Day 32/quotes.txt", encoding="utf-8") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
        
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        msg = f"Subject:Monday Motivation\n\n{quote}.".encode("utf-8")
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="eduard.kmet3@gmail.com", msg=msg)
