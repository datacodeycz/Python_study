
class Animal:
    def __init__(self, name, hp, mp, attack):
        self.name = name  # 名字
        self.init_hp = 200
        self.hp = hp  # 血量
        self.mp = mp  # 蓝量
        self.init_mp = 200
        self.attack = attack  # 攻击力
        self.skills = []  # 存放多个技能
        pass

    def __str__(self):
        pass

    # 行为有哪些
    def is_alive(self):
        """判断是否死亡
        :return: bool
        当hp为0的时候，死亡，返回False，否则返回True
        """
        return self.hp > 0

    def can_cost(self, skills_mp_cost):
        """判断是否有蓝量
        :param skills_mp_cost:
        :return: bool
        当你能够满足这个技能的蓝条时，就返回True，否则返回False
        """
        return self.mp - skills_mp_cost >= 0
        pass

    # 3. 受到伤害
    def take_damage(self, skills_hp):
        """受到伤害
        :param skills_hp:
        :return: 返回受到的伤害
        受到技能的伤害，扣除一定的血量，如果不够，血量直接为0
        """
        return max(self.hp - skills_hp, 0)

    # 4. 使用技能
    def use_skill(self, skills, target):
        """使用技能
        :param skills:技能对象
        :param target: 接收者
        :return: None
        对target使用skills技能
        """
        # 1.先判断，有没有mp
        if self.can_cost(skills_mp_cost=skills.mp_cost):
            # 有蓝量
            self.mp = self.mp - skills.mp_cost
            # 2.用技能
            skills.effect(self, target)


class Cat(Animal):
    team = 'cat'


class Dog(Animal):
    team = 'dog'
