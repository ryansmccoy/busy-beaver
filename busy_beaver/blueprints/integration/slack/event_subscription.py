import logging

from flask import jsonify, request
from flask.views import MethodView

from .slash_command import HELP_TEXT
from busy_beaver import slack

logger = logging.getLogger(__name__)


class SlackEventSubscriptionResource(MethodView):
    """Callback endpoint for Slack event subscriptions"""

    def post(self):
        data = request.json
        logger.info("[Busy Beaver] Received event from Slack", extra={"req_json": data})

        verification_request = data["type"] == "url_verification"
        if verification_request:
            logger.info("[Busy Beaver] Slack -- API Verification")
            return jsonify({"challenge": data["challenge"]})

        # bot can see its own DMs
        event = data["event"]
        msg_from_bot = event.get("subtype") == "bot_message"
        if event["type"] == "message" and msg_from_bot:
            return jsonify(None)

        dm_to_bot = event["channel_type"] == "im"
        if event["type"] == "message" and dm_to_bot:
            slack.post_message(HELP_TEXT, channel_id=event["channel"])
        return jsonify(None)
