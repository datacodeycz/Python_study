# 技能类
import random


class Skills:

    def __init__(self, name, type_, attack_cost=0, mp_cost=0, hp_life=0) -> None:
        self.name = name  # 技能名
        self.type_ = type_  # 技能类型
        self.attack_cost = attack_cost  # 伤害
        self.mp_cost = mp_cost  # 消耗值
        self.hp_life = hp_life  # 恢复值
        pass

    def effect(self, user, target):
        """使用技能

        :param user: 技能的使用者
        :param target: 技能的接收者
        :return:
        """
        pass

        if self.type_ == '伤害':
            # 1. 计算伤害
            # 1. 普通情况
            damage = int(self.attack_cost * user.attack)  # 攻击力 * 技能伤害
            # 2. 暴击情况
            if random.random() < 0.1:
                damage = damage * 3
            # 2. 谁对谁造成了伤害
            print(f"{user.name}对{target.name}使用了{self.name}, 造成了{damage}点伤害")
            hp = target.take_damage(damage)
            # 3. 受到伤害的宠物扣血
            target.hp = hp

        if self.type_ == '治疗':
            #  1.计算治疗量
            heal = self.hp_life
            #  2. 把治疗量给使用者
            print(f'{user.name}使用了{self.name}技能，恢复了自身{heal}点血量')
            user.hp = min(user.hp + heal, user.init_hp)
            pass


