
# Password Generator

<p align="left">
  <img src="https://img.shields.io/badge/python-3.10+-blue.svg" />
  <img src="https://img.shields.io/badge/CLI-Password%20Generator-orange" />
  <img src="https://img.shields.io/badge/Testing-pytest-green" />
  <img src="https://img.shields.io/badge/Status-v1.4.0%20Stable-success" />
</p>

Herramienta **CLI desarrollada en Python** para generar contraseñas aleatorias de forma segura mediante el módulo estándar **`secrets`**, tanto de forma interactiva como mediante argumentos desde la terminal.

Permite utilizar perfiles predefinidos, seleccionar distintos conjuntos de caracteres y consultar la entropía estimada y fortaleza de las contraseñas generadas.

---

### Funcionalidades

#### Core

- Generación de una o varias contraseñas aleatorias.
- Generación criptográficamente segura mediante el módulo **`secrets`** de Python.
- Longitud de contraseña configurable.
- Número de contraseñas configurable.
- Modo interactivo guiado.
- Ejecución mediante argumentos CLI.
- Perfiles predefinidos para distintos escenarios de uso.
- Conjuntos de caracteres configurables mediante `--charset`.
- Generación segura excluyendo caracteres visualmente ambiguos.
- Estimación de entropía basada en longitud y tamaño del conjunto de caracteres.
- Clasificación de fortaleza de las contraseñas generadas.
- Visualización opcional de entropía y fortaleza mediante `--show-strength`.
- Validación automática de parámetros de entrada.
- Manejo de errores mediante excepciones.
- Proyecto organizado siguiendo estructura modular `src/`.
- Instalación como paquete mediante `pyproject.toml`.
- Tests automatizados con `pytest`.

---

### Project Structure

Proyecto organizado siguiendo una estructura modular:

```text
Password_Generator/
├── src/
│   └── password_generator/
│       ├── __init__.py
│       ├── charsets.py
│       ├── cli.py
│       ├── generator.py
│       ├── profiles.py
│       └── strength.py
├── tests/
│   ├── __init__.py
│   ├── test_generator.py
│   └── test_strength.py
├── CHANGELOG.md
├── LICENSE.md
├── README.md
├── pyproject.toml
├── requirements.txt
└── main.py
```

#### Separación de responsabilidades

- `cli.py` → interfaz interactiva, argumentos CLI y resolución de configuración.
- `generator.py` → lógica de generación de contraseñas.
- `profiles.py` → perfiles predefinidos de generación.
- `charsets.py` → definición y configuración de conjuntos de caracteres.
- `strength.py` → cálculo de entropía y clasificación de fortaleza.
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

o:

```bash
password-generator -l 20 -c 5
```

---

### Password Profiles

La herramienta incluye perfiles predefinidos para distintos escenarios de uso.

| Profile | Longitud | Charset | Uso |
|---|---:|---|---|
| `web` | 16 | `all` | Contraseña de uso general |
| `wifi` | 24 | `safe` | Contraseña Wi-Fi evitando caracteres ambiguos |
| `pin` | 6 | `numbers` | PIN numérico |
| `secure` | 32 | `all` | Contraseña de alta seguridad |

#### Utilizar un perfil

```bash
password-generator --profile web
```

```bash
password-generator --profile wifi
```

```bash
password-generator --profile pin
```

```bash
password-generator --profile secure
```

Los valores definidos por un perfil pueden sobrescribirse mediante argumentos CLI.

Por ejemplo, generar un PIN de 8 dígitos:

```bash
password-generator --profile pin --length 8
```

O utilizar el perfil Wi-Fi con otro conjunto de caracteres:

```bash
password-generator --profile wifi --charset alphanumeric
```

---

### Character Sets

El argumento `--charset` permite seleccionar qué tipo de caracteres pueden utilizarse durante la generación.

| Charset | Descripción |
|---|---|
| `all` | Letras minúsculas, mayúsculas, números y símbolos |
| `letters` | Letras minúsculas y mayúsculas |
| `lowercase` | Solo letras minúsculas |
| `uppercase` | Solo letras mayúsculas |
| `numbers` | Solo números |
| `alphanumeric` | Letras y números |
| `safe` | Todos los tipos de caracteres excluyendo caracteres visualmente ambiguos |

Ejemplo:

```bash
password-generator --charset letters --length 20
```

Generar una contraseña alfanumérica:

```bash
password-generator --charset alphanumeric --length 24
```

Generar una contraseña utilizando el conjunto seguro:

```bash
password-generator --charset safe --length 24
```

El charset `safe` excluye caracteres que pueden confundirse visualmente:

```text
O 0 I l 1 | / \ ' " `
```

---

### Password Strength

La versión `v1.4.0` incorpora estimación de entropía y clasificación de fortaleza para las contraseñas generadas.

Para mostrar esta información utiliza:

```bash
password-generator --profile secure --show-strength
```

Ejemplo de salida:

```text
<generated-password>

Entropy: 209.8 bits
Strength: Very Strong
```

También puede combinarse con cualquier longitud, perfil o conjunto de caracteres:

```bash
password-generator \
  --charset safe \
  --length 24 \
  --show-strength
```

La fortaleza se clasifica en cuatro niveles:

| Entropía estimada | Clasificación |
|---:|---|
| Menos de 40 bits | `Weak` |
| 40 - 59.9 bits | `Medium` |
| 60 - 79.9 bits | `Strong` |
| 80 bits o más | `Very Strong` |

La entropía se estima teniendo en cuenta la longitud solicitada y el tamaño real del conjunto de caracteres utilizado durante la generación.

> [!NOTE]
> La estimación de entropía está diseñada para las contraseñas aleatorias generadas por esta herramienta a partir de un conjunto conocido de caracteres.
>
> No pretende funcionar como un analizador universal de contraseñas creadas manualmente por usuarios.

---

### Combinaciones

Los perfiles, conjuntos de caracteres, longitud y análisis de fortaleza pueden combinarse libremente.

Contraseña Wi-Fi de 32 caracteres:

```bash
password-generator \
  --profile wifi \
  --length 32
```

PIN de 8 dígitos mostrando su fortaleza:

```bash
password-generator \
  --profile pin \
  --length 8 \
  --show-strength
```

Generar cinco contraseñas seguras:

```bash
password-generator \
  --charset safe \
  --length 24 \
  --count 5
```

Generar tres contraseñas alfanuméricas mostrando su entropía:

```bash
password-generator \
  --charset alphanumeric \
  --length 20 \
  --count 3 \
  --show-strength
```

---

### Ayuda CLI

Para consultar todos los argumentos disponibles:

```bash
password-generator --help
```

---

### Testing

Ejecutar todos los tests:

```bash
pytest
```

La suite cubre, entre otros:

- Generación individual de contraseñas.
- Generación múltiple.
- Validación de parámetros.
- Exclusión de caracteres ambiguos.
- Cálculo de entropía.
- Clasificación de fortaleza.
- Valores límite de las distintas clasificaciones.

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
- `dataclasses`
- `math`
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
- [x] Character set customization
- [x] Exclude ambiguous characters
- [x] Predefined password profiles
- [x] Password strength indicator
- [ ] Clipboard support
- [ ] Export generated passwords
- [ ] Custom user-defined profiles

---

> [!TIP]
> ###### Si consideras útil el repositorio, puedes apoyarlo dejando una ⭐
