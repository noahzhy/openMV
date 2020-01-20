# openMV
A repository for the 2nd production of fall detection

## Notes for openMV learning
### 常用的 model
```python
import sensor, image, time, lcd
```

### 重置传感器
```python
lcd.init(freq=15000000)
sensor.reset()
```

### 色彩模式
```python
# RGB565 彩色模式
sensor.set_pixformat(sensor.RGB565)
# 灰度图模式
sensor.set_pixformat (sensor.GRAYSCALE)
```

### 图像尺寸
```python
# frames size QVGA (320x240)
sensor.set_framesize(sensor.QVGA)
```

### 传感器参数设定
```python
# 白平衡关闭
sensor.set_auto_whitebal(False)
# 自动增益关闭
sensor.set_auto_gain(False)
```

### 等待设置生效
```python
# Wait for settings take effect
sensor.skip_frames(time = 2000)
```

### 显示 FPS
```python
# Create a clock object to track the FPS
clock = time.clock()
```

### 色阶的阈值
```python
# 图像进行差值运算后，不同部分色阶的阈值
GRAYSCALE_thresholds = (20, 255)
```