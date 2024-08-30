def doSpinRight(num: number, num2: number):
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.PINK)
    music.play(music.tone_playable(262, music.beat(BeatFraction.SIXTEENTH)),
        music.PlaybackMode.IN_BACKGROUND)
    DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CW, num)
    DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CCW, num)
    basic.pause(num2)
    music.play(music.tone_playable(262, music.beat(BeatFraction.SIXTEENTH)),
        music.PlaybackMode.IN_BACKGROUND)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBA, Color.OFF)
def doDriveForward(num3: number, num22: number):
    music._play_default_background(music.built_in_playable_melody(Melodies.JUMP_UP),
        music.PlaybackMode.IN_BACKGROUND)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBA, Color.GREEN)
    DFRobotMaqueenPlus.motot_run(Motors.ALL, Dir.CW, num3)
    basic.pause(num22)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBA, Color.OFF)

def on_button_pressed_a():
    music._play_default_background(music.built_in_playable_melody(Melodies.POWER_UP),
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
    DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CW, num4)
    basic.pause(num23)
    music.play(music.tone_playable(147, music.beat(BeatFraction.SIXTEENTH)),
        music.PlaybackMode.IN_BACKGROUND)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBA, Color.OFF)

def on_logo_pressed():
    DFRobotMaqueenPlus.servo_run(Servos.S1, 45)
    music.play(music.tone_playable(220, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.IN_BACKGROUND)
    doDriveForward(50, 1500)
    DFRobotMaqueenPlus.motot_stop(Motors.ALL)
    music.play(music.tone_playable(440, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.IN_BACKGROUND)
    doSpinLeft(75, 1000)
    DFRobotMaqueenPlus.motot_stop(Motors.ALL)
    music.play(music.tone_playable(880, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    doDriveBackward(60, 1500)
    DFRobotMaqueenPlus.motot_stop(Motors.ALL)
    music.play(music.tone_playable(698, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    doSpinRight(75, 2000)
    DFRobotMaqueenPlus.motot_stop(Motors.ALL)
    music.play(music.tone_playable(349, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.IN_BACKGROUND)
    doDriveForward(100, 2500)
    music._play_default_background(music.built_in_playable_melody(Melodies.BLUES),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
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
music.set_volume(60)

def on_in_background():
    DFRobotMaqueenPlus.i2c_init()
    while True:
        if 15 > DFRobotMaqueenPlus.ultra_sonic(PIN.P1, PIN.P2):
            music.play(music.tone_playable(880, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.UNTIL_DONE)
            doDriveBackward(100, 1000)
            DFRobotMaqueenPlus.motot_stop(Motors.ALL)
            doSpinRight(50, 500)
            DFRobotMaqueenPlus.motot_stop(Motors.ALL)
        else:
            basic.pause(100)
control.in_background(on_in_background)
