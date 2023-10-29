animals=["이구아나","개","개미","고양이","박쥐","장어"]
print(len(animals))
print(animals[2])

animals[2]="암소"
print(animals)

animals.append("여우")
print(animals)

animals.remove("여우")
print(animals)

animals.sort()
print(animals)

animals.append("염소")
print(animals)

if "염소"in animals:
    print("yes")
else:
    print("no")