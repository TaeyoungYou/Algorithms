#include<iostream>
#include<string>
#include<ctime>

using namespace std;

int main() {
    time_t now = time(nullptr);
    struct tm* t = localtime(&now);
    int initYear = 1900;
    int initMon = 1;
    cout<<t->tm_year + initYear<<"-"<<t->tm_mon + initMon<<"-"<<t->tm_mday<<endl;
    return EXIT_SUCCESS;
}