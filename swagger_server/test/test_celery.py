from datetime import datetime
from swagger_server.test import BaseTestCase
from swagger_server.background  import send_message, send_notification, search_for_pending_messages
from swagger_server.models.message_post import MessagePost
import json

class TestCelery(BaseTestCase):
    def test_send_message_celery(self):
        body = MessagePost()
        body.id_sender = 1
        body.recipients_list = [2]
        body.date_delivery = datetime.now().isoformat()
        body.text = "test_celery"

        query_string = [('current_user_id', 1)]
        response = self.client.open(
            '/messages',
            method='POST',
            data=json.dumps(body.to_dict()),
            content_type='application/json',
            query_string=query_string)
        assert response.status_code == 201

        id_message = response.json['id_message']

        send_message.apply((id_message,))
        send_notification.apply((id_message,))
        search_for_pending_messages.apply()
