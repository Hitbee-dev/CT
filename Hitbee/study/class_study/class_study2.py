class Object():
    def __init__(self, hp, defence, atk):
        print(self)
        self.hp = hp            # 체력
        self.defence = defence  # 방어력
        self.atk = atk          # 공격력

    def get_damage(self, target):
        return max((self.atk - target.defence), 0)
    
    def attack(self, target):
        dmg = self.get_damage(target)
        target.hp -= dmg
        print(self.__class__, "가", target.__class__, f"를 때려서 {dmg}의 데미지를 입혔습니다!")

class Monster(Object): 
    def __init__(self, hp, defence, atk):
        # Object 상속, Object에 선언되어있는 변수를 같이 쓸 수 있다.
        # Object.__init__(self, 5, 0, 0)    # 1 직접 호출 방식
        #print(self)
        super().__init__(hp, defence, atk)           # 2 Monster(Object)의 self 호출 방식

class User(Object): 
    def __init__(self, hp, defence, atk, critical):
        # Object 상속, Object에 선언되어있는 변수를 같이 쓸 수 있다.
        # Object.__init__(self, 5, 0, 0)    # 1 직접 호출 방식
        #print(self)
        super().__init__(hp, defence, atk)           # 2 User(Object)의 self 호출 방식
        self.critial = critical

    # Method override
    def get_damage(self, target):
        import random
        dmg = super().get_damage(target)
        if random.random() * 100 < self.critial:
            print(f"{self.__class__} 로또 떠졌다! 2배 데미지!!!")
            dmg *= 2
        return dmg

monster = Monster(10, 1, 3)
chan = User(20, 5, 3, 50)

chan.attack(monster)
print(monster.hp)
        