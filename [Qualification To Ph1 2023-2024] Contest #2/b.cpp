#include <iostream>
using namespace std;

#define TOTAL_SECONDS_IN_DAY 86400

int main()
{
    int days;
    int seconds_needed;
    cin >> days >> seconds_needed;

    int busy_time[days];
    for (int day = 0; day < days; day++)
        cin >> busy_time[day];

    int needed_days = 0;

    while (seconds_needed > 0)
    {
        seconds_needed -= TOTAL_SECONDS_IN_DAY - busy_time[needed_days];
        needed_days++;
    }

    cout << needed_days;
}
