from datetime import datetime, timezone

from pydantic import BaseModel, BaseConfig


class Base(BaseModel):
    class Config(BaseConfig):
        allow_population_by_alias = True
        arbitary_types_allowed = True
        json_encoders = {
            datetime: lambda dt: dt.replace(tzinfo=timezone.utc).isoformat().replace("+00:00", "Z")
        }

