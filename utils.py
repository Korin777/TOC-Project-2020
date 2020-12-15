import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage , FlexSendMessage


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""

def send_flex_message(reply_token, alt_text, contents):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, FlexSendMessage(alt_text = alt_text,contents = contents))

    return "OK"