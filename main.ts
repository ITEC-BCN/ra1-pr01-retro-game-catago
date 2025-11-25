//  2. Disparar
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    
    //  Dispara a la derecha por defecto
    lana = sprites.createProjectileFromSprite(img`
            . . 2 2 . .
            . 2 2 2 2 .
            . 2 2 2 2 .
            . . 2 2 . .
            `, miGato, 100, 0)
})
//  5. Game Over (Enemigo toca Gato)
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_on_overlap(sprite2: Sprite, otherSprite2: Sprite) {
    game.over(false)
})
//  4. Colisiones (Disparo golpea Enemigo)
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function on_on_overlap2(sprite: Sprite, otherSprite: Sprite) {
    otherSprite.destroy()
    sprite.destroy()
    info.changeScoreBy(1)
})
let robot : Sprite = null
let lana : Sprite = null
let miGato : Sprite = null
//  1. Crear Jugador
miGato = sprites.create(img`
        . . . . . . . . . . . . . . . .
        . . . . 5 5 . . . 5 5 . . . . .
        . . . 5 f 5 5 5 5 5 f 5 . . . .
        . . . 5 5 5 5 5 5 5 5 5 . . . .
        . . . 5 5 5 5 3 5 5 5 5 . . . .
        . . . . 5 5 5 5 5 5 5 . . . . .
        . . . . . 5 5 5 5 5 . . . . . .
        . . . . . . . . . . . . . . . .
        `, SpriteKind.Player)
controller.moveSprite(miGato)
info.setScore(0)
//  3. Crear Enemigos periódicamente
game.onUpdateInterval(2000, function on_update_interval() {
    
    robot = sprites.create(img`
            . . . c c . . .
            . . c 1 1 c . .
            . c 1 1 1 1 c .
            . . c 1 1 c . .
            `, SpriteKind.Enemy)
    //  Aparecer en lugar aleatorio
    robot.x = randint(0, 160)
    robot.y = randint(0, 120)
    //  Perseguir al gato
    robot.follow(miGato, 30)
})
