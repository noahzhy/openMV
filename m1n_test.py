import sensor, image, time, lcd

lcd.init(freq=15000000)
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
# 白平衡关闭
#sensor.set_auto_whitebal(False)
# 自动增益关闭
#sensor.set_auto_gain(False)
sensor.skip_frames(time = 2000)
clock = time.clock()

while(True):
    clock.tick()
    img = sensor.snapshot()
    lcd.display(img)
    print(clock.fps())
