import os
import re

def parse_input(src_dir):
    # Parse Java files and infer component type by filename or folder
    components = []
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith(".java"):
                path = os.path.join(root, file)
                with open(path, encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                    if "@Controller" in content:
                        ctype = "Controller"
                    elif "@Service" in content:
                        ctype = "Service"
                    elif "@Repository" in content:
                        ctype = "Repository"
                    else:
                        ctype = "Class"
                name = file.replace(".java", "")
                components.append({
                    "name": name,
                    "type": ctype,
                    "path": root,
                    "content": content
                })
    return components

def generate_report(components, relationships):
    report = "Componentes encontrados:\n"
    for c in components:
        report += f"  - {c}\n"
    report += "\nRelações encontradas:\n"
    for r in relationships:
        report += f"  - {r}\n"
    return report