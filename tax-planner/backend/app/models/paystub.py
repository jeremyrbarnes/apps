from app import db
from SQLAlchemy.orm import Mapped, mapped_column
from SQLAlchemy import String, Integer, Float, DateTime
from datetime import datetime, timezone

class TaxYearSettings(db.Model):
    __tablename__ = "paystubs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    date: Mapped[datetime] = mapped_column(DateTime)

    payee: Mapped[String] = mapped_column(String)

    expected_gross_pay: Mapped[Float] = mapped_column(Float)

    actual_gross_pay: Mapped[Float] = mapped_column(Float)

    pre_tax_retirement_contribution: Mapped[Float] = mapped_column(Float)

    post_tax_retirement_contribution: Mapped[Float] = mapped_column(Float)

    medical_dental_pre_tax_contribution: Mapped[Float] = mapped_column(Float)

    federal_witholding: Mapped[Float] = mapped_column(Float)

    state_witholding: Mapped[Float] = mapped_column(Float)

    social_security_tax: Mapped[Float] = mapped_column(Float)

    medicare_tax: Mapped[Float] = mapped_column(Float)

