#include <iostream>
#include <set>
#define endl "\n"

// a b c a b c d
// 4 4 4 4 3 2 1
using namespace std;

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

int main() {
    fastIO();

    int t, n;
    string str;
    cin >> t;

    while(t--) {
        set<int> s1;
        set<int> s2;
        cin >> n;
        cin >> str;

        int arr[n];
        int freq2[26] = {0};
        int longest = 0;
        int start_idx = 0;
        int max;

        for (int i = 0; i < n; i++) {
            if (freq2[str[i] - 'a'] > 0) {
                arr[i] = 1;
            } else {
                arr[i] = 0;
            }
            freq2[str[i] - 'a']++;
        }
        int freq[n] = {0};
        for (int i = 0; i < n; i++) {
            if (arr[i] == 0) {
                longest = 0;
            } else {
                if (longest == 0) {
                    longest++;
                    start_idx = i;
                    freq[start_idx]++;
                } else {
                    longest++;
                    freq[start_idx]++;
                }
            }
        }
        max = 0;
        for (int i = 0; i < n; i++) {
            if (freq[i] > freq[max]) {
                max = i;
            }
        }

        for (int i = 0; i < n; i++) {
            if (i < max) {
                s1.insert(str[i]);
            } else {
                s2.insert(str[i]);
            }
        }

        cout << s1.size() + s2.size() << endl;
    }
}
