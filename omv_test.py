import sensor, image, time, lcd

# 重置传感器
lcd.init(freq=15000000)
sensor.reset()
# RGB565 彩色模式
#sensor.set_pixformat(sensor.RGB565)
# 灰度图 模式
sensor.set_pixformat (sensor.GRAYSCALE)
# frames size QVGA (320x240)
sensor.set_framesize(sensor.QVGA)
# Wait for settings take effect
sensor.skip_frames(time = 2000)
# 白平衡关闭
#sensor.set_auto_whitebal(False)
# 自动增益关闭
#sensor.set_auto_gain(False)
# Create a clock object to track the FPS
clock = time.clock()

# 图像进行差值运算后，不同部分色阶的阈值
GRAYSCALE_thresholds = (20, 255)

def main():
    img_pre = sensor.snapshot().copy()
    while(True):
        # Update the FPS clock
        clock.tick()
        # Copy of the image return value
        img = sensor.snapshot().copy()
        img_diff = img.difference(img_pre)
        # 按照给定的阈值，对运算后的图像进行二值化分割
        img_diff.binary([GRAYSCALE_thresholds], invert=0)
        # 侵蚀函数，需要给定噪声大小与颜色的阈值
        #img_diff.erode(1, threshold = 3)
        #img_diff.dilate (1)
        img_pre = sensor.snapshot().copy()
        # Display on LCD
        lcd.display(img_diff)
        # Note: MaixPy's Cam runs about half as fast when connected
        print(clock.fps())


if __name__ == "__main__":
    main()
