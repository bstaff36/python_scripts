from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)


# Posting to a Slack channel
def send_message_to_slack(text):
    from urllib import request, parse
    import json
 
    post = {"text": "{0}".format(text)}
 
    try:
        json_data = json.dumps(post)
        req = request.Request("https://hooks.slack.com/services/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",
                              data=json_data.encode('ascii'),
                              headers={'Content-Type': 'application/json'}) 
        resp = request.urlopen(req)
    except Exception as em:
        print("EXCEPTION: " + str(em))
 
while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if current_time == "06:30:00":
        send_message_to_slack("Yo, I'm up.")
 