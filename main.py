import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from datetime import datetime
import plotly.express as px
import streamlit.components.v1 as components
import requests
import folium
from streamlit_folium import st_folium

#diccionarios

miembros_tS = ["Seoyeon", "Hyerin", "Jiwoo", "Chaeyeon", "Yooyeon", "Soomin", "Nakyoung", "Yubin", "Kaede", "Dahyun", "Kotone", "Yeonji", "Nien", "Sohyun", "Xinyu", "Mayu", "Lynn", "Joobin", "Hayeon", "Shion", "Chaewon", "Sullin", "Seoah", "Jiyeon"]

colors_ts_hex = {
    "Seoyeon": "#1E90FF",
    "Hyerin": "#736AFF",
    "Jiwoo": "#FAFA33",
    "Chaeyeon": "#66CC33",
    "Yooyeon": "#EC118F",
    "Soomin": "#FC83A5",
    "Nakyoung": "#5F9EA0",
    "Yubin": "#FFE3E2",
    "Kaede": "#FFC936",
    "Dahyun": "#FBA0E3",
    "Kotone": "#FEE002",
    "Yeonji": "#5974FF",
    "Nien": "#FF953F",
    "Sohyun": "#1222B5",
    "Xinyu": "#D51312",
    "Mayu": "#FE8E76",
    "Lynn": "#AB63B4",
    "Joobin": "#B7F54C",
    "Hayeon": "#52D8BB",
    "Shion": "#FF428A",
    "Chaewon": "#C9A0DC",
    "Sullin": "#8FBC8F",
    "Seoah": "#E0FFFF",
    "Jiyeon": "#F7B360"
}

color_type = {
 'LIVE': "#FF0000",
 'Fancam': '#0000FF',
 'Variety': '#00FF00',
 'SIGNAL': '#FFFF00',
 'Radio': '#FF00FF',
 'Interview': '#00FFFF',
 'Concert': '#800000',
 'Behind': '#008000',
 'Performance': "#000080",
 'Playlist': '#808000',
 'SecretBase': '#800080',
 'Drama': '#008080',
 'Reality': '#C0C0C0',
 'Misc': '#808080',
 'Shorts': '#FFA500',
 'Dance': '#A52A2A',
 'Offline Event': '#FFC0CB',
 'Gravity': '#40E0D0',
 'Official Audio': '#EE82EE',
 'Special Clip': '#FFD700',
 'Vlog': '#DAA520',
 'Music Video': '#ADFF2F',
 'Singing': '#7FFF00',
 'Reaction': '#B0E0E6',
 'Awards Show': '#F08080',
 'Teaser': '#90EE90',
 'Greeting': '#ADD8E6',
 'Fan Chant': '#FFB6C1',
 'Dance Practice': '#DDA0DD',
 'Song': '#FAFAD2',
 'Highlight Medley': '#CD5C5C'
}

types = ['LIVE', 'Fancam',
 'Variety',
 'SIGNAL',
 'Radio',
 'Interview',
 'Concert',
 'Behind',
 'Performance',
 'Playlist',
 'SecretBase',
 'Drama',
 'Reality',
 'Misc',
 'Shorts',
 'Dance',
 'Offline Event',
 'Gravity',
 'Official Audio',
 'Special Clip',
 'Vlog',
 'Music Video',
 'Singing',
 'Reaction',
 'Awards Show',
 'Teaser',
 'Greeting',
 'Fan Chant',
 'Dance Practice',
 'Song',
 'Highlight Medley']

tripleS = pd.read_csv(r"DATABASE/tripleS.csv", encoding='utf-8')
tripleS_photos = pd.read_csv(r"DATABASE/tripleS_photos.csv", encoding='utf-8')
tripleS_members = pd.read_csv(r"DATABASE/tripleS_members.csv", encoding='utf-8')

not_members = ["Chaewon,Chaeyeon,Dahyun,Hayeon,Hyerin,Jiwoo,Jiyeon,Joobin,Kaede,Kotone,Lynn,Mayu,Nakyoung,Nien,Seoah,Seoyeon,Shion,Sohyun,Soomin,Sullin,Xinyu,Yeonji,Yooyeon,Yubin", "Chaeyeon,Dahyun,Hayeon,Hyerin,Jiwoo,Joobin,Kaede,Kotone,Lynn,Mayu,Nakyoung,Nien,Seoyeon,Shion,Sohyun,Soomin,Xinyu,Yeonji,Yooyeon,Yubin", "GRAVITY", "COMMERCIAL"]

selected = option_menu("Menú Principal", ["Inicio", "¿Quienes son tripleS?", "Buscador", "Informe"],
                       icons=["menu-button-fill", "patch-question", "search", "card-text"],
                       menu_icon="cast",
                       default_index=0,
                       orientation="horizontal")

