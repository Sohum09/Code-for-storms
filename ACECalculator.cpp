#include <iostream>
using namespace std;

int main()
{
    float input_kts = 0, duration = 0;
    float ACE = 0.0f;
    cout << "Enter the speed of each point in kts if the BT has it as a TC. Press 1 to stop.\n";
    do {
        cin>>input_kts;
        if(input_kts >= 35)
            ACE += (input_kts * input_kts) / 10000;
        duration += 6;
    } while (input_kts != 1);
    cout << "ACE: "<<ACE<<", Duration: "<<(duration-6) << " hours";
    return 0;
}
