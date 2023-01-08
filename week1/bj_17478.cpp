#include <iostream>
using namespace std;

// 백준은 endl대신 \n을 쓰자.
void recursion(int n, int m) {
	for (int i = 0; i < 4*(m-n); i++) cout << "_";
	cout << "\"재귀함수가 뭔가요? \"" << endl;
	if (n == 0) { // Base case: 종료 조건
		for (int i = 0; i < 4 * (m - n); i++) cout << "_";
		cout << "\"재귀함수는 자기 자신을 호출하는 함수라네\"" << endl;
		for (int i = 0; i < 4 * (m - n); i++) cout << "_";
		cout << "라고 답변하였지." << endl;
	}
	else {
		for (int i = 0; i < 4 * (m - n); i++) cout << "_";
		cout << "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어." << endl;
		for (int i = 0; i < 4 * (m - n); i++) cout << "_";
		cout << "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지." << endl;
		for (int i = 0; i < 4 * (m - n); i++) cout << "_";
		cout << "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"" << endl;
		recursion(n - 1, m); // Recursive case: 재귀
		for (int i = 0; i < 4 * (m - n); i++) cout << "_";
		cout << "라고 답변하였지." << endl;
	}
}

int main() {
	int k;
	cin >> k;
	cout << "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다." << endl;
	recursion(k, k); // _를 4의 배수로 출력할 for문을 위해 매개변수 2개 필요
}