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
        int n;
        cin >> n;
        int arr[n];
        int sum = 0;
        int min = 10000000;

        for (int i = 0; i < n; i++) {
            cin >> arr[i];
            sum += arr[i];
            if (arr[i] < min) {
                min = arr[i];
            }
        }

        cout << sum - n * min << endl;
    }
}
