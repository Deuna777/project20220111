$ pip install Flask
from flask import Flask, render_template, request, abort
from datetime import datetime, timezone, timedelta

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage
)
line_bot_api = LineBotApi("9XETPXQtMbASz5YHEsMYgi7QbIAQ3jdG1hBtnVBpG5zJG5gBIJUKBnky8P15GiGBz7g1gWsm4MBy1fhoUxCXE0tU5xTkEOrIuhViXHOVIiIYICEuGtmKTDcT3Iyikisb1wxF0CDnnABGYllW7KX9wQdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("de3b54eabda222f5828733f7484276cf")

app = Flask(__name__)



@app.route("/callback", methods=["POST"])

def callback():
    # get X-Line-Signature header value
    signature = request.headers["X-Line-Signature"]

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return "OK"

