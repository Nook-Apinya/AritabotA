from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('qBpiQjKeUZOKYG1jc1jMOcMEFJs3p7BLv7g8ZH8JC5qGVQSv4XDwHAgRtWGr463O/r5NE4cJXpw/NPVUCenl2z6Cwis6m8HVvmG8ftku7Z9SvpORORlaR0BEF5L//YJH4Eaf48h3achDqmeiEppn7wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('cbe045731caced5c132e9b3e51aa7178')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='Hello World!'))
    #line_bot_api.push_message(to, TextSendMessage(text='Hello World!'))
    


if __name__ == "__main__":
    app.run()
