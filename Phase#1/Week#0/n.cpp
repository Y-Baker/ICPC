#include <iostream>
using namespace std;

int main ()
{
    int n, x;
    long long sum = 0;
    cin >> n;
    for (int i = 0 ; i < n ; i ++)
    {
        cin >> x ;
        sum += x ;
    }
    cout << abs(sum) << endl;
}
