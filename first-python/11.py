import random

ans=random.randrange(1,51)

while True:

    num = int(input('숫자를 입력하세요: '))

    if num>ans:
        print('그 수보다 작아 이뮹텅아') 
    elif num<ans:
        print('그 수보다 커 이 똥꾸빵구야')
    else:
        print('이제야 맞췃냐? 이바부야!!정답')
        break