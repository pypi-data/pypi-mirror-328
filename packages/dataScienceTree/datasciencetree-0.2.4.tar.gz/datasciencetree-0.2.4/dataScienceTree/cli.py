import importlib
import subprocess
import os
from pathlib import Path

import click
import questionary
from cookiecutter.main import cookiecutter
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

PROJECT_CONFIGS = {
    "Análisis de Datos": {
        "estructura": [
            "data/raw",
            "data/processed",
            "notebooks",
            "src/utils",
            "src/visualization",
            "reports",
            "tests",
        ],
        "features": [
            "Pre-commit hooks",
            "Documentación (MKDocs)",
        ],
        "requirements": [
            "pandas",
            "numpy",
            "matplotlib",
            "seaborn",
            "jupyter",
            "pytest",
            "black",
            "ruff",
            "ipykernel",
        ],
        "docker": False
    },
    "Machine Learning": {
        "estructura": [
            "data/raw",
            "data/processed",
            "notebooks",
            "src/utils",
            "src/visualization",
            "src/models",
            "src/features",
            "src/evaluation",
            "models/trained",
            "reports",
            "tests",
        ],
        "features": [
            "Pre-commit hooks",
            "Documentación (MKDocs)",
            "MLflow",
            "DVC",
        ],
        "requirements": [
            "pandas",
            "numpy",
            "matplotlib",
            "seaborn",
            "scikit-learn",
            "tensorflow",
            "pytorch",
            "jupyter",
            "mlflow",
            "dvc",
            "pytest",
            "black",
            "ruff",
            "ipykernel",
        ],
        "docker": True
    },
    "Data Engineering": {
        "estructura": [
            "data/raw",
            "data/processed",
            "data/external",
            "notebooks",
            "src/utils",
            "src/visualization",
            "src/models",
            "src/features",
            "src/pipelines",
            "src/etl",
            "src/api",
            "models/trained",
            "airflow/dags",
            "docker",
            "reports",
            "tests",
        ],
        "features": [
            "Pre-commit hooks",
            "Documentación (MKDocs)",
            "FastAPI",
            "Airflow",
            "MLflow",
            "DVC",
        ],
        "requirements": [
            "pandas",
            "numpy",
            "matplotlib",
            "seaborn",
            "scikit-learn",
            "tensorflow",
            "pytorch",
            "fastapi",
            "uvicorn",
            "apache-airflow",
            "mlflow",
            "dvc",
            "docker-compose",
            "pytest",
            "black",
            "ruff",
            "ipykernel",
        ],
        "docker": True
    }
}

def get_template_path():
    with importlib.resources.path("dataScienceTree", "template") as template_path:
        return str(template_path)

def validate_project_name(name: str) -> bool:
    return all(c.isalnum() or c in ("-", "_") for c in name)

def create_project_structure(project_path: Path, estructura: list):
    for path in estructura:
        (project_path / path).mkdir(parents=True, exist_ok=True)
        (project_path / path / '__init__.py').touch()

def create_requirements(project_path: Path, requirements: list, environment_type: str):
    # Solo crear requirements.txt si es venv
    if environment_type == "venv":
        with open(project_path / 'requirements.txt', 'w') as f:
            f.write('\n'.join(requirements))

def create_dockerfile(project_path: Path, project_type: str):
    dockerfile_content = """
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
"""

    if project_type == "Data Engineering":
        dockerfile_content += '\nCMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]'
    elif project_type == "Machine Learning":
        dockerfile_content += '\nCMD ["python", "src/models/train_model.py"]'

    with open(project_path / 'Dockerfile', 'w') as f:
        f.write(dockerfile_content)

def create_pyproject_toml(project_path: Path, project_name: str, project_type: str, environment_type: str):
    if environment_type == "poetry":
        content = f"""
[tool.poetry]
name = "{project_name}"
version = "0.1.0"
description = "Proyecto de {project_type}"
authors = ["Your Name <your.email@example.com>"]

[tool.poetry.dependencies]
python = ">=3.11"

[tool.poetry.group.dev.dependencies]
pytest = "^7.0"
black = "^23.0"
ruff = "^0.1.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.ruff]
line-length = 88
target-version = "py311"

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]

[tool.black]
line-length = 88
target-version = ['py311']
"""
    elif environment_type == "uv":
        content = f"""
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "{project_name}"
version = "0.1.0"
description = "Proyecto de {project_type}"
requires-python = ">=3.11"
authors = [
    {{ name = "Your Name", email = "your.email@example.com" }}
]

[tool.hatch.build.targets.wheel]
packages = ["src"]

[tool.ruff]
line-length = 88
target-version = "py311"

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]

[tool.black]
line-length = 88
target-version = ['py311']
"""
    else:
        # Para venv no creamos pyproject.toml
        return

    with open(project_path / 'pyproject.toml', 'w') as f:
        f.write(content)

