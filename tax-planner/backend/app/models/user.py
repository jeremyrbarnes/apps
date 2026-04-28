from app import db
from SQLAlchemy.orm import Mapped, mapped_column
from SQLAlchemy import String, Integer, Float, DateTime
from datetime import datetime, timezone

class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
