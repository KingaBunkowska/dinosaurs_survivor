from game_mechanics.Position import Position
import math

class Attack:
    """
    superclass for any form of attack
    """

    def __init__(self, target, caster,speed = 8,range = float('inf'), penetrate=False):
        """
        :param target: coordinates of target
        :type target: Position

        :param caster: casting entity
        :type caster: Entity

        :param speed: speed of attack
        :type speed: float

        :param range: range of attack
        :type range: float

        :param penetrate: whether projectile pierce enemy or not (TODO: implement piercing)
        :type penetrate: bool
        """
        self.position = caster.position

        #
        self.angle, self.direction = self.calculate_angle(target)
        self.caster = caster
        self.penetrate = penetrate
        self.range = range
        self.speed = speed


    def calculate_dammage(self):
        """
        Calculate damage given with attack (impact of target statistics not taken into account)
        :return: The calculated damage output.
        :rtype: float
        """
        # TODO : connect to the statistics system
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
        Move projectile in space and reduce remaining range
        """
        self.position += (self.direction * self.speed)
        self.range -= self.speed