import datetime
import pytz


timezones = (
    'Asia/Hong_Kong',
    'America/New_York',
    'Europe/London',

)

fmt = '%m-%d %H:%M:%S'

now = datetime.datetime.now()
text = "World Clock\n"

for tz_name in timezones:
    tz = pytz.timezone(tz_name)
    tz_now = now.astimezone(tz)
    output = '{tz_name}:{tz_now_str}'.format(
        tz_name = tz_name.split("/")[1],
        tz_now_str = tz_now.strftime(fmt)
    )

    text = text + output + "\n"

from luma.core.interface.serial import i2c, spi, pcf8574
from luma.core.interface.parallel import bitbang_6800
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1309, ssd1325, ssd1331, sh1106, ws0010
from PIL import ImageFont

serial = i2c(port=1, address=0x3C)

# substitute ssd1331(...) or sh1106(...) below if using that device
device = sh1106(serial)

font1 = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf',8)

while True:
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="white", fill="black")
        draw.text((0, 0), text, fill="white", font=font1)
