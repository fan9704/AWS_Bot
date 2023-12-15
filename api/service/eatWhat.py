from linebot.v3.messaging import (
    ReplyMessageRequest,
    TextMessage
)


def eatWhat(line_bot_api, event):
    foodList = ["壽司","拉麵","鐵板燒","咖哩飯","Pizza"]
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
