#include <iostream>
using namespace std;

struct point {
    int x;
    int y;
};

int main()
{
    int size;
    cin >> size;
    point p1, p2;
    int num_of_moves;
    while (size--)
    {
        num_of_moves = 0;
        cin >> p1.x >> p1.y >> p2.x >> p2.y;
        if (p1.x == p2.x)
            num_of_moves += abs(p1.y - p2.y);
        else if (p1.y == p2.y)
            num_of_moves += abs(p1.x - p2.x);
        else
            num_of_moves += abs(p1.x - p2.x) + abs(p1.y - p2.y);
        cout << num_of_moves << endl;
    }
    
    return (0);
}