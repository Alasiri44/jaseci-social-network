from models import db

class Notification(db.Model):
    __tablename__ = "notifications"

    id = db.Column(db.Integer, primary_key=True)
    receiver_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    type = db.Column(db.Enum('like', 'follow', 'comment', name='notification_type_enum'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id', ondelete="SET NULL"))
    is_read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
