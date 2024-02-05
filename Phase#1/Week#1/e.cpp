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

    int n, q, x, counter;
    bool flag = false;
    cin >> n >> q;
    list <int> l;

    while (n--) {
        cin >> x;
        l.push_back(x);
    }

    while (q--)
    {
        counter = 1;
        cin >> x;
        for (auto it = l.begin(); it != l.end(); it++) {
            if (*it == x) {
                l.erase(it);
                l.push_front(x);
                if (flag)
                    cout << " ";
                cout << counter;
                flag = true;
                break;
            }
            counter++;
        }
        cout << endl;
    }
    
}
