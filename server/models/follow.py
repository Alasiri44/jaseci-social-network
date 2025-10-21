from models import db

class Follow(db.Model):
    __tablename__ = "follows"

    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    followed_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    __table_args__ = (db.UniqueConstraint('follower_id', 'followed_id', name='unique_follow'),)
