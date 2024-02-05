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
    int t, n, x;
    bool flag = false;
    cin >> t;

    while (t--)
    {
        flag = false;
        cin >> n;
        deque<int> q;
        for (int i = 0; i < n; i++) {
            cin >> x;
            if (!q.empty() && q.front() > x) {
                q.push_front(x);
            } else {
                q.push_back(x);
            }
        }
        for (auto it : q) {
            if (flag) {
                cout << " ";
            }
            cout << it;
            flag = true;
        }
        cout << endl;
    }
    
}
