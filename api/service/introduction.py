from linebot.v3.messaging import (
    ReplyMessageRequest,
    TextMessage
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
