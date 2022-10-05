#include <iostream>
#include <random>
#include <string>
#include <math.h>

using std::cout;
using std::endl;
using std::string;
using std::cin;

void clear_screen();
int get_random_int();
float get_random_float();
void hit();
void miss();
bool fire_shot(int facing, float distance);
int get_input(int min, int max);

int facing;
float distance;
bool result;

int main() {

	clear_screen();
	cout<<"Desert Tank Battle"<<endl;

	//Gets the distance and the facing
	distance = get_random_float();
	facing = get_random_int();

	result = fire_shot(facing, distance);

	//Checks to see if it is success or failure
	if (result) {
		hit();
	} else {
		miss();
	}
}

//Fire shot function
bool fire_shot(int facing, float distance) {

	//The player gets five chances
	for (int guess = 0; guess<5; guess ++) {

		//gets player input
		cout<<"Select Direction (-90 to 90)"<<endl;
		int direction = get_input(-90,90);

		cout<<"Select elevation (0 to 90)"<<endl;
		int elevation = get_input(0,90);

		//Calculates the distance of the shot
		float shot_distance = sin(2*(elevation/180*3.1416));

		//checks to see whether the player has hit the target
		if (abs(facing-direction)<2 || abs(distance-shot_distance)<0.05) {
			return true;
		} else {

			cout<<"The missile has landed:"<<endl;

			//determines the side of the target that the shot landed
			if (facing<direction) {
				cout<<"to the left"<<endl;
			} else if (facing>direction) {
				cout<<"to the right"<<endl;
			}

			//Determines whether the shot landed either side and too/not far
			if (abs(distance-shot_distance)>0.05 && facing != direction) {
				cout<<"and"<<endl;
			}

			//Detects whether the shot landed in front or behind
			if ((distance-shot_distance)<0.05) {
				cout<<"Too far"<<endl;
			} else if ((distance-shot_distance)>0.05) {
				cout<<"Not far enough"<<endl;
			}
		}
	}

	return false;

}

//Gets the player's input
int get_input(int min, int max) {

	bool correct_input = false;
	int entry;

	//Validates the input
	while (!correct_input) {
		cin>>entry;

		//Checks to see whether it is an integer
		if (cin.fail()) {

			cout<<"Please enter an integer"<<endl;
			cin.clear();
			cin.ignore(256,'\n');

		//Checks to see whether it is within range
		} else if (entry<min || entry>max) {

			cout<<"Please enter an integer between "<<min<<" and "<<max<<endl;
			cin.clear();
			cin.ignore(256,'\n');

		} else {

			//If validated, breaks out of the loop
			correct_input = true;
		}
	}

	return entry;

}

//Generates a random float between 0 and 1
float get_random_float() {

	std::random_device rd;
	std::mt19937 gen(rd());
	std::uniform_real_distribution <> distr(0.0,1.0);

	return distr(gen);

}

//generate a random integer between -90 and 90
int get_random_int() {

	int number = -90;

	std::random_device rd;
	std::mt19937 gen(rd());
	std::uniform_int_distribution <> distr(number, number+180);

	return distr(gen);

}

void clear_screen() {

	int number = system("clear");

	if (number == 0) {
		cout<<endl;
	}
}

//Results of the game
void hit() {
	cout<<"***KABOOOM****"<<endl;
	cout<<"You Did It!"<<endl;
}

void miss() {
	cout<<"DISASTER - You Failed"<<endl;
	cout<<"Retreat in disgrace"<<endl;
}
