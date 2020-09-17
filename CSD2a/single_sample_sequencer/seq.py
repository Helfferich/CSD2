import simpleaudio as sa, time

#BPM = const&var
cbpm = 120
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


i = [0.25, 0.5, 0.25, 0.5, 0.5, 1, 1]

i=[0]+i
count=0
timestamps16th = []

for fortemp in i:
    #time to stamps
    count=count+1
    if (count!=1):
        if (fortemp>0):
            temp=fortemp*4
            try:
                temp=temp+temp_last
                round(temp_last=temp)
            except: 
                temp_last=temp
            temp=round(temp)
            stamp=temp
            #print(stamp)
        else:
            #FIXME: bij 0 dat laten negeren
            print("nul kan niet")
            break
    else:
        stamp=0
    

    #als len
    if (count>=len(i)):
        if (stamp==16):
            print("done")
            break
        if (stamp<16):
            print("tekort, afgerond tot 16")
            break
        if (stamp>16):
            print("telang, afgerond tot 16")
            break
    timestamps16th.append(stamp)

MS=60000/bpm
steptime=MS/4
count=-1

bpmstamps = []
timestamps16th.append(16)
for temp in timestamps16th:
    if ((count+2)<len(timestamps16th)):
        count=count+1
        number = timestamps16th[(count+1)] - timestamps16th[count]
        Timebetween=number*steptime
        bpmstamps.append
    else:
        break
print(bpmstamps)
    
    
    
    
    




