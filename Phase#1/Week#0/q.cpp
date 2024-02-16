#include <iostream>

#define endl "\n"

using namespace std;

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

int main() {
    fastIO();

    int x, y, o;
    cin >> x >> y >> o;

    if (o % 2 == 0) {
        x = abs(x);
        y = abs(x);
    }
    if (x > y) {
        cout << '>' << endl;
    } else if (y > x) {
        cout << '<' << endl;
    } else {
        cout << '=' << endl;
    }
}
