# how to use smtp to send email

# import smtplib
#
# my_email = "20bmiit019@gmail.com"
# password = "lfvhtfputojkurlx"
#
# # 587 port added because of TimeOutError
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     # Encrypt data
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="sahilladola18@gmail.com",
#         msg="Subject:test\n\nHello"
#     )

# how to get current date & time

# import datetime as dt
# # current date & time
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# # make object of any date
# dob = dt.datetime(year=2003, month=7, day=18)
# print(dob)

# motivation quotes

import datetime as dt
import random
import smtplib

day = dt.datetime.now().weekday()

with open("quotes.txt", "r") as file:
    data = file.readlines()
    quote = random.choice(data)

my_email = "20bmiit019@gmail.com"
password = "lfvhtfputojkurlx"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(my_email, password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="sahilladola18@gmail.com",
                        msg=f"Subject:Motivation quote\n\n{quote}"
                        )

# Birthday wisher
# import datetime as dt
# import random
# import smtplib
# import pandas as pd
# MY_EMAIL = "20bmiit019@gmail.com"
# PASSWORD = "lfvhtfputojkurlx"
#
# now = dt.datetime.now()
# current_day = now.day
# current_month = now.month
# today = (current_month, current_day)
#
# DOB = pd.read_csv("data/birthdays.csv")
#
# birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in DOB.iterrows()}
#
# if today in birthdays_dict:
#     letters = ("letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt")
#     letter = random.choice(letters)
#     with open(letter) as file:
#         person = birthdays_dict[today]
#         file_data = file.read()
#         actual_data = file_data.replace("[NAME]", person["name"])
#
#     with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, PASSWORD)
#         connection.sendmail(from_addr=MY_EMAIL,
#                             to_addrs=person["email"],
#                             msg=f"Subject:Happy Birthday\n\n{actual_data}")
