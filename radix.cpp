//  g++ -std=c++11 radix.cpp -o radix && ./radix

#include <iostream>

using namespace std;

int main() {
    int number = 7;
    int digit = 2;
    cout << ((abs(number) >> digit) & 1) << endl;

    return 0;
}

