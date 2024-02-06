#include <iostream>
#include <queue>
#define endl "\n"


using namespace std;

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

int main() {
    fastIO();

    int t, op, x, y;
    long long count = 0;
    cin >> t;

    queue <int> q;
    while (t--)
    {
        cin >> op;
        if (op == 1) {
            cin >> x >> y;
            for (int i = 0; i < y; i++) {
                q.push(x);
            }
        }
        else if (op == 2) {
            count = 0;
            cin >> x;
            while (x-- && !q.empty())
            {
                count += q.front();
                q.pop();
            }
            cout << count << endl;
        }
    }
    
}
