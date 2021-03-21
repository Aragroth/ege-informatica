#include <iostream>
#include <cmath>
#include <set>


int main() {
    for (int number=40'000'000; number<=50'000'000;number++) {
        if (number % 1000000 == 0) {
            std::cout << number << std::endl;
        }
    
        int count = 0;
        std::set <int> mass;
        float middle = floor(sqrt(number));

        for (int delitel=1;delitel<=middle+3;delitel++) {
            if (number % delitel == 0) {
                if (pow(delitel, 2) == number) {
                    mass.insert(delitel);
                    break;
                }
                if (mass.size() > 5) {
                    break;
                }
                if (delitel % 2 == 1) {
                    mass.insert(delitel);
                }
                if (number / delitel % 2 == 1) {
                    mass.insert(number / delitel);
                }
            }
        }
        if (mass.size() == 5) {
            std::cout << "<--- " << number << std::endl;
        }
    }
}


