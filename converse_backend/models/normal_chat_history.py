from models.models import db
from datetime import datetime


class NormalChatHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chat_history = db.Column(db.JSON)
    started_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return "<NormalChatHistory %r>" % self.id + "-" + self.user_id

    def save(self):
        db.session.add(self)
        db.session.commit()
