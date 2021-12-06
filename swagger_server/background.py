from typing import List
from celery import Celery
from datetime import timedelta
import smtplib

import celery

from swagger_server import create_app

from os import environ

environ.setdefault('CELERY_CONFIG_MODULE', 'swagger_server.background_config')

celery = Celery(__name__)
celery.config_from_envvar('CELERY_CONFIG_MODULE')
_APP = create_app()


def internal_send_email(to, subject, message):
    try:
        mailserver = smtplib.SMTP('smtp.office365.com', 587)
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.login('squad03MIB@outlook.com', 'AntonioBrogi')
        mailserver.sendmail('squad03MIB@outlook.com', to, 'To:' + to +
                            '\nFrom:squad03MIB@outlook.com\nSubject: ' + subject + '\n\n' +
                            message)
        mailserver.quit()
    except (smtplib.SMTPRecipientsRefused, smtplib.SMTPDataError, smtplib.SMTPConnectError,
            smtplib.SMTPNotSupportedError, smtplib.SMTPSenderRefused, smtplib.SMTPServerDisconnected,
            smtplib.SMTPHeloError, smtplib.SMTPAuthenticationError) as e:
        print("ERROR: " + str(e))

@celery.on_after_configure.connect
def setup_periodic_task(sender, **kwargs):
    sender.add_periodic_task(timedelta(minutes=30), search_for_pending_messages, expires=10)

@celery.task
def send_message(id_message):
    from swagger_server.dao.message_manager import MessageManager, Message as Message_db
    from swagger_server.rao.user_manager import UserManager, User
    with _APP.app_context():
        msg :Message_db = MessageManager.retrieve_by_id(id_message)
        MessageManager.send_message(msg)
        
        recipient :User = UserManager.get_user_by_id(msg.id_recipient)

        internal_send_email(recipient.email, 'New bottle received',
                                    'Hey ' + recipient.firstname +
                                    ',\nyou just received a new message in a bottle.\n\nGreetings,\nThe MIB team')

@celery.task
def send_notification(id_message):
    from swagger_server.dao.message_manager import MessageManager, Message as Message_db
    from swagger_server.rao.user_manager import UserManager, User
    with _APP.app_context():
        msg :Message_db = MessageManager.retrieve_by_id(id_message)
        MessageManager.read_message(msg)
        recipient :User = UserManager.get_user_by_id(msg.id_recipient)
        sender :User = UserManager.get_user_by_id(msg.id_sender)
        internal_send_email(sender.email, 'Message reading notification',
                            recipient.firstname +
                            ' have just read your message in a bottle.\n\nGreetings,\nThe MIB team')


@celery.task
def search_for_pending_messages():
    from swagger_server.dao.message_manager import MessageManager, Message as Message_db
    with _APP.app_context():
        msgs :List[Message_db] = MessageManager.retrieve_pending_all()
        for msg in msgs:
            send_message.apply_async((msg.id_message,), eta=msg.date_delivery)

