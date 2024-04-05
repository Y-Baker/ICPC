#include <iostream>
#include <vector>
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
        int n, m, tmp;
        cin >> n >> m;

        int grid[n][m];
        int sum = 0;
        int min = 1000;
        int zeros = 0;
        int negatives = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> tmp;
                grid[i][j] = tmp;
                sum += abs(tmp);
                if (tmp < 0) {
                    negatives++;
                }
                if (abs(tmp) < min) {
                    min = abs(tmp);
                }
                if (tmp == 0) {
                    zeros = 1;
                }
            }
        }
        if (zeros) {
            cout << sum << endl;
        } else if (negatives % 2 == 0) {
            cout << sum << endl;
        } else {
            cout << sum - 2 * min << endl;
        }
    }
}
