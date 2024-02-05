#include <iostream>
#include <map>
using namespace std;

int main()
{
    int size;
    cin >> size;

    int arr[size];
    for (int i = 0; i < size; i++)
        cin >> arr[i];
    map<int, int> m;

    for (int i = 0; i < size; ++i) {
        m[arr[i]]++;
    }

    int max_height = 0;
    int total_towers = 0;

    for (const auto& entry : m) {
        if (entry.second > max_height) {
            max_height = entry.second;
        }
        total_towers++;
    }
    cout << max_height << " " << total_towers;
}
