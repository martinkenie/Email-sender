##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

import csv
import datetime as dt
import smtplib
import random

my_mail = "simprotten@gmail.com"
password = "mpgviygkorjvammp"
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


