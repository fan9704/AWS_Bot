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
    TextMessage
)
from linebot.v3.webhooks import MessageEvent, TextMessageContent
from rest_framework.response import Response


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
