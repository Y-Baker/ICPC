#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--)
    {
        int n;
        cin >> n;

        int arr[n];
        int freq[n] = {0};
    
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
            freq[arr[i] - 1]++;
        }
        bool flag = false;
        int re = -1;
        for (int i = 0; i < n; i++) {
            if (freq[i] >= 3) {
                re = i + 1;
            }
        }
        cout << re << endl;
    }
}
