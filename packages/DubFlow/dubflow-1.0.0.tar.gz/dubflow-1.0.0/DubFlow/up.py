import httpx
import requests
import json
import time
import os
from reg import *
from pydub import AudioSegment
import re
import zipfile


def delete_user_and_account(token):
    # Primer DELETE: Eliminar el usuario
    url_user = "https://app.rask.ai/api/user"
    headers_user = {
        "Host": "app.rask.ai",
        "Connection": "keep-alive",
        "sec-ch-ua-platform": "Windows",
        "Authorization": f"Bearer {token}",
        "sec-ch-ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        "sec-ch-ua-mobile": "?0",
        "baggage": "sentry-environment=prod,sentry-public_key=1641776a99d5fee8b3dca472f43779e2,sentry-trace_id=b7271bedf78a485a8e49bfad31bb9e88",
        "sentry-trace": "b7271bedf78a485a8e49bfad31bb9e88-84c14eee7021b12f",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Origin": "https://app.rask.ai",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://app.rask.ai/account",
        "Accept-Language": "es-ES,es;q=0.9,en;q=0.8",
        "Accept-Encoding": "gzip, deflate"
    }
    
    response_user = requests.delete(url_user, headers=headers_user)
    
    if response_user.status_code == 200:
        # Verificar si la respuesta contiene {"ok": true}
        try:
            data = response_user.json()
            if data.get("ok"):
                print("🗑️ User successfully deleted.")
                # Segundo DELETE: Eliminar la cuenta
                url_account = "https://rst.rask.ai/api/accounts/v1/users/current"
                headers_account = {
                    "Host": "rst.rask.ai",
                    "Connection": "keep-alive",
                    "sec-ch-ua-platform": "Windows",
                    "Authorization": f"Bearer {token}",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
                    "Accept": "application/json, text/plain, */*",
                    "sec-ch-ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
                    "sec-ch-ua-mobile": "?0",
                    "Origin": "https://app.rask.ai",
                    "Sec-Fetch-Site": "same-site",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Dest": "empty",
                    "Referer": "https://app.rask.ai/",
                    "Accept-Language": "es-ES,es;q=0.9,en;q=0.8",
                    "Accept-Encoding": "gzip, deflate"
                }

                response_account = requests.delete(url_account, headers=headers_account)
                
                if response_account.status_code == 204:
                    print("🗑️ Account successfully deleted.")
                else:
                    print(f"❌ Failed to delete account. Status code: {response_account.status_code}")
            else:
                print("❌ Failed to delete user: Unexpected response.")
        except ValueError:
            print("⚠️ Response is not in valid JSON format.")
    else:
        print(f"⚠️ Failed to delete user. Status code: {response_user.status_code}")





def delete_project(token, project_id):
    url = "https://app.rask.ai/api/project"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Host": "app.rask.ai",
        "Connection": "keep-alive",
        "sec-ch-ua-platform": "Windows",
        "sec-ch-ua": "Not(A:Brand;v=99, Google Chrome;v=133, Chromium;v=133)",
        "sec-ch-ua-mobile": "?0",
        "baggage": "sentry-environment=prod,sentry-public_key=1641776a99d5fee8b3dca472f43779e2,sentry-trace_id=b7271bedf78a485a8e49bfad31bb9e88",
        "sentry-trace": "b7271bedf78a485a8e49bfad31bb9e88-84c14eee7021b12f",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
        "Origin": "https://app.rask.ai",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://app.rask.ai/",
        "Accept-Language": "es-ES,es;q=0.9,en;q=0.8",
        "Accept-Encoding": "gzip, deflate"
    }
    data = {"project_ids": [project_id]}
    
    response = requests.delete(url, headers=headers, json=data)
    
    if response.status_code == 200 and response.json().get("ok") == True:
        return "Response is valid"
    else:
        return "Response is invalid"



def obtener_lista_audios(ruta_carpeta):
    """
    Obtiene una lista ordenada de archivos de audio en la carpeta.
    
    :param ruta_carpeta: Ruta donde están los archivos de audio.
    :return: Lista ordenada de nombres de archivo.
    """
    patron = re.compile(r"segmento_(\d+)\.mp3")
    archivos = sorted(
        [f for f in os.listdir(ruta_carpeta) if f.endswith(".mp3")],
        key=lambda x: int(patron.search(x).group(1)) if patron.search(x) else float('inf')
    )
    return archivos



def obtener_lista_audios2(ruta_carpeta):
    """
    Obtiene la lista de archivos MP3 ordenados numéricamente.
    """
    return sorted([f for f in os.listdir(ruta_carpeta) if f.endswith(".mp3")])

