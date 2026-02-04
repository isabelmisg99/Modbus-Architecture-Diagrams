# Modbus-Architecture-Diagrams
Repositorio con diagramas que explica el flujo de un mensaje desde que el Cliente lo solicita hasta que el Servidor responde.
En este diagrama represento una comunicación Modbus RTU donde el Maestro solicita datos de temperatura a un esclavo usando el código de función 03 (Read Holding Registers).
## 📊 1. Diagrama de Arquitectura (Capa Física)
En este diagrama se representa una topología de bus (Daisy Chain) usando el estándar RS-485.

![Arquitectura Modbus](./Modbus_Architecture_v1.png)

### Detalles Técnicos del Diagrama:
- **Topología:** Bus con resistencia de terminación de 120Ω para evitar reflexión de señal.
- **Dispositivos:** Un Maestro (PLC/PC) y dos Esclavos (Sensores/Actuadores).
- **Protocolo:** Modbus RTU sobre RS-485 (2-wire).

## ⚙️ 2. Ajustes de Comunicación
Para garantizar que todos los nodos se entiendan, se ha definido la siguiente configuración:
- **Baud Rate:** 9600 bps
- **Data Bits:** 8
- **Parity:** None (N)
- **Stop Bits:** 1

## 💻 3. Implementación en Python
He desarrollado un script maestro que automatiza la lectura de registros.

### Simulación de Lectura (CRC incluido)
El script `modbus_master.py` realiza una petición de lectura al **ID 1** para obtener datos de humedad.
La trama generada sigue el formato: `[ID] [Función] [Dirección] [Cantidad] [CRC]`.

```python
# Ejemplo de la trama enviada:
# [01] [03] [006B] [0001] [CRC]
