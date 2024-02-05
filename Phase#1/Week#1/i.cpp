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
    int n, x;
    bool flag = false;
    cin >> n;

    deque<int> q;
    for (int i = 0; i < n; i++) {
        cin >> x;
        if ((n % 2 == 0 && i % 2 == 0) || (n % 2 == 1 && i % 2 == 1)) {
            q.push_back(x);
        } else if ((n % 2 == 0 && i % 2 == 1) || (n % 2 == 1 && i % 2 == 0)){
            q.push_front(x);
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
