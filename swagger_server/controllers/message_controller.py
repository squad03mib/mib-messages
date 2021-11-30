from datetime import datetime
import connexion
import six

from swagger_server.models.message import Message  # noqa: E501
from swagger_server.models.message_post import MessagePost  # noqa: E501
from swagger_server import util
from swagger_server.dao.message_manager import MessageManager
from swagger_server.models_db.message import Message as Message_db
from flask import abort


def mib_resources_message_delete_message(message_id):  # noqa: E501
    """mib_resources_message_delete_message

    Delete a message by its id # noqa: E501

    :param message_id: Message Unique ID
    :type message_id: int

    :rtype: None
    """
    msg = MessageManager.retrieve_by_id(message_id)
    if msg is None:
        abort(404)
    else:
        MessageManager.delete_message(msg)
        return "", 202

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
    msg : Message_db = MessageManager.retrieve_by_id(message_id)
    if msg is None: #or (int(msg.id_receiver) == current_user.id and not msg.delivered)
        abort(404)
    #elif int(msg.id_sender) != current_user.id and int(msg.id_receiver) != current_user.id:
    #    abort(403)
    else:
        #if not msg.message_read: #and int(msg.id_receiver) == current_user.id:
        #    notify_msg_reading(msg)

        # if message contains bad words they are not showed
        #if int(msg.id_sender) != current_user.id:
        #    msg.text = purify_message(msg.text)
        return Message.from_dict(msg.serialize()).to_dict(), 200

def mib_resources_message_send_message(body):  # noqa: E501
    """Send a new message

     # noqa: E501

    :param body: Create a new message and send it
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = MessagePost.from_dict(connexion.request.get_json())  # noqa: E501
    
    message_db = Message_db()
    message_db.id_sender = body.id_sender
    message_db.id_receiver = body.recipients_list[0]
    message_db.date_delivery = datetime.fromisoformat(body.date_delivery)
    message_db.text = body.text

    message_db.date_send = datetime.now()
    message_db = MessageManager.create_message(message_db)
    return Message.from_dict(message_db.serialize()).to_dict(), 201


def mib_resources_message_withdraw_message(message_id):  # noqa: E501
    """mib_resources_message_withdraw_message

    Withdraw a sent message by its id # noqa: E501

    :param message_id: Message Unique ID
    :type message_id: int

    :rtype: None
    """
    message : Message = MessageManager.retrieve_by_id(message_id)
    if message is None:
        abort(404)
    elif message.message_delivered:
        abort(404)
    else:
        MessageManager.delete_message(message)
        return "", 200
