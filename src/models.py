from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
db = SQLAlchemy()
class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    # email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    # password: Mapped[str] = mapped_column(nullable=False)
    # is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    firstname: Mapped[str] = mapped_column(String(120), unique=False, nullable=False)
    lastname: Mapped[str] = mapped_column(String(120), unique=False, nullable=False)
    comments: Mapped[List['Comment']]=relationship(back_populates="author")
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            # do not serialize the password, its a security breach
        }
class Comment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(120), unique=False, nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    author: Mapped['User']=relationship(back_populates="comments")
class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
class Media(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str] = mapped_column(String(120), unique=False, nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
class Follower(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_from_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user_to_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    # follower: Mapped['User'] = relationship(foreign_keys=[user_from_id])
    # followed: Mapped['User'] = relationship(foreign_keys=[user_to_id])