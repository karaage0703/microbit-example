def on_received_number(receivedNumber):
    if radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH) < -100:
        music.play_melody("F F A B C5 C5 - - ", 60)
    elif radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH) < -80:
        music.play_melody("F F A B C5 C5 - - ", 120)
    elif radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH) < -60:
        music.play_melody("F F A B C5 C5 - - ", 240)
radio.on_received_number(on_received_number)

radio.set_group(1)
