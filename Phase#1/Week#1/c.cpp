#include <iostream>
#include <queue>
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    queue<int> q;
    while (t--) {
        int n;
        cin >> n;
        switch (n)
        {
        case 1:
            int x;
            cin >> x;
            q.push(x);
            break;
        case 2:
            if (!q.empty())
                q.pop();
            break;
        case 3:
            if (!q.empty()) {
                cout << q.front() << "\n";
            } else {
                cout << "Empty!\n";
            }
            break;
        
        default:
            break;
        }
    }
}
