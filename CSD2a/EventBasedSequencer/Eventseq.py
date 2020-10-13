import simpleaudio as sa, time, pathlib, os
proj_folder = pathlib.Path(f'{__file__}').parent

#input
eventNr=[0]
bpm=120
cbpm=bpm
k=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
s=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
h=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]#INST
def inst(inst, name):
    #IDEE: Lijst input
    #IDEE: Triplets & Dotted
    #IDEE: Timestretch
    #IDEE: Velocity
    #IDEE: Patterns met polyritmiek
    templist=[0]
    count=0
    print("Type stepnumber to toggle")
    print("Startin at 0")
    print("Ender d when done")
    for temp in templist:
        count=count+1
        print(inst)
        step=input(f'{name}'+"step:")   
        count = count % 24
        if (count==10):
            print("TIP: type enorme getaalen voor een soort random")
        try:
            if (step=='d'):
                print("aight")
            else:
                step=int(step)%len(k)
                if (inst[step]==0):
                    inst[step]=1
                else:
                    inst[step]=0
                templist.append(0)
        except:
            print("Je hebt waarschijnlijk woorden getypt")
            templist.append(0)

#INSTPlay
def playloop(inst, name):
    if (inst[(curstep)]==1):
        wave_obj = sa.WaveObject.from_wave_file(str(f'{proj_folder}/media/{name}.wav'))
        play_obj = wave_obj.play()
        
#Interface
print("d+enter to finish")
print("type 'helfferich' for help")
for x in eventNr:
    inp=input("ira.seq:")
    if (inp!='d'):
        eventNr.append(0)
    if (inp=='helfferich'):
#help
        print("k = kick")
        print("s = snare")
        print("h = hihat")
        print("bpm = bpmstatus")
        #IDEE: Samplerate&Bitdepth Menu
#BPM
    if (inp=='bpm'):
        print(f"bpm = {cbpm}")
        try:
            print(f"Type new bpm in numbers or enter to keep {cbpm}:")
            bpm = input("New bpm between 5 and 999:")
            bpm = int(bpm)
            if (bpm>999) or (bpm<10):
                print("invalid")
                bpm = cbpm
                print(f"Enterd without a valid new bpm in numbers so: keeping {cbpm} bpm")
            else:
                print("new bpm=", bpm)
        except:
            bpm = cbpm
            print(f"Enterd without a valid new bpm in numbers so: keeping {cbpm} bpm")
        cbpm=bpm
    if (inp=='k'):
        inst(k, "kick")
    if (inp=='s'):
        inst(s, "snare")
    if (inp=='h'):
        inst(h, "hihat")

#seq
MS=float(60000/bpm)
S=MS/1000
sleeptime=MS/10000

while True:
    for  curstep in range(16):
        playloop(k, 'kick')
        playloop(s, 'snare')
        playloop(h, 'hihat')
        print(curstep)
        time.sleep(sleeptime)

'''a=4
sequence=[]

for x in range(0, a):
    note= x*10
    sound= x
    sequence.append({"note": note, "sound": sound})'''
