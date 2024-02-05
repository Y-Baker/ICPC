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

    string s;
    bool reverse = false;
    deque<char> q;
    cin >> s;

    for (int i = 0; i < s.size(); i++) {
        q.push_back(s[i]);
    }
    int ops, x;
    cin >> ops;

    while (ops--) {
        cin >> x;
        if (x == 1) {
            reverse = !reverse;
        }
        else if (x == 2) {
            int p;
            char c;
            cin >> p >> c;
            if (!reverse) {
                if (p == 1) {
                    q.push_front(c);
                } else if (p == 2) {
                    q.push_back(c);
                }
            } else {
                if (p == 1) {
                    q.push_back(c);
                } else if (p == 2) {
                    q.push_front(c);
                }
            }
        }
    }
    
    if (reverse) {
        while (!q.empty()) {
            cout << q.back();
            q.pop_back();
        }
    } else {
        while (!q.empty()) {
            cout << q.front();
            q.pop_front();
        }
    }
    cout << endl;
}
