class Relationship:
    def __init__(self, component):
        # Dummy relationship: each component "depends on" itself for demonstration
        self.source = component.name
        self.target = component.name
        self.type = "self-dependency"

    def __repr__(self):
        return f"Relationship({self.source} -> {self.target}, type={self.type})"