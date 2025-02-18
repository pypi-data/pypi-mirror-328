import pygame

from teon.entity import Entity
from teon.functions import scale_def

class ParallaxBackground(pygame.sprite.Sprite):

    level_editor = None

    def __init__(self,player,**kwargs):

        super().__init__()
        texture = kwargs.get("image",0)
        collider = kwargs.get("collider")
        z = kwargs.get("z", 0)
        self.position = kwargs.get("position", (0,0))
        rotation = kwargs.get("rotation", 0)
        vis = kwargs.get("visible", True)
        self._scale = kwargs.get("scale",(1,1))
        collidable = kwargs.get("collidable", True)
        hitbox = kwargs.get("pixel_hitbox",False)
        self.tags = kwargs.get("tags",[])
        self.running = kwargs.get("running",True)
        self.color = kwargs.get("color",(255,255,255))
        self.is_ui = kwargs.get("is_ui", False)
        self.level_index = kwargs.get("lindex",0)

        self.axies = kwargs.get("axies",(True,False))
        self.speed = kwargs.get("speed",1)

        self.player_last_x = player.rect.centerx
        self.player_last_y = player.rect.centery
        self.player = player

        

        self.collidable = collidable
        self.visible = vis
        self.z = z
        self.collidable = False
        x,y = self.position
        x = x * scale_def()
        y = y * scale_def()
        self.position = (x,y)

        self._scale = (self._scale[0] * scale_def(),self._scale[1] * scale_def())


        if texture == 0:
            self.image = pygame.Surface((100,100))
            self.image.fill(self.color)
        else:
            self.image = texture
            self.image = pygame.transform.scale(texture,(self.image.get_width(),self.image.get_height()))

        if collider is None:
            self.rect = self.image.get_rect(center = self.position)

        else:
            self.rect = collider

        self.default_image_x = self.image.get_width()
        self.default_image_y = self.image.get_height()

        self.scale = (self._scale[0],self._scale[1],False)

        if rotation != 0:
            self.image = pygame.transform.rotozoom(self.image,rotation,1)

        self.hitbox = self.rect.copy()

        if Entity.level_editor:
            Entity.level_editor.add_entity_to_level(self)

    @property
    def scale(self):
        return self._scale

    @scale.setter
    def scale(self,scale : tuple):
        self._scale = scale
        self.image = pygame.transform.scale(self.image,(self.default_image_x * self.scale[0],self.default_image_y * self.scale[1]))
        if len(scale) >= 3 and scale[2]:
            self.rect = self.image.get_rect(center = self.rect.center)
            self.hitbox = self.rect.copy()

    def update(self):
        if self.axies[0]:
            self.rect.x -= (self.player.rect.centerx - self.player_last_x) * self.speed
            self.player_last_x = self.player.rect.centerx
        if self.axies[1]:
            self.rect.y -= (self.player.rect.centery - self.player_last_y) * self.speed
            self.player_last_y = self.player.rect.centery
        self.position = self.rect.center