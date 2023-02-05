#include <iostream>
#include <vector>
using namespace std;

int main() {
	int n, k;
	cin >> n >> k;

	vector<int> arr(n);
	for (int i = 0; i < n; i++) cin >> arr[i];

	int i, j, newItem, cnt=0;
	
	// 삽입정렬 알고리즘
	for (i = 1; i < n; i++) {
		newItem = arr[i];
		for (j = i - 1; j >= 0; j--) {
			if (newItem < arr[j]) {
				arr[j + 1] = arr[j]; // 위치 업데이트 시 cnt++
				cnt++;
				if (cnt == k) {
					cout << arr[j+1];
					return 0;
				}
			}
			else break;
		}
		
		if (j + 1 != i) {  // newItem이 같은 위치인 경우 굳이 다시 저장할 필요 X
			arr[j + 1] = newItem;  // 위치 업데이트시 cnt++
			cnt++; 
		}
		if (cnt == k) {
			cout << arr[j+1];
			return 0;
		}
	}
	// return에 걸리지 않음 = 이동횟수가 k보다 작음
	cout << -1;
}

