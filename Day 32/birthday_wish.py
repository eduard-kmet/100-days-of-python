##################### Normal Starting Project ######################
import pandas as pd
import datetime as dt
import random
import smtplib
from dotenv import load_dotenv
import os
load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("MY_PASSWORD")

today_day = dt.datetime.now().day
today_month = dt.datetime.now().month
today_tuple = (today_month, today_day)


data = pd.read_csv("Day 32/birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]):data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    person = birthdays_dict[today_tuple]
    file_path = f"Day 32/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        msg = f"Subject:Happy Birthday\n\n{contents}.".encode("utf-8")
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=person["email"], msg=msg)
else:
    print("Nenachádza")




