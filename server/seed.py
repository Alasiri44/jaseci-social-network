from faker import Faker
from models.__init_ import db
from models.user import User
from models.post import Post
from models.comment import Comment
from models.like import Like
from models.connection import Connection
from models.interest import Interest
from models.user_interest import UserInterest
from models.follow import Follow
from models.message import Message
from app import app
import random

fake = Faker()


# ---------------- USERS ----------------
def seed_users(n=100):
    users = []
    for _ in range(n):
        user = User(
            username=fake.user_name(),
            email=fake.unique.email(),
            password_hash=fake.password(length=12),  # changed from 'password' to 'password_hash'
            bio=fake.sentence(nb_words=12),
            location=fake.city(),                    # added location
            profile_image=fake.image_url(),          # changed from 'profile_picture' to 'profile_image'
            visibility=random.choice(['public', 'private'])
        )
        users.append(user)
        db.session.add(user)
    db.session.commit()
    return users

# ---------------- INTERESTS ----------------
def seed_interests():
    interest_names = [
        "Music", "Technology", "Sports", "Art", "Travel", "Coding",
        "Movies", "Books", "Fitness", "Gaming", "Cooking", "Fashion",
        "Science", "Business", "Education", "Nature", "Health", "Finance",
        "Photography", "Politics", "Volunteering", "Writing", "AI",
        "Engineering", "Architecture", "Marketing", "Startups", "Cars",
        "History", "Relationships", "Spirituality"
    ]
    for name in interest_names:
        db.session.add(Interest(name=name))
    db.session.commit()


# ---------------- POSTS ----------------
def seed_posts(users, n=250):
    posts = []
    for _ in range(n):
        user = random.choice(users)
        post = Post(
            user_id=user.id,
            content=fake.text(max_nb_chars=400)
        )
        posts.append(post)
        db.session.add(post)
    db.session.commit()
    return posts


# ---------------- COMMENTS ----------------
def seed_comments(users, n=400):
    posts = Post.query.all()
    for _ in range(n):
        user = random.choice(users)
        post = random.choice(posts)
        comment = Comment(
            user_id=user.id,
            post_id=post.id,
            content=fake.text(max_nb_chars=180)
        )
        db.session.add(comment)
    db.session.commit()


# ---------------- LIKES ----------------
def seed_likes(users, posts, n=500):
    existing_likes = set()  # to prevent duplicates

    for _ in range(n):
        user = random.choice(users)
        post = random.choice(posts)

        # prevent duplicate likes or self-likes on their own post (optional)
        if (user.id, post.id) in existing_likes:
            continue

        like = Like(user_id=user.id, post_id=post.id)
        db.session.add(like)
        existing_likes.add((user.id, post.id))

    db.session.commit()



# ---------------- CONNECTIONS ----------------
def seed_connections(users, n=150):
    for _ in range(n):
        user1, user2 = random.sample(users, 2)
        connection = Connection(
            user_id=user1.id,
            connected_user_id=user2.id,
            status=random.choice(["pending", "accepted"])
        )
        db.session.add(connection)
    db.session.commit()


# ---------------- FOLLOWS ----------------
def seed_follows(users, n=300):
    existing_pairs = set()  # store (follower_id, followed_id) pairs to avoid duplicates

    for _ in range(n):
        follower, followed = random.sample(users, 2)

        # Ensure no duplicate or self-follow
        if (follower.id, followed.id) in existing_pairs:
            continue

        follow = Follow(follower_id=follower.id, followed_id=followed.id)
        db.session.add(follow)

        existing_pairs.add((follower.id, followed.id))

    db.session.commit()


# ---------------- MESSAGES ----------------
def seed_messages(users, n=300):
    for _ in range(n):
        sender, receiver = random.sample(users, 2)
        message = Message(
            sender_id=sender.id,
            receiver_id=receiver.id,
            content=fake.sentence(nb_words=random.randint(6, 15))
        )
        db.session.add(message)
    db.session.commit()


# ---------------- USER INTERESTS ----------------
def seed_UserInterest(users):
    interests = Interest.query.all()

    for user in users:
        # assign each user 2–3 random interests
        for interest in random.sample(interests, random.randint(2, 3)):
            user_interest = UserInterest(
                user_id=user.id,
                interest_id=interest.id
            )
            db.session.add(user_interest)

    db.session.commit()


# ---------------- RUN ALL ----------------
def run_seed():
    with app.app_context():
        print("Dropping and recreating database...")
        db.drop_all()
        db.create_all()

        print("Seeding users...")
        users = seed_users()

        print("Seeding interests...")
        seed_interests()

        print("Seeding posts...")
        posts = seed_posts(users)

        print("Seeding comments...")
        seed_comments(users)

        print("Seeding likes...")
        seed_likes(users, posts)

        print("Seeding connections...")
        seed_connections(users)

        print("Seeding follows...")
        seed_follows(users)

        print("Seeding messages...")
        seed_messages(users)

        print("Seeding user interests...")
        seed_UserInterest(users)

        print("✅ Database seeded successfully!")


if __name__ == "__main__":
    run_seed()
