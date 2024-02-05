#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    while (n--) {
        int size;
        cin >> size;

        int arr[size];
        int sum_a = 0, sum_b = 0;
        for (int i = 0; i < size; i++) {
            cin >> arr[i];
            if (arr[i] % 2 == 0) {
                sum_a += arr[i];
            } else {
                sum_b += arr[i];
            }
        }
        if (sum_a > sum_b) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
}
