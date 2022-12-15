class Item():
    '''
    def print(self):
        # print("Hi")
        print(self)
    '''
    def print(this): # 여기서 알 수 있다, self는 예약어가 아니라 그냥 변수다.
        print(this)
    # 파이썬은 기본적으로 Static임을 알 수 있다.
    def print2():
        print("Hello")

a = Item()
a.print()
# Item.print() <- 불가능
Item.print("A") # 1 <- 둘 다 실행 됨
Item.print(a)   # 2 <- 둘 다 실행 됨

# a.print2() <- self를 받지 않아 사용 불가
Item.print2()

b = Item()
b.print()
Item.print(b)