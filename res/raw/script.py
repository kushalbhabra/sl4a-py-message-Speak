import android, time
droid = android.Android()
droid.startSensing()
while True:
    result = droid.sensorsGetLight().result
    if result is not None and result <= 10:
        droid.ttsSpeak('I can\'t see!')
    time.sleep(5)
