# utils.py
import africastalking
from .config import AFRICASTALKING_USERNAME, AFRICASTALKING_API_KEY

# Initialize Africa's Talking
africastalking.initialize(AFRICASTALKING_USERNAME, AFRICASTALKING_API_KEY)
sms = africastalking.SMS

def send_sms(phone_number, message):
    try:
        response = sms.send(message, [phone_number])
        return response
    except Exception as e:
        return str(e)
