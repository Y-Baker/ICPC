#include <iostream>
using namespace std;

int main()
{
    int operations, totat, num;
    cin >> operations >> totat;

    int failed = 0;
    char state;
    for (int i = 0; i < operations; i++)
    {
        cin >> state >> num;
        if (state == '+')
            totat += num;
        else
        {
            if (totat >= num)
                totat -= num;
            else
                failed++;
        }
    }
    cout << totat << " " << failed;
}

