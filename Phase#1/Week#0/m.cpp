#include <iostream>
#include <algorithm>

#define endl "\n"

using namespace std;

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

int main() {
    fastIO();

    int size, x;
    cin >> size;
    int arr[size];
    int l = 0, r = size - 1;
    int sum_l = 0, sum_r = 0, sum = 0;
    int count = 0;
    for (int i = 0; i < size; i++) {
        cin >> arr[i];
        sum += arr[i];
    }
    sort(arr, arr + size);
    reverse(arr, arr + size);

    for (int i = 0; i < size; i++) {
        sum_l += arr[i];
        count++;
        if (sum_l > sum / 2) {
            break;
        }
    } 
    cout << count << endl;
}
