from m5stack import *
from m5ui import *
from uiflow import *
import unit


setScreenColor(0x222222)
pir_1 = unit.get(unit.PIR, unit.PORTC)






title0 = M5Title(title="PIR", x=3, fgcolor=0xFFFFFF, bgcolor=0x0000FF)
label0 = M5TextBox(50, 100, "PIR Val.", lcd.FONT_UNICODE, 0xFFFFFF, rotate=0)
label1 = M5TextBox(180, 100, "label1", lcd.FONT_UNICODE, 0xFFFFFF, rotate=0)


while True:
  label1.setText(str(pir_1.state))
  wait_ms(2)