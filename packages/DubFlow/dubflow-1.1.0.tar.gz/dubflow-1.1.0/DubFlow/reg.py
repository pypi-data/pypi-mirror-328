import re
import requests
import random
import string
from bs4 import BeautifulSoup
import time
import os

def send_survey_request(token):
    url = "https://app.rask.ai/api/survey/add"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "Connection": "keep-alive",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-ch-ua": "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\", \"Google Chrome\";v=\"132\"",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
        "Origin": "https://app.rask.ai",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://app.rask.ai/",
        "Accept-Language": "es-ES,es;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "baggage": "sentry-environment=prod,sentry-public_key=1641776a99d5fee8b3dca472f43779e2,sentry-trace_id=1dbf9db5dad3406e970d2b72bb6f5b88",
        "sentry-trace": "1dbf9db5dad3406e970d2b72bb6f5b88-afa614d014270a5e"
    }

    lista1 = ["Podcasts and interviews", "Videos for my blog", "Content for TV / Media", "Educational content", "Marketing videos"]
    lista2 = ["Google Search", "X (ex-Twitter)", "Google Ads", "YouTube", "Facebook Ads", "LinkedIn", "Influencer's post", "TikTok", "Recommended by a friend", "Instagram"]
    lista3 = ["E-learning specialist", "Blogger / Influencer", "Marketer", "Video Production Manager", "Product Manager", "Founder / CEO"]

    data = {
        "id": "2",
        "name": "welcome_survey",
        "survey_data": {
            "content": {"option": random.choice(lista1), "text": ""},
            "referral": {"option": random.choice(lista2), "text": ""},
            "role": {"option": random.choice(lista3), "text": ""}
        }
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200 and response.json().get("ok"):
        print("✅ Request processed successfully.")
    else:
        print("❌ Request error.")

    return response.json()

def crear_usuario(token, referral_id=""):
    url = "https://app.rask.ai/api/user"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "Connection": "keep-alive",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-ch-ua": "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\", \"Google Chrome\";v=\"132\"",
        "sec-ch-ua-mobile": "?0",
        "baggage": "sentry-environment=prod,sentry-public_key=1641776a99d5fee8b3dca472f43779e2,sentry-trace_id=e2d13eea7c6244bd8acbfaf079be6663",
        "sentry-trace": "e2d13eea7c6244bd8acbfaf079be6663-a959feb05df889f4",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
        "Origin": "https://app.rask.ai",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://app.rask.ai/",
        "Accept-Language": "es-ES,es;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Cookie": "_vwo_uuid_v2=DEBE4BE5220FE9A68F4F9B4E205A52774|b7dd40c24513b4455370261e2d68f989; _fbp=fb.1.1739574703077.504302293496816923; _gcl_au=1.1.761700255.1739574706; _ga=GA1.1.1566320454.1739574706; mp_5e9337f33eed61106f339f11b62ec3c3_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A19506bb6c7491f-0c8c5284ed42cd-26011b51-1fa400-19506bb6c7491f%22%2C%22%24device_id%22%3A%20%2219506bb6c7491f-0c8c5284ed42cd-26011b51-1fa400-19506bb6c7491f%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%2C%22deviceType%22%3A%20%22desktop%22%7D; __hstc=169233214.ed9f97f00e3e53d2a1bbe769c039f92c.1739574710101.1739574710101.1739574710101.1; hubspotutk=ed9f97f00e3e53d2a1bbe769c039f92c; __hssrc=1; __hssc=169233214.1.1739574710101; _ga_R60NZTEKKL=GS1.1.1739574704.1.1.1739574710.54.0.1084220573"
    }

    payload = {"referral_id": referral_id}

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)

        if response.status_code in [200, 201]:
            print("✅ User created successfully.")
        else:
            print(f"❌ Error creating user.")
    except requests.RequestException as e:
        print(f"⚠️ Request error.")

