def on_gesture_eight_g():
    basic.show_icon(IconNames.SAD)
    basic.show_string("OUCH")
input.on_gesture(Gesture.EIGHT_G, on_gesture_eight_g)

def on_button_pressed_a():
    basic.show_icon(IconNames.HAPPY)
    music.play(music.string_playable("E D G F B A C5 B ", 110),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_icon(IconNames.SILLY)
    music.play(music.string_playable("F D F A E G E F ", 120),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_icon(IconNames.HEART)
    music.play(music.string_playable("E B C5 A B G A F ", 500),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.B, on_button_pressed_b)

led.set_brightness(255)
basic.show_icon(IconNames.ANGRY)
Kitronik_LAMPbit.lamp_light_led(Kitronik_LAMPbit.DisplayLamp.ON)

def on_every_interval():
    for index in range(4):
        basic.show_icon(IconNames.HEART)
        basic.clear_screen()
        basic.show_icon(IconNames.SMALL_HEART)
        basic.clear_screen()
        basic.show_icon(IconNames.HEART)
loops.every_interval(60000, on_every_interval)
b