def unir_audios(ruta_carpeta, nombre_salida="audio_final.mp3"):
    """
    Une archivos de audio en formato MP3 dentro de una carpeta, 
    siguiendo su numeración en el nombre del archivo, y luego comprime los MP3 en un ZIP.

    :param ruta_carpeta: Ruta donde están los archivos de audio.
    :param nombre_salida: Nombre del archivo final de salida.
    """
    archivos = obtener_lista_audios2(ruta_carpeta)

    if not archivos:
        print("⚠️ No MP3 files found in the folder.")
        return

    audio_final = AudioSegment.empty()
    for archivo in archivos:
        segmento = AudioSegment.from_mp3(os.path.join(ruta_carpeta, archivo))
        audio_final += segmento

    ruta_salida = os.path.join(ruta_carpeta, nombre_salida)
    audio_final.export(ruta_salida, format="mp3")
    print("🔊 Final audio created successfully!")

    # Comprimir archivos MP3 en un ZIP
    zip_output = "/content/output_final.zip"
    comprimir_archivos_mp3(ruta_carpeta, zip_output)

def comprimir_archivos_mp3(ruta_carpeta, zip_output):
    """
    Comprime todos los archivos MP3 de una carpeta en un archivo ZIP.

    :param ruta_carpeta: Carpeta donde están los archivos MP3.
    :param zip_output: Ruta de salida del archivo ZIP.
    """
    with zipfile.ZipFile(zip_output, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for archivo in os.listdir(ruta_carpeta):
            if archivo.endswith(".mp3"):
                archivo_path = os.path.join(ruta_carpeta, archivo)
                zipf.write(archivo_path, os.path.basename(archivo_path))  # Añadir solo archivos, sin subcarpetas

    print("📦 MP3 files compressed successfully in the ZIP file.")


def imprimir_primer_audio(ruta_carpeta):
    """
    Imprime el nombre del primer archivo de audio siguiendo la secuencia numérica.

    :param ruta_carpeta: Ruta donde están los archivos de audio.
    """
    archivos = obtener_lista_audios(ruta_carpeta)

    if archivos:
        print(f"📂 First audio file in sequence: {archivos[0]}")
        return archivos[0]
    else:
        print("⚠️ No MP3 files found in the folder.")
        return "Process Complete"

# 📂 Llamar a las funciones
def eliminar_archivo(ruta_archivo):
    """Elimina un archivo si existe."""
    if os.path.exists(ruta_archivo):
        os.remove(ruta_archivo)
        print("🗑️ File deleted successfully.")
    else:
        print("⚠️ The specified file does not exist.")


def get_user_data(token):
    url = "https://app.rask.ai/api/user"
    headers = {
        "Host": "app.rask.ai",
        "Connection": "keep-alive",
        "sec-ch-ua-platform": "Windows",
        "Authorization": f"Bearer {token}",
        "sec-ch-ua": '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
        "sec-ch-ua-mobile": "?0",
        "baggage": "sentry-environment=prod,sentry-public_key=1641776a99d5fee8b3dca472f43779e2,sentry-trace_id=3a89da0d6fc247e6b4d6bcdb2c70cb53",
        "sentry-trace": "3a89da0d6fc247e6b4d6bcdb2c70cb53-b0feeac35154b06a",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://app.rask.ai/",
        "Accept-Language": "es-ES,es;q=0.9,en;q=0.8",
        "Accept-Encoding": "gzip, deflate"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        credits = data.get("credits", {})
        total_minutes = credits.get("minutes", {}).get("total", 0)
        used_minutes = credits.get("minutes", {}).get("used", 0)
        total_video = credits.get("video", {}).get("total", 0)
        used_video = credits.get("video", {}).get("used", 0)
        
        if used_minutes > total_minutes:
            return {"error": "Invalid data: Used minutes cannot be greater than total minutes"}
        
        return data, total_minutes, used_minutes, total_video, used_video
    else:
        return {"error": f"Request failed with status code {response.status_code}", "details": response.text}


def descargar_y_convertir0(url, nombre_mp3="audio.mp3"):
    """
    Descarga un archivo WAV desde una URL, lo convierte a MP3 y lo elimina después de la conversión.
    
    Parámetros:
    - url (str): URL del archivo WAV.
    - nombre_mp3 (str): Nombre del archivo MP3 resultante (debe incluir .mp3).
    """

    # Definir el nombre del archivo WAV temporal
    nombre_wav = "archivo.wav"

    # Descargar el archivo WAV
    os.system(f'wget -O {nombre_wav} "{url}"')

    # Instalar FFmpeg si no está instalado
    os.system("apt-get install ffmpeg -y")

    # Convertir WAV a MP3
    os.system(f'ffmpeg -i {nombre_wav} -vn -ar 44100 -ac 2 -b:a 192k {nombre_mp3}')

    # Eliminar el archivo WAV original
    os.remove(nombre_wav)

    # Ejemplo de uso (cambia el token y project_ids según necesites)
    id_token = os.environ.get("ID_TOKEN")
    project_ids = os.environ.get("PROJECT_ID")
    validation = delete_project(id_token, project_ids)
    #print(f"Validation: {validation}")


def descargar_y_convertir(url, nombre_mp3="audio.mp3"):
    """
    Descarga un archivo WAV desde una URL, lo convierte a MP3 y lo elimina después de la conversión.

    Parámetros:
    - url (str): URL del archivo WAV.
    - nombre_mp3 (str): Nombre del archivo MP3 resultante (debe incluir .mp3).
    """
    
    # Definir el nombre del archivo WAV temporal
    nombre_wav = "archivo.wav"

    print(f"⏳ Downloading file from...")
    
    # Descargar el archivo WAV
    os.system(f'wget -O {nombre_wav} "{url}"')

    # Instalar FFmpeg si no está instalado
    os.system("apt-get install ffmpeg -y")

    print("🎵 Converting WAV file to MP3...")

    # Convertir WAV a MP3
    os.system(f'ffmpeg -y -i {nombre_wav} -vn -ar 44100 -ac 2 -b:a 192k "{nombre_mp3}"')

    # Verificar que el MP3 se creó correctamente antes de eliminar el WAV
    if os.path.exists(nombre_mp3):
        print(f"🔊 Conversion successful: {nombre_mp3} created.")
        os.remove(nombre_wav)
        # Ejemplo de uso (cambia el token y project_ids según necesites)
        id_token = os.environ.get("ID_TOKEN")
        project_ids = os.environ.get("PROJECT_ID")
        validation = delete_project(id_token, project_ids)
        print("🗑️ WAV file deleted.")
    else:
        print(f"❌ Error: MP3 file was not generated, WAV file will not be deleted.")


def get_project_info(token, project_id, name):
    contador_segundos = 0
    url = f"https://app.rask.ai/api/project/{project_id}"

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
        "Referer": f"https://app.rask.ai/project/{project_id}",
        "Accept-Language": "es-ES,es;q=0.9",
        "Accept-Encoding": "gzip, deflate",
    }

    while True:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            project_data = response.json()
            translated_video = project_data.get('translated_video', None)

            if translated_video:
                ruta = "/content/output"
                os.makedirs(ruta, exist_ok=True)  # Crea la carpeta si no existe
                
                mp3_file = f"/content/output/{name}.mp3"
                video_url = f"https://app.rask.ai{translated_video}"

                print("\n🎬 Video found. Proceeding with download and conversion...")
                descargar_y_convertir(video_url, mp3_file)

                return
            else:
                contador_segundos += 10
                minutos = contador_segundos // 60
                segundos = contador_segundos % 60
                print(f"\r⏱️ Processing... Time elapsed: {minutos} minutes and {segundos} seconds", end='', flush=True)
        else:
           print(f"❌ Error: Request failed with status code {response.status_code} and the following message: {response.text}")
           return

        time.sleep(10)


def get_project_info0(token, project_id, name):
    contador_segundos = 0
    url = f"https://app.rask.ai/api/project/{project_id}"

    # Headers necesarios para la solicitud
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
        "Referer": f"https://app.rask.ai/project/{project_id}",
        "Accept-Language": "es-ES,es;q=0.9",
        "Accept-Encoding": "gzip, deflate",
    }

    while True:
        # Realizamos la solicitud GET
        response = requests.get(url, headers=headers)

        # Verificamos el status de la respuesta
        if response.status_code == 200:
            # Convertimos la respuesta en formato JSON
            project_data = response.json()

            # Extraemos el valor de translated_video
            translated_video = project_data.get('translated_video', None)

            if translated_video:
                # Si encontramos el video, retornamos la URL completa
                ruta = "/content/output"
                os.makedirs(ruta, exist_ok=True)  # Crea la carpeta si no existe
                descargar_y_convertir(f"https://app.rask.ai{translated_video}", f"/content/output/{name}.mp3")

                return f"\nhttps://app.rask.ai{translated_video}"
            else:
                #print("Video aún no disponible, esperando 10 segundos...")
                contador_segundos += 10
                # Calcular minutos y segundos
                minutos = contador_segundos // 60
                segundos = contador_segundos % 60

                # Imprimir el resultado
                print(f"\r⏱️ Processing... Time elapsed: {minutos} minutes and {segundos} seconds", end='', flush=True)
        else:
            return f"Error {response.status_code}: {response.text}"  # En caso de error, retornamos el mensaje

        # Esperamos 10 segundos antes de realizar otro intento
        time.sleep(10)




