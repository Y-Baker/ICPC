#include <iostream>
#include <unordered_map>
#define endl "\n"

using namespace std;

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

int main() {
    fastIO();

    int t, size, x;
    bool flag = true;
    cin >> t;

    while(t--) {
        cin >> size;
        flag = true;
        unordered_map<int, int> freq;

        for (int i = 0; i < size; i++) {
            cin >> x; 
            freq[x]++;
            if (freq[x] > 1) {
                flag = false;
            }
        }

        if (flag) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
}
