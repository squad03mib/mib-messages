# coding: utf-8

from __future__ import absolute_import

import json
from six import BytesIO

from swagger_server.models.draft import Draft  # noqa: E501
from swagger_server.models.draft_post import DraftPost  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDraftController(BaseTestCase):
    '''
    """DraftController integration test stubs"""

    def test_mib_resources_draft_delete_draft(self):
        """Test case for mib_resources_draft_delete_draft

        
        """
        response = self.client.open(
            '/drafts/{draft_id}'.format(draft_id=1),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_mib_resources_draft_get_all_drafts(self):
        """Test case for mib_resources_draft_get_all_drafts

        
        """
        response = self.client.open(
            '/drafts',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_mib_resources_draft_get_draft(self):
        """Test case for mib_resources_draft_get_draft

        
        """
        response = self.client.open(
            '/drafts/{draft_id}'.format(draft_id=1),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_mib_resources_draft_save_draft(self):
        """Test case for mib_resources_draft_save_draft

        Create a new draft
        """
        body = DraftPost()
        response = self.client.open(
            '/drafts',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_mib_resources_draft_send_draft(self):
        """Test case for mib_resources_draft_send_draft

        
        """
        response = self.client.open(
            '/drafts/{draft_id}/send'.format(draft_id=1),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
    '''

if __name__ == '__main__':
    import unittest
    unittest.main()
