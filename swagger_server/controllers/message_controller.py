import connexion
import six

from swagger_server.models.message import Message  # noqa: E501
from swagger_server import util


def mib_resources_message_delete_message(message_id):  # noqa: E501
    """mib_resources_message_delete_message

    Delete a message by its id # noqa: E501

    :param message_id: Message Unique ID
    :type message_id: int

    :rtype: None
    """
    return 'do some magic!'


def mib_resources_message_get_all_messages(type):  # noqa: E501
    """mib_resources_message_get_all_messages

    Get all messages list # noqa: E501

    :param type: The types of messages to retrieve
    :type type: str

    :rtype: List[Message]
    """
    return 'do some magic!'


def mib_resources_message_get_message(message_id):  # noqa: E501
    """mib_resources_message_get_message

    Get a message by its id # noqa: E501

    :param message_id: Message Unique ID
    :type message_id: int

    :rtype: None
    """
    return 'do some magic!'


def mib_resources_message_send_message(body):  # noqa: E501
    """Send a new message

     # noqa: E501

    :param body: Create a new message and send it
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Message.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def mib_resources_message_withdraw_message(message_id):  # noqa: E501
    """mib_resources_message_withdraw_message

    Withdraw a sent message by its id # noqa: E501

    :param message_id: Message Unique ID
    :type message_id: int

    :rtype: None
    """
    return 'do some magic!'
