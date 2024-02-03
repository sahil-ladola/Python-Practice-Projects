import smtplib
import os
MY_GMAIL = os.environ.get("MY_GMAIL")
PASSWORD = os.environ.get("PASSWORD")


class NotificationManager:
    def send_emails(self, emails, message):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_GMAIL, PASSWORD)
            for email in emails:
                connection.sendmail(from_addr=MY_GMAIL,
                                    to_addrs=email,
                                    msg=f"Subject:Flight Lowest Price Alert!!!\n\n{message}".encode('utf-8')
                                    )
