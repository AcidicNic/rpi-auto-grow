import sys
import Adafruit_DHT
from datetime import datetime
from time import sleep
    
def getTime():
    return datetime.now().strftime("%H:%M:%S")

def getHumidTemp(pin):
    humidity, temperatureC = Adafruit_DHT.read_retry(11, pin)
    return humidity, (temperatureC * 9/5) + 32

def increaseFAE():
    print("\tINCREASE FAE\n")
    return True

def decreaseFAE():
    print("\tDECREASE FAE\n")
    return True

def mist():
    print("\tMIST\n")
    return True

def increaseTemp():
    print("\tINCREASE TEMP\n")
    return True

def decreaseTemp():
    print("\tDECREASE TEMP\n")
    return True

def checkTemp(temp):
    # returns 1 if the temp was successfully lowered/raised
    # returns 0 if the temp is in a good range
    # returns None if an error occured
    if temp > 76:
        if decreaseTemp():
            return 1
    elif temp < 70:
        if increaseTemp():
            return 1
    else:
        return 0

def checkRH(rh):
    # returns 1 if the RH was successfully lowered/raised
    # returns 0 if the RH is in a good range
    # returns None if an error occured
    if rh > 99:
        if increaseFAE():
            return 1
    elif rh < 90:
        if mist():
            return 1
    elif rh < 95:
        if decreaseFAE():
            return 1
    else:
        return 0
    return None
    
def main():
    while True:        
        humidity, temperature = getHumidTemp(4)
        print(f"Time: {getTime()}")
        print(f"Temp: {temperature}°F")
        print(f"Humidity: {humidity}%\n")
        
        t = checkTemp(temperature)
        if t:
            if t == 0:
                print("temp good")
        else:
            print("error changing temp")
           
        h = checkRH(humidity)
        if h:
            if h == 0:
                print("RH good")
        else:
            print("error changing RH")
        
        
        sleep(5)

main()
