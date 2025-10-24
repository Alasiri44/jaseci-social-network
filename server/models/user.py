from .__init_ import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.Text, nullable=False)
    bio = db.Column(db.Text)
    location = db.Column(db.String(100))
    profile_image = db.Column(db.Text)
    visibility = db.Column(db.Enum('public', 'private', name='visibility_enum'), default='public')
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    posts = db.relationship('Post', backref='user', lazy=True, cascade='all, delete-orphan')
    comments = db.relationship('Comment', backref='user', lazy=True, cascade='all, delete-orphan')
    likes = db.relationship('Like', backref='user', lazy=True, cascade='all, delete-orphan')
    sent_messages = db.relationship('Message', foreign_keys='Message.sender_id', backref='sender', lazy=True)
    received_messages = db.relationship('Message', foreign_keys='Message.receiver_id', backref='receiver', lazy=True)
    
    def friends(self):
        """Return list of users this user is connected with."""
        sent = [conn.connected_user for conn in self.sent_connections if conn.status == "accepted"]
        received = [conn.user for conn in self.received_connections if conn.status == "accepted"]
        return sent + received

    def __repr__(self):
        return f"<User {self.username}>"
