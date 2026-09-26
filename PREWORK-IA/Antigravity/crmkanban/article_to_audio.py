import nltk
from newspaper import Article
from gtts import gTTS
import os
import urllib.request
import tempfile
import pypdf
import re
from langdetect import detect

def clean_filename(title):
    """Limpia el título para que sea un nombre de archivo válido."""
    # Eliminar caracteres no válidos en nombres de archivo (como / \ : * ? " < > |)
    clean = re.sub(r'[\\/*?:"<>|]', "", title)
    # Quitar saltos de línea y espacios extra
    clean = " ".join(clean.split())
    
    # Si por alguna razón el título queda vacío, le damos un nombre genérico
    if not clean:
        return "articulo_audio"
    
    # Limitar el tamaño del nombre por si es un título demasiado largo
    return clean[:150]

def detect_language(text):
    """Detecta el idioma del texto (soporta es, en, fr, de)."""
    try:
        # detect() devuelve el código del idioma (ej: 'en', 'es')
        lang = detect(text)
        idiomas_soportados = ['en', 'es', 'fr', 'de']
        
        if lang in idiomas_soportados:
            print(f"🌍 Idioma detectado: {lang.upper()}")
            return lang
        else:
            print(f"🌍 Idioma detectado '{lang}' no está en la lista solicitada, usando inglés (en) por defecto.")
            return 'en'
    except Exception:
        print("⚠️ No se pudo detectar el idioma, usando inglés (en) por defecto.")
        return 'en'

def convert_article_to_audio(url):
    """
    Descarga un artículo web o PDF, extrae su texto y lo convierte en un archivo de audio MP3
    con el nombre adecuado y el idioma correcto.
    """
    print(f"Obteniendo contenido de: {url} ...")
    
    try:
        texto = ""
        titulo = "Documento"
        
        # 1. PROCESAR PDF
        if url.lower().endswith('.pdf'):
            es_archivo_temporal = False
            
            if url.startswith('http://') or url.startswith('https://'):
                print("📄 Se detectó un enlace a un PDF en internet. Descargando y procesando...")
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
                    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                    with urllib.request.urlopen(req) as response:
                        temp_pdf.write(response.read())
                    temp_pdf_path = temp_pdf.name
                    es_archivo_temporal = True
                nombre_archivo = url.split('/')[-1]
            else:
                # Es un archivo local en tu computadora
                # Quitar comillas simples o dobles que a veces pone la terminal al arrastrar
                temp_pdf_path = url.strip("\"'")
                
                print("📄 Se detectó un archivo PDF local. Procesando...")
                if not os.path.exists(temp_pdf_path):
                    print(f"❌ No se encontró el archivo en tu computadora. Verifica la ruta: {temp_pdf_path}")
                    return
                nombre_archivo = os.path.basename(temp_pdf_path)
                
            titulo = nombre_archivo.replace('.pdf', '').replace('.PDF', '')
            
            try:
                with open(temp_pdf_path, 'rb') as file:
                    reader = pypdf.PdfReader(file)
                    for i, page in enumerate(reader.pages):
                        extracted = page.extract_text()
                        if extracted:
                            texto += extracted + "\n"
            finally:
                if es_archivo_temporal:
                    os.remove(temp_pdf_path)
                    
        # 2. PROCESAR WEB
        else:
            print("🌐 Se detectó una página web. Analizando texto...")
            article = Article(url)
            article.download()
            article.parse()
            
            try:
                nltk.data.find('tokenizers/punkt')
                nltk.data.find('tokenizers/punkt_tab')
            except LookupError:
                nltk.download('punkt')
                nltk.download('punkt_tab')
                
            article.nlp()
            
            texto = article.text
            titulo = article.title
        
        if not texto.strip():
            print("❌ No se pudo extraer el texto. Verifica la URL o si el PDF contiene solo imágenes.")
            return
            
        print(f"📝 Título/Nombre detectado: {titulo}")
        
        # --- NUEVAS MEJORAS ---
        
        # A. Nombrar el archivo como el título
        nombre_limpio = clean_filename(titulo)
        output_filename = f"{nombre_limpio}.mp3"
        
        # B. Detectar el idioma del texto (inglés, español, francés, alemán)
        # Solo usamos los primeros 1000 caracteres para detectar más rápido y preciso
        lang = detect_language(texto[:1000])
        
        print(f"🎙️  Convirtiendo el texto a audio con acento nativo (puede tardar unos minutos)...")
        
        # Convertir texto a voz usando gTTS con el idioma detectado automáticamente
        tts = gTTS(text=texto, lang=lang, slow=False)
        
        # Guardar el archivo MP3
        tts.save(output_filename)
        print(f"\n✅ ¡Éxito! Audio guardado en esta carpeta como: '{output_filename}'")
        
    except Exception as e:
        print(f"\n❌ Ocurrió un error: {e}")

if __name__ == "__main__":
    print("==================================================")
    print("🎧 Convertidor Inteligente de Artículos y PDFs a Audio")
    print("==================================================")
    
    url_usuario = input("\nPor favor, pega aquí la URL (web normal o archivo .pdf):\n> ").strip()
    
    if url_usuario:
        print("\nIniciando proceso...")
        convert_article_to_audio(url_usuario)
    else:
        print("No ingresaste ninguna URL. Cancelando operación.")
