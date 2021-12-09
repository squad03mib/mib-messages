# coding: utf-8

from __future__ import absolute_import

import json
from six import BytesIO

from swagger_server.models.message import Message  # noqa: E501
from swagger_server.models.message_post import MessagePost  # noqa: E501
from swagger_server.test import BaseTestCase
from datetime import datetime


class TestMessageController(BaseTestCase):
    """MessageController integration test stubs"""

    def send_test_message(self):
        """Util function used in tests

        Sends a message and returns its id
        """
        body = MessagePost()
        body.id_sender = 0
        body.recipients_list = [1]
        body.date_delivery = datetime.now().isoformat()
        body.text = "test"

        query_string = [('current_user_id', 1)]
        response = self.client.open(
            '/messages',
            method='POST',
            data=json.dumps(body.to_dict()),
            content_type='application/json',
            query_string=query_string)
        assert response.status_code == 201
        return int(response.json["id_message"])
    
    
    def test_mib_resources_message_delete_message(self):
        """Test case for mib_resources_message_delete_message

        Send and delete a message
        """
        id=1

        query_string = [('current_user_id', 1)]
        response = self.client.open(
            '/messages/{message_id}'.format(message_id=id),
            method='DELETE',
            query_string=query_string)
        assert response.status_code == 202

    
    def test_mib_resources_message_delete_message_404(self):
        """Test case for mib_resources_message_delete_message

        Send and delete a message
        """
        id=999

        query_string = [('current_user_id', 1)]
        response = self.client.open(
            '/messages/{message_id}'.format(message_id=id),
            method='DELETE',
            query_string=query_string)
        assert response.status_code == 404


    def test_mib_resources_message_delete_message_403(self):
        """Test case for mib_resources_message_delete_message

        Send and delete a message
        """
        id=self.send_test_message()

        query_string = [('current_user_id', 999)]
        response = self.client.open(
            '/messages/{message_id}'.format(message_id=id),
            method='DELETE',
            query_string=query_string)
        assert response.status_code == 403
    

    def test_mib_resources_message_get_all_messages_sent(self):
        """Test case for mib_resources_message_get_all_messages

        
        """
        self.send_test_message()
        query_string = [('type', 'sent'), ('current_user_id', 1)]
        response = self.client.open(
            '/messages',
            method='GET',
            query_string=query_string)
        assert response.status_code == 200
    
    def test_mib_resources_message_get_all_messages_received(self):
        """Test case for mib_resources_message_get_all_messages

        
        """
        query_string = [('type', 'received'), ('current_user_id', 2)]
        response = self.client.open(
            '/messages',
            method='GET',
            query_string=query_string)
        assert response.status_code == 200
    
    def test_mib_resources_message_get_message_404(self):
        """Test case for mib_resources_message_get_message

        
        """

        query_string = [('current_user_id', 1)]
        response = self.client.open(
            '/messages/{message_id}'.format(message_id=999),
            method='GET',
            query_string=query_string)
        assert response.status_code == 404
    
    def test_mib_resources_message_send_message(self):
        """Test case for mib_resources_message_send_message

        Send a new message
        """
        body = MessagePost()
        body.id_sender = 0
        body.recipients_list = [1]
        body.date_delivery = datetime.now().isoformat()
        body.text = "test"

        query_string = [('current_user_id', 1)]
        response = self.client.open(
            '/messages',
            method='POST',
            data=json.dumps(body.to_dict()),
            content_type='application/json',
            query_string=query_string)
        assert response.status_code == 201
    
    def test_mib_resources_message_get_message(self):
        """Test case for mib_resources_message_get_message

        Send and retrieve a message
        """
        id=self.send_test_message()

        query_string = [('current_user_id', 1)]
        response = self.client.open(
            '/messages/{message_id}'.format(message_id=id),
            method='GET',
            query_string=query_string)
        assert response.status_code == 200
    
    def test_mib_resources_message_withdraw_message(self):
        """Test case for mib_resources_message_withdraw_message

        Send and withdraw a message
        """
        id=self.send_test_message()

        query_string = [('current_user_id', 1)]
        response = self.client.open(
            '/messages/{message_id}/withdraw'.format(message_id=id),
            method='POST',
            query_string=query_string)
        assert response.status_code == 403
    