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

    string s;
    cin >> s;

    int freq[26] = {0};


    for (int i = 0; i < n; i++) {
        freq[s[i] - 'a']++;
    }

    int to_remove[26] = {0};
    int i = 0;
    while (k > 0) {
        to_remove[i] = min(freq[i], k);
        k -= to_remove[i];
        if (to_remove[i] == freq[i]) {
            i++;
        }
    }

    for (int i = 0; i < n; i++) {
        if (to_remove[s[i] - 'a']) {
            to_remove[s[i] - 'a']--;
        } else {
            cout << s[i];
        }
    }

}
