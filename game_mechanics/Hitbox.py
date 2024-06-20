from game_mechanics.Position import Position


class Hitbox:
    def __init__(self, position, size =(0,0), start = (0,0)):
        self.position = position
        self.width, self.height = size
        self.start_x, self.start_y = start
        self.is_box = False if size[0] == 0 else True

    def collide(self, hitbox):
        if self.is_box:
            if hitbox.is_box:
                return not (self.get_upper_left().x > hitbox.get_lower_right().x or
                        hitbox.get_upper_left().x > self.get_lower_right().x or
                        self.get_upper_left().y > hitbox.get_lower_right().y or
                        hitbox.get_upper_left().y > self.get_lower_right().y)
            else:
                return hitbox.position.following(self.get_upper_left()) and hitbox.position.proceeding(self.get_lower_right())
        else:
            return self.position.following(hitbox.get_upper_left()) and self.position.proceeding(
                hitbox.get_lower_right())

    def get_upper_left(self):
        return Position(self.position.x - self.start_x,self.position.y - self.start_y)

    def get_lower_right(self):
        if self.is_box:
            return Position(self.position.x - self.start_x + self.width,self.position.y - self.start_y + self.height)
        else:
            return self.position

    def to_rect(self):
        if self.is_box:
            return (self.position.x - self.start_x, self.position.y - self.start_y), (self.width, self.height)
        else:
            return self.position