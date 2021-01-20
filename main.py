##################### Hard Starting Project ######################
import pandas as pd
import datetime as dt
import os, random, smtplib


# get today's day and month
today = dt.datetime.today()
month = today.month
day = today.day


# get person's day and month
data = pd.read_csv("birthdays.csv")
birthday_info = pd.DataFrame.to_dict(data, orient="records")
person_month = birthday_info[0]["month"]
person_day = birthday_info[0]["day"]
person_name = birthday_info[0]["name"]


# email info
my_email = "email"
password = "password"
receiver = my_email
wishes = "Happy Birthday!"


if person_day == day and person_month == month:
    letter = random.choice(os.listdir("letter_templates"))
    with open(f"letter_templates/{letter}") as letter_:
        data = letter_.readlines()
        new_letter = [s.replace("[NAME]", person_name) for s in data]
        letter_format = "".join(new_letter)
    # send email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        fmt = 'From: {}\r\nTo: {}\r\nSubject: {}\r\n{}'
        connection.sendmail(
            my_email,
            receiver,
            fmt.format(my_email, receiver, wishes, letter_format).encode('utf-8')
        )




