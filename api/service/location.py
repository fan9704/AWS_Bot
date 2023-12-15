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
