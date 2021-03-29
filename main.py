import wrap_py as wrap, wrap_py.ru
from wrap_py import sprite
from wrap_py import world

world.create_world(700, 800)
world.set_world_background_image("C:/Users/zhuko/wrap_py_catalog/backgrounds/fon_gori1700-800.png")
pushki = sprite.add_sprite("knopki", 40, 40, costume="pushki")
nastroiki = sprite.add_sprite("knopki", 130, 40)
pushka = sprite.add_sprite("pushka", 350, 400, False)
sprite.set_bottom_to(pushka, 668)
sprite.show_sprite(pushka)


@wrap_py.on_mouse_move
def navedenie_na_knopki(pos):
    stu = sprite.sprite_collide_point(pushki, pos[0], pos[1])
    if stu == True:
        sprite.change_sprite_size_proc(pushki, 110, 110)
    else:
        sprite.change_sprite_size_proc(pushki, 100, 100)

    stu = sprite.sprite_collide_point(nastroiki, pos[0], pos[1])
    if stu == True:
        sprite.change_sprite_size_proc(nastroiki, 110, 110)
    else:
        sprite.change_sprite_size_proc(nastroiki, 100, 100)


@wrap_py.on_mouse_down()
def perekluchenie(button, pos):
    gavs = sprite.sprite_collide_point(pushki, pos[0], pos[1])
    if gavs == True:
        ekran_pushek()

def ekran_pushek():
    print(pushka)