from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Message(db.Model):

    __tablename__ = 'message'

    # A list of fields to be serialized
    SERIALIZE_LIST = ['id', 'text', 'id_sender', 'id_receiver', 'draft', 'delivered', 'read', 'date_delivery', 'date_send']

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.Unicode(128))
    id_sender = db.Column(db.Integer)
    id_receiver = db.Column(db.Integer)
    draft = db.Column(db.Boolean, default=False)
    delivered = db.Column(db.Boolean, default=False)
    read = db.Column(db.Boolean, default=False)
    date_delivery = db.Column(db.DateTime(timezone=True))
    date_send = db.Column(db.DateTime(timezone=True))
    deleted = db.Column(db.Boolean, default=False)
    blacklisted = db.Column(db.Boolean, default=False)

    def __init__(self, *args, **kw):
        super(Message, self).__init__(*args, **kw)
    
    def serialize(self):
        return dict([(k, self.__getattribute__(k)) for k in self.SERIALIZE_LIST])