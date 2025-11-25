# 2. Disparar
def on_a_pressed():
    global lana
    # Dispara a la derecha por defecto
    lana = sprites.create_projectile_from_sprite(img("""
            . . 2 2 . .
            . 2 2 2 2 .
            . 2 2 2 2 .
            . . 2 2 . .
            """),
        miGato,
        100,
        0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

# 5. Game Over (Enemigo toca Gato)

def on_on_overlap(sprite2, otherSprite2):
    game.over(False)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

# 4. Colisiones (Disparo golpea Enemigo)

def on_on_overlap2(sprite, otherSprite):
    otherSprite.destroy()
    sprite.destroy()
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap2)

robot: Sprite = None
lana: Sprite = None
miGato: Sprite = None
# 1. Crear Jugador
miGato = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . 5 5 . . . 5 5 . . . . .
        . . . 5 f 5 5 5 5 5 f 5 . . . .
        . . . 5 5 5 5 5 5 5 5 5 . . . .
        . . . 5 5 5 5 3 5 5 5 5 . . . .
        . . . . 5 5 5 5 5 5 5 . . . . .
        . . . . . 5 5 5 5 5 . . . . . .
        . . . . . . . . . . . . . . . .
        """),
    SpriteKind.player)
controller.move_sprite(miGato)
info.set_score(0)
# 3. Crear Enemigos periódicamente

def on_update_interval():
    global robot
    robot = sprites.create(img("""
            . . . c c . . .
            . . c 1 1 c . .
            . c 1 1 1 1 c .
            . . c 1 1 c . .
            """),
        SpriteKind.enemy)
    # Aparecer en lugar aleatorio
    robot.x = randint(0, 160)
    robot.y = randint(0, 120)
    # Perseguir al gato
    robot.follow(miGato, 30)
game.on_update_interval(2000, on_update_interval)
