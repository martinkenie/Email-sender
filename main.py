import csv
import datetime as dt
import smtplib
import random

my_mail = "" #input your email
password = "" #input password obtained from gmail or yahoo app or other service provider
birthdays_dict={}

with open("birthdays.csv" , mode="r") as file:
    reader = csv.reader(file)
    
    # Iterate over rows
    for row in reader:
        if row[0] == "name":
            pass
        else:
            fields = row
            month = int(fields[3])
            day = int(fields[4])
            name = fields[0]
            email = fields[1]
            dict = {
                (month, day): [name , email],
            }
            birthdays_dict.update(dict)

    
today = dt.datetime.now()
today_month = today.month
today_day = today.day
key = (today_month , today_day)

if key in birthdays_dict:
    with open (f"./letter_templates/letter_{random.randint(1,3)}.txt" , mode="r") as text:
        my_text = text.read()
    
    message = my_text.replace("[NAME]" , f"{birthdays_dict[key][0]}")
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
        connection.starttls()
        connection.login(user=my_mail , password = password)
        connection.sendmail(from_addr=my_mail , to_addrs=f"{birthdays_dict[key][1]}" , msg=f"Subject:BIRTHDAY WISH  \n\n {message}")
        print("Success")


#HOST ON THE CLOUD WITH https://www.pythonanywhere.com