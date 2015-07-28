import voice_rec
import goslate
import pywapi

KEYS = 'погода'

def func():
    def getposit(city):
        x = 0
        pos = pywapi.get_location_ids(city)
        for i in pos:
            x += 1
            location_id = i
        result = pywapi.get_weather_from_weather_com(location_id)
        return(result['current_conditions']['temperature'])
    print('city')
    try:
        x= voice_rec.voice()
    except:
        return("don't understand")

    try:
        return(getposit(goslate.Goslate().translate(x, 'en')))
    except :
        return(x, 'not a city')