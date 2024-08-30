input.onButtonPressed(Button.A, function () {
    music.play(music.tonePlayable(262, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
})
input.onButtonPressed(Button.B, function () {
    DFRobotMaqueenPlus.I2CInit()
    DFRobotMaqueenPlus.servoRun(Servos.S1, 45)
})
basic.showIcon(IconNames.Sad)
