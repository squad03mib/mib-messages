from swagger_server import db
from sqlalchemy import ForeignKey

class Attachment(db.Model):
    
    __tablename__ = 'attachment'

    # A list of fields to be serialized
    SERIALIZE_LIST = ['id', 'id_message', 'id_draft', 'data']

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_message = db.Column(db.Integer, ForeignKey('message.id_message'))
    id_draft = db.Column(db.Integer, ForeignKey('draft.id_draft'))
    data = db.Column(db.Text)

    def __init__(self, *args, **kw):
        super(Attachment, self).__init__(*args, **kw)
    