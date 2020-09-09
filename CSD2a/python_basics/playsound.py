import simpleaudio as sa

a=int(input ("Hoevaak?"))

for x in range(0, a):
    wave_obj = sa.WaveObject.from_wave_file("/Users/irahelfferich/School/CSD2/python_basics/playsound.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()
