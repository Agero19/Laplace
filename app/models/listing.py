from datetime import datetime
from uuid import uuid4

from sqlalchemy import Boolean, Column, DateTime, Float, String
from sqlalchemy.dialects.postgresql import UUID

from app.core.database import Base


class Listing(Base):
    """
    Represents a bike listing tracked over time.

    first_seen / last_seen enable time-on-market and disappearance metrics,
    which are essential for liquidity calculations.
    """

    __tablename__ = "listings"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    marketplace = Column(String, nullable=False, index=True)

    title = Column(String, nullable=False)
    brand = Column(String, nullable=True)
    model = Column(String, nullable=True)

    category = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    location = Column(String, nullable=True)

    url = Column(String, nullable=False, unique=True)

    first_seen = Column(DateTime, default=datetime.utcnow)
    last_seen = Column(DateTime, default=datetime.utcnow)

    active = Column(Boolean, default=True)
