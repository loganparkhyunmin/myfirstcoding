import random

cChoice=random.choice("SRP")

print("가위,바위,보?")
uChoice=input("S(가위),R(바위),P(보) 중 하나를 고르세요: ").upper().strip()

print("여러분: ",uChoice)
print("컴퓨터: ",cChoice)

if uChoice == cChoice:
    print("무승부입니다!")
else:
    if uChoice == "S":
        if cChoice=="R":
            print("여려분이 졌습니다")
        elif cChoice=="P":
            print("여려분이 이겼습니다")
    elif uChoice == "R":
        if cChoice=="P":
            print("여려분이 졌습니다")
        elif cChoice=="S":
            print("여려분이 이겼습니다")   
    elif uChoice == "P":
        if cChoice=="S":
            print("여려분이 졌습니다")
        elif cChoice=="R":
            print("여려분이 이겼습니다")   
