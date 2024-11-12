#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<unordered_set>
#include<unordered_map>

using namespace std;

void modifyByValue(int);
void modifyByRef(int&);
void vectorIntro();
void setIntro();
void mapIntro();
void unorderedIntro();

int main() {
    // 정수형 변수 선언 및 산술 연산
    int a = 13;
    int b = 4;
    cout<<a+b<<endl;
    cout<<a-b<<endl;
    cout<<a*b<<endl;
    cout<<a/b<<endl;
    cout<<a%b<<endl;
    cout<<-a<<endl;

    // 정수형 비교 연산
    a = 13;
    b = 4;
    cout<< (a==b) <<endl;
    cout<< (a!=b) <<endl;
    cout<< (a>b) <<endl;
    cout<< (a<b) <<endl;
    cout<< (a>=b) <<endl;
    cout<< (a<=b) <<endl;

    // 정수형 비트 연산
    a = 13;
    b = 4;
    cout<< (a&b) <<endl;
    cout<< (a|b) <<endl;

    // 부동소수형 사칙 연산
    double d = 2.5;
    float f = 1.5f;
    cout << sizeof(d) << endl;
    cout << sizeof(f) << endl;
    cout << d << " " << endl;
    cout << d+f << endl;
    cout << d-f << endl;
    cout << d*f << endl;
    cout << d/f << endl;

    // 형변환
    int i = 65;
    f = 5.2f;
    d = i + f;  // 암시적 형 변환 (메모리가 큰 float형으로 변환)
    cout << d << endl;
    // 명시적 형변환
    cout << static_cast<int>(d) << endl;
    cout << static_cast<char>(i) << endl;

    // 문자열 선언 및 초기화
    string str1;
    string str2 = "Hello World";
    string str3(str2);
    string str4(str2, 0, 5);
    string str5(10, '*');

    cout<<str1<<endl<<str2<<endl<<str3<<endl<<str4<<endl<<str5<<endl;

    // 문자열 찾기
    string str = "Hello, C++ World!";
    size_t pos1 = str.find("Hello");
    size_t pos2 = str.find('C');
    size_t pos3 = str.find("Hello", 2);
    size_t pos4 = str.find("Python");

    cout<<pos1<<endl<<pos2<<endl<<pos3<<endl<<pos4<<endl;

    /**
     * 18446744073709551615은 string::npos값
     * size_t 타입: 주로 문자열의 크기 및 인덱스 표현할 때 사용
     */

    // replace 사용
    str = "APPLE";
    str += ", World!";
    cout<<str<<endl;

    str[7] = 'P';
    cout<<str<<endl;

    str.replace(7,4,"Col");
    cout<<str<<endl;

    // STL
    // call by value
    int value = 5;
    cout<<"주소 : "<<&value<<endl;
    cout<<"값 : "<<value<<endl;
    modifyByValue(value);
    cout<<"값 : "<<value<<endl;
    /**
     * call by value로 하면 주솟값을 넘기지 않기 때문에 값은 바뀌지 않음
     */

    // call by reference
    value = 5;
    cout<<"주소 : "<<&value<<endl;
    cout<<"값 : "<<value<<endl;
    modifyByRef(value);
    cout<<"값 : "<<value<<endl;

    // auto문
    auto num = 42;  // int로 추론
    cout<<num<<endl;
    auto pi = 3.14159;  // double로 추론
    cout<<pi<<endl;
    auto greeting = string("Hello world");  // string으로 추론
    cout<<greeting<<endl;

    // 범위기반 반복문
    vector<int> vec = {1,2,3,4,5};
    for(int num : vec) {
        cout<<num<<" ";
    }
    cout<<endl;

    map<string, int> fruitMap = {{"apple",1},{"banana",2},{"cherry",3}};
    for(const auto& pair : fruitMap) {
        cout<<pair.first<<"="<<pair.second<<" ";
    }
    cout<<endl;

    set<string> fruitSet = {"apple","banana","cherry"};
    cout<<"Set: ";
    for(const auto& fruit : fruitSet) {
        cout<<fruit<<" ";
    }
    cout<<endl;

    // 반복자
    // Vector에서의 순방향 반복자
    vec = {10,20,30,40,50};
    for(auto it = vec.begin(); it != vec.end(); ++it) {
        cout<<*it<<" ";
    }
    cout<<endl;

    auto result = find(vec.begin(), vec.end(), 30);
    if(result != vec.end()) {
        cout<<"Found: "<<*result<<endl;
    }else {
        cout<<"Not found"<<endl;
    }

    // Map에서의 순방향 반복자
    map<string, int> myMap = {{"apple",1},{"banana",2},{"cherry",3}};

    for(auto it = myMap.begin(); it != myMap.end(); ++it) {
        cout<<it->first<<" : "<<it->second<<endl;
    }

    auto result2 = myMap.find("banana");
    if(result2 != myMap.end()) {
        cout<<"Found: "<<result2->first<<" -> "<<result2->second<<endl;
    }else {
        cout<<"Not Found"<<endl;
    }

    // 역방향 반복자
    vec = {10,20,30,40,50};
    for(auto it = vec.rbegin(); it != vec.rend(); ++it) {
        cout<<*it<<" ";
    }
    cout<<endl;

    auto result3 = find(vec.rbegin(), vec.rend(), 30);
    if(result3 != vec.rend()) {
        cout<<"Found: "<<*result3<<endl;
    }else {
        cout<<"Not Found"<<endl;
    }

    // STL-2
    /**
     * STL의 컨테이너는 데이터를 저장하는 객체
     * 소개할 컨테이너는 벡터, 셋, 맵, 우선수위 큐
     */
    // vector
    vectorIntro();

    // set
    setIntro();

    // map
    mapIntro();

    // 정렬되지 않는 set, map
    unorderedIntro();

    // STL의 알고리즘
    // count()함수는 컨테이너 내에서 특정 값이 나타나는 횟수를 셈
    vector<int> v = {1,4,3,4,4,5,4,5};
    cout<<count(v.begin(), v.end(),5)<<endl;

    // sort() 함수로 정렬
    sort(v.begin(), v.end());
    sort(v.rbegin(), v.rend());
    sort(v.begin(), v.end(), [](const auto& a, const auto& b){return a<b;});

    // next_permutation() 함수로 순열 생성
    vector<int> perVec = {1,2,3};
    do {
        for(int i : perVec) {
            cout<<i<<" ";
        }
        cout<<endl;
    } while(next_permutation(perVec.begin(), perVec.end()));

    // unique() 함수로 중복 정리
    // 연속된 중복 요소를 제거하고, 중복되지 않는 고유한 요소들은 앞으로 모이게 한다
    // 제체의 크기는 줄이지 않되 새로운 끝부분, 요소가 중복되지 않는 끝부분을 반환
    v = {1,2,3,3,4,4,4,5,5,6};
    auto newEnd = unique(v.begin(), v.end());
    for(auto it = v.begin(); it != newEnd; ++it) {
        cout<<*it<<" ";
    }
    cout<<endl;

    // binary_search() 함수로 이진 탐색
    vector<int> bin_v = {1,2,3,4,5,6};
    cout<<binary_search(bin_v.begin(), bin_v.end(),3)<<endl;
    cout<<binary_search(bin_v.begin(), bin_v.end(), 7)<<endl;

    // max_element(), min_element() 함수로 최댓값, 최솟값 위치 구하기
    vector<int> el_v = {1,3,5,7,2,4,6};
    auto maxIt = max_element(el_v.begin(), el_v.end());
    auto minIt = min_element(el_v.begin(), el_v.end());
    cout<<*maxIt<<endl;
    cout<<*minIt<<endl;
    return 0;
}

