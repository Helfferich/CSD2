#include <iostream>
using namespace std;

class Instrument {
public:
	Instrument(string inst);
	~Instrument();
	void play();
private:
	string inst;
	string make;
};
