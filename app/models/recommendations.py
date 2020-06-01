from datetime import datetime
from typing import List

from .base import Base


class Recommendations(Base):
    recommendations: List[str]
    timestamp: datetime = datetime.utcnow()

