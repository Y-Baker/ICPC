#include <iostream>
#include <list>
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

    list<int> l;

    l.push_back(0);
    last = 0;

    char op[n];
    for (int i = 0; i < n; i++) {
        cin >> op[i];
        if (op[i] == 'L') {
            auto it = l.begin();
            for (int i = 0; i < last; i++) {
                it++;
            }
            l.insert(it, i + 1);
        } else if (op[i] == 'R') {
            last++;
            auto it = l.begin();
            for (int i = 0; i < last; i++) {
                it++;
            }
            l.insert(it, i + 1);
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
