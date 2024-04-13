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
        int arr[7];
        for (int i = 0; i < 7; i++) {
            cin >> arr[i];
        }
        int re1 = arr[0];
        int x = arr[6] - arr[0];
        int re2 = arr[1];
        int re3;
    
        for (int i = 2; i < 7; i++) {
            if (x - re2 == arr[i]) {
                re3 = arr[i];
                break;
            }
        }
    
        cout << re1 << " " << re2 << " " << re3 << endl;
    }
}
