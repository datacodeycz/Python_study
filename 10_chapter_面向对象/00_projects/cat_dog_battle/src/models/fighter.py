#  存放宠物角色的

from src.models.animal import Animal
from src.models.skills import Skills


# 天使猫
class AngelCat(Animal):
    def __init__(self, name, hp, mp, attack, skills):
        super().__init__(name, hp, mp, attack)
        self.skills = skills  # 技能加上

    def __str__(self):
        result = f'名字：{self.name}， 血量：{self.hp}, 蓝量：{self.mp},攻击力：{self.attack}, 技能为：\n'
        count = 0
        for skill in self.skills:
            if isinstance(skill, Skills):
                count = count + 1
                result = result + f'技能{count}:' + skill.name
        return result


# 恶魔犬
class AttackDog(Animal):
    def __init__(self, name, hp, mp, attack, skills):
        super().__init__(name, hp, mp, attack)
        self.skills = skills

    def __str__(self):
        result = f'名字：{self.name}， 血量：{self.hp}, 蓝量：{self.mp},攻击力：{self.attack}, 技能为：\n'
        count = 0
        for skill in self.skills:
            if isinstance(skill, Skills):
                count = count + 1
                result = result + f'技能{count}:' + skill.name
        return result


if __name__ == '__main__':
    skill_cat_1 = Skills('暗影斩击', type_='伤害', attack_cost=1.5, mp_cost=20)  # 关键字描述
    a_cat = AngelCat('小猫', 200, 200, 20, [skill_cat_1])
    a_dog = AttackDog('小狗', 200, 200, 20, [skill_cat_1])
    a_cat.use_skill(skill_cat_1, a_dog)
    print(a_dog.hp)
