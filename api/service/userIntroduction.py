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