def create_user(email, token):
    url = "https://rst.rask.ai/api/accounts/v1/users"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
        "sec-ch-ua-platform": "Windows",
        "sec-ch-ua": "Not A(Brand;v=8, Chromium;v=132, Google Chrome;v=132",
        "sec-ch-ua-mobile": "?0",
        "Origin": "https://app.rask.ai",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://app.rask.ai/",
        "Accept-Language": "es-ES,es;q=0.9,en;q=0.8",
        "Accept-Encoding": "gzip, deflate"
    }
    payload = {
        "email": email,
        "referral_id": "",
        "token": token
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        user_id = data.get("id")
        user_email = data.get("email")
        cognito_id = data.get("cognito_id")
        
        return user_id, user_email, cognito_id
    else:
        print("❌ Error creating user account.")
        return None, None, None

def autenticar_usuario(client_id, username, password):
    url = "https://cognito-idp.us-east-2.amazonaws.com/"
    headers = {
        "Host": "cognito-idp.us-east-2.amazonaws.com",
        "Connection": "keep-alive",
        "X-Amz-User-Agent": "aws-amplify/5.0.4 auth framework/1",
        "sec-ch-ua-platform": "\"Windows\"",
        "Cache-Control": "no-store",
        "sec-ch-ua": "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\", \"Google Chrome\";v=\"132\"",
        "sec-ch-ua-mobile": "?0",
        "X-Amz-Target": "AWSCognitoIdentityProviderService.InitiateAuth",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
        "Content-Type": "application/x-amz-json-1.1",
        "Accept": "*/*",
        "Origin": "https://app.rask.ai",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://app.rask.ai/",
        "Accept-Language": "es-ES,es;q=0.9",
        "Accept-Encoding": "gzip, deflate"
    }

    data = {
        "AuthFlow": "USER_PASSWORD_AUTH",
        "ClientId": client_id,
        "AuthParameters": {
            "USERNAME": username,
            "PASSWORD": password
        },
        "ClientMetadata": {}
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        response_json = response.json()
        auth_result = response_json.get("AuthenticationResult", {})

        access_token = auth_result.get("AccessToken")
        id_token = auth_result.get("IdToken")

        return access_token, id_token
    else:
        print(f"❌ Authentication error.")
        return None, None

def confirmar_registro(client_id, confirmation_code, username):
    url = "https://cognito-idp.us-east-2.amazonaws.com/"
    headers = {
        "Host": "cognito-idp.us-east-2.amazonaws.com",
        "Connection": "keep-alive",
        "X-Amz-User-Agent": "aws-amplify/5.0.4 auth framework/1",
        "sec-ch-ua-platform": "\"Windows\"",
        "Cache-Control": "no-store",
        "sec-ch-ua": "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\", \"Google Chrome\";v=\"132\"",
        "sec-ch-ua-mobile": "?0",
        "X-Amz-Target": "AWSCognitoIdentityProviderService.ConfirmSignUp",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
        "Content-Type": "application/x-amz-json-1.1",
        "Accept": "*/*",
        "Origin": "https://app.rask.ai",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://app.rask.ai/",
        "Accept-Language": "es-ES,es;q=0.9",
        "Accept-Encoding": "gzip, deflate"
    }

    data = { 
        "ClientId": client_id,
        "ConfirmationCode": confirmation_code,
        "Username": username,
        "ForceAliasCreation": True
    }

    response = requests.post(url, headers=headers, json=data)

    return response.status_code, response.text

def enviar_solicitud_signup(username, password, email):
    url = "https://cognito-idp.us-east-2.amazonaws.com/"

    headers = {
        "Host": "cognito-idp.us-east-2.amazonaws.com",
        "Connection": "keep-alive",
        "X-Amz-User-Agent": "aws-amplify/5.0.4 auth framework/1",
        "sec-ch-ua-platform": "Windows",
        "Cache-Control": "no-store",
        "sec-ch-ua": '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
        "sec-ch-ua-mobile": "?0",
        "X-Amz-Target": "AWSCognitoIdentityProviderService.SignUp",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
        "Content-Type": "application/x-amz-json-1.1",
        "Accept": "*/*",
        "Origin": "https://app.rask.ai",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://app.rask.ai/",
        "Accept-Language": "es-ES,es;q=0.9",
        "Accept-Encoding": "gzip, deflate"
    }

    payload = {
        "ClientId": "3l205dqshftlhc51jbgppfe68n",
        "Username": username,
        "Password": password,
        "UserAttributes": [
            {
                "Name": "email",
                "Value": email
            }
        ],
        "ValidationData": None
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        return response.json()
    except Exception as e:
        return None

def extraer_codigo(html):
    soup = BeautifulSoup(html, "html.parser")
    
    codigo_tag = soup.find("p", style="margin: 30px 0; font-size: 24px")
    if codigo_tag:
        return codigo_tag.text.strip()
    
    codigo_match = re.search(r"\b\d{6}\b", soup.get_text())
    if codigo_match:
        return codigo_match.group()
    
    return None

def generar_nombre_completo():
    nombres = ["Juan", "Pedro", "Maria", "Ana", "Luis", "Sofia", "Diego", "Laura", "Javier", "Isabel",
               "Pablo", "Marta", "David", "Elena", "Sergio", "Irene", "Daniel", "Alicia", "Carlos", "Sandra",
               "Antonio", "Lucia", "Miguel", "Sara", "Jose", "Cristina", "Alberto", "Blanca", "Alejandro", "Marta",
               "Francisco", "Esther", "Roberto", "Silvia", "Manuel", "Patricia", "Marcos", "Victoria", "Fernando", "Rosa",
               "James", "John", "Robert", "Michael", "William", "David", "Richard", "Joseph", "Charles", "Thomas",
               "Christopher", "Daniel", "Matthew", "Anthony", "Mark", "Donald", "Steven", "Paul", "Andrew", "Joshua",
               "Kenneth", "Kevin", "Brian", "George", "Edward", "Ronald", "Timothy", "Jason", "Jeffrey", "Ryan",
               "Jacob", "Gary", "Nicholas", "Eric", "Jonathan", "Stephen", "Larry", "Justin", "Scott", "Brandon",
               "Benjamin", "Samuel", "Frank", "Gregory", "Raymond", "Alexander", "Patrick", "Jack", "Dennis", "Jerry",
               "Tyler", "Aaron", "Henry", "Douglas", "Jose", "Peter", "Adam", "Zachary", "Nathan", "Walter", 
               "Kyle", "Harold", "Carl", "Arthur", "Gerald", "Roger", "Keith", "Jeremy", "Terry", "Lawrence",
               "Sean", "Christian", "Ethan", "Austin", "Joe", "Jordan", "Albert", "Jesse", "Willie", "Billy"]

    apellidos = ["Garcia", "Rodriguez", "Gonzalez", "Fernandez", "Lopez", "Martinez", "Sanchez", "Perez", "Alonso", "Diaz",
                 "Martin", "Ruiz", "Hernandez", "Jimenez", "Torres", "Moreno", "Gomez", "Romero", "Alvarez", "Vazquez",
                 "Gil", "Lopez", "Ramirez", "Santos", "Castro", "Suarez", "Munoz", "Gomez", "Gonzalez", "Navarro",
                 "Dominguez", "Lopez", "Rodriguez", "Sanchez", "Perez", "Garcia", "Gonzalez", "Martinez", "Fernandez", "Lopez",
                 "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
                 "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
                 "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
                 "Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
                 "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts",
                 "Gomez", "Phillips", "Evans", "Turner", "Diaz", "Parker", "Cruz", "Edwards", "Collins", "Reyes",
                 "Stewart", "Morris", "Morales", "Murphy", "Cook", "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper",
                 "Peterson", "Bailey", "Reed", "Kelly", "Howard", "Ward", "Cox", "Diaz", "Richardson", "Wood"]

    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)
    numero = random.randint(100, 999)

    nombre_completo = f"{nombre}_{apellido}_{numero}"
    return nombre_completo

def generar_contrasena():
    caracteres = string.ascii_letters + "0123456789" + "#$%&/()@_-*+[]"
    longitud = 10
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def enviar_formulario(url, datos):
    response = requests.post(url, data=datos)
    return response

def extraer_dominios(response_text):
    dominios = re.findall(r'id="([^"]+\.[^"]+)"', response_text)
    return dominios

def obtener_sitio_web_aleatorio(response_text):
    dominios = extraer_dominios(response_text)
    sitio_web_aleatorio = random.choice(dominios)
    return sitio_web_aleatorio

COMMON_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'es-ES,es;q=0.9',
    'Accept-Encoding': 'gzip, deflate'
}

def delete_temp_mail(username_email, dominios_dropdown, extracted_string):
    EMAIL_FAKE_URL = 'https://email-fake.com/'
    url = f"{EMAIL_FAKE_URL}/del_mail.php"

    headers = {
        'Host': 'email-fake.com',
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'Origin': 'https://email-fake.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Accept-Language': 'es-ES,es;q=0.9',
        'Cookie': f'embx=%5B%22{username_email}%40{dominios_dropdown}%22%2C',
    }

    data = f'delll={extracted_string}'

    response = requests.post(url, headers=headers, data=data)

    if "Message deleted successfully" in response.text:
        print("🗑️ Temporary mail deleted...")
        return True
    else:
        print("⚠️ Error deleting temporary email...")
        return False

def get_verification_code(username_email, dominios_dropdown):
    EMAIL_FAKE_URL = 'https://email-fake.com/'
    url = f"{EMAIL_FAKE_URL}/"

    headers = {
        'Host': 'email-fake.com',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        **COMMON_HEADERS,
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Windows',
        'Cookie': f'surl={dominios_dropdown}%2F{username_email}',
    }

    response = requests.get(url, headers=headers)

    verification_code = extraer_codigo(response.text)
    identifier_match = re.search(r'delll:\s*"([a-zA-Z0-9]+)"', response.text)

    if verification_code and identifier_match:
        identifier = identifier_match.group(1)
        return verification_code, identifier
    else:
        return None, None

def post_reg():
    print("⏳ Creating temporary email...")
    password_segura = generar_contrasena()
    url = 'https://email-fake.com/'

    datos = {'campo_correo': 'ejemplo@dominio.com'}
    response = enviar_formulario(url, datos)

    sitio_domain = obtener_sitio_web_aleatorio(response.text)
    nombre_completo = generar_nombre_completo()

    correo = f'{nombre_completo}@{sitio_domain}'
    username = correo
    password = password_segura
    email = correo
    
    print("📝 User registration started...")
    datitos = enviar_solicitud_signup(username, password, email)

    time.sleep(3)

    if 'UserSub' in datitos:
        print("🔐 Waiting for verification code...")
        
        attempts = 6
        for attempt in range(attempts):
            print(f"🔍 Checking verification code... Attempt {attempt + 1}")
            
            verification_code, identifier = get_verification_code(nombre_completo, sitio_domain)

            if verification_code:
                print("🔓 Verification code received.")
                break

        if verification_code:
            print("✅ Confirming registration...")
            time.sleep(3)
            # Ejemplo de uso
            client_id = "3l205dqshftlhc51jbgppfe68n"
            username = correo
            password = password_segura
            status, response_text = confirmar_registro(client_id, verification_code, username)

            if response_text == "{}":
                print("🗑️ Deleting temporary email...")
                delete_temp_mail(nombre_completo, sitio_domain, identifier)

                print("🔐 Authenticating user...")
                access_token, id_token = autenticar_usuario(client_id, username, password)

                if access_token:
                    print("🔓 User authenticated.")
                    os.environ["ACCESS_TOKEN"] = access_token
                    os.environ["ID_TOKEN"] = id_token
                    os.environ["CORREO"] = correo
                    os.environ["CLAVE"] = password_segura

                    # Ejemplo de uso:
                    email = correo
                    token = id_token
                    
                    user_id, user_email, cognito_id = create_user(email, id_token)

                    if user_id:
                        print("✅ User profile created.")
                        crear_usuario(id_token, referral_id="")
                        time.sleep(1)
                        # Uso: Reemplazar 'your_token_here' con el token correspondiente
                        response = send_survey_request(id_token)
                        print("📤 Survey request sent.")
                else:
                    print("❌ Authentication error.")
        else:
            print("🚫 Verification code not received.")
    else:
        print("❌ User registration failed.")
