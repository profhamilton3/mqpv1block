function doSpinRight (num: number, num2: number) {
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBR, Color.PINK)
    music.play(music.tonePlayable(262, music.beat(BeatFraction.Sixteenth)), music.PlaybackMode.InBackground)
    DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CW, num)
    DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CCW, num)
    basic.pause(num2)
    music.play(music.tonePlayable(262, music.beat(BeatFraction.Sixteenth)), music.PlaybackMode.InBackground)
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBA, Color.OFF)
}
function doDriveForward (num: number, num2: number) {
    music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Dadadadum), music.PlaybackMode.InBackground)
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBA, Color.GREEN)
    DFRobotMaqueenPlus.mototRun(Motors.ALL, Dir.CW, num)
    basic.pause(num2)
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBA, Color.OFF)
}
input.onButtonPressed(Button.A, function () {
    music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Prelude), music.PlaybackMode.InBackground)
    DFRobotMaqueenPlus.I2CInit()
    basic.showIcon(IconNames.Angry)
    music.play(music.tonePlayable(262, music.beat(BeatFraction.Double)), music.PlaybackMode.InBackground)
})
function doSpinLeft (num: number, num2: number) {
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBL, Color.PINK)
    music.play(music.tonePlayable(147, music.beat(BeatFraction.Sixteenth)), music.PlaybackMode.InBackground)
    DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CCW, num)
    DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CW, num)
    basic.pause(num2)
    music.play(music.tonePlayable(147, music.beat(BeatFraction.Sixteenth)), music.PlaybackMode.InBackground)
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBA, Color.OFF)
}
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    DFRobotMaqueenPlus.servoRun(Servos.S1, 45)
    doDriveForward(50, 1000)
    doSpinLeft(30, 200)
    doDriveBackward(35, 150)
    doSpinRight(30, 200)
    doDriveForward(50, 1000)
    DFRobotMaqueenPlus.mototStop(Motors.ALL)
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBA, Color.RED)
})
function doDriveBackward (num: number, num2: number) {
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBA, Color.YELLOW)
    music.play(music.tonePlayable(262, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    DFRobotMaqueenPlus.mototRun(Motors.ALL, Dir.CCW, num)
    basic.pause(num2)
    music.play(music.tonePlayable(262, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBA, Color.OFF)
}
basic.showIcon(IconNames.Asleep)
