import random
import time

# Placeholder functions for sending SMS and emails
def send_sms(phone_number, message):
    print(f"Sending SMS to {phone_number}: {message}")

def send_email(email_address, message):
    print(f"Sending email to {email_address}: {message}")

def generate_otp():
    otp = ""
    for _ in range(6):
        otp += str(random.randint(0, 9))
    return otp

def send_otp(recipient, recipient_type):
    otp = generate_otp()
    if recipient_type == "mobile":
        send_sms(recipient, f"Your OTP is: {otp}")
    elif recipient_type == "email":
        send_email(recipient, f"Your OTP is: {otp}")
    else:
        raise ValueError(f"Invalid recipient type: {recipient_type}")

def verify_otp(recipient, otp, recipient_type):
    # Implement a mechanism to store and retrieve OTPs for verification
    # Compare the provided OTP with the stored OTP for the recipient
    # Return True if they match, False otherwise
    pass

if __name__ == "__main__":
    recipient = input("Enter recipient (mobile number or email address): ")
    recipient_type = input("Enter recipient type (mobile or email): ")

    send_otp(recipient, recipient_type)

    # Simulate a delay for OTP expiration
    time.sleep(60)

    entered_otp = input("Enter OTP: ")
    if verify_otp(recipient, entered_otp, recipient_type):
        print("OTP verified successfully!")
    else:
        print("Invalid OTP!")
def generate_otp(length=6):
    otp = ""
    for i in range(length):
        otp += random.choice("0123456789")
    return otp
def generate_otp(length=6):
    otp = ""
    for i in range(length):
        otp += random.choice("0123456789")
    return otp
def verify_email_otp(otp, email):
    now = datetime.datetime.now()
    expiry_time = datetime.datetime.timestamp(now) + 180

    if otp != email_otps[email]:
        return False

    if expiry_time < now.timestamp():
        return False

    return True
def main():
    email = input("Enter your email address: ")

    # Generate an OTP
    otp = generate_otp()

    # Send the OTP
    send_email_otp(otp, email)

    # Verify the OTP
    user_otp = input("Enter the OTP sent to your email address: ")
    if verify_email_otp(user_otp, email):
        print("Your email address has been verified successfully!")
    else:
        print("Invalid OTP.")

if __name__ == "__main__":
    main()
