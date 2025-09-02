import sys
from diagrams import Diagram
from diagrams.c4 import Container, Database, Relationship

from components import Component
from utils import parse_input
from config import load_paths

def find_autowired_targets(content, all_names):
    # Procura por linhas com @Autowired e o nome da classe injetada
    targets = []
    for name in all_names:
        if f"@Autowired" in content and name in content:
            targets.append(name)
    return targets

def filter_components_by_path(components, path):
    return [comp for comp in components if path.replace("\\", "/") in comp.path.replace("\\", "/")]

def main():
    CONTROLLERS_PATH, SERVICES_PATH, REPOSITORIES_PATH = load_paths()

    print("Analisando componentes...")
    components_data = (
        parse_input(CONTROLLERS_PATH)
        + parse_input(SERVICES_PATH)
        + parse_input(REPOSITORIES_PATH)
    )
    print(f"Encontrados {len(components_data)} componentes.")

    components = [Component(data) for data in components_data]
    all_names = [comp.name for comp in components]

    # Filtra controllers, services e repositories
    controllers = filter_components_by_path(components, CONTROLLERS_PATH)
    services = filter_components_by_path(components, SERVICES_PATH)
    repositories = filter_components_by_path(components, REPOSITORIES_PATH)

    # Identifica explicitamente os services usados nos controllers via @Autowired
    explicit_service_names = set()
    controller_services_map = {}
    for ctrl in controllers:
        autowired_targets = find_autowired_targets(getattr(ctrl, "content", ""), [srv.name for srv in services])
        controller_services_map[ctrl.name] = autowired_targets
        explicit_service_names.update(autowired_targets)

    # Filtra apenas os services explicitamente usados nos controllers
    explicit_services = [srv for srv in services if srv.name in explicit_service_names]

    # Identifica explicitamente os repositories usados nos services explicitamente ligados aos controllers
    explicit_repository_names = set()
    service_repositories_map = {}
    for srv in explicit_services:
        autowired_targets = find_autowired_targets(getattr(srv, "content", ""), [repo.name for repo in repositories])
        service_repositories_map[srv.name] = autowired_targets
        explicit_repository_names.update(autowired_targets)

    explicit_repositories = [repo for repo in repositories if repo.name in explicit_repository_names]

    relations_log = []

    with Diagram("C4 - Componentes Java Detectados", filename="output/C4_Componentes_Java.png", show=False, direction="TB"):
        containers = {}
        # Adiciona controllers
        for comp in controllers:
            containers[comp.name] = Container(comp.name, "Controller", comp.name)
        # Adiciona apenas os services explicitamente ligados aos controllers
        for comp in explicit_services:
            containers[comp.name] = Container(comp.name, "Service", comp.name)
        # Adiciona apenas os repositories explicitamente ligados aos services
        for comp in explicit_repositories:
            containers[comp.name] = Container(comp.name, "Repository", comp.name)

        db = Database("Database", "Relational DB", "Armazena dados")

        # Relações controllers -> services
        for ctrl_name, service_names in controller_services_map.items():
            for srv_name in service_names:
                if srv_name in containers:
                    containers[ctrl_name] >> Relationship("@Autowired") >> containers[srv_name]
                    relations_log.append(f"{ctrl_name} --> {srv_name} [@Autowired]")

        # Relações services -> repositories
        for srv_name, repo_names in service_repositories_map.items():
            for repo_name in repo_names:
                if repo_name in containers:
                    containers[srv_name] >> Relationship("@Autowired") >> containers[repo_name]
                    relations_log.append(f"{srv_name} --> {repo_name} [@Autowired]")

        # Repositórios conectam ao banco de dados
        for comp in explicit_repositories:
            containers[comp.name] >> Relationship("Conecta") >> db
            relations_log.append(f"{comp.name} --> Database [Conecta]")

    print("\nRelações identificadas:")
    for rel in relations_log:
        print(rel)

    print("\nDiagrama finalizado.")

if __name__ == "__main__":
    main()