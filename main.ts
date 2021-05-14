let reading = 0
basic.forever(function () {
    reading = input.lightLevel()
    led.plotBarGraph(
    input.lightLevel(),
    255
    )
})
