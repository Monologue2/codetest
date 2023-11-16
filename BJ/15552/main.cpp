#include <iostream>

using namespace std;

int main(int argc, char* argv[]){
    // 이 코드는 C와 C++의 표준 stream의 동기화를 끊는 역할을 한다.
    // printf scanf getchar 사용 불가
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);

    int N;
    cin >> N;
    for(int i = 0; i < N; i++){
        int A, B;
        cin >> A >> B;
        cout << A + B << '\n';
    }
}