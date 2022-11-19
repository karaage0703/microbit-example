radio.set_group(1)

def on_forever():
    radio.send_number(0)
basic.forever(on_forever)
