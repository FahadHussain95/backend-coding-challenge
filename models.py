from pydantic import BaseModel
from pydantic.schema import Optional
from sqlalchemy import Column, Boolean, ForeignKey, Integer, String, Float, DateTime, JSON, TIMESTAMP

from databse import Base


class Planning(Base):
    __tablename__ = "planning"

    id = Column(Integer, primary_key=True, index=True)
    original_id = Column(String, unique=True, index=True, nullable=False)
    talent_id = Column(String(50), nullable=True)
    talent_name = Column(String(50), nullable=True)
    talent_grade = Column(String(50), nullable=True)
    booking_grade = Column(String(50), nullable=True)
    operating_unit = Column(String(50), nullable=False)
    officer_city = Column(String(50), nullable=True)
    office_postal_code = Column(String(50), nullable=False)
    job_manager_name = Column(String(50), nullable=True)
    job_manager_id = Column(String(50), nullable=True)
    total_hours = Column(Float(50), nullable=False)
    start_date = Column(String, nullable=False)
    end_date = Column(String, nullable=False)
    client_name = Column(String(50), nullable=True)
    client_id = Column(String(50), nullable=False)
    industry = Column(String(50), nullable=True)
    required_skills = Column(String, nullable=True)
    optional_skills = Column(String, nullable=True)
    is_unassigned = Column(Boolean, default=True)

    # items = relationship("Item", back_populates="owner")
