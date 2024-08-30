function doDriveForward (num: number, num2: number) {
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBA, Color.GREEN)
    DFRobotMaqueenPlus.mototRun(Motors.ALL, Dir.CW, num)
    basic.pause(num2)
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBA, Color.OFF)
}
input.onButtonPressed(Button.A, function () {
    music.play(music.tonePlayable(262, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
})
input.onButtonPressed(Button.B, function () {
    DFRobotMaqueenPlus.I2CInit()
    DFRobotMaqueenPlus.servoRun(Servos.S1, 45)
    doDriveForward(50, 100)
    doDriveBackward(35, 150)
})
function doDriveBackward (num: number, num2: number) {
	
}
basic.showIcon(IconNames.Sad)
