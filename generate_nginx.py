#!/usr/bin/env python3
import os
import sys

try:
    from dotenv import load_dotenv
except ImportError:
    print("Error: python-dotenv not installed.")
    print("Install it using: source venv/bin/activate && pip install python-dotenv")
    sys.exit(1)

# Cargar las variables de entorno del archivo .env
env_path = '.env'
if not os.path.exists(env_path):
    print("Error: .env file not found.")
    sys.exit(1)

load_dotenv(env_path)

# Leer el template
template_path = 'nginx.conf.template'
output_path = 'nginx.conf'

if not os.path.exists(template_path):
    print(f"Error: Template file {template_path} not found.")
    sys.exit(1)

with open(template_path, 'r') as file:
    template_content = file.read()

# Reemplazar las variables manualmente
config_content = template_content
config_content = config_content.replace('${PORT}', os.getenv('PORT', '8080'))
config_content = config_content.replace('${PORT_BACK}', os.getenv('PORT_BACK', '8000'))
config_content = config_content.replace('${PORT_FRONT}', os.getenv('PORT_FRONT', '5173'))

# Escribir el archivo de salida
with open(output_path, 'w') as file:
    file.write(config_content)

print(f"✅ nginx.conf generated successfully in {output_path}")
