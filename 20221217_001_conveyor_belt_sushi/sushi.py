def on_button_pressed_a():
    global start_flag
    start_flag = True
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global start_flag
    start_flag = False
input.on_button_pressed(Button.B, on_button_pressed_b)

x = 0
start_flag = False
basic.show_leds("""
    . # . # .
        # # # # #
        # # # # #
        . # # # .
        . . # . .
""")
pins.servo_write_pin(AnalogPin.P0, 0)

def on_forever():
    global x
    while start_flag == True:
        x = 0
        while x < 180:
            pins.servo_write_pin(AnalogPin.P0, x)
            basic.pause(100)
            x += 5
        while x > 0:
            pins.servo_write_pin(AnalogPin.P0, x)
            basic.pause(100)
            x += 0 - 5
basic.forever(on_forever)
