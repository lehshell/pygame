import pygame
from pygame.locals import Rect, QUIT, K_LEFT, K_RIGHT, K_UP, K_DOWN
import sys

def main():
    (w, h) = (600, 400)    # 画面サイズ   w, h = 600, 400 と同じ
    (x, y) = (w//2, h//2)  # 中心座標     x, y = w//2, h//2 と同じ
    pygame.init()          # pygame 初期化
    pygame.display.set_mode((w, h))        # 画面設定
    screen = pygame.display.get_surface()  # 表示用 surface 取得

    while True:
        # マウス・キーイベント処理(キャラクタ画像の移動)
        x1, y1 = pygame.mouse.get_pos()    # マウス座標取得
        if 0 < x1 < int(screen.get_width()) - 5 and 0 < y1 < int(screen.get_height()) - 5:
            # 現在の座標とマウスの座標の間の座標を（重み付け３：１）で設定する
            x = (x * 3 + x1) / 4
            y = (y * 3 + y1) / 4
        else:
            keys = pygame.key.get_pressed()
            if keys[K_LEFT]:
                x -= 5
            if keys[K_RIGHT]:
                x += 5
            if keys[K_UP]:
                y -= 5
            if keys[K_DOWN]:
                y += 5
        
        pygame.display.update()     # 画面更新
        pygame.time.wait(20)        # 更新時間間隔
        screen.fill((128, 176, 240, 0))  # 画面の背景色
        # 円を描画
        pygame.draw.circle(screen, (220, 248, 180), (int(x), int(y)), 5)
        # イベント処理
        for event in pygame.event.get():
            # 画面の閉じるボタンを押したとき
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
