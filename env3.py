from m5stack import *
from m5ui import *
from uiflow import *
import unit


setScreenColor(0xffc200)
env3_0 = unit.get(unit.ENV3, unit.PORTA)






title0 = M5Title(title="ENV III. Sensor", x=3, fgcolor=0xFFFFFF, bgcolor=0x0000FF)
label0 = M5TextBox(20, 50, "Press.", lcd.FONT_UNICODE, 0x0000ff, rotate=0)
label1 = M5TextBox(20, 100, "Temp.", lcd.FONT_UNICODE, 0xff0000, rotate=0)
label2 = M5TextBox(20, 150, "Humid.", lcd.FONT_UNICODE, 0x00ff00, rotate=0)
label3 = M5TextBox(120, 50, "label3", lcd.FONT_DejaVu24, 0xFFFFFF, rotate=0)
label4 = M5TextBox(120, 100, "label4", lcd.FONT_DejaVu24, 0xFFFFFF, rotate=0)
label5 = M5TextBox(120, 150, "label5", lcd.FONT_DejaVu24, 0xFFFFFF, rotate=0)
label6 = M5TextBox(250, 50, "Pa", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label7 = M5TextBox(250, 100, "*C", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label8 = M5TextBox(250, 150, "%", lcd.FONT_Default, 0xFFFFFF, rotate=0)


while True:
  label3.setText(str(env3_0.pressure))
  label4.setText(str(env3_0.temperature))
  label5.setText(str(env3_0.humidity))
  wait_ms(2)