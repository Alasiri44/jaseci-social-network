from models import db

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    content = db.Column(db.Text, nullable=False)
    media_url = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    comments = db.relationship('Comment', backref='post', lazy=True, cascade='all, delete-orphan')
    likes = db.relationship('Like', backref='post', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Post {self.id}>"
