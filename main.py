class 붕어빵:
    def __init__(self, name, contents, price):
        self.name = name
        self.contents = contents
        self.price = price
        self.total = 0

    def sell(self):
        print(f"{self.name}이 판매되었습니다.")
        self.total += self.price

    def eat(self):
        print(f"{self.name}을 먹었습니다.")
        self.total += self.price

# 객체 생성
슈크림 = 붕어빵("슈크림 붕어빵", "슈크림", 500)
팥 = 붕어빵("팥 붕어빵", "팥", 500)

슈크림.sell()
팥.sell()

슈크림.eat()
팥.eat()

print(f"{슈크림.total, 팥.total}원")