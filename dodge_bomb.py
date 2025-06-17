import os
import random  #アルファベット順
import sys
import pygame as pg


WIDTH, HEIGHT = 1100, 650
DELTA = {  # 移動量辞書
    pg.K_UP:(0, -5),
    pg.K_DOWN:(0, +5),
    pg.K_LEFT:(-5, 0),
    pg.K_RIGHT:(+5, 0),
}
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg")    
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 0.9)
    kk_rct = kk_img.get_rect() 
    kk_rct.center = 300, 200
    # kk_rctという変数にget_rect()を入れる。その後、get_rect()の値を300,200に設定することで「こうかとん」がその座標に現れる

    # 新しいsurfaceはループのwhile文の前に作る
    bb_img = pg.Surface((20,20))  #空のSurfaceを作る
    pg.draw.circle(bb_img,(255,0,0),(10,10),10)  #赤い円
    bb_img.set_colorkey((0,0,0))
    bb_rct = bb_img.get_rect()  #爆弾を作る
    bb_rct.centerx = random.randint(0,WIDTH)  #横幅を超えないように設定する　center[x]という区切り　爆弾の設定
    bb_rct.centery = random.randint(0,HEIGHT)  #縦幅を超えないように設定する center[y]という区切り　爆弾の設定
    vx,vy = +5,+5

    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        screen.blit(bg_img, [0, 0]) 
        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        for key,mv in DELTA.items():
            if key_lst[key]:
                sum_mv[0] += mv[0]
                sum_mv[1] += mv[1]
        # key →　g.K_UPなどのkey　mv　→ -= 5 の5の部分を指す items()
        # if key_lst[pg.K_UP]:
        #     sum_mv[1] -= 5
        # if key_lst[pg.K_DOWN]:
        #     sum_mv[1] += 5
        # if key_lst[pg.K_LEFT]:
        #     sum_mv[0] -= 5
        # if key_lst[pg.K_RIGHT]:
        #     sum_mv[0] += 5
        kk_rct.move_ip(sum_mv)
        screen.blit(kk_img, kk_rct)
        bb_rct.move_ip(vx,vy)
        screen.blit(bb_img, bb_rct)  #爆弾の表示
        pg.display.update()
        tmr += 1
        clock.tick(50)




if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
