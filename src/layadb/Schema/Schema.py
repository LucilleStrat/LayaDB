from pydantic import BaseModel
from . import Enums

class IntentSchema(BaseModel):
    intent: Enums.Intent
