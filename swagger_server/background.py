from celery import Celery
from datetime import timedelta
import smtplib

import celery

from swagger_server import create_app

from os import environ

environ.setdefault('CELERY_CONFIG_MODULE', 'swagger_server.background_config')

#BACKEND = BROKER = 'redis://localhost:6379'
#celery = Celery(__name__, backend=BACKEND, broker=BROKER)
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
    from swagger_server.dao.message_manager import MessageManager
    with _APP.app_context():
        msg = MessageManager.retrieve_by_id(id_message)
        MessageManager.send_message(msg)
        return
        usr = None

        internal_send_email(usr.email, 'New bottle received',
                                    'Hey ' + usr.firstname +
                                    ',\nyou just received a new message in a bottle.\n\nGreetings,\nThe MIB team')

@celery.task
def send_notification(id_message):
    from swagger_server.dao.message_manager import MessageManager
    with _APP.app_context():
        msg = MessageManager.retrieve_by_id(id_message)
        MessageManager.read_message(msg)
        return
        current_user = None
        usr = None
        internal_send_email(usr.email, 'Message reading notification',
                            current_user.firstname +
                            ' have just read your message in a bottle.\n\nGreetings,\nThe MIB team')


@celery.task
def search_for_pending_messages():
    from swagger_server.dao.message_manager import MessageManager
    with _APP.app_context():
        msgs = MessageManager.retrieve_pending_all()
        for msg in msgs:
            send_message.apply_async((msg.id_message,), eta=msg.date_delivery)

