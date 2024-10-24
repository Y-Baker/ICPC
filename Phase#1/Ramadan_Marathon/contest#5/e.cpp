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
    int n, k;
    cin >> n >> k;
    int arrA[n];
    int arrB[n];
    int freqA[100010];
    int freqB[100010];
    for (int i = 1; i <= n; i++) {
        cin >> arrA[i];
        freqA[arrA[i]]++;
    }
    for (int i = 1; i <= n; i++) {
        cin >> arrB[i];
        freqB[arrB[i]]++;
    }
    int cnt1 = 0;
    int cnt2 = 0;

    for (int i = n; i > 1; i--) {
        freqA[arrA[i]]--;
        if (k - arrA[i] > 0) {
            cnt1 += freqB[k - arrA[i]];
        }
    }
    for (int i = n; i > 1; i--) {
        freqB[arrB[i]]--;
        if (k - arrB[i] > 0) {
            cnt2 += freqA[k - arrB[i]];
        }
    }

    cout << cnt1 << " " << cnt2 << endl;
    if (cnt1 > cnt2) {
        cout << "Mahmoud" << endl;
    } else if (cnt1 < cnt2) {
        cout << "Bashar" << endl;
    } else {
        cout << "Draw" << endl;
    }

}
