#include <iostream>
using namespace std;

int main()
{

    /*
    A B C
    D E F     for n = 3
    G H I
    */
    int i, j, n;
    cin >> n;
    char ch = 'A';
    cout << "Patter1" << endl;
    for (i = 1; i <= n; i++)
    {
        for (j = 1; j <= n; j++)
        {
            cout << ch << " ";
            ch += 1;
        }
        cout << endl;
    }

    /*
    A B C
    B C D       for n = 3
    C D E
    */
    char c = 'A';
    cout << "Patter2" << endl;

    for (i = 1; i <= n; i++)
    {
        for (j = 1; j <= n; j++)
        {
            c = 'A' + i + j - 2;

            cout << c << " ";
        }
        cout << endl;
    }

    /*
    A
    B B             for n = 3
    C C C
    */
    char h = 'A';
    cout << "Patter3" << endl;

    for (i = 1; i <= n; i++)
    {
        for (j = 1; j <= i; j++)
        {
            cout << h << " ";
        }
        h += 1;
        cout << endl;
    }

    // Try pattern3 with formula (ch + i - 1)

    cout << "Patter4" << endl;
    /*
    A
    B C
    D E F           for n = 4
    G H I J
    */
    i = 1, j = 1;
    c = 'A';
    while (i <= n)
    {
        j = 1;
        while (j <= i)
        {
            cout << c << " ";
            c = c + 1;
            j = j + 1;
        }
        cout << endl;
        i = i + 1;
    }

    cout << "Pattern5" << endl;
    /*
    A
    B C
    C D E                for n = 4
    D E F G
    */
    char m = 'A';
    for (i = 1; i <= n; i++)
    {
        // int value = i;
        // c = 'A';

        for (j = 1; j <= i; j++)
        {
            m = 'A' + i + j - 2;

            cout << m << " ";
        }

        cout << endl;
    }
    /*Patern6:
    E
    D E
    C D E                            for n = 5
    B C D E
    A B C D E
    */
    cout << "Patern6:" << endl;
    char _n = 'A';
    for (i = 1; i <= n; i++)
    {
        _n = ('A' + n - i);
        // cout<<_n<<endl;
        // break;
        for (j = 1; j <= i; j++)
        {
            cout << _n << " ";
            _n += 1;
        }
        cout << endl;
    }
    /*
    Pattern7:
        *
       **
      ***
     ****
    *****
    */
    cout << "Pattern7:" << endl;
    for (i = 1; i <= n; i++)
    {
        int space_count = n - i;
        // first print spaces
        for (j = space_count; j >= 1; j--)
        {
            cout << " ";
        }
        // then print stars
        for (j = 1; j <= i; j++)
        {
            cout << "*";
        }
        cout << endl;
    }
    /*
    Pattern8:
    *****
    ****
    ***
    **
    *

    */
    cout << "Pattern8:" << endl;
    for (i = 1; i <= n; i++)
    {
        // first print stars
        for (j = i; j <= n; j++)
        {
            cout << "*";
        }
        cout << endl;
    }

    /*
       Patern9:
*****
 ****
  ***
   **
    *

    */

    cout << "Patern9:" << endl;
    for (i = 1; i <= n; i++)
    {
        int space_count = i - 1;
        // first print spaces
        for (j = space_count; j > 0; j--)
        {
            cout << " ";
        }
        // then print stars
        for (j = i; j <= n; j++)
        {
            cout << "*";
        }
        cout << endl;
    }
    /*
    Patern10:
    11111
     2222
      333
       44
        5
    */
    cout << "Patern10:" << endl;
    for (i = 1; i <= n; i++)
    {
        int space_count = i - 1;
        // first print spaces
        for (j = space_count; j > 0; j--)
        {
            cout << " ";
        }
        // then print stars
        for (j = i; j <= n; j++)
        {
            cout << i;
        }
        cout << endl;
    }
    /*
    Patern11:
        1
       22
      333
     4444
    55555
    */
    cout << "Patern11:" << endl;
    for (i = 1; i <= n; i++)
    {
        int space_count = n - i;
        // first print spaces
        for (j = space_count; j > 0; j--)
        {
            cout << " ";
        }
        // then print stars
        for (j = 1; j <= i; j++)
        {
            cout << i;
        }
        cout << endl;
    }

    /*Home work
    pattern12:
    1 2 3 4
      2 3 4
        3 4                  for n = 4
          4
*/

    cout << "Patern12:" << endl;
    for (i = 1; i <= n; i++)
    {

        // first triangle for space print
        int space_count = i - 1;
        for (j = space_count; j > 0; j--)
        {
            cout << " ";
        }
        int count = i;
        for (j = i; j <= n; j++)
        {
            cout << count;
            count += 1;
        }
        cout << endl;
    }

    /*    Patern13:
          1
        2 3                   for n = 4
      4 5 6
    7 8 9 10
*/
    int count = 1;
    cout << "Patern13:" << endl;
    for (i = 1; i <= n; i++)
    {
        int space_count = n - i;
        // cout<<space_count<<endl;break;
        // printing space triangle
        for (j = 1; j <= space_count; j++)
        {
            cout << " ";
        }
        // printing 2nd triangle
        for (j = 1; j <= i; j++)
        {
            cout << count;
            count += 1;
        }
        cout << endl;
    }

    /* Patern14:
          1
        1 2 1
      1 2 3 2 1
    1 2 3 4 3 2 1
*/

    cout << "Patern14:" << endl;
    for (i = 1; i <= n; i++)
    {
        int space_count = n - i;
        // printing space triangle
        for (j = 1; j <= space_count; j++)
        {
            cout << " ";
        }
        int count = 1;
        // printing 2nd triangle
        for (j = 1; j <= i; j++)
        {
            cout << count;
            count += 1;
        }
        // printing 3rd triangle
        int c = i - 1;
        for (j = 1; j < i; j++)
        {
            cout << c;
            c = c - 1;
        }
        cout << endl;
    }

    /*
       Patern15:
        1 2 3 4 5 5 4 3 2 1
        1 2 3 4 * * 4 3 2 1             for n = 5
        1 2 3 * * * * 3 2 1
        1 2 * * * * * * 2 1
        1 * * * * * * * * 1
    */

    cout << "Patern15:" << endl;
    for (i = 1; i <= n; i++)
    {
        // print 1st triangle
        int count = 1;
        for (j = i; j <= n; j++)
        {
            cout << count << " ";
            count += 1;
        }
        // print 2nd triangle
        // int var = i-1;
        for (j = 1; j < i; j++)
        {
            cout << "*"
                 << " ";
        }
        // print 3rd triangle
        for (j = 1; j < i; j++)
        {
            cout << "*"
                 << " ";
        }
        int count2 = n - i + 1;
        for (j = i; j <= n; j++)
        {
            cout << count2 << " ";
            count2 -= 1;
        }
        // count2 -= 1;

        cout << endl;
    }
    return 0;
}