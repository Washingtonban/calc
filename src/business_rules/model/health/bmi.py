import enum
from sqlalchemy import Column, Integer, String, Float, Enum, DATETIME
from src.business_rules.model.base_model import BaseHealth


class BmiClassify(enum.Enum):
    THINNESS = 0
    NORMAL = 0
    OVERWEIGHT = 1
    OBESITY = 2
    SERIUS_OBESITY = 3


class Bmi(BaseHealth):
    __tablename__ = 'bmi'

    id = Column(Integer, primary_key=True)
    user = Column(String(50), nullable=False)
    description = Column(String(250), nullable=False)
    bmi = Column(Float, nullable=False)
    classify = Column(Enum(BmiClassify), nullable=False)
    created_at = Column(DATETIME, nullable=False)
    updated_at = Column(DATETIME, nullable=False)
