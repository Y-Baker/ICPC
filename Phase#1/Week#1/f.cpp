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
    int t, n;
    cin >> t;
    int counter = 0;
    int open = 0;
    while (t--)
    {
        open = 0, counter = 0;
        cin >> n;
        if (n % 2 != 0) {
            cout << "Can't be odd" << endl;
            cin.ignore();
            continue;
        }
        deque<char> q(n);
        for (auto &it : q) {
            cin >> it;
            if (it == '(')
                open++;
            else {
                if (open == 0) {
                    counter++;
                }
                else {
                    open--;
                }
            }
        }
        cout << counter << endl;

    }
    
}
