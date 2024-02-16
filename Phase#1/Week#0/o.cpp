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

    int t, size;
    cin >> t;

    while(t--) {
        int x, sum = 0;
        cin >> size;
        for (int i = 0; i < size; i++) {
            cin >> x;
            sum += x;
        }
        if (sum > size) {
            cout << sum - size << endl;
        } else if (sum < size) {
            cout << 1 << endl;
        } else {
            cout << 0 << endl;
        }
    }
}
