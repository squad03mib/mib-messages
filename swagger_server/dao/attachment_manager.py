from swagger_server.dao.manager import Manager
from swagger_server.models_db.attachment import Attachment


class AttachmentManager(Manager):

    @staticmethod
    def create_attachment(attachment: Attachment):
        Manager.create(attachment=attachment)
        return attachment

    @staticmethod
    def retrieve_by_id(id_):
        Manager.check_none(id=id_)
        return Attachment.query.get(id_)
    
    @staticmethod
    def retrieve_by_message_id(message_id: int):
        return Attachment.query.filter(Attachment.id_message==message_id).all()
    
    @staticmethod
    def retrieve_by_draft_id(draft_id: int):
        return Attachment.query.filter(Attachment.id_draft==draft_id).all()
    
    @staticmethod
    def delete_attachment(attachment: Attachment):
        Manager.delete(attachment=attachment)
    
    @staticmethod
    def delete_attachment_by_message_id(message_id: int):
        attachment_list = AttachmentManager.retrieve_by_message_id(message_id)
        for attachment in attachment_list:
            AttachmentManager.delete_attachment(attachment)
    
    @staticmethod
    def delete_attachment_by_draft_id(draft_id: int):
        attachment_list = AttachmentManager.retrieve_by_draft_id(draft_id)
        for attachment in attachment_list:
            AttachmentManager.delete_attachment(attachment)
