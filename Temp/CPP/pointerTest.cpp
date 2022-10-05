#include <iostream>
#include <thread>
#include <unistd.h>
#include <algorithm>

using std::cout;
using std::endl;
using std::string;
using std::cin;

void check(int* shot) {

	cout<<shot<<endl;
	cout<<*shot<<endl;

}

void foo(int Z) {

	for (int i=0; i<Z; i++) {

		cout<<"Hello"<<endl;
		sleep(1);

	}

}

void bar(int Z) {


	for (int i=0; i<10; i++) {
		cout<<"bon jour"<<endl;
		sleep(1);
	}

}


int main (int argc, char** argv) {

	int number = 1;
	cout<<number<<" "<<&number<<endl;

	int* num = &number;

	cout<<num<<" "<<*num<<endl;

	check(num);

	std::thread th1(foo, 5);
	std::thread th2(bar, 5);


	th1.join();
	th2.join();


}
