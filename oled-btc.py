import datetime
import requests
import pytz
import time

def text():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()

    text = "Bitcoin Price: \n"
    
    text += "BTCUSD: {}\n".format(data['bpi']['USD']['rate'])
    text += "BTCEUR: {}".format(data['bpi']['EUR']['rate'])

    return text

from luma.core.interface.serial import i2c, spi, pcf8574
from luma.core.interface.parallel import bitbang_6800
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1309, ssd1325, ssd1331, sh1106, ws0010

# rev.1 users set port=0
# substitute spi(device=0, port=0) below if using that interface
# substitute bitbang_6800(RS=7, E=8, PINS=[25,24,23,27]) below if using that interface
serial = i2c(port=1, address=0x3C)

# substitute ssd1331(...) or sh1106(...) below if using that device
device = sh1106(serial)

# fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)

while True:
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="white", fill="black")
        draw.text((0, 0), text(), fill="white")
        time.sleep(1)

        
        
