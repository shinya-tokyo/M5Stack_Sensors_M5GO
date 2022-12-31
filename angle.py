from m5stack import *
from m5ui import *
from uiflow import *
import unit


setScreenColor(0x222222)
angle_0 = unit.get(unit.ANGLE, unit.PORTB)






title0 = M5Title(title="Angle", x=3, fgcolor=0xFFFFFF, bgcolor=0x0000FF)
label0 = M5TextBox(50, 100, "Angle:", lcd.FONT_UNICODE, 0xFFFFFF, rotate=0)
label1 = M5TextBox(150, 100, "label1", lcd.FONT_UNICODE, 0xFFFFFF, rotate=0)


while True:
  label0.setText(str(angle_0.read()))
  wait_ms(2)