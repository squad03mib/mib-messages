import connexion
import six
import json

from swagger_server.models.draft import Draft  # noqa: E501
from swagger_server.models.draft_post import DraftPost  # noqa: E501
from swagger_server import util
from swagger_server.dao.draft_manager import DraftManager
from swagger_server.models_db.draft import Draft as Draft_db
from datetime import datetime
from flask import abort
import swagger_server.controllers.message_controller as MessageController
from swagger_server.models.message_post import MessagePost


def mib_resources_draft_delete_draft(draft_id):  # noqa: E501
    """mib_resources_draft_delete_draft

    Delete a draft by its id # noqa: E501

    :param draft_id: Draft Unique ID
    :type draft_id: int

    :rtype: None
    """
    draft = DraftManager.retrieve_by_id(draft_id)
    if draft is None:
        abort(404)
    else:
        DraftManager.delete_draft(draft)
        return "", 202


def mib_resources_draft_get_all_drafts():  # noqa: E501
    """mib_resources_draft_get_all_drafts

    Get all drafts list # noqa: E501


    :rtype: List[Draft]
    """
    draft_list = []

    for draft in DraftManager.retrieve_all():
        draft_list.append(Draft.from_dict(draft.serialize()).to_dict())

    return draft_list


def mib_resources_draft_get_draft(draft_id):  # noqa: E501
    """mib_resources_draft_get_draft

    Get a draft by its id # noqa: E501

    :param draft_id: Draft Unique ID
    :type draft_id: int

    :rtype: None
    """
    draft : Draft_db = DraftManager.retrieve_by_id(draft_id)
    if draft is None:
        abort(404)
    else:
        return Draft.from_dict(draft.serialize()).to_dict(), 200


def mib_resources_draft_save_draft(body):  # noqa: E501
    """Create a new draft

     # noqa: E501

    :param body: Create and save a new draft
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = DraftPost.from_dict(connexion.request.get_json())  # noqa: E501
    
    draft_db = Draft_db()
    draft_db.id_sender = body.id_sender
    draft_db.recipient_json = json.dumps(body.recipients_list)
    draft_db.date_delivery = datetime.fromisoformat(body.date_delivery)
    draft_db.text = body.text

    draft_db = DraftManager.create_draft(draft_db)
    
    return Draft.from_dict(draft_db.serialize()).to_dict(), 201


def mib_resources_draft_send_draft(draft_id):  # noqa: E501
    """mib_resources_draft_send_draft

    Send a draft by its id # noqa: E501

    :param draft_id: Draft Unique ID
    :type draft_id: int

    :rtype: None
    """
    draft : Draft_db = DraftManager.retrieve_by_id(draft_id)
    if draft is None:
        abort(404)
    else:
        msg_post = MessagePost()
        msg_post.recipients_list = json.loads(draft.recipient_json)
        msg_post.date_delivery = draft.date_delivery.isoformat()
        msg_post.id_sender = draft.id_sender
        msg_post.text = draft.text
        (msg, _) = MessageController.mib_resources_message_send_message_internal(msg_post)
        DraftManager.delete_draft(draft)
        return msg, 200