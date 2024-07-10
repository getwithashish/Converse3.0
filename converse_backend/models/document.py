from models.models import db


class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    document_name = db.Column(db.String(80), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    user = db.relationship("User", back_populates="documents")

    def __repr__(self):
        return "<UploadedDocuments %r>" % self.document_name

    def save(self):
        db.session.add(self)
        db.session.commit()