def post_request(token, name, dst_lang, num_speakers, src_lang, video_id):
    url = "https://app.rask.ai/api/project/"

    # Datos para el body de la solicitud (editable)
    data = {
        "name": name,
        "dst_lang": dst_lang,
        "free_dubbing": False,
        "num_speakers": num_speakers,
        "src_lang": src_lang,
        "video_id": video_id
    }

    # Headers necesarios para la solicitud
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
        "Origin": "https://app.rask.ai",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://app.rask.ai/",
    }

    # Realizamos la solicitud POST
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Verificamos el status de la respuesta
    if response.status_code == 200:
        # Extraemos el ID de la respuesta JSON
        response_data = response.json()
        project_id = response_data.get('id')  # Obtenemos el 'id' del JSON
        return project_id  # Devolvemos el ID
    else:
        print(f"❌ Error: Request failed with status code {response.status_code} and message: {response.text}")
        return




def upload_audio(file_path, token):
    url = "https://rst.rask.ai/api/library/v1/media"
    headers = {
        "Authorization": f"Bearer {token}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Origin": "https://app.rask.ai",
        "Referer": "https://app.rask.ai/"
    }

    try:
        with open(file_path, "rb") as file:
            files = {"data": ("1.mp3", file, "audio/mpeg")}

            response = httpx.post(url, headers=headers, files=files, timeout=60)
            response.raise_for_status()
            data = response.json()

            return data.get("id")  # Devuelve solo el ID
    except httpx.ReadTimeout:
        print("⏳ Error: The read operation timed out.")
        return
    except httpx.HTTPStatusError as e:
        print(f"⚠️ HTTP Error: {e.response.status_code}")
        return
    except FileNotFoundError:
        print("⚠️ Error: The file was not found. Please check the file path.")
        return
    except Exception as e:
        print("❌ An unexpected error occurred.")
        return



