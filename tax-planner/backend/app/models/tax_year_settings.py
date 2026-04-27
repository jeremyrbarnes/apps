from app import db
from SQLAlchemy.orm import Mapped, mapped_column
from SQLAlchemy import String, Integer, Float, DateTime
from datetime import datetime, timezone

class TaxYearSettings(db.Model):
    __tablename__ = "tax_year_settings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    year: Mapped[int] = mapped_column(Integer)
