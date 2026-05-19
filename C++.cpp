#include <iostream>
using namespace std;

class Persona {
private:
    string nombre;

public:
    Persona(string n) {
        nombre = n;
    }

    void saludar() {
        cout << "Hola, soy " << nombre << endl;
    }
};

int main() {
    Persona p("Julian");
    p.saludar();

    return 0;
}