def upload(dst_lang, num_speakers, src_lang):
    ruta_audio = "/content/audios/"
    audio_name = imprimir_primer_audio(ruta_audio)

    if audio_name == "Process Complete":
        print("✅ Process Complete")
        unir_audios("/content/output/", "/content/mi_audio_final.mp3")
    else:
        print(audio_name)


    id_token = os.environ.get("ID_TOKEN")
    data = get_user_data(id_token)

    if isinstance(data, dict) and "error" in data:
        #print("ERROR:", data["error"])
        strError = data["error"]
        if strError == "Request failed with status code 401":
            post_reg()  # Assuming this function handles registration
            time.sleep(1)
            upload(dst_lang, num_speakers, src_lang)
    else:
      
        data, total_minutes, used_minutes, total_video, used_video = data
        print("▶️ My Channel: https://www.youtube.com/@IA.Sistema.de.Interes")
        print(f"⏱️ Total Minutes: {total_minutes}, Used Minutes: {used_minutes}")
        #print(f"Total Video: {total_video}, Used Video: {used_video}")

        if used_minutes < total_minutes:
            print("✅ Used minutes is less than total minutes available.")
            # Llamada a la función con la ruta de tu archivo y token
            patch_mp3 = f"{ruta_audio}{audio_name}"
            audio_id = upload_audio(patch_mp3, id_token)
            #print(audio_id) #Prints ID

            if audio_id:
                # Ejemplo de uso
                name = os.path.splitext(os.path.basename(patch_mp3))[0]
                #name = "avatar_bucle_videoaudio"
                #dst_lang = "en-us"
                #num_speakers = 10
                #src_lang = "es"
                #video_id = audio_id
                # Llamamos a la función y obtenemos el ID
                project_id = post_request(id_token, name, dst_lang, num_speakers, src_lang, audio_id)
                os.environ["PROJECT_ID"] = project_id
                #print(f"Project ID: {project_id}")
                print(f"🆔 Project ID: xxxxx-xxxxx-xxxxxx-xxxxx")

                if project_id:
                  # Llamamos a la función para obtener el valor de translated_video
                  translated_video_url = get_project_info(id_token, project_id, name)
                  eliminar_archivo(patch_mp3)
                  #print(translated_video_url)

        else:
            # Llamada de ejemplo
            id_token = os.environ.get("ID_TOKEN")
            delete_user_and_account(id_token)
            print(f"⏱️ Total Minutes: {total_minutes}, Used Minutes: {used_minutes}")
            #print(f"Total Video: {total_video}, Used Video: {used_video}")
            post_reg()
            time.sleep(1)
            upload(dst_lang, num_speakers, src_lang)

        #print(f"Total Minutes: {total_minutes}, Used Minutes: {used_minutes}")
        #print(f"Total Video: {total_video}, Used Video: {used_video}")