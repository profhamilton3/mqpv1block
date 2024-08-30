def doDriveForward(num: number, num2: number):
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBA, Color.GREEN)
    DFRobotMaqueenPlus.motot_run(Motors.ALL, Dir.CW, num)
    basic.pause(num2)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBA, Color.OFF)

def on_button_pressed_a():
    music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    DFRobotMaqueenPlus.i2c_init()
    DFRobotMaqueenPlus.servo_run(Servos.S1, 45)
    doDriveForward(50,100)

input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_icon(IconNames.SAD)