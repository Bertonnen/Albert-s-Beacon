# 🌐 Albert's Beacon

Albert's Beacon es un **dashboard interactivo** desarrollado con [Streamlit](https://streamlit.io/) que combina información de **criptomonedas, acciones, clima y noticias** en una sola aplicación.  
La app incluye **soporte multi-idioma (español/inglés)** y se integra con diversas APIs públicas y privadas.

📄 En mi [LinkedIn](https://www.linkedin.com/in/alberto-ortiz-fernandez/) tienes un [artículo](https://www.linkedin.com/pulse/abras-20-pesta%C3%B1as-en-tu-navegador-haz-esto-alberto-ortiz-fern%C3%A1ndez-dbaxf/?trackingId=vuQNwsboKdWnG0e0ROYgZg%3D%3D) dedicado a este pequeño proyecto.

---

## ✨ Funcionalidades principales

- 📈 **Crypto & Stocks**  
  - Consulta precios históricos de criptomonedas (CoinGecko) y acciones (Yahoo Finance).  
  - Métricas y gráficos interactivos con Plotly.  
  - Calculadora de inversión personalizada.  

- ☀️ **Weather**  
  - Datos meteorológicos en tiempo real desde OpenWeatherMap.  
  - Información de temperatura, humedad, viento e íconos del clima.  

- 📰 **News**  
  - Noticias actualizadas según idioma, región y categoría.  
  - Integración con GNews y Mediastack.  

## 📸 Capturas de pantalla

📊 Seguimiento de criptomonedas
![Streamlit-GoogleChrome2025-08-2811-33-09-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/e6e3e671-7c21-4229-9bc1-ffd5dd40eb2b)
Consulta precios históricos e información de diferentes criptomonedas en tiempo real.

💹 Cotización de acciones
![Streamlit-GoogleChrome2025-08-2811-40-01-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/acf5d24a-2bbf-49d3-813b-8baa4b212fb6)
Visualiza el precio de las acciones de cualquier empresa con gráficos y métricas interactivas.

☀️ Clima en tiempo real
![Streamlit-GoogleChrome2025-08-2811-43-12-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/59ebb2aa-ed5b-4d0d-bd37-2f5c920767e4)
Obtén la temperatura, humedad, viento y otros parámetros de climatología en cualquier ciudad del mundo.

📰 Noticias actualizadas
![Streamlit-GoogleChrome2025-08-2811-44-57-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/b0310d16-f711-40d4-b831-de5162cd5559)
Accede a noticias nacionales e internacionales filtradas por idioma, región y categoría.


## Instrucciones
Instrucciones para ejecutar Albert’s Beacon

Sigue estos pasos para poner en marcha la aplicación en tu ordenador:

1. Descargar el proyecto
   - Haz clic en el botón verde Code y selecciona Download ZIP.
   - Extrae el archivo ZIP en una carpeta de tu ordenador.

2. Instalar Python (si no lo tienes ya)
   - Asegúrate de tener instalado Python 3.9 o superior.

3. Abrir una terminal en la carpeta del proyecto
   - En Windows: abre la carpeta donde descomprimiste el proyecto, mantén pulsada la tecla Shift, haz clic derecho y selecciona "Abrir ventana de PowerShell aquí" (o Terminal).
   - En Mac/Linux: abre la Terminal y navega hasta la carpeta con cd ruta/del/proyecto.

4. Crear un entorno virtual (opcional, pero recomendable)
   - En Windows:
     python -m venv venv
     venv\Scripts\activate

   - En Mac/Linux:
     python3 -m venv venv
     source venv/bin/activate

5. Instalar las dependencias necesarias
   - Dentro de la terminal, escribe:
     pip install -r requirements.txt

6. Ejecutar la aplicación
   - Una vez instaladas las dependencias, ejecuta:
     streamlit run app.py

   - Esto abrirá automáticamente la aplicación en tu navegador por defecto (si no, copia la URL que aparece en la terminal, normalmente http://localhost:8501).

7. ¡Listo!
   Ya puedes empezar a usar Albert’s Beacon desde tu navegador.
