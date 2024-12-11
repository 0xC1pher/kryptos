<div align="center">
  <h2 align="center">KRYPTOS</h2>

  <p align="center">
    Herramienta DDoS (<b> por 0X4171341 </b>)
    <br />
    <br />
    <a href="https://github.com/RetrO-M/TorNet/issues">⚠️ Reportar Error</a>
  </p>
</div>

## ❗ Descargo de responsabilidad

- **Propósitos Educativos Únicamente**
  - No ataquen sitios web a los que no tienen permiso, ya que hacerlo sería ilegal. Cree su propio sitio web y haga lo que quiera con él. No nos hacemos responsables de sus estupideces.
  - Este script ha sido desarrollado con un propósito estrictamente legítimo para ayudar a los profesionales de la ciberseguridad y las fuerzas del orden a probar la resistencia y robustez de los sistemas informáticos. Es una herramienta de prueba de carga diseñada para evaluar la capacidad de un servidor o infraestructura de red para soportar grandes cantidades de tráfico de datos.

  - Esta herramienta no está destinada a ser utilizada para ataques maliciosos, como ataques DDoS, o cualquier otra forma de ciberataques que violen la ley. Su uso está reservado exclusivamente para pruebas autorizadas por los propietarios del sistema, con el consentimiento explícito de las autoridades competentes.

  - **IMPORTANTE**: Este proyecto está destinado únicamente a fines legítimos y solo debe ser utilizado con la debida autorización. Cualquier uso contrario a estas pautas está estrictamente prohibido. Como creador de esta herramienta, no asumo ninguna responsabilidad por el mal uso del script fuera de los parámetros legales y éticos aquí descritos.

  - Violar las leyes de ciberseguridad puede resultar en graves sanciones penales, incluidas fuertes multas y prisión.

  - El uso de esta herramienta siempre debe ir precedido de una evaluación de los posibles impactos y un proceso de planificación exhaustivo para evitar cualquier interrupción no deseada de servicios esenciales.

## ⚙️ Instalación

* **Linux-py**: `sudo apt install python3`
* **Win-py**: [Descargar Python](https://www.python.org/downloads/)
* **Inicio-Win**: `python main.py`
* **Inicio-Linux**: `python3 main.py`

### Configuración de TOR en Linux

```shell
root~# sudo apt update
root~# sudo apt install tor
root~# tor --version
root~# tor --hash-password < tu_contraseña >
root~# sudo nano /etc/tor/torrc   
# Desplázate hacia abajo y busca "HashedControlPassword" y "ControlPort 9051" y elimina el "#"
ControlPort 9051
HashedControlPassword < TU_HASH_DE_CONTRASEÑA >
CookieAuthentication 0
root~# sudo systemctl restart tor

**-Anonimato** 
- Sin VPN o TOR

- Sin VPN o TOR, el anonimato será de 70-80%.

- Si usas un PROXY TOR, pero no tienes una VPN

- El anonimato será de 90-95%.

- Si tienes una VPN + PROXY TOR

##El anonimato será de 95-99%.
## Mas funciones 
Ahora incluye 
- pruebas de stress 
- Inyecciones SQL 
- Fuzzing 
- Escaneo de cabeceras 
- Detección de WAF
- Escaneo de puertos y subdominios.
**Los encabezados hacen que el rastreo sea difícil, pero si usas una VPN + TOR, será complejo.**
