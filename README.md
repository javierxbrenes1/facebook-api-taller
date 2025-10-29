# Facebook API - Taller de Extracción de Datos

## 📋 Propósito del Proyecto

Este proyecto es un **cliente de Python para la API de Facebook** diseñado para ser utilizado en un taller práctico de clase. El objetivo es aprender a extraer datos de Facebook (páginas, publicaciones, comentarios y reacciones) y almacenarlos en bases de datos NoSQL como MongoDB.

---

## 🖥️ Requisitos Previos

### 1. Verificar o Instalar un Editor de Código

Para trabajar con este proyecto, necesitas un editor de código. Recomendamos **Visual Studio Code**.

#### ¿Cómo verificar si tienes un editor instalado?
- Busca en el menú de inicio de Windows "Visual Studio Code" o "VSCode"

#### Si no tienes un editor, instala Visual Studio Code:
1. Ve a: https://code.visualstudio.com/
2. Haz clic en "Download for Windows"
3. Ejecuta el instalador descargado
4. Sigue las instrucciones del asistente de instalación
5. Marca la opción "Agregar al PATH" durante la instalación (importante)

---

### 2. Verificar o Instalar Python 3

Este proyecto utiliza **Python 3** (específicamente Python 3.7 o superior).

#### ¿Cómo verificar si tienes Python instalado?

1. Abre el **Símbolo del sistema** (CMD):
   - Presiona `Windows + R`
   - Escribe `cmd` y presiona Enter

2. En la ventana negra que se abre, escribe:
   ```bash
   python --version
   ```

3. Si Python está instalado, verás algo como: `Python 3.11.5` o similar
   - Si ves `Python 3.x.x` (donde x es cualquier número), ¡perfecto! Ya tienes Python 3 instalado
   - Si ves `Python 2.x.x`, necesitas instalar Python 3
   - Si aparece un error diciendo que "python" no es reconocido, necesitas instalar Python

#### Cómo instalar Python 3 en Windows 11:

1. Ve a la página oficial: https://www.python.org/downloads/
2. Haz clic en el botón grande amarillo "Download Python 3.x.x"
3. Ejecuta el archivo descargado
4. **¡MUY IMPORTANTE!** En la primera pantalla del instalador:
   - ✅ Marca la casilla "Add Python to PATH"
   - ✅ Marca la casilla "Install pip"
5. Haz clic en "Install Now"
6. Espera a que termine la instalación
7. Cierra y vuelve a abrir el Símbolo del sistema (CMD)
8. Verifica nuevamente con: `python --version`

---

## 🚀 Configuración del Proyecto

### Paso 1: Abrir el Proyecto en VSCode

1. Abre Visual Studio Code
2. Ve a **Archivo > Abrir Carpeta** (o File > Open Folder)
3. Navega hasta la carpeta `facebook-client`
4. Haz clic en "Seleccionar carpeta"

### Paso 2: Abrir la Terminal en VSCode

