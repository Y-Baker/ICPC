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
    int t;
    bool flag = true;
    cin >> t;
    deque<int> q;

    while (t--)
    {
        string s;
        cin >> s;

        if (s == "toFront") {
            int x;
            cin >> x;
            flag ? q.push_front(x) : q.push_back(x);
        } else if (s == "push_back") {
            int x;
            cin >> x;
            flag ? q.push_back(x) : q.push_front(x);
        } else if (s == "back") {
            if (!q.empty()) {
                if (flag) {
                    cout << q.back() << endl;
                    q.pop_back();
                } else {
                    cout << q.front() << endl;
                    q.pop_front();
                }
            } else {
                cout << "No job for Ada?" << endl;
            }
        } else if (s == "front") {
            if (!q.empty()) {
                if (flag) {
                    cout << q.front() << endl;
                    q.pop_front();
                } else {
                    cout << q.back() << endl;
                    q.pop_back();
                }
            } else {
                cout << "No job for Ada?" << endl;
            }
        } else if (s == "reverse") {
            flag = !flag;
        }
    }
    
}
