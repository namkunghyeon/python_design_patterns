from LightSwitch import LightSwitch

if __name__ == "__main__":
    lightSwitch = LightSwitch()
    print "Switch ON test."
    lightSwitch.switch("ON")

    print "Switch OFF test"
    lightSwitch.switch("OFF")

    print "Invalid Command test"
