input.onGesture(Gesture.EightG, function () {
    basic.showIcon(IconNames.Sad)
    basic.showString("OUCH")
})
input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Happy)
    music.play(music.stringPlayable("E D G F B A C5 B ", 110), music.PlaybackMode.UntilDone)
})
input.onButtonPressed(Button.AB, function () {
    basic.showIcon(IconNames.Silly)
    music.play(music.stringPlayable("F D F A E G E F ", 120), music.PlaybackMode.UntilDone)
})
input.onButtonPressed(Button.B, function () {
    basic.showIcon(IconNames.Heart)
    music.play(music.stringPlayable("E B C5 A B G A F ", 500), music.PlaybackMode.UntilDone)
})
led.setBrightness(255)
basic.showIcon(IconNames.Angry)
Kitronik_LAMPbit.lampLightLED(Kitronik_LAMPbit.DisplayLamp.On)
loops.everyInterval(60000, function () {
    for (let index = 0; index < 4; index++) {
        basic.showIcon(IconNames.Heart)
        basic.clearScreen()
        basic.showIcon(IconNames.SmallHeart)
        basic.clearScreen()
        basic.showIcon(IconNames.Heart)
    }
})
