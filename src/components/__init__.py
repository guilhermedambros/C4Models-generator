class Component:
    def __init__(self, data):
        self.name = data.get("name", "")
        self.type = data.get("type", "")
        self.path = data.get("path", "")
        self.content = data.get("content", "")  # Adicione este atributo

    def __repr__(self):
        return f"Component(name={self.name}, type={self.type}, path={self.path})"

    def find_autowired_targets(self, all_names):
        return find_autowired_targets(self.content, all_names)