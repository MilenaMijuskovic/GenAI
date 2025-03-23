from wildfirepredictor import wildFirePredictor
from sheltermanager import shelterManager
from routemanager import routeManager
import random 

temperature = 1
humidity = 2
pressure = 3
gas = 4
chanceofwildfire = 0

# class serialReader: 
#     def __init__(self): 
#         self.prediction = 0 
#         self.ser = serial.Serial('COM3', 9600, timeout=0.1)         # 1/timeout is the frequency at which the port is read
#     def readserial(self, timestamp=False):
#         data = self.ser.readline().decode().strip()
#         if data and timestamp:
#             timestamp = time.strftime('%H:%M:%S')
#             print(f'{timestamp} > {data}')
#         elif data:
#             data = data.split(',')
#             try: 
#                 temperature = data[0]
#                 pressure = data[1]
#                 humidity = data[2]
#                 print(f"Temperature={temperature} degrees Celsius, Pressure={pressure}hPa, Relative Humidity={humidity}%")
#                 return data
#             except: 
#                 return False 
if __name__ == '__main__':
    #sr = serialReader()
    wfp = wildFirePredictor()
    sm = shelterManager()
    rm = routeManager()
    while True: 
        data = sr.readserial()
        if data: 
            temperature = data[0] 
            humidity = data[2]
            prediction = wfp.predict_wildfire(temp=temperature, RH=humidity, month="aug", day="fri")
            # lol i'm just using this instead of prediction so we get variation
            chanceofwildfire = random.randint(0,1)
            #print(f"{'Wildfire Likely' if prediction else 'Wildfire unlikely'}")
            if chanceofwildfire: 
                example_origin_latitude = 40.7128  # Example latitude (LA)
                example_origin_longitude = -74.0060  # Example longitude (LA)
                closest_accessible_shelters = sm.get_accessible_shelters(example_origin_latitude, example_origin_longitude)
                closest_accessible_shelter = closest_accessible_shelters[0]["location"]
                origin_coords = [example_origin_latitude, example_origin_longitude]
                destination_coords = [closest_accessible_shelter['lat'], closest_accessible_shelter['lng']]
                rm.generate_html(origin_coords, destination_coords)


#from serialreader import serialReader
#import random
# if __name__ == '__main__':
#     sr = serialReader()
#     wfp = wildFirePredictor()
#     sm = shelterManager()
#     rm = routeManager()
#     while True: 
#         data = sr.readserial()
#         if data: 
#             temperature = data[0] 
#             humidity = data[2]
#             prediction = wfp.predict_wildfire(temp=temperature, RH=humidity, month="aug", day="fri")
#             # lol i'm just using this instead of prediction so we get variation
#             chanceofwildfire = random.randint(0,1)
#             #print(f"{'Wildfire Likely' if prediction else 'Wildfire unlikely'}")
#             if chanceofwildfire: 
#                 example_origin_latitude = 40.7128  # Example latitude (LA)
#                 example_origin_longitude = -74.0060  # Example longitude (LA)
#                 closest_accessible_shelters = sm.get_accessible_shelters(example_origin_latitude, example_origin_longitude)
#                 closest_accessible_shelter = closest_accessible_shelters[0]["location"]
#                 origin_coords = [example_origin_latitude, example_origin_longitude]
#                 destination_coords = [closest_accessible_shelter['lat'], closest_accessible_shelter['lng']]
#                 rm.generate_html(origin_coords, destination_coords)