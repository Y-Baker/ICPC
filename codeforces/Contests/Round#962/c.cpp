#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

#define endl "\n"
#define ll long long

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
        int n, q;
        cin >> n >> q;
        string one, two;
        cin >> one >> two;
        vector<int> freqA = vector<int>(26, 0);
        vector<int> freqB = vector<int>(26, 0);
        vector<vector<int>> prefixFreqA (n, vector<int>(26, 0));
        vector<vector<int>> prefixFreqB (n, vector<int>(26, 0));
        for (int i = 0; i < n; i++) {
            freqA[one[i] - 'a'] += 1;
            freqB[two[i] - 'a'] += 1;
            vector<int> tmpA = freqA;
            vector<int> tmpB = freqB;
            prefixFreqA[i] = tmpA;
            prefixFreqB[i] = tmpB;
        }
        while (q--) {
            int i, j;
            cin >> i >> j;
            i -= 1;
            j -= 1;
            int cnt = 0;

            fill(freqA.begin(), freqA.end(), 0);
            fill(freqB.begin(), freqB.end(), 0);

            for (int k = 0; k < 26; k++) {
                if (i > 0) {
                    freqA[k] = prefixFreqA[j][k] - prefixFreqA[i - 1][k];
                    freqB[k] = prefixFreqB[j][k] - prefixFreqB[i - 1][k];
                } else {
                    freqA[k] = prefixFreqA[j][k];
                    freqB[k] = prefixFreqB[j][k];
                }
            }

            for (int k = 0; k < 26; k++) {
                cnt += abs(freqA[k] - freqB[k]);
            }

            cout << cnt / 2 << endl;
        }
    }
}
