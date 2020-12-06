#include <iostream>
#include "instrument.h"

Instrument::Instrument (string inst)
{
  std::cout << inst << " doet " << std::endl;
}

Instrument::~Instrument()
{
}

void Instrument::play()
{
    std::cout << "FFFRRRTTTT" << std::endl;
}

/*void Instrument::play(string make)
{

  if (sound=="fluit")
    make = "Frrrrtt"; 
  std::cout << make << std::endl;
}*/