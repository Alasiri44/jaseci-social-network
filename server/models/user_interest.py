from .__init_ import db

class UserInterest(db.Model):
    __tablename__ = "user_interests"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    interest_id = db.Column(db.Integer, db.ForeignKey('interests.id', ondelete="CASCADE"), nullable=False)

    __table_args__ = (db.UniqueConstraint('user_id', 'interest_id', name='unique_user_interest'),)
