from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class User(db.Model,UserMixin):
    __tablename__ = "user_account"
    id = db.Column(Integer, primary_key=True)
    email = db.Column(String(30), unique = True)
    first_name = db.Column(String(30))
    last_name = db.Column(String(30))
    password = db.Column(String(30))
    address = db.Column(String(30))
    city = db.Column(String(30))
    state = db.Column(String(30))
    zip = db.Column(Integer())
    foods = relationship(
        "Food", back_populates="user", cascade="all, delete-orphan"
    )
    def __repr__(self):
        return f"User(id={self.id!r}, email={self.email!r}, firstname={self.first_name!r}, lastname={self.last_name!r},password={self.password!r},address={self.address!r},city={self.city!r},state={self.state!r},zip={self.zip!r})"



class Food(db.Model):
    __tablename__ = "food_item"
    id = db.Column(Integer, primary_key=True)
    food_name = db.Column(String(20))
    description = db.Column(String(1000))
    user_id = db.Column(Integer, ForeignKey("user_account.id"), nullable=False)
    user = relationship("User", back_populates="foods")
    def __repr__(self):
        return f"Food(id={self.id!r}, food_name={self.food_name!r}, description={self.description!r})"
