#include <iostream>

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
    cin >> t;

    while (t--) {
        int n, k;
        cin >> n >> k;

        if (n < k) {
            cout << "NO" << endl;
            continue;
        }
        if (n % k == 0) {
            cout << "YES" << endl;
            for (int i = 0; i < k; i++) {
                cout << n / k << " ";
            }
            cout << endl;
        } else {
            int rem = n % k;
            int div = n / k;
            if (rem % 2 == 0) {
                cout << "YES" << endl;
                for (int i = 0; i < k; i++) {
                    if (i == k - 1) {
                        cout << div + rem << " ";
                    } else {
                        cout << div << " ";
                    }
                }
                cout << endl;
            } else {
                int x = k - rem;
                bool flag = false;
                if (x & 1) { // odd
                    cout << "NO" << endl;
                } else if (div == 1 && x > 0) {
                    cout << "NO" << endl;
                } else {
                    cout << "YES" << endl;
                    for (int i = 0; i < k; i++) {
                        if (rem > 0) {
                            cout << div + 1 << " ";
                            rem--;
                        } else if (flag) {
                            cout << div + 1 << " ";
                            flag = false;
                        } else {
                            cout << div - 1<< " ";
                            flag = true;
                        }
                    }
                    cout << endl;
                }
            }
        }
    }
}
