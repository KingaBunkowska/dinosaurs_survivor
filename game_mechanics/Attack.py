import random

from game_mechanics.Position import Position
import math

class Attack:
    """
    superclass for any form of attack
    """

    def __init__(self, target, caster,speed = 8,range = float('inf'), penetrate=True, accuracy = 0):
        """
        :param target: coordinates of target
        :type target: Position

        :param caster: casting entity
        :type caster: Entity

        :param speed: speed of attack
        :type speed: float

        :param range: range of attack
        :type range: float

        :param penetrate: whether projectile pierce enemy or not TODO: implement piercing
        :type penetrate: bool
        """
        self.position = caster.position.copy()
        self.accuracy = accuracy
        self.angle, self.direction = self.calculate_angle(target)

        self.caster = caster
        self.penetrate = penetrate
        self.range = range
        self.speed = speed
        self.attacked = set()
        self.target = target

    #TODO: change name damage
    def calculate_dammage(self,target):
        """
        Calculate damage given with attack (impact of target statistics not taken into account)
        :param entity: object taking damage
        :return: The calculated damage output.
        :rtype: float
        """
        # TODO : connect to the statistics system
        if target in self.attacked:
            return 0
        self.attacked.add(target)
        return 1.

    def calculate_angle(self,target):
        """
        Calculate the firing angle
        :param target: Position  of target
        :type target: Position
        :return: The calulacted angle at witch self was fired, noramilzed vector indicating direction of momentum
        :rtype: (float, float)
        """

        vector = target - self.position
        vector.normalized()
        vector += Position(random.uniform(-self.accuracy,self.accuracy),random.uniform(-self.accuracy,self.accuracy))
        return math.degrees(math.atan2(-vector.y, vector.x)), vector
    
    def fly(self):
        """
        Move projectile in space and reduce remaining range
        """
        self.position += (self.direction * self.speed)
        self.range -= self.speed