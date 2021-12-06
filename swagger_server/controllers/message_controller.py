from datetime import datetime
import connexion
import six

from swagger_server.models.message import Message  # noqa: E501
from swagger_server.models.message_post import MessagePost  # noqa: E501
from swagger_server.dao.message_manager import MessageManager
from swagger_server.models_db.message import Message as Message_db
from swagger_server.dao.attachment_manager import AttachmentManager
from swagger_server.models_db.attachment import Attachment as Attachment_db
from swagger_server.models.user import User
from swagger_server.rao.user_manager import UserManager
from flask import abort, request

import pytz


def mib_resources_message_delete_message(current_user_id, message_id):  # noqa: E501
    """mib_resources_message_delete_message

    Delete a message by its id # noqa: E501

    :param message_id: Message Unique ID
    :type message_id: int

    :rtype: None
    """
    msg :Message_db = MessageManager.retrieve_by_id(message_id)
    if msg is None:
        abort(404)
    elif (msg.id_sender != current_user_id and msg.id_recipient != current_user_id) and\
         (msg.id_recipient == current_user_id and not msg.message_delivered):
        abort(403)
    else:
        AttachmentManager.delete_attachment_by_message_id(message_id)
        MessageManager.delete_message(msg)
        return "", 202

def mib_resources_message_get_all_messages(current_user_id, type):  # noqa: E501
    """mib_resources_message_get_all_messages

    Get all messages list # noqa: E501

    :param type: The types of messages to retrieve
    :type type: str

    :rtype: List[Message]
    """
    message_list = []

    for msg in MessageManager.retrieve_all(type, current_user_id):
        message : Message = Message.from_dict(msg.serialize())
        attachment_list = AttachmentManager.retrieve_by_message_id(msg.id_message)
        if attachment_list is not None:
            message.attachment_list = []
            for attachment in attachment_list:
                message.attachment_list.append(attachment.data)
        message.text+=' - delivered: '
        message.text+= 'True' if msg.message_delivered else 'False'
        message_list.append(message.to_dict())

    return message_list

def mib_resources_message_get_message(current_user_id, message_id):  # noqa: E501
    """mib_resources_message_get_message

    Get a message by its id # noqa: E501

    :param message_id: Message Unique ID
    :type message_id: int

    :rtype: None
    """
    msg : Message_db = MessageManager.retrieve_by_id(message_id)
    if msg is None:
        abort(404)
    elif (msg.id_sender != current_user_id and msg.id_recipient != current_user_id) and\
         (msg.id_recipient == current_user_id and not msg.message_delivered):
        abort(403)
    else:
        if not msg.message_read and msg.id_recipient == current_user_id:
            from swagger_server.background import send_notification as send_notification_task
            send_notification_task.apply_async((msg.id_message,), eta=datetime.utcnow())
        # TODO: bad words
        # if message contains bad words they are not showed
        #if int(msg.id_sender) != current_user.id:
        #    msg.text = purify_message(msg.text)
        message : Message = Message.from_dict(msg.serialize())
        attachment_list = AttachmentManager.retrieve_by_message_id(message_id)
        if attachment_list is not None:
            message.attachment_list = []
            for attachment in attachment_list:
                message.attachment_list.append(attachment.data)
        return message.to_dict(), 200

def mib_resources_message_send_message(body, current_user_id):  # noqa: E501
    """Send a new message

     # noqa: E501

    :param body: Create a new message and send it
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = MessagePost.from_dict(connexion.request.get_json())  # noqa: E501
    
    return mib_resources_message_send_message_internal(body)

def mib_resources_message_send_message_internal(body):
    message_db = None

    for recipient in body.recipients_list:
        message_db = Message_db()
        message_db.id_sender = body.id_sender
        message_db.id_recipient = recipient
        message_db.date_delivery = datetime.fromisoformat(body.date_delivery)
        message_db.text = body.text

        # TODO: check blacklist

        message_db.date_send = datetime.now()
        message_db = MessageManager.create_message(message_db)

        if body.attachment_list is not None:
            for attachment in body.attachment_list:
                attachment_db = Attachment_db()
                attachment_db.id_message = message_db.id_message
                attachment_db.data = attachment
                AttachmentManager.create_attachment(attachment_db)
        
        from swagger_server.background import send_message as send_message_task
        send_message_task.apply_async((message_db.id_message,), eta=message_db.date_delivery.astimezone(pytz.UTC))
    
    return Message.from_dict(message_db.serialize()).to_dict(), 201

def mib_resources_message_withdraw_message(current_user_id, message_id):  # noqa: E501
    """mib_resources_message_withdraw_message

    Withdraw a sent message by its id # noqa: E501

    :param message_id: Message Unique ID
    :type message_id: int

    :rtype: None
    """
    msg = MessageManager.retrieve_by_id(message_id)
    if msg is None:
        abort(404)
    elif (msg.id_sender != current_user_id) and\
         (msg.id_sender == current_user_id and msg.message_delivered):
         # TODO: Check Lottery points
        abort(403)
    else:
        AttachmentManager.delete_attachment_by_message_id(message_id)
        MessageManager.delete_message(msg)
        return "", 200
