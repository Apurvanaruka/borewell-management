from dotenv import load_dotenv
from os import getenv

import twilio
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import random # generate random number

load_dotenv()

account_sid = getenv('ACCOUNT_SID')
auth_token = getenv('AUTH_TOKEN')
client = Client(account_sid, auth_token)


# Function to generate random OTP
def generate_otp():
    return ''.join(random.choices('0123456789', k=4))

# verify otp
def verify_otp(entered_otp, expected_otp):
    return entered_otp == expected_otp

# Function to send OTP via Twilio
def send_otp(recipient_number):
    return 1234
    otp = generate_otp()
    message = client.messages.create(
        body=f'Your Borewell Management System verification code is: {otp}',
        from_='+1 469 777 4238',
        to=recipient_number
    )
    print("OTP sent successfully!")
    return otp

# Replace RECIPIENT_NUMBER with the recipient's phone number
#recipient_number = '+919602119226'
#send_otp(recipient_number)