1. En VSCode, ve al menú superior: **Terminal > Nueva Terminal** (o presiona `` Ctrl + ` ``)
2. Se abrirá una terminal en la parte inferior de VSCode
3. Asegúrate de que estés en la carpeta correcta. Deberías ver algo como:
   ```
   PS C:\ruta\a\tu\proyecto\facebook-client>
   ```

### Paso 3: Crear el Entorno Virtual (venv)

Un entorno virtual es un espacio aislado para instalar las dependencias del proyecto sin afectar tu sistema.

1. En la terminal de VSCode, escribe:
   ```bash
   python -m venv venv
   ```

2. Espera unos segundos. Verás que se crea una carpeta llamada `venv` en tu proyecto

3. Activa el entorno virtual:
   ```bash
   venv\Scripts\activate
   ```

4. Si la activación fue exitosa, verás `(venv)` al inicio de tu línea de comandos:
   ```
   (venv) PS C:\ruta\a\tu\proyecto\facebook-client>
   ```

**Nota:** Si Windows te muestra un error de permisos al activar el entorno virtual, ejecuta este comando en PowerShell como administrador:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Luego intenta activar el venv nuevamente.

### Paso 4: Instalar las Dependencias

Con el entorno virtual activado, instala las librerías necesarias:

1. Asegúrate de que `(venv)` aparezca en tu terminal
2. Ejecuta:
   ```bash
   pip install -r requirements.txt
   ```

3. Además, necesitamos instalar algunas dependencias adicionales que el proyecto utiliza:
   ```bash
   pip install requests pymongo
   ```

4. Espera a que se descarguen e instalen todas las librerías

---

## 📚 Explicación de los Archivos del Proyecto

### 1. `facebook_client.py`

Este archivo contiene todas las funciones para interactuar con la **API de Facebook Graph**.

**Funciones principales:**

- **`get_pages()`**: Obtiene todas las páginas de Facebook asociadas a tu cuenta
  - Retorna una lista con información de cada página (nombre, ID, token de acceso)

- **`get_posts(page_id, page_access_token)`**: Obtiene todas las publicaciones de una página específica
  - Parámetros:
    - `page_id`: El identificador único de la página
    - `page_access_token`: Token de acceso de la página
  - Retorna: Lista de publicaciones con su contenido

- **`get_comments(post_id, page_access_token)`**: Obtiene todos los comentarios de una publicación
  - Parámetros:
    - `post_id`: El identificador de la publicación
    - `page_access_token`: Token de acceso de la página
  - Retorna: Lista de comentarios

- **`get_reactions(post_id, page_access_token)`**: Obtiene todas las reacciones (me gusta, me encanta, etc.) de una publicación
  - Parámetros similares a `get_comments`
  - Retorna: Lista de reacciones con tipo y usuario

**Variables importantes:**
- `access_token`: Tu token de acceso personal de Facebook (necesario para autenticarte)
- `host`: URL base de la API de Facebook Graph (v24.0)

---

### 2. `storage.py`

Este archivo maneja el **almacenamiento de datos** en bases de datos.

**Funciones principales:**

- **`get_mongodb_database()`**: Establece conexión con MongoDB local
  - Conecta a `mongodb://localhost:27017/`
  - Crea/obtiene la base de datos llamada `facebook`
  - Retorna: Objeto de base de datos

- **`save_posts_in_mongodb(posts)`**: Guarda las publicaciones en MongoDB
  - Parámetros:
    - `posts`: Lista de publicaciones con comentarios y reacciones
  - Crea/usa la colección `facebook_posts`
  - Inserta todas las publicaciones

- **`save_posts_in_sql_server(posts)`**: **Función por completar** (parte del taller)
  - Esta función está vacía y es parte del ejercicio práctico
  - Los estudiantes deben implementarla para guardar en SQL Server

**Nota:** Para usar MongoDB, necesitas tener MongoDB instalado localmente en tu máquina y el servicio corriendo en el puerto 27017.

---

### 3. `main.py`

Este es el **archivo principal** que ejecuta todo el flujo del programa.

**Flujo de ejecución paso a paso:**

1. **Importa los módulos necesarios:**
   - `facebook_client`: Para obtener datos de Facebook
   - `storage`: Para guardar los datos

2. **Paso 1 - Obtiene todas las páginas:**
   ```python
   pages = facebook_client.get_pages()
   ```
   
3. **Paso 2 - Filtra la página deseada:**
   - Busca la página llamada "CUC Almacenes de datos"
   - Usa `next()` para encontrar la primera página que coincida con el nombre

4. **Paso 3 - Obtiene las publicaciones:**
   - Usa el ID y token de acceso de la página encontrada
   - Descarga todas las publicaciones

5. **Paso 4 - Enriquece cada publicación:**
   - Para cada publicación, obtiene sus comentarios
   - Para cada publicación, obtiene sus reacciones
   - Agrega esta información a la publicación

6. **Paso 5 - Guarda en MongoDB:**
   - Llama a la función de storage para guardar todo

**TODOs del taller (actividades para completar):**
- Línea 31: Leer la documentación del Pages API y obtener información adicional
- Línea 38: Implementar el guardado en SQL Server

---

## ▶️ Cómo Ejecutar el Proyecto

### Ejecutar el Programa Principal

1. Asegúrate de que el entorno virtual esté activado (debes ver `(venv)` en tu terminal)

2. Verifica que MongoDB esté corriendo (si vas a usar la función de guardado):
   - Abre otra ventana de CMD
   - Ejecuta: `net start MongoDB` (si tienes MongoDB instalado como servicio)

3. En la terminal de VSCode, ejecuta:
   ```bash
   python main.py
   ```

4. El programa ejecutará todos los pasos automáticamente:
   - Obtendrá las páginas de tu cuenta
   - Buscará la página "CUC Almacenes de datos"
   - Descargará todas las publicaciones
   - Obtendrá comentarios y reacciones
   - Guardará todo en MongoDB

5. Si todo funciona correctamente, verás el proceso completarse sin errores


## 🎯 Actividades del Taller

Como parte del taller, se espera que completes las siguientes actividades:

### Actividad 1: Explorar el API de Facebook
- Lee la documentación oficial: https://developers.facebook.com/docs/graph-api/reference/page/
- Identifica qué otra información puedes obtener de las páginas
- Modifica `facebook_client.py` para agregar una nueva función que obtenga esa información

### Actividad 2: Implementar Guardado en SQL Server
- Completa la función `save_posts_in_sql_server()` en `storage.py`
- Instala el driver necesario: `pip install pyodbc`
- Crea la conexión a SQL Server
- Diseña las tablas necesarias
- Implementa la lógica de inserción

### Actividad 3: Analizar los Datos
- Usa MongoDB Compass o cualquier herramienta para visualizar los datos guardados
- Analiza qué información es más relevante
- Piensa en qué consultas podrías hacer sobre estos datos

---

## 📝 Notas Adicionales
- Este código es solo para fines educativos
- Respeta las políticas de uso de la API de Facebook

---

## 🆘 Ayuda

Si tienes problemas durante el taller:
1. Lee cuidadosamente los mensajes de error
2. Verifica que todos los pasos previos se hayan completado correctamente
3. Consulta con el grupo que esta exponiendo
4. Revisa la documentación oficial de las herramientas utilizadas

---

## 📖 Recursos Útiles

- [Documentación de Python](https://docs.python.org/es/3/)
- [Facebook Graph API Documentation](https://developers.facebook.com/docs/graph-api/)
- [MongoDB Documentation](https://docs.mongodb.com/)
- [Requests Library](https://requests.readthedocs.io/)

---

¡Buena suerte con el taller! 🚀

