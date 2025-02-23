# item function dictionary
import pygame #type: ignore

def normalArrow():
    print("This is a normal arrow.")

def normalArrowFire():
    print("This is a normal arrow with fire.")

def slimedArrow():
    print("This is a slimed arrow.")

def slimedArrowFire(sprite):
    display = pygame.display.get_surface()
    img = sprite.image
    rect = sprite.rect

    rect.x += 1

    display.blit(img, rect)
    print(sprite.item_id)


items = {
    102: ["normal_arrow", normalArrow, normalArrowFire],
    103: ["slimed_arrow", slimedArrow, slimedArrowFire]
}
