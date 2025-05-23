# -*- coding: utf-8 -*-
"""Despliegue_CalidadAgua_Stremlite2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1w52YP4Y8mo0HHV_BiIKMiccHx03BY5iI

# **Despliegue de Calidad del agua con interfaz gráfica de Streamlit y enlace público con LocalTunnel**

Se debe cargar:
* app.py: aplicación con el despliegue
* modelo.pkl: modelos de machine learning

# **Streamlit**
Es una plataforma de código abierto que se utiliza para crear aplicaciones web interactivas y de visualización de datos.

https://streamlit.io/

**Streamlit para despliegue de modelos**

Nos permite crear aplicaciones web para despliegue de modelos predictivos.

Se debe tener previamente una aplicación app.y

* Para ejecutar en un equipo local: !streamlit run app.py
* Desde Google Colab necesitamos un tunel que nos permita simular un servidor web local y asi acceder la aplicación por un enlace público. Se puede hacer con localtunnel.
"""

#Instalación
!pip install streamlit

#Correr la app en background, recuerda cargar el archivo app.py
!nohup streamlit run app.py &

!npm install localtunnel

import urllib.request

print("Password/Enpoint IP for localtunnel is:",urllib.request.urlopen('https://ipv4.icanhazip.com').read().decode('utf8').strip("\n"))

#Se crea un túnel hacia un servidor local que se está ejecutando en el puerto 8501.
!npx localtunnel --port 8501