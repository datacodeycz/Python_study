from src.models.fighter import AngelCat, AttackDog
from src.models.skills import Skills


def battle(fighter1, fighter2):
    """回合制战斗流程实现
    :param fighter1: Animal 子类实例
    :param fighter2: Animal 子类实例
    :return: None
    """
    print("--------游戏开始----------")
    print("左手方信息如下")
    print(fighter1)
    print("右手方信息如下")
    print(fighter2)
    print("开始战斗")
    # 回合数
    # turn
    trun = 0

if __name__ == '__main__':
    skill_cat_1 = Skills('暗影斩击', type_='伤害', attack_cost=5, mp_cost=20)  # 关键字描述
    skill_cat_2 = Skills('生命回复', type_='治疗', hp_life=30 , mp_cost=15)  # 关键字描述

    a_cat = AngelCat('小猫', 200, 200, 20, [skill_cat_1, skill_cat_2])
    a_dog = AttackDog('小狗', 200, 200, 20, [skill_cat_1, skill_cat_2])
    battle(a_cat, a_dog)
    pass
