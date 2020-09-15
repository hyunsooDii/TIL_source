#include <iostream>
using namespace std;

class Pizza{
public:
    int size;
    Pizza(int s) : size(s) {}
};

void makeDouble(Pizza p){
    p.size *= 2;
}

int main(int argc, char const *argv[]) {
   Pizza pizza(10);
   makeDouble(pizza);
   cout << pizza.size << "inch pizza" << endl;
   
   return 0;
}