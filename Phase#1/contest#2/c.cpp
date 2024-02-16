#include <iostream>
#include <unordered_set>
#define endl "\n"

using namespace std;

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

int main() {
    fastIO();

    int size;
    int flag = false;
    cin >> size;
    int arr[size];

    for (int i = 0; i < size; i++) {
        cin >> arr[i];
    }

    unordered_set <int> s;

    for (int i = size - 1; i >= 0; i--) {
        s.insert(arr[i]);
    }

    cout << s.size() << endl;
    for (auto it : s) {
        if (flag) {
            cout << " ";
        }
        cout << it;
        flag = true;
    }
}
