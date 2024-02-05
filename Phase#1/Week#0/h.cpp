#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--)
    {
        int size;
        cin >> size;
        int arr[size];
        int minmum;
        for (int i = 0; i < size; i++)
        {
            cin >> arr[i];
            if (i == 0) {
                minmum = arr[i];
            } else {
                if (arr[i] < minmum) {
                    minmum = arr[i];
                }
            }
        }
        int count = 0;
        for (int i = 0; i < size; i++)
        {
            count += arr[i] - minmum;
        }
        cout << count << endl;
    }
}
