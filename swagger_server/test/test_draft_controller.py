# coding: utf-8

from __future__ import absolute_import

import json
from six import BytesIO

from swagger_server.models.draft import Draft  # noqa: E501
from swagger_server.models.draft_post import DraftPost  # noqa: E501
from swagger_server.test import BaseTestCase
from datetime import datetime


class TestDraftController(BaseTestCase):
    """DraftController integration test stubs"""

    def save_test_draft(self):
        """Util function used in tests

        Save a draft and returns its id
        """
        body = DraftPost()
        body.id_sender = 1
        body.recipients_list = [2]
        body.date_delivery = datetime.now().isoformat()
        body.text = "test"
        body.attachment_list = ["wjfklsjfkljfklsdjfklsjklfj"]

        query_string = [('current_user_id', 1)]
        response = self.client.open(
            '/drafts',
            method='POST',
            data=json.dumps(body.to_dict()),
            content_type='application/json',
            query_string=query_string)
        assert response.status_code == 201
        return int(response.json["id_draft"])

    def test_mib_resources_draft_delete_draft(self):
        """Test case for mib_resources_draft_delete_draft

        
        """
        id=self.save_test_draft()

        query_string = [('current_user_id', 1)]
        response = self.client.open(
            '/drafts/{draft_id}'.format(draft_id=id),
            method='DELETE',
            query_string=query_string)
        assert response.status_code == 202
        
    def test_mib_resources_draft_get_all_drafts(self):
        """Test case for mib_resources_draft_get_all_drafts

        
        """

        query_string = [('current_user_id', 1)]
        response = self.client.open(
            '/drafts',
            method='GET',
            query_string=query_string)
        assert response.status_code == 200
        
    def test_mib_resources_draft_get_draft_404(self):
        """Test case for mib_resources_draft_get_draft

        
        """

        query_string = [('current_user_id', 1)]
        response = self.client.open(
            '/drafts/{draft_id}'.format(draft_id=999),
            method='GET',
            query_string=query_string)
        assert response.status_code == 404
        
    def test_mib_resources_draft_save_draft(self):
        """Test case for mib_resources_draft_save_draft

        Create a new draft
        """
        body = DraftPost()
        body.id_sender = 1
        body.recipients_list = [2]
        body.date_delivery = datetime.now().isoformat()
        body.text = "test"

        query_string = [('current_user_id', 1)]
        response = self.client.open(
            '/drafts',
            method='POST',
            data=json.dumps(body.to_dict()),
            content_type='application/json',
            query_string=query_string)
        assert response.status_code == 201
        
    def test_mib_resources_draft_get_draft(self):
        """Test case for mib_resources_draft_get_draft

        
        """
        id=self.save_test_draft()

        query_string = [('current_user_id', 1)]
        response = self.client.open(
            '/drafts/{draft_id}'.format(draft_id=id),
            method='GET',
            query_string=query_string)
        assert response.status_code == 200
    
    def test_mib_resources_draft_send_draft(self):
        """Test case for mib_resources_draft_send_draft

        
        """
        id=self.save_test_draft()

        query_string = [('current_user_id', 1)]
        response = self.client.open(
            '/drafts/{draft_id}/send'.format(draft_id=id),
            method='POST',
            query_string=query_string)
        assert response.status_code == 200