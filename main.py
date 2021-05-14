reading = 0

def on_forever():
    global reading
    reading = input.light_level()
    led.plot_bar_graph(input.light_level(), 255)
basic.forever(on_forever)