def install_dependencies(project_path: Path, environment_type: str, requirements: list):
    if environment_type == "poetry":
        # No necesitamos ejecutar poetry init ya que ya tenemos el pyproject.toml
        for requirement in requirements:
            subprocess.run(
                ["poetry", "add", requirement.strip()],
                cwd=project_path,
                capture_output=True
            )
    elif environment_type == "uv":
        # Crear el entorno virtual primero
        subprocess.run(
            ["python", "-m", "venv", ".venv"],
            cwd=project_path,
            capture_output=True
        )
        # Usar uv para instalar las dependencias
        if os.name == 'nt':  # Windows
            uv_pip = str(project_path / ".venv" / "Scripts" / "python") + " -m pip"
        else:  # Unix/Linux
            uv_pip = str(project_path / ".venv" / "bin" / "python") + " -m pip"

        for requirement in requirements:
            subprocess.run(
                f"{uv_pip} install {requirement}",
                cwd=project_path,
                shell=True,
                capture_output=True
            )
    elif environment_type == "venv":
        subprocess.run(
            ["python", "-m", "venv", ".venv"],
            cwd=project_path,
            capture_output=True
        )
        if os.name == 'nt':  # Windows
            pip_path = project_path / ".venv" / "Scripts" / "pip"
        else:  # Unix/Linux
            pip_path = project_path / ".venv" / "bin" / "pip"
        subprocess.run(
            [str(pip_path), "install", "-r", "requirements.txt"],
            cwd=project_path,
            capture_output=True
        )

@click.command()
@click.argument("project_name", required=True)
def main(project_name: str):
    """Crear un nuevo proyecto Python con buenas prácticas y herramientas modernas."""
    console.print(Panel.fit("Crear Proyecto Python", style="bold blue"))

    if not project_name:
        project_name = questionary.text(
            "¿Cuál es el nombre de tu proyecto?",
            validate=lambda text: len(text) > 0 and validate_project_name(text),
        ).ask()

    project_type = questionary.select(
        "Selecciona el tipo de proyecto:",
        choices=list(PROJECT_CONFIGS.keys())
    ).ask()

    environment_type = questionary.select(
        "¿Qué tipo de entorno virtual deseas usar?",
        choices=["poetry", "uv", "venv"]
    ).ask()

    use_docker = False
    if project_type in ["Data Engineering", "Machine Learning"]:
        use_docker = questionary.confirm(
            "¿Deseas incluir Docker en tu proyecto?",
            default=True
        ).ask()

    config = PROJECT_CONFIGS[project_type].copy()
    config["docker"] = use_docker

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console
    ) as progress:
        # Crear el proyecto base
        task = progress.add_task("Creando estructura del proyecto...", total=None)
        project_path = Path.cwd() / project_name
        project_path.mkdir(exist_ok=True)

        # Crear estructura de carpetas
        progress.update(task, description="Creando directorios...")
        create_project_structure(project_path, config["estructura"])

        # Crear requirements.txt si es necesario
        progress.update(task, description="Configurando dependencias...")
        create_requirements(project_path, config["requirements"], environment_type)

        # Crear pyproject.toml si es necesario
        progress.update(task, description="Creando archivo de configuración...")
        create_pyproject_toml(project_path, project_name, project_type, environment_type)

        # Crear Dockerfile si es necesario
        if config["docker"]:
            progress.update(task, description="Configurando Docker...")
            create_dockerfile(project_path, project_type)

        # Instalar dependencias
        progress.update(task, description="Instalando dependencias...")
        install_dependencies(project_path, environment_type, config["requirements"])

        # Inicializar git
        progress.update(task, description="Inicializando repositorio git...")
        subprocess.run(["git", "init"], cwd=project_path, capture_output=True)

        progress.update(task, description="¡Proyecto creado exitosamente!")

    console.print(f"\n✨ ¡Proyecto [bold green]{project_name}[/] creado exitosamente!")
    console.print("\nEstructura creada para:", project_type)
    console.print("\nEntorno virtual:", environment_type)
    console.print("\nCaracterísticas incluidas:")
    for feature in config["features"]:
        console.print(f"  - {feature}")

    console.print("\nPróximos pasos:")
    console.print(f"  1. cd {project_name}")

    if environment_type == "poetry":
        console.print("  2. poetry shell")
        console.print("  3. poetry install")
    elif environment_type == "venv":
        if os.name == 'nt':
            console.print("  2. .venv\\Scripts\\activate")
        else:
            console.print("  2. source .venv/bin/activate")
    elif environment_type == "uv":
        if os.name == 'nt':
            console.print("  2. .venv\\Scripts\\activate")
        else:
            console.print("  2. source .venv/bin/activate")

    if config["docker"]:
        console.print(f"  3. docker build -t {project_name} .")
        console.print(f"  4. docker run -p 8000:8000 {project_name}")

if __name__ == "__main__":
    main()