from typing import Dict, List
from pydantic import BaseModel


class GlobalConfig(BaseModel):
    device: str
    parameters: Dict[str, str]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }
