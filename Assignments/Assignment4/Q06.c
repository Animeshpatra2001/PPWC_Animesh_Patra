#include <stdio.h>

int main() {
    int a = 12, b = 52, c = 8;
    int *ptr1 = &a, *ptr2 = &b, *ptr3 = &c;
    
    *ptr1 += 10;
    *ptr2 += 10;
    *ptr3 += 10;

    printf("a: %d\nb: %d\nc: %d\n", a, b, c);
    return 0;
}

/*
Output
a: 22
b: 62
c: 18
*/