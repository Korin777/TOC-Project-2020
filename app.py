import os
import sys
import threading

from flask import Flask, jsonify, request, abort, send_file, make_response
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage


from selenium import webdriver
import time
import requests

from fsm import TocMachine
from utils import send_text_message


chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless") #無痕模式
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
# print(driver.get_window_size())
driver.set_window_size(1024, 768) 
url = 'https://accounts.pixiv.net/login?return_to=https%3A%2'+"F%"+"2Fwww.pixiv.net"+"%"+'2F&lang=zh_tw&source=pc&view_type=page'
# driver = webdriver.Chrome('./chromedriver', chrome_options=options)
driver.get(url)

input = driver.find_element_by_id("LoginComponent").find_elements_by_tag_name("input")
input[0].send_keys('k777k777tw123@gmail.com')
input[1].send_keys('ko95701ko')
input[1].submit()

# driver2 = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
# # print(driver.get_window_size())
# driver2.set_window_size(1024, 768)
# driver2.get("https://www.pixiv.net/ranking.php")


load_dotenv()


machine = TocMachine(driver = driver,#driver2 = driver2,
    states=["initial", "menu", "pixiv", "find_pixiv_id","instruction","find_artist_artwork","walk_around","download", "fsm"],
    transitions=[   
        {"trigger": "advance", "source": "initial", "dest": "menu", "conditions": "is_going_to_menu"},
        {"trigger": "advance", "source": ["menu","find_pixiv_id"], "dest": "pixiv", "conditions": "is_going_to_pixiv"},
        {"trigger": "advance", "source": "pixiv", "dest": "find_pixiv_id", "conditions": "is_going_to_find_pixiv_id"},
        {"trigger": "advance", "source": "*", "dest": "menu", "conditions": "is_going_to_menu"},
        {"trigger": "advance", "source": "*", "dest": "instruction", "conditions": "is_going_to_instruction"},
        {"trigger": "advance", "source": "*", "dest": "fsm", "conditions": "is_going_to_fsm"},
        {"trigger": "advance", "source": "find_pixiv_id", "dest": "find_artist_artwork", "conditions": "is_going_to_find_artist_artwork"},
        {"trigger": "advance", "source": "pixiv", "dest": "walk_around", "conditions": "is_going_to_walk_around"},
        {"trigger": "advance", "source": "find_pixiv_id", "dest": "download", "conditions": "is_going_to_download"},

        {"trigger": "back_artist_artwork", "source": "download", "dest": "find_artist_artwork"},
        {"trigger": "back_pixiv", "source": ["find_pixiv_id","walk_around"], "dest": "pixiv"},
        {"trigger": "back_id", "source": "find_artist_artwork", "dest": "find_pixiv_id"},
        {"trigger": "ins_back_ini", "source": ["instruction","fsm"], "dest": "initial"},
        {"trigger": "ins_back_menu", "source":  ["instruction","fsm"], "dest": "menu"},
        {"trigger": "ins_back_pix", "source":  ["instruction","fsm"], "dest": "pixiv"},
        {"trigger": "ins_back_find", "source":  ["instruction","fsm"], "dest": "find_pixiv_id"}
    ],
    initial="initial",
    auto_transitions=False,
    show_conditions=True,
)


app = Flask(__name__, static_url_path="")


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


class MyWorker():

    def __init__(self,events,body):
        self.events = events
        self.body = body
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        # if event is MessageEvent and message is TextMessage, then echo text
        for event in self.events:
            if not isinstance(event, MessageEvent):
                continue
            if not isinstance(event.message, TextMessage):
                continue
            if not isinstance(event.message.text, str):
                continue
            print(f"\nFSM STATE: {machine.state}")
            print(f"REQUEST BODY: \n{self.body}")
            response = machine.advance(event)
            if response == False:
                send_text_message(event.reply_token, "Not Entering any State")




@app.route('/', methods=['GET'])
def display_img():
    if request.method == 'GET':
        image_data = open("fsm.png", "rb").read()
        response = make_response(image_data)
        response.headers['Content-Type'] = 'image/jpg'
        return response
    else:
        pass


@app.route('/download')
def downloadFile ():
    path = "img/archive.zip"
    return send_file(path, as_attachment=True)



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

    # # if event is MessageEvent and message is TextMessage, then echo text
    # for event in events:
    #     if not isinstance(event, MessageEvent):
    #         continue
    #     if not isinstance(event.message, TextMessage):
    #         continue
    #     if not isinstance(event.message.text, str):
    #         continue
    #     print(f"\nFSM STATE: {machine.state}")
    #     print(f"REQUEST BODY: \n{body}")
    #     response = machine.advance(event)
    #     if response == False:
    #         send_text_message(event.reply_token, "Not Entering any State")
    MyWorker(events,body)

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
