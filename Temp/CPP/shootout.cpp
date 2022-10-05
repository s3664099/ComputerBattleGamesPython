#include <iostream>
#include <string>
#include <random>
#include <unistd.h>
#include <algorithm>
#include <thread>

using std::cout;
using std::endl;
using std::string;
using std::cin;

void clear_screen();
int get_random();
void draw();
void your_shot(int* check_shot);
void his_shot(int* check_shot);

int main (int argc, char** argv) {

	clear_screen();

	cout<<"Cowboy Shootout"<<endl;
	sleep(2);
	cout<<"You are back to back"<<endl;
	sleep(2);
	cout<<"You take ten paces"<<endl;

	for (int i = 0; i < 10; i++) {

		cout<<"--"<<endl;
		sleep(2);
	}

	draw();
}

void draw() {

	int check_fire = 0;
	int* shot = &check_fire;
}

int get_random() {

	int number = 1;

	std::random_device rd;
	std::mt19937 gen(rd());
	std::uniform_int_distribution <> distr(number, number+25);

	return distr(gen);

}

void clear_screen() {

	int number = system("clear");

	if (number == 0) {
		cout<<endl;
	}
}