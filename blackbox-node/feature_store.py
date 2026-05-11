from dataclasses import dataclass, asdict
from typing import Dict, List


@dataclass
class FeatureSchema:
    version: str
    features: List[str]


class FeatureStore:
    """
    Control de versiones de features.
    Evita mismatch entre training vs inference.
    """

    def __init__(self):
        self.schemas: Dict[str, FeatureSchema] = {}

    def register_schema(self, version: str, features: List[str]):
        self.schemas[version] = FeatureSchema(version, features)

    def get_schema(self, version: str) -> FeatureSchema:
        return self.schemas.get(version)

    def validate(self, version: str, input_features: List[str]) -> bool:
        schema = self.get_schema(version)
        if not schema:
            return False
        return schema.features == input_features


feature_store = FeatureStore()