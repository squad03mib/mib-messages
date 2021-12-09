from swagger_server import db
class Draft(db.Model):

    __tablename__ = 'draft'

     # A list of fields to be serialized
    SERIALIZE_LIST = ['id_draft', 'text', 'id_sender', 'recipient_json', 'date_delivery']

    id_draft = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.Text)
    id_sender = db.Column(db.Integer)
    recipient_json = db.Column(db.Unicode(128))
    date_delivery = db.Column(db.DateTime(timezone=True))

    def __init__(self, *args, **kw):
        super(Draft, self).__init__(*args, **kw)
    
    def serialize(self):
        return dict([(k, self.__getattribute__(k)) for k in self.SERIALIZE_LIST])