void modifyByValue(int value) {
    value = 10;
    cout<<"주소 : " <<&value<<endl;
    cout<<"값 : "<<value<<endl;
}

void modifyByRef(int& value) {
    value = 10;
    cout<<"주소 : "<<&value<<endl;
    cout<<"값 : "<<value<<endl;
}

void vectorIntro() {
    /**
     * vector는 배열과 매우 유사한 컨테이너
     * 데이터를 순차적으로 저장하고, 인덱스를 통해서 특정 위치의 원소에 쉽게 접근할 수 있음
     */
    vector<int> v;  // 빈 vector
    vector<int> v2 = {1,2,3,4,5};   // 초기화 리스트를 활용해서 초기화와 동시에 원소 다섯개 넣은 vector
    vector<int> v3(4,3);    // 초기 벡터의 크기를 4로 하고, 모든 원소를 3으로 채운다
    vector<int> v4(v3);     // v3를 복사해서 v4에 독립된 새로운 백터 생성

    vector<vector<int>> v_1;     // 빈 2차원 vector 선언
    // 특정 크기로 초기화된 2차원 vector
    int rows = 3;
    int cols = 4;
    vector<vector<int>> v_2(rows, vector<int>(cols));
    // 특정 값으로 초기화된 2차원 벡터
    int val = 9;
    vector<vector<int>> v_3(rows, vector<int>(cols, val));
    // 초기화 리스트를 사용한 2차원 vector 초기화
    vector<vector<int>> v_4 = {
        {1,2,3},
        {4,5,6},
        {7,8,9}
    };

    // 원소 변경
    vector<int> vec = {1,2,3,4,5,6};
    vec[2] = 10;

    // vector의 삽입과 삭제
    vec = {2,3,4,5};
    vec.push_back(6);
    vec.pop_back();
    vec.insert(vec.begin(), 1);
    vec.erase(vec.begin());
}

