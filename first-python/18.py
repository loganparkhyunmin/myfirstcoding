train=['성진','찬경','준영']

train.append('주아')
print('서울역 도착.//',train)

train.insert(0,'동빈')
print('대전역 도착.//',train)

train.sort()
print('부산역 도착.//',train)
print('오늘도 코딩별 기차를 이용해주셔서 감사합니다')


fruits=['바나나','딸기','두리안','망고']

if '딸기'in fruits:
    fruits.remove('딸기')
else:
    print('딸기는 fruits 안에 없습니다!')