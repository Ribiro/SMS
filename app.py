from flask import Flask
app = Flask(__name__)


# Sending SMS
# import package
import africastalking


# Initialize SDK
username = "#"    # use 'sandbox' for development in the test environment
# use your sandbox app API key for development in the test environment
api_key = "#"
africastalking.initialize(username, api_key)


# Initialize a service e.g. SMS
sms = africastalking.SMS

number = '0715785746'
code = '+254'
number = number[1:]
number = code + number
name = "George"


# Use the service synchronously
response = sms.send("Hello Message!" + name, [number])
print(response)















