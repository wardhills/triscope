# Sensors 



# ADXL345

https://circuitpython.readthedocs.io/projects/adxl34x/

Datasheet: https://www.analog.com/media/en/technical-documentation/data-sheets/ADXL345.pdf

installation 

``` python:

pip3 install adafruit-circuitpython-adxl34x

```

## Example 


```python:

import time
import board
import busio
import adafruit_adxl34x

i2c = busio.I2C(board.SCL, board.SDA)

# For ADXL343
accelerometer = adafruit_adxl34x.ADXL343(i2c)
# For ADXL345
# accelerometer = adafruit_adxl34x.ADXL345(i2c)

accelerometer.enable_motion_detection()
# alternatively you can specify the threshold when you enable motion detection for more control:
# accelerometer.enable_motion_detection(threshold=10)

while True:
    print("%f %f %f" % accelerometer.acceleration)

    print("Motion detected: %s" % accelerometer.events["motion"])
    time.sleep(0.5)
``

Range of sensor


    range

        The measurement range of the sensor.

````python:

class adafruit_adxl34x.DataRate

    An enum-like class representing the possible data rates. Possible values are

        DataRate.RATE_3200_HZ
        DataRate.RATE_1600_HZ
        DataRate.RATE_800_HZ
        DataRate.RATE_400_HZ
        DataRate.RATE_200_HZ
        DataRate.RATE_100_HZ
        DataRate.RATE_50_HZ
        DataRate.RATE_25_HZ
        DataRate.RATE_12_5_HZ
        DataRate.RATE_6_25HZ
        DataRate.RATE_3_13_HZ
        DataRate.RATE_1_56_HZ
        DataRate.RATE_0_78_HZ
        DataRate.RATE_0_39_HZ
        DataRate.RATE_0_20_HZ
        DataRate.RATE_0_10_HZ

class adafruit_adxl34x.Range

    An enum-like class representing the possible measurement ranges in +/- G.

    Possible values are

        Range.RANGE_16_G
        Range.RANGE_8_G
        Range.RANGE_4_G
        Range.RANGE_2_G
```



 
