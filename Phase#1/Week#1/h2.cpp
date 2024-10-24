#include <iostream>
#include <deque>
#include <vector>

#define endl "\n"

using namespace std;

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

void fn() {
    int n;
    cin >> n;
    string s;
    cin >> s;
    deque<int> arr(1, 0);
    auto it = arr.begin(); 
    for (int i = 0; i < n; i++) {
        if (s[i] == 'R') {
            it++; 
            arr.insert(it, i + 1); 
        } else {
            if (it == arr.begin()) {
                arr.insert(it, i + 1);
                it --;
            } else {
                arr.insert(it, i + 1);
            }
        }
    }
    for (auto x : arr) {
        cout << x << " ";
    }
    cout << endl;
}

int main() {
    fastIO();
    fn();
    return 0;
}
