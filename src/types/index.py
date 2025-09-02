from typing import List, Dict, Any

class Component:
    def __init__(self, name: str, description: str, component_type: str):
        self.name = name
        self.description = description
        self.component_type = component_type

class Relationship:
    def __init__(self, source: Component, target: Component, relationship_type: str):
        self.source = source
        self.target = target
        self.relationship_type = relationship_type

def get_component_types() -> List[str]:
    return ["Person", "Container", "Database", "SystemBoundary"]

def get_relationship_types() -> List[str]:
    return ["Uses", "Consumes", "Stores", "Triggers"]