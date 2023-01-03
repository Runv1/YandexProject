import itertools

from common import player_group, monster_group
from inventory import SmallHealPotion, Sword, LeftHand, RightHand
from settings import KEY_COLOR, VECTORS_TO_DIRECTION, FPS, SLOT_RIGHT_HAND, SLOT_LEFT_HAND
from tiles import Animation, Creature
from utils import load_image


def load_creature_images(name, frames):
    images = {}
    for dx, dy, n in itertools.product([-1, 0, 1], [-1, 0, 1], range(frames)):
        fname = f'{name}\\{name}_{VECTORS_TO_DIRECTION[dx, dy]}_{n}.png'
        image = load_image(fname, KEY_COLOR)
        if (dx, dy) in images.keys():
            images[dx, dy].append(image)
        else:
            images[dx, dy] = [image]
    return images


class Player(Creature):
    def __init__(self, pos_x, pos_y):
        images = load_creature_images("mara", 2)
        animations = dict()
        for k in images.keys():
            if k == (0, 0):
                animations[k] = Animation(images[k], 10, False)
            else:
                animations[k] = Animation(images[k], 10, False)
        super().__init__(animations, 100, pos_x, pos_y, [player_group])
        for i in range(7):
            super().get_inventory().add_item(SmallHealPotion())
        super().get_inventory().add_item(Sword())
        self.get_ammunition().assign_default(LeftHand(), SLOT_LEFT_HAND)
        self.get_ammunition().assign_default(RightHand(), SLOT_RIGHT_HAND)


class Monster(Creature):
    def __init__(self, pos_x, pos_y):
        images = load_creature_images("mara", 2)
        animations = dict()
        for k in images.keys():
            if k == (0, 0):
                animations[k] = Animation(images[k], 10, False)
            else:
                animations[k] = Animation(images[k], 10, False)
        super().__init__(animations, 100, pos_x, pos_y, [monster_group])








