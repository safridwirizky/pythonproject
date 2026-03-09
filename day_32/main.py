import smtplib, os
from pathlib import Path
from random import randint
from datetime import datetime
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
my_mail = os.getenv("MY_EMAIL")
password = os.getenv("MY_PASSWORD")

# Get data from csv
df = pd.read_csv(BASE_DIR / "birthdays.csv")

# Check birthday date
today = datetime.now()
today_birthdays = df[
    (df['month'] == today.month) &
    (df['day'] == today.day)
]

# Open connection with Gmail
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_mail, password=password)

    for _, row in today_birthdays.iterrows():
        # Get letter from txt
        txt_path = BASE_DIR / "letter_templates" / f"letter_{randint(1,3)}.txt"
        with open(txt_path) as file:    
            content = file.read()
        personal_letter = content.replace("[NAME]", row['name'])

        # send email
        connection.sendmail(
            from_addr=my_mail,
            to_addrs=row['email'],
            msg=f"Subject:Hello {row['name']}\n\n{personal_letter}"
        )