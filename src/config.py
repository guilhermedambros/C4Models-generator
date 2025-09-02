import configparser
import os

def load_paths(properties_file=None):
    if properties_file is None:
        # Caminho absoluto para garantir que o arquivo seja encontrado
        properties_file = os.path.join(os.path.dirname(__file__), "paths.properties")
    config = configparser.ConfigParser()
    config.read(properties_file)
    if not config.has_section("paths"):
        raise Exception(f"Seção [paths] não encontrada em {properties_file}")
    return (
        config.get("paths", "CONTROLLERS_PATH"),
        config.get("paths", "SERVICES_PATH"),
        config.get("paths", "REPOSITORIES_PATH"),
    )