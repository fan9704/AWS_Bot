import logging

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest
from linebot.v3 import WebhookHandler
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage,
    ImageMessage
)
from linebot.v3.webhooks import MessageEvent, TextMessageContent
from rest_framework import status
from rest_framework.response import Response

configuration = Configuration(access_token=settings.LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(settings.LINE_CHANNEL_SECRET)

logger = logging.getLogger(__name__)


def callback(request):
    if request.method == "POST":
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode()
        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            return Response(status=status.HTTP_400_BAD_REQUEST)  # Invalid Signature
        except Exception as E:
            print(E)
            return Response(status=status.HTTP_400_BAD_REQUEST)  # Exception
        return HttpResponse("Success.")  # Success
    else:
        return HttpResponseBadRequest()


# Basic Reply same word as user input
@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        keyword = event.message.text.lower().split()
        if "app介紹" in keyword:
            introduction(line_bot_api,event)
        elif "人物介紹" in keyword:
            userIntroduction(line_bot_api,event)
        elif "配對地點" in keyword:
            location(line_bot_api, event)
        elif "任務挑戰" in keyword:
            taskChallenge(line_bot_api, event)
        elif "使用者體驗" in keyword:
            userExperience(line_bot_api, event)
        elif "吃甚麼" in keyword:
            eatWhat(line_bot_api, event)
        else:
            line_bot_api.reply_message_with_http_info(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text=event.message.text)]
                )
            )

def eatWhat(line_bot_api, event):
    foodList = ["火鍋", "拉麵", "壽司", "咖哩飯", "Pizza"]
    response = []
    for food in foodList:
        response.append(
            TextMessage(text=f"{food}")
        )
    line_bot_api.reply_message_with_http_info(
        ReplyMessageRequest(
            reply_token=event.reply_token,
            messages=response
        )
    )
def introduction(line_bot_api, event):
    profile = line_bot_api.get_profile(event.source.user_id)
    username = profile.display_name

    # App Introduction
    response = [
        TextMessage(text="凜冬將至"),
        TextMessage(text="一年一度的聖誕夜即將來臨"),
        TextMessage(text="今天還是一個人嗎？"),
        TextMessage(text="快來看看這些優質男士"),
        TextMessage(text="給自己一個重獲新生的機會"),
    ]
    line_bot_api.reply_message_with_http_info(
        ReplyMessageRequest(
            reply_token=event.reply_token,
            messages=response
        )
    )
def location(line_bot_api, event):
    profile = line_bot_api.get_profile(event.source.user_id)

    response = []
    locationList = [
        "信義商圈", "中山商圈", "板橋耶誕城", "南紡購物中心", "華泰名品城"
    ]
    for district in locationList:
        response.append(TextMessage(text=f"{district}!"))
    line_bot_api.reply_message_with_http_info(
        ReplyMessageRequest(
            reply_token=event.reply_token,
            messages=response
        )
    )
def taskChallenge(line_bot_api, event):
    profile = line_bot_api.get_profile(event.source.user_id)
    username = profile.display_name

    response = []
    taskList = [
        "雙人吃pocky", "頭套絲襪", "對視十秒", "十連拍", "交互蹲跳20下"
    ]
    # User Introduction
    for task in taskList:
        response.append(TextMessage(text=f"{task}!"))
    line_bot_api.reply_message_with_http_info(
        ReplyMessageRequest(
            reply_token=event.reply_token,
            messages=response
        )
    )
def userExperience(line_bot_api, event):
    profile = line_bot_api.get_profile(event.source.user_id)

    response = []
    experienceList = [
        "今天配對到的人還滿意嗎？","一到五顆星你願意給他幾顆呢？","有留下後續聯絡方式了嗎？","有後續約出來嗎"
    ]
    # User Introduction
    for experience in experienceList:
        response.append(TextMessage(text=f"{experience}"))
    response.append(
        ImageMessage(
            original_content_url = "https://line-workshop-test.s3.amazonaws.com/06_developing.png",
            preview_image_url = "https://line-workshop-test.s3.amazonaws.com/06_developing.png",
        ),
    )
    line_bot_api.reply_message_with_http_info(
        ReplyMessageRequest(
            reply_token=event.reply_token,
            messages=response
        )
    )
def userIntroduction(line_bot_api, event):
    profile = line_bot_api.get_profile(event.source.user_id)
    username = profile.display_name

    response = []
    userList = [
        "羅",
        "沈",
        "Neil",
        "FKT",
        "柏均",
    ]
    # User Introduction
    for user in userList:
        response.append(TextMessage(text=f"Hi 我叫做{user}!"))
    line_bot_api.reply_message_with_http_info(
        ReplyMessageRequest(
            reply_token=event.reply_token,
            messages=response
        )
    )
