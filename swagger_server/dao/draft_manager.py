from swagger_server.dao.manager import Manager
from swagger_server.models_db.draft import Draft


class DraftManager(Manager):

    @staticmethod
    def create_draft(draft: Draft):
        Manager.create(draft=draft)
        return draft

    @staticmethod
    def retrieve_by_id(id_):
        Manager.check_none(id=id_)
        return Draft.query.get(id_)
    
    @staticmethod
    def retrieve_all(user_id = None):
        if user_id is not None:
            return Draft.query.filter(Draft.id_sender == user_id).all()
        else:
            return Draft.query.all()
    
    @staticmethod
    def delete_draft(draft: Draft):
        Manager.delete(draft=draft)
    
    @staticmethod
    def delete_draft_by_id(id_: int):
        draft = DraftManager.retrieve_by_id(id_)
        DraftManager.delete_draft(draft)
