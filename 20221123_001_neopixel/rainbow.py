y = 0
x = 180
strip = neopixel.create(DigitalPin.P0, 24, NeoPixelMode.RGB)

def on_forever():
    global x, y
    basic.pause(10)
    x += 1
    y += 1
    strip.show_rainbow(x, y)
    if x > 360:
        x = 0
    if y > 360:
        y = 0
basic.forever(on_forever)
