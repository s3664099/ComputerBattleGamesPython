#include <iostream>
#include <ncurses.h>

int main()
{
    char ch; //or 'int ch;' (it doesn't really matter)

    while (true) {
        //the program pauses here until a key is pressed
        ch = getch();

        if(ch == 'a')
            std::cout << "You pressed a!" << std::endl;

    }

    return 0;
}