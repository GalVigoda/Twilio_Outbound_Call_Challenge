from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC3d41a378faff3b92d1582db214266627"
# Your Auth Token from twilio.com/console
auth_token  = "d8307b685e0429839281a80843bb163d"

client = Client(account_sid, auth_token)

call = client.calls.create(
    to="+972524215556",
    from_="+14435507034",
    url="https://handler.twilio.com/twiml/EHf5d7bec7ba96e4472be7b0eb5559392b"



)

print(message.sid)
##523632205##