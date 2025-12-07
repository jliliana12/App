*Sistema de Trazabilidad de Equipos METRONEX – COLMETRO SAS*

Este proyecto es una aplicación web desarrollada con Flask (Python) para gestionar el registro, trazabilidad y control de básculas, balanzas y equipos de pesaje en un laboratorio metrológico.
Permite registrar equipos, actualizar su estado, consultar historial, generar informes y recibir alertas internas.

*Objetivos del Proyecto*

- Simular la trazabilidad de equipos ingresados a reparación.

- Controlar el flujo de información desde la recepción hasta la entrega.

- Visualizar el estado de cada equipo en tiempo real.

- Generar informes consultables sobre equipos y su historial.

*Tecnologías Utilizadas*

Frontend:

- HTML5

- CSS3

- Bootstrap 5

- Bootstrap Icons

Backend:

- Python 3

- Flask

- Jinja2

Control de versión:

- Git

- GitHub

*Estructura del Proyecto*

Funcionalidades Principales

✔ Registrar equipos

Formulario para agregar información técnica del equipo recibido.

✔ Actualizar estado

Cambiar estado: recibido, en diagnóstico, reparación, calibración, entregado, etc.

✔ Historial

Visualiza cambios, estados y fechas asociados a cada equipo.

✔ Alertas

Genera alertas internas (por ejemplo: equipos retrasados).

✔ Informes

Módulo para generar y descargar informes de trazabilidad

📁 Instalación Local
# 1. Clonar el repositorio
git clone https://github.com/jliliana12/METRONEX-APP.git

# 2. Crear entorno virtual 
python -m venv venv
venv\Scripts\activate 

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar la aplicación
python app.py

Autor

Proyecto desarrollado para la materia de desarrollo de aplicaciones web, con fines académicos.

Estudiante: Vicky Liliana Merchan Amezquita
Empresa simulada: Laboratorio de Metrología Colmetro SAS
Año: 2025

📜 Licencia


Este proyecto es de uso académico y no tiene fines comerciales.