if selected == "Inicio":
    st.markdown("<h1 style='text-align: center;'>¿No son 24 demasiadas?: La desigualdad de contenido entre las 24 integrantes del grupo tripleS. Un análisis de datos sobre su primer año como grupo completo.</h1>", unsafe_allow_html=True)
    texto = """
    Bienvenidxs a ¿No son 24 demasiadas?, esta página es el trabajo integrador del curso 1CCO19
    "Pensamiento Computacional para Comunicadores" como parte de cierre del curso.
    El trabajo a sido realizado en su totalidad por Jesus Quiroga.
    """
    col1, col2 = st.columns(2)
    col1.image("tripleS.jpeg", caption='tripleS', width=300)
    col2.markdown(f"<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>{texto}</div>", unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center;'>Introducción</h2>", unsafe_allow_html=True)
    
    texto_intro = """
    El problema surge a partir de mi participación en el fandom de tripleS. tripleS es un grupo de K-pop creado por 
    la empresa MODHAUS cuál proyecto comenzó en Mayo de 2022 con la revelación de la primera miembro o S1 Yoon SeoYeon.
    Desde Octubre de 2023 he estado siguiendo el recorrido del grupo y como se va completando hasta que el 4 de abril 
    de 2024 se reveló la última miembro Ji SuhYeon y con ello, tripleS estaba completo. Al tener un megagrupo la 
    pregunta común en lxs nuevxs fans ha sido, ¿Es justo para todas? ¿Acaso todas ellas ganan el mismo dinero? 
    ¿Acaso todas llegan a cantar en las canciones o se ven en los videos?
    Para muchxs solo les importa la música y el sonido, pero para quienes quieren conocer a cada una de las miembros 
    esta pregunta ha sido coherente. Algunas de estas preguntas se han ido respondiendo durante los dos años de Pre-Debut,
    el tiempo antes de que se completen las 24. 
    La mayor parte del dinero que ganan es a través de compras de objekts o photocards virtuales de las miembros a través
    de una aplicación y fomenta el coleccionismo. El éxito del grupo y la venta de objekts ha llevado a que ellas vayan
    recibiendo grandes sumas de dinero durante los últimos meses. Kim YooYeon (S5) reveló en una entrevista que gana
    aproximadamente 65 mil dólares. Aunque los pagos no son mensuales, como se reveló en SIGNAL 240404 y como lo han 
    revelado las miembros en distintas entrevistas.
    Pero respecto a el tiempo en canciones, videos musicales y demás no hay una clara respuesta de MODHAUS o de las 
    miembros. Algunas hacen bromas sobre las pocas líneas que tienen en canciones, pero sobre su aparición en contenido 
    de entretenimiento que provee la compañía o en la cual participan ellas fuera de la compañía, ya sea programas 
    reality, festivales, radio, etc.., es incierta.
    """
    st.markdown(f"<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>{texto_intro}</div>", unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align: center;'>Solución</h2>", unsafe_allow_html=True)

    texto_solucion1 = """
    Para tener una respuesta más clara sobre cómo funciona la distribución de contenido de las miembros se va a realizar un análisis a partir de gráficos y cuartiles. Por cada gráfico donde se tome al menos 8 miembros (el tamaño mínimo de una subunidad es 4 son pocos los casos en los que hay 4 miembros, al menos que sea una situación tan exclusiva como mayor cantidad de primer puesto en canciones o videos musicales). Habrán excepciones cuando los gráficos den valores discretos como primer puesto en canciones o MVS. 
    Se crearon gráficos a partir de dos tipos de base de datos:
    Por un lado, las bases de datos que contaban con valores enteros ya sumados y establecidos, hechos por mí. Entonces el trabajo era solo generar los gráficos sin ninguna operación.
    """
    Muestra1 = """
    Muestra1: Cuadro “Cantidad de primer puesto en videoclips”
    
    base = {}
    for index, row in tripleS_mvs.iterrows():
    if row["TOTAL_1ST_PLACE"] != 0:
        base[row["MEMBER"]] = round(row["TOTAL_1ST_PLACE"], 2)

    base = dict(sorted(base.items(), key=lambda item:item[-1], reverse=True))

    colors_base = []

    for i in base:
    i_color = colors_ts_hex[i]
    colors_base.append(i_color)

    base1 = {
        "Miembro": [],
        "Cantidad": []
    }

    for member, time in base.items():
    base1["Miembro"].append(member)
    base1["Cantidad"].append(time)

    prueba = px.bar(base1,
                x='Miembro',
                y="Cantidad",
                color="Miembro",
                title="Cantidad de primer puesto en videos musicales por miembro",
                color_discrete_sequence=colors_base,
                text="Cantidad"
                )"""
    
    Muestra2 = """
    Pero la mayoría de los gráficos se realizaron con el siguiente código:
    
    not_members = ["Chaewon,Chaeyeon,Dahyun,Hayeon,Hyerin,Jiwoo,Jiyeon,Joobin,Kaede,Kotone,Lynn,Mayu,Nakyoung,Nien,Seoah,Seoyeon,Shion,Sohyun,Soomin,Sullin,Xinyu,Yeonji,Yooyeon,Yubin", "Chaeyeon,Dahyun,Hayeon,Hyerin,Jiwoo,Joobin,Kaede,Kotone,Lynn,Mayu,Nakyoung,Nien,Seoyeon,Shion,Sohyun,Soomin,Xinyu,Yeonji,Yooyeon,Yubin", "GRAVITY", "COMMERCIAL"]
    tripleS_total = {}
    for index, row in tripleS.iterrows():
    if row['MEMBERS'] not in not_members:
        if len(str(row['MEMBERS'])) <= 8:
        if row['MEMBERS'] not in tripleS_total:
            (h, m, s) = row['DURATION'].split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            tripleS_total[row['MEMBERS']] = float(d.total_seconds())
        else:
            (h, m, s) = row['DURATION'].split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            tripleS_total[row['MEMBERS']] += float(d.total_seconds())
        else:
        members = row['MEMBERS'].split(",")
        for i in members:
            if i not in tripleS_total:
            (h, m, s) = row['DURATION'].split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            tripleS_total[i] = float(d.total_seconds())
            else:
            (h, m, s) = row['DURATION'].split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            tripleS_total[i] += float(d.total_seconds())
    tripleS_total_ord = dict(sorted(tripleS_total.items(), key=lambda item:item[-1], reverse=True))
    colors_ts_tripleS_total = []
    for i in tripleS_total_ord:
    i_color = colors_ts_hex[i]
    colors_ts_tripleS_total.append(i_color)

    for key in tripleS_total_ord:
    new = tripleS_total_ord[key]/60/60/24
    tripleS_total_ord[key] = round(new, 4)

    tripleS_total_ord1 = {
        "Miembro": [],
        "Tiempo (en días)": []
    }

    for member, time in tripleS_total_ord.items():
    tripleS_total_ord1["Miembro"].append(member)
    tripleS_total_ord1["Tiempo (en días)"].append(time)

    tripleS_px = px.bar(tripleS_total_ord1,
                x='Miembro',
                y='Tiempo (en días)',
                color="Miembro",
                color_discrete_sequence=colors_ts_tripleS_total,
                title="Participación total de las miembros de tripleS en videos",
                text="Tiempo (en días)"
                )
    tripleS_px.show()
   
    """
    st.markdown(f"<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>{texto_solucion1}</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>{Muestra1}</div>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: justify;'>1. Preparación de datos:</h3>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: justify; font-size: 17px; margin-bottom: 10px'><b>Inicializar el diccionario 'base':</b> El código comienza inicializando un diccionario vacío llamado 'base'</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: justify; font-size: 17px; margin-bottom: 10px'><b>Iterar el DataFrame 'tripleS_mvs':</b> El código itera cada fila del DataFrame 'tripleS_mvs'.</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: justify; font-size: 17px; margin-bottom: 10px'><b>Comprobar si 'TOTAL_1ST_PLACE' no es 0:</b> Para cada fila, el código comprueba si el valor de 'TOTAL_1ST_PLACE' no es 0.</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: justify; font-size: 17px; margin-bottom: 10px'><b>Añadir MEMBER, el nombre de la miembro, como clave y 'TOTAL_1ST_PLACE', el valor como valor al diccionario 'base':</b> Si el valor no es 0, el código añade el nombre de la miembro como clave y el valor de 'TOTAL_1ST_PLACE' (redondeado a 2 decimales) como valor en el diccionario 'base'.</div>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: justify;'>2. Asignacion de Color:</h3>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: justify; font-size: 17px; margin-bottom: 10px'><b>Ordenar el diccionario 'base' por valores en orden descendente:</b> El código ordena el diccionario 'base' por los valores en orden descendente mediante la función sorted().</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: justify; font-size: 17px; margin-bottom: 10px'><b>Generar la lista 'colors_base':</b> El código itera sobre el diccionario 'base' ordenado y recupera el código hexadecimal del color correspondiente a cada miembro del diccionario 'colors_ts_hex', agregándolo a la lista 'colors_base'.</div>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: justify;'>3. Estructurar la información para que se apta en el cuadro de barras:</h3>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: justify; font-size: 17px; margin-bottom: 10px'><b>Crear el diccionario 'base1':</b> El código crea un nuevo diccionario 'base1' con dos claves: 'Miembro' y 'Cantidad'. A continuación, itera sobre el diccionario 'base' ordenado, agregando los nombres de las miembros a la lista 'Miembro' y los valores de 'TOTAL_1ST_PLACE' a la lista 'Cantidad'.</div>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: justify;'> 4. Visualización de datos:</h3>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: justify; font-size: 17px; margin-bottom: 10px'><b>Crear un gráfico de barras de Plotly:</b> El código utiliza la función px.bar() de Plotly Express para crear un gráfico de barras. Establece el eje 'x' como 'Miembro', el eje 'y' como 'Cantidad', el 'color' como 'Miembro' para tener una leyenda por color, el 'title' como 'Cantidad de primer puesto en videos musicales por miembro', la 'color_discrete_sequence' como 'colors_base' y el 'texto' en 'Cantidad' para que en cada columna se vea el texto.</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: justify; font-size: 17px; margin-bottom: 10px'><b>Visualizar el gráfico:</b> Vemos el gráfico</div>", unsafe_allow_html=True)
    st.image("MUESTRA2.png", caption='1er Diagrafa de Flujo: Cantidades ya establecidas', width=700)

    st.markdown(f"<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>{Muestra2}</div>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: justify;'>1. Preprocesamiento de datos:</h3>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: justify; font-size: 17px; margin-bottom: 10px'><b>Inicializar el diccionario 'triples_total':</b> El código comienza inicializando un diccionario vacío llamado 'triples_total'</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: justify; font-size: 17px; margin-bottom: 10px'><b>Iterar el DataFrame 'tripleS':</b> El código itera cada fila del DataFrame 'tripleS'.</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: justify; font-size: 17px; margin-bottom: 10px'><b>Comprobar si el valor no es parte de “not_members”:</b> Para cada fila, el código comprueba si el valor de 'MEMBERS' no es OT24 (grupo completo) OT20 (previo grupo completo), GRAVITY (no aprece ninguna miembro), COMMERCIAL (Un comercial del grupo general).</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: justify; font-size: 17px; margin-bottom: 10px'><b>Comprobar si el valor es menor o igual a 8:</b> La miembro con el nombre más largo es Nakyoung y hay tres miembros con nombres cortos Nien, Mayu y Lynn, que en un producto donde aparezca alguna de las dos se considerará como máximo 9 caracteres. Entonces para que saber si solo tenemos a una miembro el valor debe ser menor o igual a 8.</div>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: justify;'>2. Agregar datos:</h3>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: justify; font-size: 17px; margin-bottom: 10px'><b>Comprobar que el valor no esté en la lista:</b> Se comprueba que el valor no esté en la lista. Si el valor no está en la lista se le agrega como clave el nombre de la miembro y como valor la duración del producto. Si el valor está en la lista se suma al valor ya habido. Esto gracias a datetime que convierte el valor en formato HH:MM:SS en una variable que se transforma en una variable de tiempo que se vuelve segundos para ser manejable</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: justify; font-size: 17px; margin-bottom: 10px'><b>Se realiza el mismo procedimiento si hay más de una miembro</b></div>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: justify;'>3. Orden y formación de datos:</h3>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: justify; font-size: 17px; margin-bottom: 10px'><b>Ordenar el diccionario 'triples_total' por valores en orden descendente:</b> El código ordena el diccionario 'triples_total' por los valores en orden descendente mediante la función sorted(). Se convierte los valores a lo necesitado, en este caso de segundos a días.</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: justify; font-size: 17px; margin-bottom: 10px'><b>Generar la lista 'colors_ts_tripleS_total':</b> El código itera sobre el diccionario 'triples_total' ordenado y recupera el código hexadecimal del color correspondiente a cada miembro del diccionario 'colors_ts_hex', agregándolo a la lista 'colors_ts_tripleS_total'</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: justify; font-size: 17px; margin-bottom: 10px'><b>Crear el diccionario 'tripleS_total_ord1':</b> El código crea un nuevo diccionario con dos claves: 'Miembro' y 'Tiempo'. A continuación, itera sobre el diccionario 'tripleS_total_ord1' ordenado, agregando los nombres de las miembros a la lista 'Miembro' y los valores de 'Duración' a la lista 'Tiempo'. Este diccionario se prepara para visualizarse.</div>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: justify;'> 4. Visualización de datos:</h3>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: justify; font-size: 17px; margin-bottom: 10px'><b>Crear un gráfico de barras de Plotly:</b> El código utiliza la función px.bar() de Plotly Express para crear un gráfico de barras. Establece el eje 'x' como 'Miembro', el eje 'y' como 'Cantidad', el 'color' como 'Miembro' para tener una leyenda por color, el 'title' como 'Cantidad de primer puesto en videos musicales por miembro', la 'color_discrete_sequence' como 'colors_base' y el 'texto' en 'Cantidad' para que en cada columna se vea el texto.</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: justify; font-size: 17px; margin-bottom: 10px'><b>Visualizar el gráfico:</b> Vemos el gráfico</div>", unsafe_allow_html=True)
    st.image("MUESTRA1.png", caption='2do Diagrafa de Flujo: Suma de duración', width=700)
    text_refl = """
    Las limitaciones de este proyecto son pocas y se resume en los contenidos de media. Los contenidos de media donde aparece más de una miembro no se sabe cuánto tiempo del video cada miembro aparece. Por ejemplo, en un SIGNAL con más de 10 miembros, a cada miembro se le cuenta el tiempo del video completo, aproximadamente 5 minutos, pero de esos 5 minutos solo aparece 1 minuto. Para poder mejorar solucionar esto se podría entrenar un algoritmo que pueda analizar cada frame e identificar que miembro es. Luego se cuenta cuanto tiempo apareció y es más preciso con los resultados. Otra limitación del proyecto son los festivales y fancams que no todas son subidas a YouTube enteras. El caso de ‘Waterbomb Tokyo’ donde no había ningún video en YouTube y tuve que juntar todas las fancams del evento que encontré en Twitter, ahora X. También están en los fancafé, fansigns, y ahora con la implementación de Cosmo Live, una forma de las miembros de realizar Live cuando ellas deseen desde sus celulares y con total control. Y no olvidar los posts en Instagram donde cada cierto tiempo un grupo de 6 miembros aproximadamente sube un post, y la cantidad de posts subidos de una miembro también influye en que tanto se le promociona en redes sociales. Más sobre los resultados se compartirán en la parte del Informe.
    """
    st.markdown("<h2 style='text-align: center;'>Reflexión</h2>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{text_refl}</div>", unsafe_allow_html=True)
elif selected =="¿Quienes son tripleS?":
    st.image(tripleS_photos.loc[24, "PHOTO1"])
    st.markdown("<h1 style='text-align: center;'>¿Quienes son tripleS?</h1>", unsafe_allow_html=True)  
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>tripleS (Hangul: 트리플에스, Japonés: トリプルS), también conocida como SSS y SocialSonyoSeoul, es un grupo musical surcoreano multinacional de 24 integrantes bajo el sello MODHAUS. El grupo debutó oficialmente el 13 de febrero de 2023 con el miniálbum ASSEMBLE y la canción principal, 'Rising', con la participación de las diez integrantes reveladas. Posteriormente, regresaron como grupo completo con las 24 integrantes el 8 de mayo de 2024 con el lanzamiento de su primer álbum de estudio, ASSEMBLE24, y la canción principal, 'Girls Never Die'.</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>tripleS trabaja principalmente en subunidades rotativas, elegidas por los fans mediante votación. La primera unidad, Acid Angel de Asia, debutó el 28 de octubre de 2022, seguida de +(KR)ystal Eyes el 4 de mayo de 2023, LOVElution el 17 de agosto de 2023, EVOLution el 11 de octubre de 2023, Aria el 15 de enero de 2024, Visionary Vision el 23 de octubre de 2024, ∞!el 20 de noviembre de 2024.</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>El grupo cuenta actualmente con nueve subunidades oficiales: Acid Angel de Asia, +(KR)ystal Eyes, LOVElution, EVOLution, NXT, Aria, Glow, Visionary Vision y ∞!, incluyendo una subunidad colaborativa, ACID EYES, compuesta por miembros de AAA y KRE. NXT y Glow son las únicas subunidades no votadas ni promocionadas, y existieron como una forma de presentar a las últimas ocho integrantes.</div>", unsafe_allow_html=True)
    st.image(tripleS_photos.loc[24, "PHOTO2"])
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>tripleS significa SocialSonyoSeoul, lo que refleja la idea de que el grupo representa a las chicas/idols sociales de Seúl. El nombre del grupo también transmite la idea de que las 's' minúsculas (aprendices) se unen para crear una gran 'S' (miembros oficiales).</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Toda esta información fue recolectada de tripleS Wiki</div>", unsafe_allow_html=True)
    url_tS = "https://triples.fandom.com/wiki/TripleS"
    st.markdown("[tripleS](%s)" % url_tS)
    st.image(tripleS_photos.loc[24, "PHOTO3"])
    miembro = st.selectbox("ELIGE UNA MIEMBRO:", miembros_tS)
    for i in miembros_tS:
        if i == miembro:
            index = tripleS_photos.index[tripleS_photos["MEMBER"] == i].tolist()
            st.markdown(f"<h1 style='text-align: center;'>{miembro}</h1>", unsafe_allow_html=True)
            st.image(tripleS_photos.loc[index[0], "PHOTO1"])
            st.markdown(f"<h4 style='text-align: justify;'>N° S</h4>", unsafe_allow_html=True)
            st.markdown(f"<div style='text-align: justify; font-size: 17px; margin-bottom: 10px'>{tripleS_members.loc[index[0], "N° S"]}</div>", unsafe_allow_html=True)
            st.markdown(f"<h4 style='text-align: justify;'>STAGE NAME</h4>", unsafe_allow_html=True)
            st.markdown(f"<div style='text-align: justify; font-size: 17px; margin-bottom: 10px'>{tripleS_members.loc[index[0], "STAGE NAME"]}</div>", unsafe_allow_html=True)
            st.markdown(f"<h4 style='text-align: justify;'>NOMBRE LEGAL</h4>", unsafe_allow_html=True)
            st.markdown(f"<div style='text-align: justify; font-size: 17px; margin-bottom: 10px'>{tripleS_members.loc[index[0], "NOMBRE LEGAL"]}</div>", unsafe_allow_html=True)
            st.markdown(f"<h4 style='text-align: justify;'>OTROS NOMBRES</h4>", unsafe_allow_html=True)
            st.markdown(f"<div style='text-align: justify; font-size: 17px; margin-bottom: 10px'>{tripleS_members.loc[index[0], "OTROS NOMBRES"]}</div>", unsafe_allow_html=True)
            st.markdown(f"<h4 style='text-align: justify;'>POSICIÓN</h4>", unsafe_allow_html=True)
            st.markdown(f"<div style='text-align: justify; font-size: 17px; margin-bottom: 10px'>{tripleS_members.loc[index[0], "POSICIÓN"]}</div>", unsafe_allow_html=True)
            st.image(tripleS_photos.loc[index[0], "PHOTO2"])
            st.markdown(f"<h4 style='text-align: justify;'>CUMPLEAÑOS</h4>", unsafe_allow_html=True)
            st.markdown(f"<div style='text-align: justify; font-size: 17px; margin-bottom: 10px'>{tripleS_members.loc[index[0], "CUMPLEAÑOS"]}</div>", unsafe_allow_html=True)
            st.markdown(f"<h4 style='text-align: justify;'>NACIONALIDAD</h4>", unsafe_allow_html=True)
            st.markdown(f"<div style='text-align: justify; font-size: 17px; margin-bottom: 10px'>{tripleS_members.loc[index[0], "NACIONALIDAD"]}</div>", unsafe_allow_html=True)
            st.markdown(f"<h4 style='text-align: justify;'>SIGNO ZODIACAL</h4>", unsafe_allow_html=True)
            st.markdown(f"<div style='text-align: justify; font-size: 17px; margin-bottom: 10px'>{tripleS_members.loc[index[0], "SIGNO ZODIACAL"]}</div>", unsafe_allow_html=True)
            st.markdown(f"<h4 style='text-align: justify;'>ALTURA</h4>", unsafe_allow_html=True)
            st.markdown(f"<div style='text-align: justify; font-size: 17px; margin-bottom: 10px'>{tripleS_members.loc[index[0], "ALTURA"]}</div>", unsafe_allow_html=True)
            st.markdown(f"<h4 style='text-align: justify;'>GRUPO SANGUINEO</h4>", unsafe_allow_html=True)
            st.markdown(f"<div style='text-align: justify; font-size: 17px; margin-bottom: 10px'>{tripleS_members.loc[index[0], "GRUPO SANGUINEO"]}</div>", unsafe_allow_html=True)
            st.markdown(f"<h4 style='text-align: justify;'>MBTI</h4>", unsafe_allow_html=True)
            st.markdown(f"<div style='text-align: justify; font-size: 17px; margin-bottom: 10px'>{tripleS_members.loc[index[0], "MBTI"]}</div>", unsafe_allow_html=True)
            st.image(tripleS_photos.loc[index[0], "PHOTO3"])
            st.markdown(f"<h4 style='text-align: justify;'>EMOJI</h4>", unsafe_allow_html=True)
            st.markdown(f"<div style='text-align: justify; font-size: 17px; margin-bottom: 10px'>{tripleS_members.loc[index[0], "EMOJI"]}</div>", unsafe_allow_html=True)
            st.markdown(f"<h4 style='text-align: justify;'>COLOR</h4>", unsafe_allow_html=True)
            st.markdown(f"<div style='text-align: justify; font-size: 17px; margin-bottom: 10px'>{tripleS_members.loc[index[0], "COLOR"]}</div>", unsafe_allow_html=True)
            st.markdown(f"<h4 style='text-align: justify;'>REVEAL</h4>", unsafe_allow_html=True)
            st.markdown(f"<div style='text-align: justify; font-size: 17px; margin-bottom: 10px'>{tripleS_members.loc[index[0], "REVEAL"]}</div>", unsafe_allow_html=True)
            st.markdown(f"<h4 style='text-align: justify;'>DEBUT</h4>", unsafe_allow_html=True)
            st.markdown(f"<div style='text-align: justify; font-size: 17px; margin-bottom: 10px'>{tripleS_members.loc[index[0], "DEBUT"]}</div>", unsafe_allow_html=True)
            st.markdown(f"<h4 style='text-align: justify;'>SUB UNIDADES</h4>", unsafe_allow_html=True)
            st.markdown(f"<div style='text-align: justify; font-size: 17px; margin-bottom: 10px'>{tripleS_members.loc[index[0], "SUB UNIDADES"]}</div>", unsafe_allow_html=True)
            st.markdown(f"<h4 style='text-align: justify;'>HOGAR</h4>", unsafe_allow_html=True)
            st.markdown(f"<div style='text-align: justify; font-size: 17px; margin-bottom: 10px'>{tripleS_members.loc[index[0], "HOGAR"]}</div>", unsafe_allow_html=True)          
            coords = tripleS_members.loc[index[0], "COORDS"]
            coords1 = coords.split(", ")
            for i in coords1:
                coords1.append(float(i))
            st.write(coords1)
elif selected == "Buscador":
    st.markdown("<h1 style='text-align: center;'>Buscador</h1>", unsafe_allow_html=True)
    yesno = ["No", "Si/Yes"]
    yesno_choose = ["No, no he terminado/No, I've not", "Si, terminé/Yes, I finish"]
    yesno_type = ["Si, tipos exclusivos/Yes, exclusive types", "No, no tipos exclusivos/No, no exclusive types"]
    yesno_member = ["Si, miembros exclusivos/Yes, exclusive members", "No, no miembros exclusivos/No, no exclusive members"]
    yesno_df = ["No, no quiero ver la base de datos completa/No, I don't want to see the whole database", "Si, quiero ver la base de datos completa/Yes, I want to see the whole database"]
    posibilidades = ["Por fechas/By Date", "Por tipos/By Type", "Por miembros/By Members"]
    start = st.selectbox("¿Quieres iniciar el buscador?/Do you wanna start the searching?:", yesno)
    if start == "Si/Yes":
        base_busc = []
        df_base_busc = pd.Series()
        start_pos = st.multiselect("¿Como quieres buscar?/How do you wanna search?:", posibilidades)
        if "Por fechas/By Date" in start_pos:
            day_in = st.date_input("A partir de:", min_value= "2024-04-04", max_value="2025-04-03")
            st.write("A partir de:", day_in)
            day_out = st.date_input("Hasta:", min_value= "2024-04-04", max_value="2025-04-03")
            st.write("Hasta:", day_out)
        if "Por tipos/By Type" in start_pos:
            busc_types = st.multiselect("Elige una o más tipos/Choose one or more types:", types)
            exclusive_type = st.selectbox("¿Deseas que sea una búsqueda exclusiva?/Do you want a exclusive research?:", yesno_type)
            st.write("Una búsqueda exclusiva será más rigurosa y solo tomará en cuenta que los valores pedidos de tipos sean exactos.")
        if "Por miembros/By Members" in start_pos:
            busc_member = st.multiselect("Elige una o más miembros/Choose one or more members:", miembros_tS)
            exclusive_mem = st.selectbox("¿Deseas que sea una búsqueda exclusiva?/Do you want a exclusive research?:", yesno_member)
            st.write("Una búsqueda exclusiva será más rigurosa y solo tomará en cuenta que los valores pedidos de miembros sean exactos.")
        finish = st.selectbox("¿Terminaste de elegir?/Did you finish choosing?:", yesno_choose, key="No")
        if finish == "Si, terminé/Yes, I finish":
            base_date = []
            base_type_exc = []
            base_type = []
            base_mem_exc = []
            base_mem = []
            if "Por fechas/By Date" in start_pos:
                for index, row in tripleS.iterrows():
                    datedf = datetime.strptime(row["DATE"], "%Y-%m-%d")
                    if day_in <= datedf.date() <= day_out:
                        base_date.append(row["code"])
            if "Por tipos/By Type" in start_pos:
                if exclusive_type == "Si, tipos exclusivos/Yes, exclusive types":
                    busc_types.sort()
                    busc_types1 = ",".join(busc_types)
                    for index, row in tripleS.iterrows():
                        if row["TYPE"] == busc_types1:
                            base_type_exc.append(row["code"])
                else:
                    for index, row in tripleS.iterrows():
                        if "," in row["TYPE"]:
                            types_in = row["TYPE"].split(",")
                            for i in types_in:
                                if i in busc_types:
                                    if row["code"] not in base_type:
                                        base_type.append(row["code"])
                        else:
                            if row["TYPE"] in busc_types:
                                base_type.append(row["code"])
            if "Por miembros/By Members" in start_pos:
                if exclusive_mem == "Si, miembros exclusivos/Yes, exclusive members":
                    busc_member.sort()
                    busc_member1 = ",".join(busc_member)
                    for index, row in tripleS.iterrows():
                        if row["MEMBERS"] == busc_member1:
                            base_mem_exc.append(row["code"])
                else:
                    for index, row in tripleS.iterrows():
                        if "," in row["MEMBERS"]:
                            members_in = row["MEMBERS"].split(",")
                            for i in members_in:
                                if i in busc_member:
                                    if row["code"] not in base_mem:
                                        base_mem.append(row["code"])
                        else:
                            if row["MEMBERS"] in busc_member:
                                base_mem.append(row["code"])
            if base_date:
                if base_type_exc:
                    if base_mem_exc:
                        for i in base_date:
                            if i in base_type_exc and base_mem_exc:
                                base_busc.append(i)
                    elif base_mem:
                        for i in base_date:
                            if i in base_type_exc and base_mem:
                                base_busc.append(i)
                    else:
                        for i in base_date:
                            if i in base_type_exc:
                                base_busc.append(i)
                elif base_type:
                    if base_mem_exc:
                        for i in base_date:
                            if i in base_type and base_mem_exc:
                                base_busc.append(i)
                    elif base_mem:
                        for i in base_date:
                            if i in base_type and base_mem:
                                base_busc.append(i)
                    else:
                        for i in base_date:
                            if i in base_type:
                                base_busc.append(i)
                else:
                    for i in base_date:
                        base_busc.append(i)
            elif base_type_exc:
                if base_mem_exc:
                    for i in base_type_exc:
                        if i in base_mem_exc:
                            base_busc.append(i)
                elif base_mem:
                    for i in base_type_exc:
                        if i in base_mem:
                            base_busc.append(i)
                else:
                    for i in base_type_exc:
                        base_busc.append(i)
            elif base_type:
                if base_mem_exc:
                    for i in base_type:
                        if i in base_mem_exc:
                            base_busc.append(i)
                elif base_mem:
                    for i in base_type:
                        if i in base_mem:
                            base_busc.append(i)
                else:
                    for i in base_type:
                        base_busc.append(i)
            elif base_mem_exc:
                for i in base_mem_exc:
                    base_busc.append(i)
            elif base_mem:
                for i in base_mem:
                    base_busc.append(i)
            else:
                st.write("Ha habido un error, no hay videos bajo ese criterio, vuelve a realizar la busqueda o llama a SUAH")
            if base_busc:
                for index, row in tripleS.iterrows():
                    if row["code"] in base_busc:
                        df_base_busc = pd.concat([df_base_busc, row], axis=1, ignore_index=True)
                df_base_busc_1 = df_base_busc.transpose().drop(0)
                df_base_busc_2 = df_base_busc_1[["NAME", "DATE", "TYPE", "DURATION", "LINK", "MEMBERS"]]
                st.data_editor(df_base_busc_2,
                                    column_config={
                                        "LINK": st.column_config.LinkColumn(),
                                    },
                                    hide_index=True,
                                )
                showdf = st.selectbox("¿Quieres ver la base de datos completa?/Do you want to see the whole database?:", yesno_df)
                if showdf == "Si, quiero ver la base de datos completa/Yes, I want to see the whole database":
                    st.data_editor(df_base_busc_1,
                                    column_config={
                                        "LINK": st.column_config.LinkColumn(),
                                    },
                                    hide_index=True,
                                )
elif selected == "Informe":
    st.markdown("<h1 style='text-align: center;'>Informe</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>1. DATOS GENERALES</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: justify;'>1.1 Para el análisis:</h3>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Para llegar a una conclusión si existe o no desigualdad en el grupo se va tomar el primer cuartil de cada gráfico resultante. Las miembros en el primer cuartirl recibirán un punto. Al final se mostrará la tabla con los resultados, y a partir de esa tabla podemos establecer una desigualdad a partir de la diferencia de presencia mayoritaria de las miembros en general.</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>La asignación de puntajes se realizó de la siguiente manera, se tomo el primer cuartil del gráfico, a la miembro que encabezaba el gráfico se le otroga 6 puntos, de ahi va menorando de 1 en 1 otorgando puntaje a todo el top6. En caso el primer cuartil sea menor que 6, se divide 6 entre la cantidad necesaria para cubrir los puntajes. Por ejemplo, solo dos miembros sobresalen, entonces a la primera se le otorga 6 puntos y a la segunda 3. La proporcionalidad nos ayudará a tener un mayor entendimiento de como están repartidas las miembros a través del contenido multimedia</div>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: justify;'>1.2 Terminología:</h3>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'><b>DIMENSIONS:</b> Subunidades o Dimensions son el sistema con el que funciona tripleS, se realiza una votación o Grand Gravity donde los fans eligen qué miembros están en que subunidad, además de otras actividades durante las promociones.</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'><b>SEASON:</b> MODHAUS separa etapas de tripleS en Seasons, al momento ha habido seis seasons. Bloque 01: Atom, Binary, Cream, Divine, Ever y Bloque 02: Atom</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'><b>OT24:</b> Cuando el grupo está completo, OT significa “One True”, 24, la cantidad de miembros.</div>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: justify;'>1.3 Sobre las bases de datos:</h3>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Para el análisis de la aparición de las miembros se utilizaron tres bases de datos:</div>", unsafe_allow_html=True)
    lista_markdown = """
    *   Distribucion de lineas en canciones
    *   Tiempo en pantalla en videos musicales
    *   Productos audiovisuales en general    """
    st.markdown(f"{lista_markdown}")
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>La primera base de datos toma en cuenta que a partir de la cantidad de miembros y la cantidad de canciones, no todas tienen la oportunidad de cantar lo mismo. Dentro del K-pop, la distribución de líneas es desigual, y está bien. Algunas miembros tienen mayor experiencia vocal y brillan cantando. Las miembros que destaquen en esta sección deberán ser las que son consideradas Vocalistas principales o líder. Los datos de esta base de datos han sido recopilados de distintos canales de YouTube y realización propia.</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>La segunda base de datos se centra en el tiempo en pantalla de las miembros en videos musicales. Se toma en cuenta los videos que se han subido al canal oficial de tripleS en YouTube. El video de Closer de Nakyoung no se considerará al ser subido en otro canal, por lo que no tuvo promoción de MODHAUS. Los datos son todos de realización propia, donde se cuenta como tiempo en pantalla cuando las miembros son enfocadas en solo, dúo o trios. </div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>La tercera y última base de datos es una adaptación del trabajo de (AUTORA). Ella ha recogido información en su base de datos de casi todos los productos audiovisuales de tripleS en toda su historia por diversión. Tome todo el contenido desde el 4 de abril de 2024 hasta el 4 de abril de 2025, esto toma todo el primer año de Ji SuHyeon como parte del grupo, en otras palabras, el primer año del grupo completo.</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>La base de datos cuenta con las siguientes columnas</div>", unsafe_allow_html=True)
    lista_markdown1 = """
    *   NAME: AAAA.MM.DD [TYPE] Título relevante
    *   DATE: Fecha en la que fue añadido a la base de datos, o se subió.
    *   TYPE: Tipo del contenido
    *   TITLE: Título original del video.
    *   DURATION: Duración del video en formato HH:MM:SS
    *   LINK: Link al contenido
    *   ENG SUB: Si tiene o no subtítulos.
    *   MEMBERS: Miembros que aparecen en el video
    *   KEYWORDS: Palabras clave para filtrar el contenido sobre lo que sucede en los videos
    *   TAG: Etiquetas generales para filtrar el contenido
    *   ERA: A que Era pertenece en cuanto a los lanzamientos del grupo
    *   SEASON: Temporada según los reglamentos 
    *   EPISODE: Si el video forma parte de una serie de episodios o capítulos.
    *   SOURCE: Fuente
    *   NOTES: Información relevante 
    *   ALT LINKS: Links alternos para acceder al mismo contenido
    """
    st.markdown(f"{lista_markdown1}")
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>A partir de la información base, se revisó las aproximada 1700 entradas, y se realizaron las siguientes modificaciones:</div>", unsafe_allow_html=True)
    lista_markdown2 = """
    *   Corrección de links repetidos
    *   Corrección de entradas repetidas
    *   Rellenar casillas vacías
    *   Agregar entradas (Waterbomb, COSMO EXCLUSIVE SIGNAL)
    *   Separar presentaciones por subunidades donde no todas las miembros indicadas participaban. 
    """
    st.markdown(f"{lista_markdown2}")
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Si desean acceder a la base de datos tomada en cuenta para este producto es la siguiente:</div>", unsafe_allow_html=True)
    url = "https://docs.google.com/spreadsheets/d/14jEpB8iPhw_vaOlUNyZMIIIfa-lJPF3Z/edit?usp=sharing&ouid=103238436875544229591&rtpof=true&sd=true"
    st.markdown("[BASE DE DATOS - tripleS 240404 - 250404](%s)" % url)
    st.markdown("<h2 style='text-align: center;'>2. HIPOTESIS</h2>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>A partir de una encuesta realizada a aproximadamente 300 personas entre el 250616 y 250618 se llegaron a ciertas conclusiones sobre la percepción de los fans en cuantó a la desiguladad en el grupo.</div>", unsafe_allow_html=True)
    class Tweet(object):
        def __init__(self, s, embed_str=False):
            if not embed_str:
                # Use Twitter's oEmbed API
                # https://dev.twitter.com/web/embedded-tweets
                api = "https://publish.twitter.com/oembed?url={}".format(s)
                response = requests.get(api)
                self.text = response.json()["html"]
            else:
                self.text = s

        def _repr_html_(self):
            return self.text

        def component(self):
            return components.html(self.text, height=600)
    t = Tweet("https://x.com/YisvaQC_02/status/1934073866034323797").component()
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>El '89.5%' considera que no todas las miembros tienen el mismo tiempo en pantalla a través de la media</div>", unsafe_allow_html=True)
    #AGREGAR CUADRO SI NO
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Del '89.5%', '50.2%' cree la multimedia esta enfocada en las miembros que venden más objekts, luego un '14%' que considera que las miembros extrovertidas tienen mayor foco, por último un '10.9%' considera que las primeras 16 miembros son las que tienen mayor foco (S1 - S16)</div>", unsafe_allow_html=True)
    #AGREGAR CUADRO NO
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Por otro lado, del '5.8%' consideran que si hay una igualdad con las miembros, '47.1%' piensa que algunas miembros brillan más en media por sus personalidades</div>", unsafe_allow_html=True)
    #AGREGAR CUADRO SI
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Primero consideremos los valores de ventas de objekts durante las primeras 24 horas durante el periodo que se esta estudiando</div>", unsafe_allow_html=True)
    #AGREGAR CUADRO VENTAS
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Por otro lado, las miembros extrovertidas (según su MBTI) son las siguientes: </div>", unsafe_allow_html=True)
    lista_markdown3 = """
    *   Hyerin
    *   Chaeyeon
    *   Soomin
    *   Yubin
    *   Kotone
    *   Yeonji
    *   Nien
    *   Xinyu
    *   Mayu
    *   Hayeon
    *   Shion
    *   Seoah
    """
    st.markdown(f"{lista_markdown3}")
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>De la misma maneras, las primeras 16 miembros son las siguientes: </div>", unsafe_allow_html=True)
    lista_markdown4 = """
    *   Seoyeon
    *   Hyerin
    *   Jiwoo
    *   Chaeyeon
    *   Yooyeon
    *   Soomin
    *   Nakyoung
    *   Yubin
    *   Kaede
    *   Dahyun
    *   Kotone
    *   Yeonji
    *   Nien
    *   Sohyun
    *   Xinyu
    *   Mayu
    """
    st.markdown(f"{lista_markdown4}")
    st.markdown("<h2 style='text-align: center;'>3. CANCIONES</h2>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Durante el primer año del grupo completo se han lanzado 29 canciones, 11 como grupo completo, las demás son subunidades (Inner Dance, Performante y Untitled), OSTs (Polaroid, Dreaming, PainDrop, First Night Of Snow) y un solo (Closer de Nakyoung).</div>", unsafe_allow_html=True)
    with open("SONGS/TOTAL.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Tomando en cuenta que no todas las canciones son del grupo completo, se analiza otro gráfico con solo las canciones OT24.</div>", unsafe_allow_html=True)
    with open("SONGS/TOTALot24.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Por miembro, la cantidad de canciones que tienen varia en su participación en subunidades</div>", unsafe_allow_html=True)
    with open("SONGS/CANTIDADTOTAL.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass    
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Por lo que el promedio de tiempo en segundos es el siguiente</div>", unsafe_allow_html=True)
    with open("SONGS/PROM.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass    
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Son pocas las miembros que fueron las que cantaron más en cada canción, ellas tuvieron el primer puesto, todas reciben un punto</div>", unsafe_allow_html=True)
    with open("SONGS/FIRST.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass
    st.markdown("<h2 style='text-align: center;'>3.1 ¿Quieres ver la distribución de una canción específica?</h2>", unsafe_allow_html=True) 
    canciones = ['S','Girls Never Die', 'Heart Raider', 'Midnight Flower',
       'White Soul Sneakers', 'Chiyu', '24', 'Beyond the Beyond', 'Non Scale',
       'Dimension', 'Inner Dance', '###', 'Visual Virtue', 'Hit the Floor',
       'Choom', 'Éclair', '연애소설 (Love Soseol)', 'Atmosphere (VV Ver.)',
       '12 Rings', 'Vision', 'Bionic Power', 'Vision@ry Vision', 'Polaroid',
       'Untitled', '### (∞! Ver.)', 'Dreaming', 'Closer',
       'First Night Of Snow', 'PainDrop', 'TOTAL', 'TOTAL_OT24', 'TOTAL SONGS',
       'TOTAL_1ST_PLACE', 'PROM']

    entrada = st.selectbox("INGRESA UNA CANCION:", canciones)
    tripleS_songs = pd.read_csv(r"DATABASE/tripleS_songs.csv", encoding='utf-8')
    tripleS_songs = tripleS_songs.fillna(0)
    base = {}
    for index, row in tripleS_songs.iterrows():
        if row[entrada] != 0:
            base[row["MEMBER"]] = row[entrada]

    base = dict(sorted(base.items(), key=lambda item:item[-1], reverse=True))

    colors_base = []

    for i in base:
        i_color = colors_ts_hex[i]
        colors_base.append(i_color)

    base1 = {
        "Miembro": [],
        "Tiempo (en segundos)": []
    }

    for member, time in base.items():
        base1["Miembro"].append(member)
        base1["Tiempo (en segundos)"].append(time)

    prueba = px.bar(base1,
                x='Miembro',
                y="Tiempo (en segundos)",
                color="Miembro",
                title=f"Distribucón de lineas en {entrada}",
                color_discrete_sequence=colors_base,
                text="Tiempo (en segundos)"
                )
    st.write(prueba)
    st.markdown("<h2 style='text-align: center;'>4. VIDEOS MUSICALES</h2>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Durante el primer año del grupo completo se han lanzado 4 videos musicales, 1 como grupo completo, los demás como parte de las subunidades.</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>De la misma manera, se trabajará por cuartiles según cada video. </div>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>4.1 Girls Never Die</h3>", unsafe_allow_html=True)
    with open("MVS/GND.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass    
    st.markdown("<h3 style='text-align: center;'>4.2 Inner Dance</h3>", unsafe_allow_html=True)
    with open("MVS/ID.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass    
    st.markdown("<h3 style='text-align: center;'>4.3 Hit The Floor</h3>", unsafe_allow_html=True)
    with open("MVS/HTF.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass    
    st.markdown("<h3 style='text-align: center;'>4.4 Untitled</h3>", unsafe_allow_html=True)
    with open(r"MVS/UNTITLED1.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>En total, este fue el tiempo total de pantalla que tuvieron las miembros en todos los videos musicales</div>", unsafe_allow_html=True)
    with open("MVS/TOTAL_MVS.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Esta fue la cantidad de videos musicales en la que cada una participó</div>", unsafe_allow_html=True)
    with open("MVS/TOTAL_CANTIDAD.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Por lo tanto, este fue el promedio de su participación en los videos musicales</div>", unsafe_allow_html=True)
    with open("MVS/TOTAL_PROM.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Al haber cuatro videos musicales, fueron aún menos las miembros que fueron las que más brillaron, todas reciben un punto</div>", unsafe_allow_html=True)
    with open("MVS/TOTAL_1ST.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass
    st.markdown("<h2 style='text-align: center;'>5. CONTENIDO MULTIMEDIA</h2>", unsafe_allow_html=True)
    #TOTAL
    st.markdown("<h3 style='text-align: center;'>5.1 ANÁLISIS GENERAL</h3>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Esta amplia base de datos nos ayuda a entender de forma masiva como se han ido comportando los patrones de participación de las miembros de tripleS. </div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Esta gráfico muestra una sumatoria total indiscriminada de todos los videos.</div>", unsafe_allow_html=True)
    with open("VIDEOS/GRAFICO_TOTAL.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass    
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Como parte del analisis tambien se va a tomar en cuenta cuando en el contenido multimedia solo aparece una miembro</div>", unsafe_allow_html=True)
    with open(r"VIDEOS/GRAFICO_TOTAL_SOLO.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass    
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Tener esta información en crudo nos da una primera perspectiva hacia dónde vamos, pero debemos de ir ramificando poco a poco nuestra base de datos para tener claro en que productos y formatos cada miembro resalta más. </div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Por ello es necesario hacer un analisis de los tipos de videos que encontramos en esta base de datos</div>", unsafe_allow_html=True)
    with open("VIDEOS/GRAFICO_TOTAL_TYPE.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass       
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Y claro, su equivalencia en tiempo</div>", unsafe_allow_html=True)
    with open("VIDEOS/GRAFICO_TOTAL_TYPE_TIME.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass       
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Por lo tanto la mejor forma de entender los videos es si los dividimos en dos categorias, On Stage y Off Stage.</div>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>5.2 ANÁLISIS ON STAGE</h3>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Se considera On Stage todos los productos audiovisuales donde una o más miembros de tripleS se presentan con canciones personales o del grupo.</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Para la selección de los videos que entran dentro de esta categoria se tomaron en cuenta los tipos: 'Fancam', 'Music Video', 'Dance', 'Special Clip', 'Performance', 'Dance Practice', 'Concert', 'Playlist', 'Official Audio' y 'Song'.</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Playlist considera todas las entradas de la base de datos que cuentan con más de un video y se organizaron por playlist para mayor facilidad de reproducción.</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Según el siguiente gráfico estos son los tipos de videos principales en los productos Off Stage:</div>", unsafe_allow_html=True)
    with open("VIDEOS/GRAFICO_TOTAL_ON_STAGE_TYPE.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass   
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>A partir de los productos On Stage resultó el siguiente gráfico:</div>", unsafe_allow_html=True)
    with open("VIDEOS/GRAFICO_TOTAL_ON_STAGE.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass   
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Parte de las presentaciones On Stage en especial en los shows musicales son las fancams, este es un gráfico que representa todas las fancams/facecams individuales. </div>", unsafe_allow_html=True)  
    with open("VIDEOS/GRAFICO_TOTAL_ON_STAGE_FANCAM.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass     
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>A partir de este gráfico se puede ramificar los productos entre los videos que se consideran como promoción para una DIMENSION específica (Visionary Vision, Hatchi y tripleS Come True (para el tour mundial)) y los demás que son festivales, presentaciones especiales en premiaciones y eventos diversos.</div>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>5.2.1 ANÁLISIS ON STAGE - DIMENSIONS</h4>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Las unidades que se promocionaron durante el primer año del grupo completo fueron Visionary Vision, Hatchi y tripleS Come True.</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Visionary Vision fue la subunidad de baile del grupo, que fue elegida a través de un Grand Gravity. Las miembros elegidas fueron: HyeRin, YooYeon, NaKyoung, YuBin, Kaede, Kotone, YeonJi, Nien, SoHyun, Xinyu, Lynn, JiYeon. Debutaron el 23 de octubre de 2024 y promocionaron en shows musicales desde el 24 de octubre hasta el 10 de noviembre del mismo año. A la fecha no está confirmado que la subunidad vuelva a promocionar en un futuro próximo.</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Hatchi es la primera subunidad japonesa del grupo, al igual que Visionary Vision fue elegida en un Grand Gravity. Las miembros elegidas fueron: JiWoo, ChaeYeon, YooYeon, SooMin, Kotone, Mayu, ShiOn, ChaeWon. La subunidad se promociona exclusivamente en Japón, por lo que no se presentó en shows musicales. Debutaron el 20 de noviembre de 2024 y están preparando su primer comeback para la segunda mitad de 2025</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>tripleS Come True es la subunidad que realizó el segundo tour mundial del grupo. Las miembros elegidas fueron SeoYeon, NaKyoung, DaHyun, Nien, JooBin, HaYeon, Sullin, SeoAh. Este tour llegó a Sur Asia y NorteAmérica con 10 presentaciones. Todos los conciertos han sido subidos a YouTube, en videos o playlists.</div>", unsafe_allow_html=True)
    with open("VIDEOS/GRAFICO_TOTAL_ON_STAGE_DIMENSIONS.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Como se ve en el gráfico, las miembros Nakyoung y Nien destacan más al pertenecer a dos subunidades, VV y tCT. Por lo que es necesario analizar a Visionary Vision como subunidad.</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Respecto a tCT, al promocionarlas en el tour se considera una intención completa de MODHAUS en promover a 8 miembros. Por lo que se considerará con mayor prioridad a las 8.</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'></div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'></div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'></div>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center;'>5.2.1.1 ANÁLISIS ON STAGE - VISIONARY VISION</h5>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>El siguiente gráfico representa solo los productos On Stage que tienen en sus palabras clave: Visionary Vision.</div>", unsafe_allow_html=True)
    with open("VIDEOS/GRAFICO_TOTAL_ON_STAGE_VV.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass 
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Como se ve en el gráfico, no hay una igualdad exacta entre las miembros, tomando en cuenta que son 12 miembros, el primer cuartil o el top 3 son las miembros:</div>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>5.2.2 ANÁLISIS ON STAGE - NO DIMENSIONS</h4>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Respecto a las miembros, su participación en eventos de no subunidades es la siguiente:</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Las miembros que resaltan son las que no han promocionado en shows musicales.</div>", unsafe_allow_html=True)
    with open("VIDEOS/GRAFICO_TOTAL_ON_STAGE_NON_DIMENSIONS.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass    
    st.markdown("<h3 style='text-align: center;'>5.3 ANÁLISIS OFF STAGE</h3>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Se considera Off Stage todos los productos audiovisuales excluyentes a los On Stage, ya sea, detrás de cámaras, blogs, SIGNALs, Secret Bases, LIVE y demás. Según el siguiente gráfico estos son los tipos de videos principales en los productos Off Stage:</div>", unsafe_allow_html=True)    
    with open("VIDEOS/GRAFICO_TOTAL_OFF_STAGE_TYPE.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>A partir de los productos Off Stage resultó el siguiente gráfico:</div>", unsafe_allow_html=True)
    with open("VIDEOS/GRAFICO_TOTAL_OFF_STAGE.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Del gráfico mostrado, este representa los productos donde las miembros aparecen solas</div>", unsafe_allow_html=True)
    with open("VIDEOS/GRAFICO_TOTAL_OFF_STAGE_SOLO.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>A partir de la información que tenemos podemos ramificarla por origen</div>", unsafe_allow_html=True)
    with open("VIDEOS/GRAFICO_TOTAL_OFF_STAGE_SOURCE.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>A partir de este gráfico se puede ramificar los productos entre los videos que se consideran oficiales, subidos en el canal de YouTube de tripleS official y no oficiales, subidos por otros canales.</div>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>5.3.1 ANÁLISIS OFF STAGE - OFFICIAL</h4>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Los videos oficiales son los publicados en el canal de YouTube de tripleS official, y los LIVE resubidos.</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Los LIVE no se guardan en el canal oficial, una cuenta fan (MangoNim) los subtitula y resube. Por lo que todos los LIVE se contarán como Official, porque fueron transmitidos de manera oficial en la cuenta de Youtube.</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Respecto a los tipos dentro del contenido oficial, los tipos se reparten de la siguiente manera:</div>", unsafe_allow_html=True)
    with open("VIDEOS/GRAFICO_TOTAL_OFF_STAGE_OFFICIAL_TYPE.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Como vemos, en el gráfico hay una predominancia de los tipos Shorts, SIGNAL, Secret Base y Live.</div>", unsafe_allow_html=True)
    with open("VIDEOS/GRAFICO_TOTAL_OFF_STAGE_OFFICIAL.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass
    with open("VIDEOS/GRAFICO_TOTAL_OFF_STAGE_OFFICIAL_SOLO.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass
    st.markdown("<h5 style='text-align: center;'>5.3.1.1 ANÁLISIS OFFICIAL SHORTS</h5>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Shorts considera todos los videos cortos subidos en TikTok o YouTube. Considera trends, dance challenge y demás. No considera shorts que son teasers resubidos o similares.</div>", unsafe_allow_html=True)
    with open("VIDEOS/GRAFICO_TOTAL_OFFICIAL_SHORTS.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass
    with open("VIDEOS/GRAFICO_TOTAL_OFFICIAL_SHORTS_SOLO.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass
    st.markdown("<h5 style='text-align: center;'>5.3.1.2 ANÁLISIS SIGNAL</h5>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>SIGNAL es un reality web show que sigue a las miembros de tripleS en su día a día. En un principio se subía contenido diario, de lunes a viernes, hasta que bajó de frecuencia en la temporada Cream01, solo lunes, miércoles y viernes.</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Dentro de SIGNAL, están los COSMO EXCLUSIVE SIGNAL. Contenido que se sube exclusivamente en la aplicación de cosmo, app de MODHAUS y han sido resubidas a Youtube.</div>", unsafe_allow_html=True)
    with open("VIDEOS/GRAFICO_TOTAL_SIGNAL.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass
    with open("VIDEOS/GRAFICO_TOTAL_SIGNAL_SOLO.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass
    st.markdown("<h5 style='text-align: center;'>5.3.1.3 ANÁLISIS SECRET BASE</h5>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>SecretBase en un vlog semanal personal de cada miembro, un formato simple donde por unos minutos hablan sobre temas variados y sus percepciones frente a próximos proyectos o similares. Usualmente los vlogs son subidos días o semanas después de ser grabados. Antes de un comeback, todas las miembros que participan en las promociones suben un SecretBase donde hablan sobre el próximo lanzamiento.</div>", unsafe_allow_html=True)
    with open("VIDEOS/GRAFICO_TOTAL_SECRETBASE.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass
    st.markdown("<h5 style='text-align: center;'>5.3.1.4 ANÁLISIS LIVE</h5>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>LIVE o SIGNAL LIVE es un en vivo que realiza una o más miembros durante la semana, entre uno o tres por semana. Duran aproximadamente entre cuarenta minutos y una hora.</div>", unsafe_allow_html=True)
    with open("VIDEOS/GRAFICO_TOTAL_LIVE.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass
    with open("VIDEOS/GRAFICO_TOTAL_LIVE_SOLO.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass
    st.markdown("<h4 style='text-align: center;'>5.3.2 ANÁLISIS OFF STAGE - NON OFFICIAL</h4>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Se considera No Oficial todo el contenido off stage que no está publicado en el canal oficial de tripleS oficial en YouTube o TikTok.</div>", unsafe_allow_html=True)
    with open("VIDEOS/GRAFICO_TOTAL_OFF_STAGE_NON_OFFICIAL_TYPE.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Predominan los Variety, programas de contenido diverso de entretenimiento.</div>", unsafe_allow_html=True)
    with open("VIDEOS/GRAFICO_TOTAL_OFF_STAGE_NON_OFFICIAL.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass
    with open("VIDEOS/GRAFICO_TOTAL_OFF_STAGE_NON_OFFICIAL_SOLO.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass
    st.markdown("<h5 style='text-align: center;'>5.3.2.1 ANÁLISIS NON OFFICIAL SHORTS</h5>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>De la misma manera que los Shorts Oficiales, se suben en distintas cuentas pero igual promocionan el grupo</div>", unsafe_allow_html=True)
    with open("VIDEOS/GRAFICO_TOTAL_NON_OFFICIAL_SHORTS.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass
    with open("VIDEOS/GRAFICO_TOTAL_NON_OFFICIAL_SHORTS_SOLO.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass
    st.markdown("<h5 style='text-align: center;'>5.3.2.2 ANÁLISIS VARIETY</h5>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>A lo largo del internet surcoreano y el internet en general hay diversos productos que no se categorizan especificamente en uno u otro, por lo que se les considera Variety o de Variedad de Entretenimiento</div>", unsafe_allow_html=True)
    with open("VIDEOS/GRAFICO_TOTAL_OFF_STAGE_NON_OFFICIAL_VARIETY.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass
    with open("VIDEOS/GRAFICO_TOTAL_OFF_STAGE_NON_OFFICIAL_VARIETY_SOLO.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=500)
    pass
    st.markdown("<h2 style='text-align: center;'>6. CONCLUSIONES</h2>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Para considerar que existe una equidad, o una intención de MODHAUS para promocionar a todas las miembros por igual, cada una debería de aparecer como mínimo una vez en algún primer cuartil de los gráficos realizados. Y tener una puntuación mayor de 20.</div>", unsafe_allow_html=True)
    df = pd.read_csv(r"CONCLUSIONS.csv", encoding='utf-8')
    st.dataframe(df)
    CONCLUSIONS_TOTAL = pd.read_csv(r"CONCLUSIONS_TOTAL.csv", encoding='utf-8')
    base = {}
    for index, row in CONCLUSIONS_TOTAL.iterrows():
        if row["TOTAL"] != 0:
            base[row["MEMBER"]] = round(row["TOTAL"])
    base = dict(sorted(base.items(), key=lambda item:item[-1], reverse=True))

    colors_base = []

    for i in base:
        i_color = colors_ts_hex[i]
        colors_base.append(i_color)

    base1 = {
        "Miembro": [],
        "Cantidad": []
    }

    for member, time in base.items():
        base1["Miembro"].append(member)
        base1["Cantidad"].append(time)

    prueba1 = px.bar(base1,
                x='Miembro',
                y="Cantidad",
                color="Miembro",
                title="Presencia de las miembros de tripleS a través de sus contenidos multimedia",
                color_discrete_sequence=colors_base,
                text="Cantidad"
                )
    st.write(prueba1)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Las miembros que quedan fuera de los parámetros establecidos son Hyerin, Soomin, Kaede, Yeonji, Mayu, Lynn, Shion, Sullin y Seoah. Algunos factores en común entre ellas son los siguientes: </div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Todas menos Mayu representan la maknae-line, es decir, las miembros menores del grupo. Solo faltaria añadir a Joobin, Hayeon y Chaewon, las cuales se encuentran en top 15, 10 y 6 de participación en el grupo. </div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>La promoción diferenciada de Hayeon y Chaewon por parte de MODHAUS se puede explicar a partir de un par de razones. Entre ambas existe un ship o dinamica llamda MoChiz. El fandom empareja a las idols a partir de sus interacciones y luego van ganando más fama dentro del grupo. Caso parecido sucedio con Sohyun y Xinyu, SoXinz, que desde que ambas llegaron a la compañia, sus interacciones han generado un apoyo constante a ambas.</div>", unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=UywRWZzwB54")
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Respecto a Joobin, ella tiene un programa de entrevistas donde habla con otras miembros del grupo, además es reconocida como la que maneja mejor el idioma Inglés por lo que forma parte constantemente de eventos, en especial festivales y conciertos. </div>", unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=Ec-iKxDomIw")
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Por otra parte, Chaewon viene de un programa de supervivencia, Universe Ticket. La cultura de los programas de supervivencia es un tema que se debe de abordar aparte, pero es resaltante que el apoyo a una o dos participantes entre las decenas de concursantes hace que generen un fandom masivo por haber participado previamente en un programa.</div>", unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=EiEZVYV9Xuk")
    col1, col2 = st.columns(2)
    col1.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Por último, Hayeon se la considera una miembro caotica en un sentido positivo, tomando en cuenta su participación en Badge War Temporada 3, un reality de supervivencia anual que realiza el grupo, su popularidad estará escalando.</div>", unsafe_allow_html=True)
    col2.video("https://www.youtube.com/watch?v=Ho-fdGAF_R4")
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Otro factor en común, que se acerca a nuestra hipótesis, son las ventas. Las miembros mencionadas conforman el top 12-24 de ventas. Junto a Chaeyeon, Dahyun, Nien y Joobin, en orden de menos a más ventas. Estas cuatro miembros mencionadas se encuentran en los puestos 11, 7, 4 y 15 respectivamente.</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>¿Que las diferencia? Chaeyeon fue parte de Busters, un grupo pequeño de hace un par de años, pero eso no quita que tenga un fandom de su grupo anterior. Además para el fandom la personalidad de Chaeyeon es la que más resalta en el grupo, en internet la consideran “El alma de la fiesta”, “Ruidosa sin intención”, “Tonta (goofy) con un arco narrativo”. Estos adjetivos complementan que ella aparezca un poco más en videos oficiales, y también su experiencia para aparecer en Radio y Programas de Variedad.</div>", unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=4hPWgW1NY2o")
    col3, col4 = st.columns(2)
    col3.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Dahyun, por su parte, es la vocalista principal de tripleS, los gráficos de canciones la han hecho alcanzar el top 7, es una miembro que siempre va a resaltar en la música.</div>", unsafe_allow_html=True)
    col4.video("https://www.youtube.com/watch?v=zOJKs7EFABA")
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Por último, Nien, también conocida por sus habilidades de baile, se encuentra en los primeros puestos a pesar de sus ventas por una gran clara razón “Chef’s Crash Landing: Hakka Kitchen”. El programa mencionado fue un reality de corta duración producido en Taiwan, un grupo de celebridades y un chef ayudan a un restaurante Hakka, de la cultura China Hakka. Al ser un programa de aproximadamente 50 minutos, destaca notablemente entre las demás miembros. Sumado a su participación en Visionary Vision y tripleS Come True. </div>", unsafe_allow_html=True)
    st.video("https://youtu.be/EsUOGoLagG4")
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Ahora, ya entendiendo como MODHAUS promociona algunos miembros podemos regresar a Hyerin, Soomin, Kaede, Yeonji, Mayu, Lynn, Shion, Sullin y Seoah, para comprobar si tienen un trato desigual en comparación con las demás miembros. </div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Todas han participado en una subunidad. La inclusión de Sullin se debe a su poco manejo de coreano que ha ido mejorando a lo largo de su participación en el grupo, aún asi, ella más de una vez ha sido vocal sobre el deseo de participar más. Hyerin, Soomin, Yeonji, Lynn, Shion y Seoah al estar en etapa de formación académica cuentan con menos tiempo para participar dentro de contenidos, en especial Seoah al estar aún en la secundaria. Respecto a Mayu, es incierto. Kaede destaca no solo bailando sino también cantando. En la subunidad de Visionary Vision fue la que más líneas tuvo, realizando notas altas tanto en el álbum como en presentaciones en vivo. Últimamente el fandom ha notado cierta separación de Mayu, ya que estuvo en un hiatus durante un tiempo para revelar que estaba tratando de retomar su universidad aunque decidió dejarla y dedicarse completamente al grupo.</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'>Por lo tanto, cada miembro que no aparece en la media seguido tiene una razón porque o se desempeña perfectamente en otro ámbito, pero eso no significa que la compañía no tenga que ver formas de ser transparente con ello. Desde el primer promocional OT24 la idea que MODHAUS sólo impulsa a las miembros que venden más es constante. En sí, coincide que las miembros que venden menos tienen razones para no aparecer seguido. La desigualdad es notable y la empresa tiene mejores herramientas para darle una atención más igualitaria a cada una. Que algunas miembros superen los 15 gráficos nos da a entender que hay miembros que se sobreexigen en más de un ámbito lo que puede afectar la imagen del grupo a la larga. Por ejemplo, Miss A, donde Suzy, miembro y actriz del grupo, destacaba mucho que el grupo empezó a llamarse  Suzy y sus amigas. La igualdad de contenido no es solo para los fans que buscan conocer sobre su idol favorita, sino también dentro de la psicología de las miembros, donde pueden sobreexigirse o sentirse menos, lo que a la larga afecta la reputación del grupo. </div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 15px; margin-bottom: 10px'></div>", unsafe_allow_html=True)
