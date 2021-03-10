import os, sys
from flask import Flask, request
from utils import wit_response
from pymessenger import Bot

app = Flask("My echo Bot")

PAGE_ACCESS_TOKEN = "EAATzGVXlz7YBAHYTQLi8EfEzFOnKrKo3RbDZBXStcE4t8TWvZC0OC8VLYqquJFIuu1rMfkxix8dCMbgXgUxXYL80KxiKKpAK1uIhZBT9jMskh2LxCGsVZAsV9RhdM2XPI8aDIzUYyPzwZCf8bGPQHQ2VIJwkkEU9FonrQHJae3QZDZD"

bot = Bot(PAGE_ACCESS_TOKEN)


@app.route('/', methods=['GET'])
def verify():
	# Webhook verification
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "hello":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():
	data = request.get_json()
	log(data)

	if data['object'] == 'page':
		for entry in data['entry']:
			for messaging_event in entry['messaging']:

				# IDs
				sender_id = messaging_event['sender']['id']
				recipient_id = messaging_event['recipient']['id']

				if messaging_event.get('message'):
					# Extracting text message
					if 'text' in messaging_event['message']:
						messaging_text = messaging_event['message']['text']
					else:
						messaging_text = 'no text'

					response = None

					entity, value = wit_response(messaging_text)
					if entity == 'location':
						response = "Ok, I will send you the weather of {}".format(str(value))
					elif entity == 'weather':
						response = "Ok, I will send you the {} of India".format(str(value))

					if response == None:
						response = "I have no idea what you are saying!"
						
					bot.send_text_message(sender_id, response)

	return "ok", 200


def log(message):
	print(message)
	sys.stdout.flush()


if __name__ == "__main__":
	app.run(debug = True, port = 80)
