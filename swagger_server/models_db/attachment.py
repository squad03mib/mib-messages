from swagger_server import db
from sqlalchemy import ForeignKey

class Attachment(db.Model):
    
    __tablename__ = 'attachment'

    # A list of fields to be serialized
    SERIALIZE_LIST = ['id', 'id_message', 'id_draft', 'data']

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_message = db.Column(db.Unicode(128), ForeignKey('message.id_message'))
    id_draft = db.Column(db.Unicode(128), ForeignKey('draft.id_draft'))
    data = db.Column(db.Unicode(128))

    def __init__(self, *args, **kw):
        super(Attachment, self).__init__(*args, **kw)
    
    def serialize(self):
        return dict([(k, self.__getattribute__(k)) for k in self.SERIALIZE_LIST])