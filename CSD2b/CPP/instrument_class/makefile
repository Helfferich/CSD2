#target: source #geeft aan welke bronnen hij wil gebruiken
#		cp source target #geeft aan wat hij doet

instument: main.o instrument.o
		g++ -o  instrument main.o instrument.o

#oscsynth: main.o oscillator.o fm_thing.o
#		g++ -o osctest main.o oscillator.o

main.o: main.cpp
		g++ -c main.cpp

instrument.o: instrument.cpp instrument.h
		g++  -c instrument.cpp

#-std=c++11

#install:
#		cp osctest /usr/local/bin

clean:
		rm osctest main.o oscillator.o

#osctest: oscillator.cpp
#		g++ -c main.cpp
#		g++ -c oscillator.cpp
#		g++ -o osctest main.o oscillator.o