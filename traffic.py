from gpiozero import LED
from gpiozero import Button
from time import sleep

led1 = LED(2)
led2 = LED(17)
led3 = LED(27)
button1 = Button(22)
button2 = Button(10)
count = 0


while True:
	pos = count % 3
	
	if pos == 0:
		led1.on()
		led2.off()
		led3.off()
		sleep(0.1)
	elif pos == 1:
		led2.on()
		led3.off()
		led1.off()
		sleep(0.1)
	elif pos == 2:
		led3.on()
		led1.off()
		led2.off()
		sleep(0.1)
		
		
	if button1.is_pressed:
		count -= 1
	elif button2.is_pressed:
		count += 1
	print(pos)
		
	
