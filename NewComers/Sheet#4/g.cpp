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

    int counter = 0;
    string s;
    cin >> s;
    char ptr = 'a';
    for (char c : s) {
        counter += min(abs(c - ptr), 26 - abs(c - ptr));
        ptr = c;
    }
    cout << counter << endl;
}
