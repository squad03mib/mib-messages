# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.message import Message  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMessageController(BaseTestCase):
    """MessageController integration test stubs"""

    def test_mib_resources_message_delete_message(self):
        """Test case for mib_resources_message_delete_message

        
        """
        response = self.client.open(
            '/messages/{message_id}'.format(message_id=1),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_mib_resources_message_get_all_messages(self):
        """Test case for mib_resources_message_get_all_messages

        
        """
        query_string = [('type', 'type_example')]
        response = self.client.open(
            '/messages',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_mib_resources_message_get_message(self):
        """Test case for mib_resources_message_get_message

        
        """
        response = self.client.open(
            '/messages/{message_id}'.format(message_id=1),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_mib_resources_message_send_message(self):
        """Test case for mib_resources_message_send_message

        Send a new message
        """
        body = Message()
        response = self.client.open(
            '/messages',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_mib_resources_message_withdraw_message(self):
        """Test case for mib_resources_message_withdraw_message

        
        """
        response = self.client.open(
            '/messages/{message_id}/withdraw'.format(message_id=1),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