void setIntro() {
    /**
     * Set은 중복을 허용하지 않고, 저장된 데이터를 자동으로 정렬하는 컨테이너, 집합
     */

    // Set 선언 및 초기화
    set<int> s1;    // 빈 set 선언
    set<int> s2 = {3,1,2,3,5};      // 초기화 리스트를 사용한 set 초기화
    set<int> s3(s2);    // 다른 set을 사용하여 초기화

    // set에서 원소 탐색
    set<int> nums = {1,2,3,4,5,6};
    int targets[] = {3,7};
    for(int target : targets) {
        auto it  = nums.find(target);
        if(it != nums.end()) {
            cout<<"원소 : "<<target<<"를 찾았습니다. 값: "<<*it<<endl;
        }else {
            cout<<"원소 : "<<target<<"를 찾지 못했습니다."<<endl;
        }
    }

    // set의 삽입과 삭제
    set<int> s_1 = {1,3,2,1,5};
    s_1.insert(4);
    s_1.erase(2);
    auto it = s_1.find(4);
    if(it != s_1.end()) {
        cout<<"삽입 됨"<<endl;
    }

}

void mapIntro() {
    /**
     * 키와 값을 쌍으로 갖는 컨테이너
     * 키와 값의 쌍을 entry, STL에서는 std::pair 타입으로 표현
     */

    // map의 선언 및 초기화
    map<string, double> employeeSalaries;   // 빈 map 선언
    map<string, double> studentGrades = {
        {"John",3.7},
        {"Emma",3.9},
        {"Sophia",4.0}
    };

    // map에서 특정 키에 접근
    map<string, int> studentScores;

    studentScores["Alice"] = 95;
    studentScores["Bob"] = 88;
    studentScores["Charlie"] = 92;

    cout<<studentScores["Alice"]<<endl;
    cout<<studentScores["rabbit"]<<endl;

    auto it = studentScores.find("Charlie");
    if(it != studentScores.end()) {
        cout<<it->second<<endl;
    }

    // map의 값 변경
    map<string, int> myMap = {{"Apple",1},{"Banana",2},{"Cherry",3}};
    myMap["Banana"] = 10;

    // map의 삽입
    myMap.insert(make_pair("Apple",1));
    myMap.insert({"Banana",2});
    myMap["Cherry"] = 3;
    myMap.erase("Apple");
}

void unorderedIntro() {
    /**
     * STL의 set과 map은 기본적으로 이진 탐색 트리, 정렬 상태 유지
     * 정렬이 필요없다면 성능 저하
     * 정렬되지 않는 set과 정렬되지 않는 map
     * unordered_set, unordered_map
     */

    unordered_set<int> mySet;
    mySet.insert(3);
    mySet.insert(4);
    mySet.insert(4);
    mySet.insert((2));

    for(int num : mySet) {
        cout<<num<<" ";
    }
    cout<<endl;

    unordered_map<int, string> myMap;
    myMap[1] = "apple";
    myMap[2] = "banana";
    myMap[3] = "cherry";

    for(auto key : myMap) {
        cout<<key.first<<" : "<<key.second<<endl;
    }
}