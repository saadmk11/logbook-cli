import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
)
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class LogBook(Base):
    """Table to store users log entries"""
    __tablename__  = "log_book"

    id = Column(Integer, primary_key=True)
    description = Column(String(320), nullable=False)
    log_datetime = Column(DateTime, nullable=False)

    created_at = Column(
        DateTime,
        default=datetime.datetime.now,
        nullable=False
    )
    updated_at = Column(
        DateTime,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now,
        nullable=False
    )
