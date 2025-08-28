# ---------------------------
# Importación de librerías
# ---------------------------
import streamlit as st                           # Framework web para dashboards interactivos
import pandas as pd                              # Manejo y análisis de datos en DataFrames
import yfinance as yf                            # Para descargar datos financieros de acciones
import requests                                  # Para hacer solicitudes HTTP a APIs externas
import plotly.express as px                      # Para crear gráficos interactivos
from datetime import datetime                    # Manejo de fechas
from streamlit_option_menu import option_menu    # Menú lateral estilizado para Streamlit

# ---------------------------
# Sidebar: Selector de idioma
# ---------------------------
# Permite cambiar entre inglés y español en toda la app
language = st.sidebar.radio(
    "Select language / Selecciona idioma:",
    ["English", "Español"],
    key="language_selector"
)

# ---------------------------
# Diccionario de textos multi-idioma
# ---------------------------
# Contiene todos los textos mostrados en la app en inglés y español
texts = {
    "English": {
        "dashboard": "Albert's Beacon",
        "crypto_stocks": "Crypto & Stock Prices",
        "select_type": "Select type:",
        "crypto": "Crypto",
        "stock": "Stock",
        "enter_crypto": "Enter cryptocurrency name (e.g., bitcoin, ethereum):",
        "select_currency": "Select currency:",
        "select_period": "Select period:",
        "price": "Price",
        "price_change": "Price change",
        "enter_stock": "Enter stock symbol (e.g., AAPL):",
        "open": "Open",
        "close": "Close",
        "volume": "Volume",
        "show_table": "Show price table",
        "calculator": "Calculator",
        "enter_amount": "Enter amount to invest:",
        "weather": "Weather Information",
        "enter_city": "Enter city name:",
        "temperature": "Temperature",
        "humidity": "Humidity",
        "wind_speed": "Wind Speed",
        "weather_desc": "Weather description",
        "news": "News",
        "select_region": "Select language/region:",
        "select_category": "Select category:",
        "no_news": "No news found for the selected filters."
    },
    "Español": {
        "dashboard": "Albert's Beacon",
        "crypto_stocks": "Criptomonedas & Acciones",
        "select_type": "Selecciona tipo:",
        "crypto": "Cripto",
        "stock": "Acción",
        "enter_crypto": "Introduce el nombre de la criptomoneda (ej.: bitcoin, ethereum):",
        "select_currency": "Selecciona moneda:",
        "select_period": "Selecciona periodo:",
        "price": "Precio",
        "price_change": "Cambio de precio",
        "enter_stock": "Introduce el símbolo de la acción (ej.: AAPL):",
        "open": "Apertura",
        "close": "Cierre",
        "volume": "Volumen",
        "show_table": "Mostrar tabla de precios",
        "calculator": "Calculadora",
        "enter_amount": "Introduce la cantidad a invertir:",
        "weather": "Información del Clima",
        "enter_city": "Introduce el nombre de la ciudad:",
        "temperature": "Temperatura",
        "humidity": "Humedad",
        "wind_speed": "Velocidad del viento",
        "weather_desc": "Descripción del clima",
        "news": "Noticias",
        "select_region": "Selecciona idioma/región:",
        "select_category": "Selecciona categoría:",
        "no_news": "No se encontraron noticias para los filtros seleccionados."
    }
}

# Shortcut para acceder a los textos del idioma seleccionado
t = texts[language]

# ---------------------------
# Sidebar: Menú principal
# ---------------------------
# Permite navegar entre las secciones principales de la app
with st.sidebar:
    selected = option_menu(
        t["dashboard"],
        ["Crypto & Stocks", "Weather", "Noticias"] if language == "Español" else ["Crypto & Stocks", "Weather", "News"],
        icons=["currency-bitcoin", "cloud-sun", "newspaper"],  # Iconos de cada sección
        menu_icon="cast",
        default_index=0,  # Inicio en la primera sección
        key="main_menu"
    )

# ---------------------------
# Encabezado principal
# ---------------------------
# Muestra el título centrado con estilo
st.markdown(
    f"<h1 style='text-align: center; color: #4B8BBE;'>{t['dashboard']}</h1>",
    unsafe_allow_html=True
)
# Línea divisoria
st.markdown("<hr style='height:2px;border-width:0;color:gray;background-color:gray'>", unsafe_allow_html=True)

