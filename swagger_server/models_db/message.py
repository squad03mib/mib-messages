from swagger_server import db

class Message(db.Model):

    __tablename__ = 'message'

    # A list of fields to be serialized
    SERIALIZE_LIST = ['id_message', 'text', 'id_sender', 'id_recipient', 'draft', 'message_delivered', 'message_read', 'date_delivery', 'date_send']

    id_message = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.Text)
    id_sender = db.Column(db.Integer)
    id_recipient = db.Column(db.Integer)
    draft = db.Column(db.Boolean, default=False)
    message_delivered = db.Column(db.Boolean, default=False)
    message_read = db.Column(db.Boolean, default=False)
    date_delivery = db.Column(db.DateTime(timezone=True))
    date_send = db.Column(db.DateTime(timezone=True))
    deleted = db.Column(db.Boolean, default=False)
    blacklisted = db.Column(db.Boolean, default=False)

    def __init__(self, *args, **kw):
        super(Message, self).__init__(*args, **kw)
    
    def serialize(self):
        return dict([(k, self.__getattribute__(k)) for k in self.SERIALIZE_LIST])