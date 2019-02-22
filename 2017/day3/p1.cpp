#include <bits/stdc++.h>
using namespace std;

void printSpiral(int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            // x stores the layer in which (i, j)th
            // element lies
            // Finds minimum of four inputs
            int x = min(min(i, j), min(n-1-i, n-1-j));
            int el;
 
            // For upper right half
            if (i <= j) {
                el = (n-2*x)*(n-2*x) - (i-x)
                       - (j-x);
                printf("%2d ", el);
            }
 
            // for lower left half
            else {
                el = (n-2*x-2)*(n-2*x-2) + (i-x)
                       + (j-x);
                printf("%2d ", el);
            }
        }
        printf("\n");
    }
}

void findInSpiral(int q) {
    int n = ceil(sqrt(q));
    int ci = n/2;
    int cj = ci;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int x = min(min(i, j), min(n-1-i, n-1-j));
            int el;

            if (i <= j) {
                el = (n-2*x)*(n-2*x) - (i-x) - (j-x);
            } else {
                el = (n-2*x-2)*(n-2*x-2) + (i-x) + (j-x);
            }

            if (el == q) {
                int d = abs(i - ci) + abs(j - cj);
                printf("Found, %d!\n", el);
                printf("Distance: %d\n", d);
                return;
            }
        }
    }
}

int main(int argc, char** argv) {
    int n;

    if (argc > 1)
        n = atoi(argv[1]);
    else
        n = 265149;

    findInSpiral(n);
    return 0;
}

