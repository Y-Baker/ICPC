#include <iostream>
#include <utility>
#include <deque>
#define endl "\n"

#define int long long

using namespace std;

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

int32_t main() {
    fastIO();

    int t, op, x, y;
    long long counter = 0;

    cin >> t;

    deque <pair<int, int>> q;

    while (t--)
    {
        cin >> op;
        if (op == 1) {
            cin >> x >> y;
            q.push_back(make_pair(x, y));
        }
        else if (op == 2) {
            counter = 0;
            cin >> x;
            while (x > 0 && !q.empty())
            {
                pair<int, int> temp = q.front();
                if (x >= temp.second)
                {
                    counter += temp.first * temp.second;
                    x -= temp.second;
                    q.pop_front();
                } else {
                    counter += temp.first * x;
                    temp.second -= x;
                    q.pop_front();
                    q.push_front(temp);
                    x = 0;
                }
            }
            cout << counter << endl;
        }
    }
}
