#include <iostream>
#include <string>
#include <random>

using std::cout;
using std::endl;
using std::string;
using std::cin;

bool playing = true;
bool main_game();
int get_random_number();

char letter;

int main (int argc, char** argv) {

	bool playing = true;

	while (playing == true) {

		bool letterFound = main_game();
	
		if (letterFound == false) {

			cout<<"BOOM!!! You blew it!!"<<endl;
			cout<<"The correct code was "<<letter<<endl;

		} else {

			cout<<"Tick ... click ... fizzz"<<endl;
			cout<<"Congratulations, you disarmed the missile"<<endl;
		}

		char play;

		cout<<"Do you want to play again? "<<endl;
		cin>>play;

		if (play == 'n' || play == 'N') {

			playing = false;
		}

	}
}

bool main_game() {

	int turn = 0;

	letter = (char)get_random_number();

	cout<<"Robot Missile"<<endl<<endl;
	cout<<"Type the correct code"<<endl;
	cout<<"Letter (A-Z) to Defuse the missile"<<endl;
	cout<<"you have 4 chances"<<endl<<endl;

	while (turn<4) {

		turn ++;
		char letterGuess;

		cout<<"Please select a letter: ";
		cin>>letterGuess;

		letterGuess = toupper(letterGuess);

		if (letterGuess < letter) {
			cout<<"The letter is higher"<<endl;
		} else if (letterGuess > letter) {
			cout<<"The letter is lower"<<endl;
		} else {
			return true;
		}

		letterGuess = '0';

	}

	return false;
}

int get_random_number() {

	int char_number = 65;

	std::random_device rd;
	std::mt19937 gen(rd());
	std::uniform_int_distribution <> distr(char_number,char_number+25);

	return distr(gen);
}