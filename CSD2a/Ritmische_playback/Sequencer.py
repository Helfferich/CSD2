import simpleaudio as sa, time, pathlib, os
proj_folder = pathlib.Path(f'{__file__}').parent

a=int(input ("Hoevaak?"))
BPM=int(input("BPM:"))
MS=float(60000/BPM)
S=MS/1000
sequence=[]
sound=[]

for x in range(0, a):
    note= (S*float(input("note:")))
    sound= input("sound:")
    sequence.append({"note": note, "sound": sound})
    
while True:
    for t in sequence:
        print(t)
        wave_obj = sa.WaveObject.from_wave_file(str(f'{proj_folder}/media/{t["sound"]}.wav'))
        play_obj = wave_obj.play()
        time.sleep(t["note"])
