# 필요한 라이브러리 불러오기
import random

# choices 정의하기
# choices="HT"
choices=["앞면","뒷면"]

# 무작위로 고르기
coinToss= random.choice(choices)

# 고른 것을 출력하기
print(coinToss,"입니다")