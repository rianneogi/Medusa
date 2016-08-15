from src.MovingComponent import *
from src.Sprite import *
from src.MovingComponent import *
import math

class Projectile:
    def __init__(self, spriteenum, owner, pos, velocity, start_func, update_func, collide_func):
        self.sprite = Sprite(spriteenum)
        self.owner = owner
        self.level = owner.level

        self.start_func = start_func
        self.update_func = update_func
        self.collide_func = collide_func

        self.moving_component = MovingComponent(self, self.level)
        self.moving_component.move(pos)
        self.moving_component.velocity = velocity
        self.moving_component.on_collision = self.collide_func

        self.start_func(self)

    def draw(self, screen, camera):
        self.sprite.draw(screen, camera)

    def update(self, deltatime):
        self.moving_component.update(deltatime)
        self.update_func(self)

        self.sprite.set_rotation(math.pi + math.atan2(self.moving_component.velocity[1],self.moving_component.velocity[0]))