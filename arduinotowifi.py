from controllShelly import ShellyPlug
import serial
import private
ser = serial.Serial("COM3")
ser.flushInput()
def main():
    LivingRoomPlug = ShellyPlug("https://shelly-35-eu.shelly.cloud",private.SHELLY_KEY,channel="0",id=private.SHELLY_ID)
    while True:
        ser_bytes=ser.readline()
        decoded_bytes = str(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        print(decoded_bytes)
        if decoded_bytes=="1":
            LivingRoomPlug.TurnOn()
        else:
            LivingRoomPlug.TurnOff()

if __name__ == "__main__":
    main()
    