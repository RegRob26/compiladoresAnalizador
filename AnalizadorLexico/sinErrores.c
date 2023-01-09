int main() {
    int a = 5;
    float b = 6.5;

    if (a > b) {
        printf("pruebota");
    } else {
        printf("Dato");
    }

    while (a > 0) {
        printf("a");
        a = a - 1;
    }

    do {
        printf("a");
        a = a - 1;
    } while (a > 0);

    for (i = 0; i < 10; i = i + 1) {
        printf("menor");
    }
}

int suma(int a, int b) {
    int resultado = a + b;
    return resultado;
}

char concatenar(char a, char b) {
    char c;
    return c + "a";
}
