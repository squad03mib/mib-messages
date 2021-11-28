from swagger_server.dao.manager import Manager
from swagger_server.models_db.message import Message


class MessageManager(Manager):

    @staticmethod
    def create_message(message: Message):
        Manager.create(message=message)

    @staticmethod
    def retrieve_by_id(id_):
        Manager.check_none(id=id_)
        return Message.query.get(id_)
    
    @staticmethod
    def delete_message(message: Message):
        Manager.delete(message=message)
    
    @staticmethod
    def delete_message_by_id(id_: int):
        message = MessageManager.retrieve_by_id(id_)
        MessageManager.delete_message(message)
