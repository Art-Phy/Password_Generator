# Password Generator

<p align="left">
  <img src="https://img.shields.io/badge/python-3.10+-blue.svg" />
  <img src="https://img.shields.io/badge/CLI-Password%20Generator-orange" />
  <img src="https://img.shields.io/badge/Testing-pytest-green" />
  <img src="https://img.shields.io/badge/Status-v1.5.0%20Stable-success" />
</p>

Herramienta **CLI desarrollada en Python** para generar contraseñas aleatorias de forma segura mediante el módulo estándar **`secrets`**, tanto de forma interactiva como mediante argumentos desde la terminal.

Permite utilizar perfiles predefinidos, seleccionar distintos conjuntos de caracteres, consultar la entropía estimada y fortaleza de las contraseñas generadas y copiarlas directamente al portapapeles sin mostrarlas en la terminal.

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
- Copia directa de contraseñas al portapapeles mediante `--copy`.
- Protección de la salida CLI para evitar mostrar contraseñas cuando se utiliza `--copy`.
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
│       ├── clipboard.py
│       ├── generator.py
│       ├── profiles.py
│       └── strength.py
├── tests/
│   ├── __init__.py
│   ├── test_cli.py
│   ├── test_clipboard.py
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
- `clipboard.py` → integración con el portapapeles del sistema operativo.
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

La instalación incluye las dependencias necesarias para utilizar las funcionalidades disponibles, incluyendo `pyperclip` para la integración con el portapapeles.

> [!NOTE]
> En algunos entornos Linux puede ser necesario instalar herramientas adicionales para acceder al portapapeles, dependiendo del servidor gráfico y de la configuración del sistema.
>
> El soporte del portapapeles depende de los mecanismos disponibles en el sistema operativo.

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

La versión `v1.4.0` incorporó estimación de entropía y clasificación de fortaleza para las contraseñas generadas.

Para mostrar esta información utiliza:

```bash
password-generator --profile secure --show-strength
```

Ejemplo de salida:

```text
<generated-password>

Entropy: 209.7 bits
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

### Clipboard Support

La versión `v1.5.0` incorpora soporte para copiar contraseñas directamente al portapapeles del sistema operativo.

El argumento `--copy` permite generar una contraseña y copiarla sin mostrar su contenido en la terminal.

#### Copiar una contraseña

```bash
password-generator --copy
```

Salida:

```text
Password copied to clipboard
```

La contraseña queda disponible en el portapapeles para pegarla posteriormente.

#### Copiar utilizando un perfil

```bash
password-generator --profile secure --copy
```

También puede utilizarse con conjuntos de caracteres y longitudes personalizadas:

```bash
password-generator \
  --charset safe \
  --length 24 \
  --copy
```

#### Copiar mostrando la fortaleza

El argumento `--copy` puede combinarse con `--show-strength` para consultar la entropía y fortaleza sin revelar la contraseña.

```bash
password-generator \
  --profile secure \
  --copy \
  --show-strength
```

Ejemplo de salida:

```text
Password copied to clipboard

Entropy: 209.7 bits
Strength: Very Strong
```

#### Limitaciones

El argumento `--copy` está diseñado para trabajar con una única contraseña.

No permite copiar varias contraseñas simultáneamente:

```bash
password-generator --count 5 --copy
```

En este caso, la herramienta devuelve un error:

```text
password-generator: error: --copy only supports generating one password
```

Esto evita comportamientos ambiguos al generar múltiples contraseñas.

#### Consideraciones de seguridad

El portapapeles es un recurso compartido del sistema operativo y no debe considerarse un almacenamiento seguro.

Password Generator aplica las siguientes medidas:

- No muestra la contraseña en la terminal cuando se utiliza `--copy`.
- No guarda automáticamente las contraseñas generadas en archivos.
- Gestiona los errores de acceso al portapapeles.
- Limita `--copy` a una única contraseña por ejecución.
- Permite consultar la fortaleza sin revelar la contraseña copiada.

> [!WARNING]
> Las contraseñas copiadas pueden permanecer en el portapapeles hasta que su contenido sea sustituido o eliminado.
>
> Algunas aplicaciones o gestores de historial del portapapeles pueden conservar copias adicionales.
>
> La versión actual no implementa borrado automático del portapapeles. Se recomienda limpiar su contenido después de utilizar la contraseña, especialmente en equipos compartidos.

---

### Combinaciones

Los perfiles, conjuntos de caracteres, longitud, análisis de fortaleza y soporte de portapapeles pueden combinarse según las necesidades.

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

Generar una contraseña segura y copiarla directamente:

```bash
password-generator \
  --profile wifi \
  --copy
```

Generar una contraseña personalizada, copiarla y consultar su fortaleza:

```bash
password-generator \
  --charset safe \
  --length 32 \
  --copy \
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

Ejecutar los tests con información detallada:

```bash
pytest -v
```

Ejecutar únicamente los tests de integración del portapapeles:

```bash
pytest tests/test_clipboard.py tests/test_cli.py -v
```

La suite cubre, entre otros:

- Generación individual de contraseñas.
- Generación múltiple.
- Validación de parámetros.
- Exclusión de caracteres ambiguos.
- Cálculo de entropía.
- Clasificación de fortaleza.
- Valores límite de las distintas clasificaciones.
- Copia de contraseñas mediante el portapapeles.
- Manejo de errores cuando el portapapeles no está disponible.
- Validación de contraseñas vacías durante la copia.
- Protección de la salida CLI para evitar mostrar contraseñas copiadas.
- Rechazo de `--copy` cuando se solicitan múltiples contraseñas.

Los tests relacionados con el portapapeles utilizan mocks para comprobar su funcionamiento sin depender de un portapapeles real.

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
- `pyperclip`
- `unittest.mock`
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
- [x] Clipboard support
- [ ] Export generated passwords
- [ ] Custom user-defined profiles

---

> [!TIP]
> ###### Si consideras útil el repositorio, puedes apoyarlo dejando una ⭐
