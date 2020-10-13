#—————————————————————————————————————#
                #Import
#—————————————————————————————————————#
import simpleaudio as sa, time, pathlib, os, math, random
proj_folder = pathlib.Path(f'{__file__}').parent

#Input
bpm=120
cbpm=bpm

tijds = 4
eenheid = 4
ts=eenheid*tijds

ctijds = tijds
ceenheid = eenheid
cts = ceenheid*ctijds

k=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
s=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
h=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#—————————————————————————————————————#
                #DEF
#—————————————————————————————————————#
#INST
def inst(inst, name):
    #IDEE: Lijst input
    #IDEE: Triplets & Dotted
    #IDEE: Timestretch
    #IDEE: Velocity
    #IDEE: Patterns met polyritmiek
    templist=[0]
    count=0
    print("Typ het nummer van de stap om de kans daarvan in te vullen")
    print("Start bij 0")
    print("typ d als je klaar bent")
    for temp in templist:
        count=count+1
        print(inst)
        step=input(f'{name}'+"step:")   
        count = count % 24
        if (count==10):
            print("TIP: typ enorme getaalen voor een soort random")
        try:
            if (step=='d'):
                print("aight")
            else:
                step=int(step)%len(k)
                if (inst[step]==0):
                    print("Kans van 0 t/m 100")
                    inst[step]=(int(input("Kans:"))%101)
                    #IDEE: enkel enter switchts 0 of 100
                else:
                    inst[step]=0
                templist.append(0)
        except:
            print("Je hebt waarschijnlijk woorden of helemaal niks getypt. Misschien zelfs floats...")
            templist.append(0)

#INSTPlay
def playloop(inst, name):
    rando=int(random.random()*100)
    return
    if (inst[(curstep)]>rando):
        wave_obj = sa.WaveObject.from_wave_file(str(f'{proj_folder}/media/{name}.wav'))
        play_obj = wave_obj.play()
    #IDEE: Random laten zien in een print

#—————————————————————————————————————#
               #Code
#—————————————————————————————————————#       
#Interface
eventNr=[1]
print("d+enter als je klaar bent")
print("typ 'helfferich' voor hulp")
print('TijdsEenheid:',f'{tijds}'+'/'+f'{eenheid}')
print('BPM:' , bpm)
for x in eventNr:
    inp=input("ira.seq:")
    if (inp!='d'):
        eventNr.append(0)
        print('Je kan "helfferich" typen voor hulp.')
    if (inp=='helfferich'):
#help
        print("k = kick")
        print("s = snare")
        print("h = hihat")
        print("bpm = bpmstatus")
        print("ts = TimeSignature")
        print("d = klaar en sla op")
        #IDEE: r = klaar maar sla niet op
        #IDEE: Samplerate&Bitdepth Menu
#inst
    if (inp=='k'):
        inst(k, "kick")
    if (inp=='s'):
        inst(s, "snare")
    if (inp=='h'):
        inst(h, "hihat")
#BPM
    if (inp=='bpm'):
        bpm
        print(f"bpm = {cbpm}")
        try:
            print(f"Type new bpm in numbers or enter to keep {cbpm}:")
            bpm = input("New bpm between 5 and 999:")
            bpm = int(bpm)
            if (bpm>999) or (bpm<=4):
                print("invalid")
                bpm = cbpm
                print(f"Enterd without a valid new bpm in numbers so: keeping {cbpm} bpm")
            else:
                print("new bpm=", bpm)
                cbpm=bpm
        except:
            bpm = cbpm
            print(f"Enterd without a valid new bpm in numbers so: keeping {cbpm} bpm")
            cbpm=bpm
#Tijd        
    MS=float(60000/bpm)
    S=MS/1000
    sleeptime=MS/10000

#Maat
    if (inp=='ts'):
        try:
            print("Huidige Tijdseenheid:", f'{tijds}'+'/'+f'{eenheid}')
            tijds = int(input("Time:"))
            eenheid = int(input("Signature:"))
            temp=(math.log(eenheid,2))
            if (tijds==eenheid):
                print(f"naar beneden geschaald omdat {tijds}/{eenheid} hetzelfde is als 4/4") 
                tijds=4
                eenheid=4
            if (temp.is_integer()):
                ts=cts
                print("Nieuwe Tijdseenheid:", f'{tijds}'+'/'+f'{eenheid}')
                ts = tijds*eenheid
                ts = int(ts /(eenheid/2))
            else:
                tijds=ctijds
                eenheid=ceenheid
                print(f"Enterd without a valid new TimeSignature in numbers so: keeping {tijds}/{eenheid}")
            ctijds=tijds
            ceenheid=eenheid
        except:
            tijds=ctijds
            eenheid=ceenheid
            print(f"Enterd without a valid new TimeSignature in numbers so: keeping {tijds}/{eenheid}")
        k=[]
        s=[]
        h=[]
        for temp in range(ts):
            k.append(0)
            s.append(0)
            h.append(0)

#seq
while True:
    for  curstep in range(ts):
        playloop(k, 'kick')
        playloop(s, 'snare')
        playloop(h, 'hihat')
        print(curstep)
        time.sleep(sleeptime)
