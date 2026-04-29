from app import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Float, DateTime
from datetime import datetime, timezone

class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    first_name: Mapped[String] = mapped_column(String)

    last_name: Mapped[String] = mapped_column(String)

    email: Mapped[String] = mapped_column(String)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, 
        default=lambda: datetime.now(timezone.utc)
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime, 
        default=lambda: datetime.now(timezone.utc)
    )

    def __repr__(self):
        return f"<User {self.email}: {self.first_name} {self.last_name}>"