# ---------------------------
# Sección Crypto & Stocks
# ---------------------------
if selected in ["Crypto & Stocks", "Criptomonedas & Acciones"]:
    st.subheader(f"📈 {t['crypto_stocks']}")
    
    # Selector de tipo de activo: Cripto o Acción
    asset_type = st.radio(t["select_type"], [t["crypto"], t["stock"]], key="asset_type")

    # ---------------------------
    # Sub-sección Criptomonedas
    # ---------------------------
    if asset_type == t["crypto"]:
        # Entrada del nombre de la criptomoneda
        crypto_name = st.text_input(t["enter_crypto"], "bitcoin", key="crypto_name").lower()
        # Selector de moneda
        currency = st.radio(t["select_currency"], ["USD", "EUR", "GBP"], key="crypto_currency")
        # Selector de periodo
        period = st.select_slider(t["select_period"], ["1d", "7d", "30d", "90d"], key="crypto_period")
        
        # Mapeo de periodos a días
        period_days = {"1d":1, "7d":7, "30d":30, "90d":90}
        days = period_days[period]
        
        try:
            # Llamada a la API de CoinGecko para obtener datos históricos
            url = f"https://api.coingecko.com/api/v3/coins/{crypto_name}/market_chart?vs_currency={currency}&days={days}"
            response = requests.get(url).json()
            
            if "prices" not in response:
                st.warning(f"Cryptocurrency not found. Check the name and try again.")
            else:
                # Convertir los datos a DataFrame
                df = pd.DataFrame(response["prices"], columns=["timestamp", "price"])
                df["date"] = pd.to_datetime(df["timestamp"], unit='ms')
                
                # Cálculo del último precio y cambio desde el inicio
                last_price = df["price"].iloc[-1]
                change = last_price - df["price"].iloc[0]
                
                # Mostrar métricas en dos columnas
                col1, col2 = st.columns(2)
                col1.metric(f"💰 {t['price']}", f"{last_price:.2f} {currency.upper()}")
                col2.metric(f"📊 {t['price_change']}", f"{change:.2f} {currency.upper()}")
                
                # Gráfico de línea con Plotly
                fig = px.line(df, x="date", y="price", title=f"{crypto_name.title()} price in {currency.upper()}")
                st.plotly_chart(fig, use_container_width=True)
                
                # ---------------------------
                # Calculadora de inversión en cripto
                # ---------------------------
                with st.expander(f"💡 {t['calculator']}"):
                    with st.form(key="crypto_calc_form"):
                        amount = st.number_input(f"💵 {t['enter_amount']}", min_value=0.0, value=100.0)
                        submitted = st.form_submit_button("Calculate")
                        if submitted:
                            units = amount / last_price
                            # Mostrar resultado en el idioma seleccionado
                            if language == "Español":
                                st.write(f"Puedes comprar aproximadamente **{units:.6f} {crypto_name.upper()}** con {amount} {currency.upper()}.")
                            else:
                                st.write(f"You can buy approximately **{units:.6f} {crypto_name.upper()}** with {amount} {currency.upper()}.")
        
        except Exception as e:
            st.error(f"Error fetching crypto data: {e}")

    # ---------------------------
    # Sub-sección Acciones
    # ---------------------------
    elif asset_type == t["stock"]:
        # Entrada del símbolo de la acción
        symbol = st.text_input(t["enter_stock"], "AAPL", key="stock_symbol")
        # Selector de moneda
        currency = st.radio(t["select_currency"], ["USD", "EUR", "GBP"], key="stock_currency")
        # Selector de periodo
        period = st.select_slider(t["select_period"], ["1d", "1wk", "1mo", "3mo", "6mo", "1y", "max"], key="stock_period")

        if symbol:
            try:
                # Descargar datos históricos de la acción con yfinance
                data = yf.download(symbol, period=period, progress=False)

                # Ajuste si los datos tienen MultiIndex
                if isinstance(data.columns, pd.MultiIndex):
                    data.columns = data.columns.get_level_values(0)

                if data.empty:
                    st.warning("No data found for this symbol.")
                else:
                    # Última fila para mostrar métricas
                    last_row = data.iloc[-1]
                    open_val = float(last_row['Open'])
                    close_val = float(last_row['Close'])
                    volume_val = int(last_row['Volume'])

                    # Conversión de divisas si no es USD
                    if currency != "USD":
                        fx_symbol = f"{currency}USD=X"
                        fx_data = yf.download(fx_symbol, period="5d", progress=False)
                        if not fx_data.empty:
                            rate = float(fx_data['Close'].iloc[-1])
                            if rate > 0:
                                conv_rate = 1 / rate
                                open_val *= conv_rate
                                close_val *= conv_rate
                                data[['Open','High','Low','Close']] *= conv_rate

                    # Mostrar métricas en tres columnas
                    col1, col2, col3 = st.columns(3)
                    col1.metric(f"🟢 {t['open']}", f"{open_val:.2f} {currency}")
                    col2.metric(f"🔴 {t['close']}", f"{close_val:.2f} {currency}")
                    col3.metric(f"📦 {t['volume']}", f"{volume_val:,}")

                    # Gráfico de línea con Plotly
                    fig = px.line(
                        data, 
                        y="Close", 
                        title=f"{symbol} Price in {currency}", 
                        labels={"index":"Date","Close":"Price"}
                    )
                    st.plotly_chart(fig, use_container_width=True)

                    # ---------------------------
                    # Tabla de precios filtrable por fecha
                    # ---------------------------
                    with st.expander(t["show_table"]):
                        if not pd.api.types.is_datetime64_any_dtype(data.index):
                            data.index = pd.to_datetime(data.index)
                        start_date = st.date_input("Start date", value=data.index.min(), key="stock_start_date")
                        end_date = st.date_input("End date", value=data.index.max(), key="stock_end_date")
                        filtered_data = data.loc[start_date:end_date].copy()
                        st.dataframe(filtered_data[["Open","High","Low","Close","Volume"]], height=400)

                    # ---------------------------
                    # Calculadora de inversión en acciones
                    # ---------------------------
                    with st.expander(f"💡 {t['calculator']}"):
                        with st.form(key="stock_calc_form"):
                            amount = st.number_input(f"💵 {t['enter_amount']}", min_value=0.0, value=1000.0)
                            submitted = st.form_submit_button("Calculate")
                            if submitted:
                                shares = amount / close_val
                                if language == "Español":
                                    st.write(f"Puedes comprar aproximadamente **{shares:.4f} acciones de {symbol.upper()}** con {amount} {currency}.")
                                else:
                                    st.write(f"You can buy approximately **{shares:.4f} shares of {symbol.upper()}** with {amount} {currency}.")
        
            except Exception as e:
                st.error(f"Error fetching stock data: {e}")

