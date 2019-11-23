from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests

app = Flask(__name__)


@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World!'


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body','').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    if 'hi' in incoming_msg or 'hello' in incoming_msg:
        msg.body('Hey Arun! Whats up?')
        responded = True

    if 'quote' in incoming_msg:
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'Hey! I could not retrieve a quote at this time, Sorry :('
        msg.body(quote)
        responded = True

    if 'cat' in incoming_msg:
        msg.media('https://cataas.com/cat')
        responded = True

    if 'dog' in incoming_msg:
        msg.media('https://dog.ceo/api/breeds/image/random')
        responded = True

    if not responded:
        msg.body('I only know famous quotes and cats, Sorry :(')

    return str(resp)


if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
