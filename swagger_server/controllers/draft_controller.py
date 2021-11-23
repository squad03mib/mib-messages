import connexion
import six

from swagger_server.models.draft import Draft  # noqa: E501
from swagger_server import util


def mib_resources_draft_delete_draft(draft_id):  # noqa: E501
    """mib_resources_draft_delete_draft

    Delete a draft by its id # noqa: E501

    :param draft_id: Draft Unique ID
    :type draft_id: int

    :rtype: None
    """
    return 'do some magic!'


def mib_resources_draft_get_all_drafts():  # noqa: E501
    """mib_resources_draft_get_all_drafts

    Get all drafts list # noqa: E501


    :rtype: List[Draft]
    """
    return 'do some magic!'


def mib_resources_draft_get_draft(draft_id):  # noqa: E501
    """mib_resources_draft_get_draft

    Get a draft by its id # noqa: E501

    :param draft_id: Draft Unique ID
    :type draft_id: int

    :rtype: None
    """
    return 'do some magic!'


def mib_resources_draft_save_draft(body):  # noqa: E501
    """Create a new draft

     # noqa: E501

    :param body: Create and save a new draft
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Draft.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def mib_resources_draft_send_draft(draft_id):  # noqa: E501
    """mib_resources_draft_send_draft

    Send a draft by its id # noqa: E501

    :param draft_id: Draft Unique ID
    :type draft_id: int

    :rtype: None
    """
    return 'do some magic!'
