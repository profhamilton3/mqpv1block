def doSpinRight(num: number, num2: number):
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.PINK)
    music.play(music.tone_playable(262, music.beat(BeatFraction.SIXTEENTH)),
        music.PlaybackMode.IN_BACKGROUND)
    DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CW, num)
    DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CCW, num)
    basic.pause(num2)
    music.play(music.tone_playable(262, music.beat(BeatFraction.SIXTEENTH)),
        music.PlaybackMode.IN_BACKGROUND)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBA, Color.OFF)
def doDriveForward(num3: number, num22: number):
    music._play_default_background(music.built_in_playable_melody(Melodies.DADADADUM),
        music.PlaybackMode.IN_BACKGROUND)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBA, Color.GREEN)
    DFRobotMaqueenPlus.motot_run(Motors.ALL, Dir.CW, num3)
    basic.pause(num22)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBA, Color.OFF)

def on_button_pressed_a():
    music._play_default_background(music.built_in_playable_melody(Melodies.PRELUDE),
        music.PlaybackMode.IN_BACKGROUND)
    DFRobotMaqueenPlus.i2c_init()
    basic.show_icon(IconNames.ANGRY)
    music.play(music.tone_playable(262, music.beat(BeatFraction.DOUBLE)),
        music.PlaybackMode.IN_BACKGROUND)
input.on_button_pressed(Button.A, on_button_pressed_a)

def doSpinLeft(num4: number, num23: number):
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.PINK)
    music.play(music.tone_playable(147, music.beat(BeatFraction.SIXTEENTH)),
        music.PlaybackMode.IN_BACKGROUND)
    DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CCW, num4)
    DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CW, num4)
    basic.pause(num23)
    music.play(music.tone_playable(147, music.beat(BeatFraction.SIXTEENTH)),
        music.PlaybackMode.IN_BACKGROUND)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBA, Color.OFF)

def on_logo_pressed():
    DFRobotMaqueenPlus.servo_run(Servos.S1, 45)
    doDriveForward(50, 1000)
    doSpinLeft(30, 200)
    doDriveBackward(35, 150)
    doSpinRight(30, 200)
    doDriveForward(50, 1000)
    DFRobotMaqueenPlus.motot_stop(Motors.ALL)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBA, Color.RED)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def doDriveBackward(num5: number, num24: number):
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBA, Color.YELLOW)
    music.play(music.tone_playable(262, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    DFRobotMaqueenPlus.motot_run(Motors.ALL, Dir.CCW, num5)
    basic.pause(num24)
    music.play(music.tone_playable(262, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBA, Color.OFF)
basic.show_icon(IconNames.ASLEEP)