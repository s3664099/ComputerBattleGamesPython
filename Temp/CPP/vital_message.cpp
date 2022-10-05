#include <iostream>
#include <string>
#include <random>
#include <unistd.h>
#include <algorithm>

using std::cout;
using std::endl;
using std::string;
using std::cin;

bool playing = true;
void main_game();
string get_message(int difficulty);
int get_difficulty();
void clear_screen();
string to_upper_case(string message);

int main (int argc, char** argv) {

	string message_sent;
	char answer;

	clear_screen();

	while (playing == true) {

		cout<<"The Vital Message"<<endl;
		cout<<"-----------------"<<endl<<endl;

		int difficulty = get_difficulty();
		
		string message = get_message(difficulty);

		clear_screen();

		cout<<"Send this message"<<endl;
		cout<<message<<endl;
		sleep(5);
		clear_screen();

		cout<<"Send the message"<<endl;
		cin>>message_sent;

		message_sent = to_upper_case(message_sent);

		if (message == message_sent) {

			cout<<"The message is correct"<<endl;
			cout<<"The war is over"<<endl;
		} else {

			cout<<"You got it wrong"<<endl;
			cout<<"You should have sent: "<<message<<endl;
		}

		cout<<"Do you want to play again?"<<endl;
		cin>>answer;

		answer = toupper(answer);

		if( answer == 'N') {
			playing = false;
		}

	}

}

string to_upper_case(string message) {

	std::for_each(message.begin(), message.end(), [](char & c) {
		c = ::toupper(c);
	});

	return message;
}

string get_message(int difficulty) {

	int char_number = 65;
	string message;

	for (int x = 0; x<difficulty; x++) {

		std::random_device rd;
		std::mt19937 gen(rd());
		std::uniform_int_distribution <> distr(char_number,char_number+25);

		message += (char)distr(gen);
	}

	return message;

}

//Asks for a difficulty level
int get_difficulty() {

	int difficulty;
	bool validate = true;

	while (validate) {
		
		cout<<"How difficult (4-10)?"<<endl;
		
		//Validates the input to confirm that it is an integer
		if (cin>>difficulty) {

			if (difficulty > 3 and difficulty < 11) {

				return difficulty;
			} 
		}

		//if it is not an integer, or falls out of range
		//We clear the buffer and try again.
		cin.clear();
		cin.ignore();

		cout<<"Please enter a number between 4 and 10"<<endl;
	}

	return difficulty;

}

void clear_screen() {

	int number = system("clear");

	if (number == 0) {
		cout<<endl;
	}
}