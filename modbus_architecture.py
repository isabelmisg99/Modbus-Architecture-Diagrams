# Función simple para calcular el CRC de Modbus
def calcular_crc(datos):
    crc = 0xFFFF
    for pos in datos:
        crc ^= pos
        for i in range(8):
            if (crc & 1) != 0:
                crc >>= 1
                crc ^= 0xA001
            else:
                crc >>= 1
    return crc

# Probamos con tu trama del diagrama: [01] [03] [00] [6B] [00] [01]
trama = [0x01, 0x03, 0x00, 0x6B, 0x00, 0x01]
resultado = calcular_crc(trama)

print(f"El CRC para tu diagrama es: {hex(resultado)}")