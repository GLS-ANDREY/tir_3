import wrap_py as wrap, wrap_py.ru
from wrap_py import sprite
from wrap_py import world

world.create_world(700, 800)
world.set_world_background_image("C:/Users/zhuko/wrap_py_catalog/backgrounds/fon_gori1700-800.png")
pushki = sprite.add_sprite("knopki", 40, 40, costume="pushki")
nastroiki = sprite.add_sprite("knopki", 130, 40)
zamochek = sprite.add_sprite("knopki", 285, 625, False, "zamochek")
OK = sprite.add_sprite("knopki", 350, 625, False, "OK")
ball_blast = sprite.add_sprite("ball_blast", 350, 200)
pushka = sprite.add_sprite("pushka", 350, 400, False)
ruka = sprite.add_sprite("ball_blast", 350, 450, costume="ruka")
palka = sprite.add_sprite("ball_blast", 350, 400, costume="palka")
najmi = sprite.add_text(350, 365, "нажми чтобы начать", font_size=25, bold=True)
sprite.set_bottom_to(pushka, 668)
sprite.show_sprite(pushka)


@wrap_py.on_mouse_move
def navedenie_na_knopki(pos):
    navedenie_na_knopku(pushki, pos)
    navedenie_na_knopku(nastroiki, pos)
    navedenie_na_knopku(OK, pos)
    navedenie_na_knopku(zamochek, pos)


def navedenie_na_knopku(nomer_knopki, pos):
    stu = sprite.sprite_collide_point(nomer_knopki, pos[0], pos[1])
    if stu == True:
        sprite.change_sprite_size_proc(nomer_knopki, 110, 110)
    else:
        sprite.change_sprite_size_proc(nomer_knopki, 100, 100)


@wrap_py.on_mouse_down()
def perekluchenie(button, pos):
    gavs = sprite.sprite_collide_point(pushki, pos[0], pos[1])
    if gavs == True:
        ekran_pushek()

    gavs = sprite.sprite_collide_point(nastroiki, pos[0], pos[1])
    if gavs == True:
        ekran_nastroek()

    gavs = sprite.sprite_collide_point(OK, pos[0], pos[1])
    if gavs == True:
        gl_ekran()


def gl_ekran():
    world.set_world_background_image("C:/Users/zhuko/wrap_py_catalog/backgrounds/fon_gori1700-800.png")
    sprite.hide_sprite(OK)
    sprite.hide_sprite(zamochek)
    sprite.show_sprite(ball_blast)
    sprite.show_sprite(nastroiki)
    sprite.show_sprite(pushki)
    sprite.show_sprite(pushka)
    sprite.show_sprite(ruka)
    sprite.show_sprite(palka)
    sprite.show_sprite(najmi)


def ekran_nastroek():
    skrit_gl_ekran()
    world.set_world_background_image("C:/Users/zhuko/wrap_py_catalog/backgrounds/pixel.png")
    world.set_world_background_color([88, 88, 88])
    sprite.show_sprite(OK)
    sprite.move_sprite_to(OK, 350, 625)


def skrit_gl_ekran():
    sprite.hide_sprite(pushka)
    sprite.hide_sprite(pushki)
    sprite.hide_sprite(nastroiki)
    sprite.hide_sprite(ball_blast)
    sprite.hide_sprite(ruka)
    sprite.hide_sprite(palka)
    sprite.hide_sprite(najmi)


def ekran_pushek():
    skrit_gl_ekran()
    world.set_world_background_image("C:/Users/zhuko/wrap_py_catalog/backgrounds/pixel.png")
    world.set_world_background_color([88, 88, 88])
    sprite.show_sprite(zamochek)
    sprite.show_sprite(OK)
    sprite.move_sprite_to(OK, 400, 625)


@wrap.always
def dvigat_ruku():
    ruka_x = sprite.get_sprite_x(ruka)
    #ruka_y = sprite.get_sprite_y(ruka)
    sprite.move_sprite_to(ruka, ruka_x - 5, 450)
    #sprite.move_sprite_to(ruka, ruka_y - 5, 450)
