#include <iostream>
#include <cstring>
#include <string>
#include <cctype>
using namespace std;

string upperCase_convert(string str){
    char ch;
    int i;
    string newStr="";
    for(i=0; i<str.length(); i++){
        ch = toupper(str[i]);
        newStr += ch;
    }
    return newStr;
}

void curvedBand(){
    float dt, angle;
    cout << "Enter the degrees measured from the spiral log pattern: ";
    cin >> angle;
    string W;
    if(angle < 0) //Boundary condition
        cout << 1.0;
    if(angle <= 0.35)
        dt = 2.0;
    else if(angle <= 0.55)
        dt = 2.5;
    else if(angle <= 0.75)
        dt = 3.0;
    else if(angle <= 1)
        dt = 3.5;
    else if(angle <= 1.3)
        dt = 4.0;
    else if(angle <= 1.7)
        dt = 4.5;
    else 
        cout << "DT: " << 1.0;
    cout << "What is the curved band color? ";
    cin >> W;
    W = upperCase_convert(W);
    if(!W.compare("W") || !W.compare("CMG") || !W.compare("CDG"))
        cout << "DT: "<< (dt+0.5);
    else
        cout << "DT: " << dt;
}

void shearPattern(){
    float dist, dt, diam;
    cout << "Enter the diameter of the CB in degrees (must be >1.5 degrees for DT>2.0): ";
    cin >> diam;
    cout << "Enter distance of LLC from DG convection in degrees: ";
    cin >> dist;
    if(dist >= 0.75)
        dt = 2.0;
    else if(dist >= 0.5)
        dt = 2.5;
    else if(dist <= 0.49 && dist >= -0.32) 
        dt = 3.0; //Here, -ve distance means that the LLC is only partially exposed and inside convection.
    else if(dist < -0.32)
        dt = 3.5;
    else //Boundary case
        dt = 1.0;
    if(diam <= 1.5)
        cout << "DT: " << 2.0;
    else
        cout << "DT: " << dt;
}

int embedCode(string ctops){
    if(ctops.compare("CMG")==0)
        return 0;
    else if(ctops.compare("W")==0)
        return 1;
    else if(ctops.compare("B")==0)
        return 2;
    else if(ctops.compare("LG")==0)
        return 3;
    else if(ctops.compare("MG")==0)
        return 4;
    else if(ctops.compare("DG")==0)
        return 5;
    else if(ctops.compare("OW")==0)
        return 6;
    return 0;
}
int surrCode(string ctops){
    if(ctops.compare("CMG")==0)
        return 6;
    else if(ctops.compare("W")==0)
        return 5;
    else if(ctops.compare("B")==0)
        return 4;
    else if(ctops.compare("LG")==0)
        return 3;
    else if(ctops.compare("MG")==0)
        return 2;
    else if(ctops.compare("DG")==0)
        return 1;
    else if(ctops.compare("OW")==0)
        return 0;
    return 0;
}
int eyeCode(string ctops){
    if(ctops.compare("WMG")==0)
        return 0;
    else if(ctops.compare("OW")==0)
        return 1;
    else if(ctops.compare("DG")==0)
        return 2;
    else if(ctops.compare("MG")==0)
        return 3;
    else if(ctops.compare("LG")==0)
        return 4;
    else if(ctops.compare("B")==0)
        return 5;
    else if(ctops.compare("W")==0)
        return 6;
    return 0;
}

void eyePattern(){
    float eyeAdjustment[7][7] = {{0, -0.5, -2, -2, -2, -2, -2}, 
                                 {0, 0, -0.5, -2, -2, -2, -2},
                                 {0, 0, -0.5, -0.5, -2, -2, -2},
                                 {0.5, 0, 0, -0.5, -0.5, -2, -2},
                                 {1, 0.5, 0, 0, -0.5, -0.5, -2},
                                 {1, 0.5, 0.5, 0, 0, -1, -1},
                                 {1, 0.5, 0.5, 0, 0, -0.5, -1}};
    float eyeNum[7] = {6.5, 6, 5.5, 5, 4.5, 4.5, 4};
    float dt;

    string embed, surr, eye;
    cout << "Enter embedded ring of CTOPs around the eye (in caps): ";
    cin >> embed;
    cout << "Enter surrounding ring of CTOPs around the eye (in caps): ";
    cin >> surr;
    cout << "Enter eye temp (in caps): ";
    cin >> eye;

    dt = eyeNum[embedCode(upperCase_convert(embed))] + eyeAdjustment[surrCode(upperCase_convert(surr))][eyeCode(upperCase_convert(eye))];
    cout << "DT: " << dt; 
}

int embeddedCode(string embed){
    if(embed.compare("CDG")==0 || embed.compare("CMG")==0 || embed.compare("W")==0)
        return 0;
    else if (embed.compare("B")==0)
        return 1;
    else if(embed.compare("LG")==0)
        return 2;
    else if(embed.compare("MG")==0)
        return 3;
    else if(embed.compare("DG")==0)
        return 4;
    else if(embed.compare("OW")==0)
        return 5;
    return 0;
}

void embeddedPattern(){
    float dt;
    string embed;
    float cf[6] = {5, 5, 4.5, 4, 4, 3.5};
    cout << "Enter embedded value: ";
    cin >> embed;
    dt = cf[embeddedCode(upperCase_convert(embed))];
    cout << "DT: " << dt;
}

int main(){
    float ft24, ft12;
    int ch=0;
    cout << "Enter FT of the last 24 hours. Enter 1.0 if the system has been designated in the last 24 hours.\n";
    cin >> ft24;
    cout << "Enter FT of the last 12 hours.\n";
    cin >> ft12;
    do{
        cout << "\n--------Dvorak DT calculator---------";
        cout << "\n1. Curved Band Scene";
        cout << "\n2. Shear pattern";
        cout << "\n3. Eye pattern";
        cout << "\n4. Embedded CDO pattern";
        cout << "\n5. Exit";
        cout << "\nEnter choice[1-5]: ";
        cin >> ch;

        switch(ch){
            case 1:
            curvedBand();
            break;

            case 2:
            cout << "While this calculator shall proceed, it must be noted that MET is recommended for this mode.\n";
            shearPattern();
            break;

            case 3:
            if(ft24 <= 2)
                cout << "\nEye pattern is not allowed if 24 hour FT is not greater than FT2.0.";
            else
                eyePattern();
            break;
            
            case 4:
            if(ft12 <= 3)
                cout << "\nEmbedded pattern is only allowed if 12 hour FT is >= FT3.5.";
            else
                embeddedPattern();
            break;

            case 5:
            cout << "\nThanks for using!";
            break;

            default:
            cout << "\nInvalid input!";
        }
    }while(ch!=5);
    return 0;
}