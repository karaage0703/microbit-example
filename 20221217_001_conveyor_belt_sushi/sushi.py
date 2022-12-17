x = 0

def on_forever():
    global x
    x = 0
    while x < 180:
        pins.servo_write_pin(AnalogPin.P0, x)
        basic.pause(100)
        x += 5
basic.forever(on_forever)
