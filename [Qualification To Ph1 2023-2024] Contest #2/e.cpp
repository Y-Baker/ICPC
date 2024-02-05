#include <iostream>
using namespace std;

int main()
{
    int num;
    bool flag = false;
    cin >> num;

    string str;
    while (num--)
    {
        flag = false;
        cin >> str;
        string re;
        for (int i = 0; i < str.size(); i++)
        {
            if (flag)
            {
                flag = false;
                continue;
            }
            if (str[i + 1] == '\0' || str[i] != str[i + 1])
            {
                if (re.find(str[i]) == string::npos)
                {
                    re += str[i];
                }
            }
            else
                flag = true;
        }

        for (int i = 0; i < re.size(); i++)
        {
            for (int j = i + 1; j < re.size(); j++)
            {
                if (re[i] > re[j])
                {
                    char temp = re[i];
                    re[i] = re[j];
                    re[j] = temp;
                }
            }
        }
        for (int i = 0; i < re.size(); i++)
            cout << re[i];
        cout << endl;
    }
    
}
