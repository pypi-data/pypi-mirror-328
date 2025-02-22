import contextlib
import html
import logging
import os

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

import hkkang_utils.misc as misc_utils
import hkkang_utils.socket as socket_utils

# Load environment variables
misc_utils.load_dotenv(stack_depth=2)
# Get default access token
DEFAULT_ACCESS_TOKEN = (
    os.environ["SLACK_ACCESS_TOKEN"] if "SLACK_ACCESS_TOKEN" in os.environ else None
)

logger = logging.getLogger("SlackMessenger")


class SlackMessenger:
    """A Slack messaging wrapper for sending messages with an optional short preview.

    Example:
        messenger = SlackMessenger(channel="test-channel")
        messenger.send_message("Hello World")
    """

    def __init__(
        self,
        channel: str,
        token: str = DEFAULT_ACCESS_TOKEN,
        append_src_info: bool = True,
    ):
        self.channel = channel
        self.token = token
        self.append_src_info = append_src_info
        self.__post_init__()

    def __post_init__(self):
        if self.token is None:
            raise ValueError(
                """Please set token or set SLACK_ACCESS_TOKEN environment variable.
                    If you don't have the access token, follow the tutorial 
                    to get bot OAuthToken and setup the bot permissions. 
                    https://github.com/slackapi/python-slack-sdk/tree/main/tutorial"""
            )

    def send(self, text: str, short_preview: bool = False) -> None:
        """Send a Slack message with optional short preview.

        :param text: The message content (could be long)
        :param short_preview: If True, send a short preview with an expandable option.
        """

        send_message(
            token=self.token,
            channel=self.channel,
            text=text,
            short_preview=short_preview,
            append_src_info=self.append_src_info,
        )


def send_message(
    channel: str,
    text: str,
    token: str = DEFAULT_ACCESS_TOKEN,
    short_preview: bool = False,
    append_src_info: bool = True,
) -> None:
    """Send a Slack message with an optional short preview.

    :param channel: Slack channel name or ID
    :param text: Message content
    :param token: Slack bot token
    :param short_preview: If True, send only a short preview with a button to expand
    :param append_src_info: Whether to include source info in the message
    """
    if token is None:
        raise ValueError(
            "Please set token or set SLACK_ACCESS_TOKEN environment variable."
        )

    client = WebClient(token=token)

    if append_src_info:
        ip = socket_utils.get_local_ip()
        host_name = socket_utils.get_host_name()
        text_with_prefix = f"Message from {host_name}({ip}):\n{text}"
    else:
        text_with_prefix = text

    # If short preview is enabled, truncate text and add a "Show More" button
    if short_preview:
        lines = text_with_prefix.split("\n")
        preview_text = "\n".join(lines[:5]) + "\n..."
        full_text = f"```{text_with_prefix}```"

        message_blocks = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"Here’s a preview:\n```{preview_text}```",
                },
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "Show Full Code"},
                        "value": full_text,
                        "action_id": "show_code",
                    }
                ],
            },
        ]

        try:
            client.chat_postMessage(channel=channel, blocks=message_blocks)
            logger.info(f"Sent preview message to {channel}: {preview_text}")
        except SlackApiError as e:
            logger.error(f"Error sending message: {e.response['error']}")
    else:
        try:
            response = client.chat_postMessage(
                channel=channel, text=f"```{text_with_prefix}```"
            )
            decoded_text = html.unescape(response["message"]["text"])
            assert decoded_text == f"```{text_with_prefix}```", f"{decoded_text}"
            logger.info(f"Sending message to channel {channel}: {text_with_prefix}")
        except SlackApiError as e:
            logger.error(f"Error sending message: {e.response['error']}")


@contextlib.contextmanager
def notification(
    channel: str,
    success_msg: str = None,
    error_msg: str = None,
    token: str = DEFAULT_ACCESS_TOKEN,
    short_preview: bool = False,
    disable: bool = False,
) -> None:
    """Send a message when the task within the code block is finished, with an optional short preview.

    Example:
        import hkkang_utils.slack as slack_utils

        with slack_utils.notification(
            channel="test-channel",
            success_msg="Process done!",
            error_msg="Error raised during the process",
            short_preview=True
        ):
            # Perform your task here
            ...

    :param channel: Name of the channel to send the message
    :type channel: str
    :param success_msg: Message to send when the given code block completes, defaults to None
    :type success_msg: str, optional
    :param error_msg: Message to send when an error occurs, defaults to None
    :type error_msg: str, optional
    :param token: Slack access token, defaults to DEFAULT_ACCESS_TOKEN
    :type token: str, optional
    :param disable: Whether to disable Slack notifications, defaults to False
    :type disable: bool, optional
    :param short_preview: If True, sends only a short preview for long messages, defaults to True
    :type short_preview: bool, optional
    :rtype: None
    """
    if misc_utils.is_debugger_active():
        disable = True

    if disable:
        yield None
        return None

    slack_messenger = SlackMessenger(channel=channel, token=token)
    try:
        yield slack_messenger
        if success_msg is not None:
            slack_messenger.send(success_msg, short_preview=short_preview)
    except Exception as e:
        if error_msg is None:
            message_to_send = f"Error occurred at {e.__class__.__name__}: {e}"
        else:
            message_to_send = f"{error_msg} ({e.__class__.__name__}: {e})"
        slack_messenger.send(message_to_send, short_preview=short_preview)
        raise e


@contextlib.contextmanager
def slack_notification(*args, **kwargs):
    raise NotImplementedError("Please use notification instead of slack_notification")
