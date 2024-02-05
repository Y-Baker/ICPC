#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int minumum_distinct(int arr[], int size);


int main() {
    int t;
    cin >> t;

    while (t--)
    {
        int size;
        cin >> size;
        int arr[size];
        for (int i = 0; i < size; i++)
        {
            cin >> arr[i];
        }
        cout << minumum_distinct(arr, size) << endl;
    }
}

int minumum_distinct(int arr[], int size)
{
    vector <int> v;
    for (int i = 0; i < size; i++)
    {
        if (find(v.begin(), v.end(), arr[i]) == v.end())
        {
            v.push_back(arr[i]);
        }
    }
    int unique = v.size();
    int deleted = size - unique;
    if (deleted % 2 == 1) {
        unique--;
    }

    return unique;
}
