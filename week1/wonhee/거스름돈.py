n=1260
count=0

#큰 단위의 화폐부터 차례대로 확인
coin_types=[500,100,50,10]

for coin in coin_types:
	count+= n//coin #각 화폐 단위로 거슬러 줄 수 있는 동전의 개수 세기
	n%=coin #해당 화폐 단위로 거슬러 줄 수 있는 만큼 거슬러주고 남은 거스름돈을 업데이트

print(count)