from .__init_ import db
from datetime import datetime


class Connection(db.Model):
    __tablename__ = "connections"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    connected_user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    status = db.Column(db.String(20), default="pending")  # pending | accepted | blocked
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", foreign_keys=[user_id], backref="sent_connections")
    connected_user = db.relationship("User", foreign_keys=[connected_user_id], backref="received_connections")

    def __repr__(self):
        return f"<Connection {self.user_id} -> {self.connected_user_id} ({self.status})>"
