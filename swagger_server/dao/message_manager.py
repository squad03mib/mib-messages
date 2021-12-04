from swagger_server.dao.manager import Manager
from swagger_server.models_db.message import Message
import datetime


class MessageManager(Manager):

    @staticmethod
    def create_message(message: Message):
        Manager.create(message=message)
        return message

    @staticmethod
    def retrieve_by_id(id_):
        Manager.check_none(id=id_)
        return Message.query.get(id_)
    
    @staticmethod
    def retrieve_all():
        return Message.query.all()
    
    @staticmethod
    def retrieve_pending_all():
        return Message.query.filter(Message.message_delivered.is_(False), Message.blacklisted.is_(
            False), Message.date_delivery < datetime.datetime.now()).all()
    
    @staticmethod
    def delete_message(message: Message):
        Manager.delete(message=message)
    
    @staticmethod
    def delete_message_by_id(id_: int):
        message = MessageManager.retrieve_by_id(id_)
        MessageManager.delete_message(message)
    
    @staticmethod
    def send_message(message: Message):
        message.message_delivered = True
        Manager.update()
    
    @staticmethod
    def read_message(message: Message):
        message.message_read = True
        Manager.update()
