from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC3d41a378faff3b92d1582db214266627"
# Your Auth Token from twilio.com/console
auth_token  = "d8307b685e0429839281a80843bb163d"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+972524215556",
    from_="+972524215556",
    body="Hello from Python!")

print(message.sid)
##523632205##