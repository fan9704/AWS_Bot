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
from rest_framework.response import Response


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
