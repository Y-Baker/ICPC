#include <iostream>
using namespace std;

#define NEEDED_TIME_PER_ITEM 5
#define NEEDED_TIME_PER_CUSTOMER 15


int main() {
    int num_cashiers, total_people, items, second_needed;
    int minumum_time = INT32_MAX;
    cin >> num_cashiers;

    int cashiers[num_cashiers];

    for (int i = 0; i < num_cashiers; i++)
        cin >> cashiers[i];

    for (int i = 0; i < num_cashiers; i++) {
        second_needed = NEEDED_TIME_PER_CUSTOMER * cashiers[i];
        for (int j = 0; j < cashiers[i]; j++) {
            cin >> items;
            second_needed += items * NEEDED_TIME_PER_ITEM;
        }
        if (minumum_time > second_needed)
            minumum_time = second_needed;
    }
    cout << minumum_time;
    return 0;
}
