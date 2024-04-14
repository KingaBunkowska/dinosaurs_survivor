from game_mechanics.Position import Position
import math

class Attack:
    """
    superclass for any form of attack
    """

    def __init__(self, target, caster):
        """
        Initialize a new instance of Attack.

        :param target: the target location
        :type target: Position

        :param caster: entity who threw an attack
        :type caster: entity

        :param position: current position of the attack
        :type position: Position
        """
        self.position = caster.position

        #
        self.angle, self.direction = self.calculate_angle(target)
        self.caster = caster


    def calculate_dammage(self):
        """
        Calculate damage given with attack (impact of target statistics not taken into account)
        :return: The calculated damage output.
        :rtype: float
        """
        # TODO : system of statistics to come up with
        return 1. #PLACEHOLDER
    def calculate_angle(self,target):
        """
        Calculate the firing angle
        :param target: Position  of target
        :type target: Position
        :return: The calulacted angle at witch self was fired, noramilzed vector indicating direction of momentum
        :rtype: (float, float)
        """

        vector = self.position - target
        vector.normalized()
        vector *= -1
        return math.degrees(math.atan2(-vector.y, vector.x)), vector
    def fly(self):
        """
        Move projectile with speed ...
        """
        self.position += (self.direction * 3 ) #PLACEHOLDER