# ---------------------------
# Sección Weather (Clima)
# ---------------------------
elif selected in ["Weather", "Información del Clima"]:
    st.subheader(f"🌤️ {t['weather']}")
    city = st.text_input(t["enter_city"], "London", key="weather_city")
    api_key = "28866150b9805644dbb9d6b443d30847"  # API Key OpenWeatherMap
    
    # Diccionario de íconos según descripción del clima
    weather_icons = {
        "clear sky": "☀️",
        "few clouds": "🌤️",
        "scattered clouds": "🌥️",
        "broken clouds": "☁️",
        "shower rain": "🌦️",
        "rain": "🌧️",
        "thunderstorm": "⛈️",
        "snow": "❄️",
        "mist": "🌫️"
    }
    
    try:
        # Llamada a API OpenWeatherMap
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url).json()
        if response.get("cod") != 200:
            st.warning("City not found or API error.")
        else:
            temp = response['main']['temp']
            humidity = response['main']['humidity']
            wind = response['wind']['speed']
            desc = response['weather'][0]['description']
            icon = weather_icons.get(desc.lower(), "🌈")

            # Mostrar métricas en columnas
            col1, col2, col3 = st.columns(3)
            col1.metric(f"🌡️ {t['temperature']}", f"{temp} °C")
            col2.metric(f"💧 {t['humidity']}", f"{humidity}%")
            col3.metric(f"🌬️ {t['wind_speed']}", f"{wind} m/s")
            
            st.markdown(f"**{t['weather_desc']}:** {icon} {desc.title()}")
    except Exception as e:
        st.error(f"Error fetching weather: {e}")

# ---------------------------
# Sección Noticias
# ---------------------------
elif selected in ["News", "Noticias"]:
    st.subheader(f"📰 {t['news']}")

    # Selección de idioma/región
    region = st.sidebar.radio(
        t["select_region"],
        ["English (US)", "Español (España)", "Español (Latam)"],
        key="news_region"
    )

    # Selección de categoría de noticias
    category = st.sidebar.selectbox(
        t["select_category"],
        ["general", "business", "technology", "entertainment", "sports", "science", "health"],
        key="news_category"
    )

    try:
        # APIs diferentes según región
        if region in ["English (US)", "Español (Latam)"]:
            api_key_gnews = "e29b31bc1af40c5d325e03f4604b6ba2"
            base_url_gnews = "https://gnews.io/api/v4/top-headlines"
            if region == "English (US)":
                lang = "en"
                country = "us"
            else:
                lang = "es"
                country = None
            params = {"token": api_key_gnews, "lang": lang, "topic": category if category!="general" else None, "max":20}
            if country:
                params["country"] = country
            response = requests.get(base_url_gnews, params=params).json()
            articles = response.get("articles", [])
        else:
            api_key_mediastack = "4111559d6fa1913f848bc9602ad33859"
            base_url_mediastack = "http://api.mediastack.com/v1/news"
            category_param = category if category != "general" else None
            params = {"access_key": api_key_mediastack, "languages":"es","countries":"es","categories":category_param,"limit":20}
            response = requests.get(base_url_mediastack, params=params).json()
            articles = response.get("data", [])

        if not articles:
            st.info(t["no_news"])
        else:
            # Mostrar cada noticia
            for article in articles:
                if region in ["English (US)", "Español (Latam)"]:
                    title = article.get("title", "Sin título")
                    url = article.get("url", "#")
                    source = article.get("source", {}).get("name", "Desconocida")
                    published_at = article.get("publishedAt", "")
                    description = article.get("description", "")
                    image = article.get("image", "")
                else:
                    title = article.get("title", "Sin título")
                    url = article.get("url", "#")
                    source = article.get("source", "Desconocida")
                    published_at = article.get("published_at", "")
                    description = article.get("description", "")
                    image = article.get("image", "")

                # Mostrar imagen si existe
                if image:
                    st.image(image, use_container_width=True)
                # Mostrar título con enlace
                st.markdown(f"### [{title}]({url})")
                st.markdown(f"*Fuente: {source} | Fecha: {published_at[:10]}*")
                if description:
                    st.markdown(description)
                st.markdown("---")
    except Exception as e:
        st.error(f"Error al obtener noticias: {e}")
