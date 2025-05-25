class Hero:
    def __init__(self, name, health):
        self.__name =  name
        self.__health = health

    def get_name(self):
        return self.__name
    
    def get_health(self):
        return self.__health
    
    def take_damage(self, damage):
        self.__health -= damage

class Archer(Hero):
    def __init__(self, name, health, num_arrows):
        super().__init__(name, health)
        self.__num_arrows = num_arrows
    
    def shoot(self, target):
        if self.__num_arrows <= 0:
            raise Exception("not enough arrows")
        self.__num_arrows -= 1
        target.take_damage(10)

class Wizard(Hero):
    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self.__mana = mana
    
    def cast(self, target):
        if self.__mana < 25:
            raise Exception("not enough mana")
        self.__mana -= 25
        target.take_damage(25)


class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        if (self.pos_x >= x_1 and self.pos_x <= x_2) and (self.pos_y >= y_1 and self.pos_y <= y_2):
            return True
        return False

class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        x_fire_range_left, x_fire_range_right = x - self.__fire_range, x + self.__fire_range
        y_fire_range_left, y_fire_range_right = y - self.__fire_range, y + self.__fire_range
        
        self.unit_hit_list = []
        for unit in units:
            if unit.in_area(x_fire_range_left, y_fire_range_left, x_fire_range_right, y_fire_range_right) == True:
                self.unit_hit_list.append(unit)
        return self.unit_hit_list


chai = [1, 2, 3 ,4]
print(chai.pop())