#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;

    while (n--)
    {
        int size;
        cin >> size;
        char last;
        for (int i = 0; i < size; i++)
        {
            char c;
            cin >> c;
            if (i == 0) {
                last = c;
            }
            if (c > last) {
                last = c;
            }
        }
        cout << int (last - 'a') + 1 << endl;

    }
    
}
