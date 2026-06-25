
<p align="left">
  <img src="https://img.shields.io/badge/python-3.10+-blue.svg" />
  <img src="https://img.shields.io/badge/CLI-Password%20Generator-orange" />
  <img src="https://img.shields.io/badge/Testing-pytest-green" />
  <img src="https://img.shields.io/badge/Status-v1.2.0%20Stable-success" />
  <img src="https://img.shields.io/badge/License-MIT-lightgrey" />
</p>

Herramienta **CLI desarrollada en Python** para generar contraseñas aleatorias de forma segura mediante el módulo estándar **`secrets`**, tanto de forma interactiva como mediante argumentos desde la terminal.

Ideal como utilidad ligera para generar contraseñas criptográficamente seguras desde cualquier entorno.

---

### Funcionalidades

#### Core

- Generación de una o varias contraseñas aleatorias.
- Generación mediante el módulo **`secrets`** de Python para mayor seguridad.
- Longitud de contraseña configurable.
- Número de contraseñas configurable.
- Modo interactivo guiado.
- Ejecución mediante argumentos CLI.
- Validación automática de parámetros de entrada.
- Manejo de errores mediante excepciones.
- Proyecto organizado siguiendo estructura modular `src/`.
- Instalación como paquete mediante `pyproject.toml`.
- Tests automatizados con `pytest`.

---

### Project Structure

Proyecto reorganizado siguiendo una estructura modular profesional:

```text
Password_Generator/
├── src/
│   └── password_generator/
│       ├── __init__.py
│       ├── cli.py
│       └── generator.py
├── tests/
│   ├── __init__.py
│   └── test_generator.py
├── CHANGELOG.md
├── LICENSE.md
├── README.md
├── pyproject.toml
├── requirements.txt
└── main.py
```

#### Separación de responsabilidades

- `cli.py` → interfaz interactiva y argumentos CLI.
- `generator.py` → lógica de generación de contraseñas.
- `tests/` → pruebas automatizadas.

---

### Instalación

Clona el repositorio:

```bash
git clone https://github.com/Art-Phy/Password_Generator.git
cd Password_Generator
```

Crea un entorno virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instala el proyecto:

```bash
python3 -m pip install -e .
```

---

### Uso

#### Modo interactivo

```bash
password-generator
```

Permite generar una o varias contraseñas respondiendo a unas sencillas preguntas desde la terminal.

---

#### Generar una contraseña

```bash
password-generator --length 20
```

o su versión corta:

```bash
password-generator -l 20
```

---

#### Generar varias contraseñas

```bash
password-generator --length 20 --count 5
```

o

```bash
password-generator -l 20 -c 5
```

---

#### Ayuda CLI

```bash
password-generator --help
```

---

### Testing

Ejecutar todos los tests:

```bash
pytest
```

---

> [!NOTE]
> ###### Durante el desarrollo también puedes ejecutar el proyecto mediante:
>
> ```bash
> python3 main.py
> ```

---

### Stack Tecnológico

- Lenguaje: Python
- `secrets`
- `string`
- `argparse`
- Packaging mediante `pyproject.toml`
- Testing: `pytest`

---

### Roadmap

- [x] Modular project structure
- [x] Automated testing
- [x] Installable package
- [x] Interactive mode
- [x] CLI arguments
- [x] Cryptographically secure password generation
- [ ] Character set customization
- [ ] Exclude ambiguous characters
- [ ] Password strength indicator
- [ ] Clipboard support

---

> [!TIP]
> ###### Si consideras útil el repositorio, puedes apoyarlo dejando una ⭐