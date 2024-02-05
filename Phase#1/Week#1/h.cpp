#include <iostream>
#include <deque>
#define endl "\n"

using namespace std;

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

int main() {
    fastIO();
    int n, last;
    bool flag = false;
    cin >> n;

    deque<int> l;

    l.push_back(n);
    last = 0;

    string ops;
    cin >> ops;
    for (int i = n - 1; i >= 0; i--) {
        if (ops[i] == 'L') {
            l.push_back(i);
        } else if (ops[i] == 'R') {
            l.push_front(i);
        }
    }
    for (auto it : l) {
        if (flag) {
            cout << " ";
        }
        cout << it;
        flag = true;
    }
    
}
