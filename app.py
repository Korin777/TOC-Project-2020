import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
from bs4 import BeautifulSoup


load_dotenv()


machine = TocMachine(
    states=["initial", "menu", "pixiv", "find_pixiv_id", "state2"],
    transitions=[
        {"trigger": "advance", "source": "initial", "dest": "menu", "conditions": "is_going_to_menu"},
        {"trigger": "advance", "source": "menu", "dest": "pixiv", "conditions": "is_going_to_pixiv"},
        {"trigger": "advance", "source": "pixiv", "dest": "find_pixiv_id", "conditions": "is_going_to_find_pixiv_id"},
        {"trigger": "advance","source": "menu","dest": "state2","conditions": "is_going_to_state2"},
        {"trigger": "go_back", "source": ["pixiv", "state2"], "dest": "initial"},
        {"trigger": "advance", "source": ["pixiv", "state2","find_pixiv_id"], "dest": "menu", "conditions": "is_going_to_menu"}
    ],
    initial="initial",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")

# os.environ['LINE_CHANNEL_SECRET'] = 'b98212fb58db63b10770e6ab8abf47d7'
# os.environ['LINE_CHANNEL_ACCESS_TOKEN'] = 'VzJCjfnMQl2ILx68AdawvJEWf9f8LIH9w3Ue3wdkJHkoOBP8U4DCMrtLaQN7d2JtORLTTCW0vU5cOiXNtVEbF03/Qg6nIAXphWI8D1PWMUa7tXzx9XFnWXNV3pfhDrFiXRyqLv6L82qQXOhdGgOfHwdB04t89/1O/w1cDnyilFU='


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)

# @app.route("/")
# def home():
#     return "hello flask"


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "Not Entering any State")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
