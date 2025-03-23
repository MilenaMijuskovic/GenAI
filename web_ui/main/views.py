from web_ui.main import bp 
from flask import request, render_template, current_app
from wildfirepredictor import wildFirePredictor
from sheltermanager import shelterManager
from routemanager import routeManager
import random
import serial
import time 

wfp = wildFirePredictor()
sm = shelterManager()
rm = routeManager()
data = [] 

def process_sensorvals(sensorvals): 
    temperature = sensorvals[0]
    pressure = sensorvals[1]
    humidity = sensorvals[2]
    current_app.logger.info(f'Temperature={temperature}, Humidity={humidity}, Pressure={pressure}')
    chanceofwildfire = random.randint(0,1)
    #chanceofwildfire = wfp.predict_wildfire(temp=temperature, RH=humidity, month="aug", day="fri")
    return chanceofwildfire

def generate_map(chanceofwildfire):
    if chanceofwildfire: 
        current_app.logger.info("CHANCE OF WILDFIRE")
        example_origin_latitude = 40.7128  # Example latitude (LA)
        example_origin_longitude = -74.0060  # Example longitude (LA)
        closest_accessible_shelters = sm.get_accessible_shelters(example_origin_latitude, example_origin_longitude)
        closest_accessible_shelter = closest_accessible_shelters[0]["location"]
        origin_coords = [example_origin_latitude, example_origin_longitude]
        destination_coords = [closest_accessible_shelter['lat'], closest_accessible_shelter['lng']]
        rm.generate_html(origin_coords, destination_coords)
    else: 
        current_app.logger.info("NO WILDFIRE")

def readserial(conn, timestamp=False):
    data = conn.readline().decode().strip()
    if data and timestamp:
        timestamp = time.strftime('%H:%M:%S')
        print(f'{timestamp} > {data}')
    elif data:
        print(data)
        data = data.split(',')
        try: 
            temperature = data[0]
            pressure = data[1]
            humidity = data[2]
            return data
        except Exception as e: 
            print(e)
            return False

# @bp.route("/api/sensor", methods=['POST'])
# def refresh_sensor():
#     conn = serial.Serial('COM3', 9600, timeout=0.1)
#     data = False
#     current_app.logger.info('Starting to read sensor data')
#     while data==False or data is None: 
#         data = readserial(conn)

@bp.route("/", methods=['GET', 'POST'])
def index():
    #####comment this part out to run without sensor connected#####
    # conn = serial.Serial('COM3', 9600, timeout=0.1)
    # data = False
    # current_app.logger.info('Starting to read sensor data')
    # while data==False or data is None: 
    #     data = readserial(conn)
    #####comment this part out to run without sensor connected#####


    data = [24.36, 997.98, 30.73]
    chanceofwildfire = process_sensorvals(data)
    generate_map(chanceofwildfire)

    if request.method == 'POST': 
        html = render_template('main/danger.html') if chanceofwildfire else render_template('main/all_good.html')
        return html 
    
    return render_template(
        'main/index.html',
        title='Wildfire Escaper',
        data=data,
        chanceofwildfire=chanceofwildfire, 
    )

@bp.route("/map")  
def map():
    return render_template('main/route_map.html')