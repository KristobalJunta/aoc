#include <bits/stdc++.h>
using namespace std;

int m[501][501];

int main(int argc, char** argv) {
    // freopen("d3p2.out", "w", stdout);
    int n;

    if (argc > 1)
        n = atoi(argv[1]);
    else
        n = 265149;

    int dir[][2] = {{0, 1}, {-1, 0}, {0, -1}, {1, 0}};
    int nb[][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}, {1, 1}, {-1, -1}, {1, -1}, {-1, 1}};

    int cur = 0;
    int i = 250;
    int j = 250;
    m[i][j] = 1;
    j++;
    int lrNum = 1;
    int curSt = 1;
    int lrW = 3;
    int curD = 1;
    int k = 0;

    while (cur <= n) {
        cur = 0;
        for (int q = 0; q < 8; q++) {
            cur += m[i+nb[q][0]][j+nb[q][1]];
        }

        m[i][j] = cur;
        curSt++;
        k++;

        if (curSt >= lrW) {
            curSt = 1;
            curD = curD + 1 < 4 ? curD + 1 : 0;
            // cerr << "Turn point at " << i << " " << j << endl;
        }

        if (k % (8*lrNum) == 0) {
            lrNum++;
            lrW += 2;
            k = 0;
        }

        if (k == 0) {
            i = i + dir[0][0];
            j = j + dir[0][1];
        } else {
            i = i + dir[curD][0];
            j = j + dir[curD][1];
        }
    }

    for (int a = 240; a < 261; a++) {
        for (int b = 240; b < 261; b++) {
            printf("%4d ", m[a][b]);
        }
        cout << endl;
    }
    cout << endl;

    cout << cur << endl;

    return 0;
}
