#include <iostream>
#include <unordered_map>
#define endl "\n"

using namespace std;

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

int main() {
    fastIO();

    int t;
    cin >> t;

    while (t--) {
        string x1, x2;
        cin >> x1 >> x2;

        unordered_map<char, int> m1(4), m2(4);
        for (char c : x1) {
            m1[c]++;
        }
        for (char c : x2) {
            m2[c]++;
        }
        int re1 = 0, re2 = 0;
        re1 = (m1['M'] * 2) + (m1['L'] * 3) + (m1['L'] * m1['X']) + m1['S'] - (m1['S'] * m1['X']);
        re2 = (m2['M'] * 2) + (m2['L'] * 3) + (m2['L'] * m2['X']) + m2['S'] - (m2['S'] * m2['X']);
        if (re1 == re2) {
            cout << "=" << endl;
        } else if (re1 > re2) {
            cout << ">" << endl;
        } else {
            cout << "<" << endl;
        }
    }
}
