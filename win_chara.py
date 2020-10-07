import pygame
from pygame.locals import Rect, QUIT, K_LEFT, K_RIGHT, K_UP, K_DOWN
import sys
import os

BG_FILE = "./image/bg.jpg"
CHARA_FILE = "./image/foo.png"
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
space = 2

def main():
    pygame.init()                                 # pygame 初期化
    (w, h) = (600, 400)
    (x, y) = (w//2, h//2)
    screen = pygame.display.set_mode((w, h))      # ウィンドウサイズ（幅, 高）の指定
    pygame.display.set_caption("Pygame Sample")   # タイトル
    if os.path.isfile(BG_FILE):
        bg = pygame.image.load(BG_FILE).convert() # 背景画像の指定
        rect_bg = bg.get_rect()                   # 背景画像のサイズ取得
    if os.path.isfile(CHARA_FILE):
        img = pygame.image.load(CHARA_FILE).convert_alpha() # キャラ画像の指定
        player = pygame.transform.scale(img, (73, 73))
        rect_player = player.get_rect()           # player 画像のサイズ取得
        rect_player.center = (x, y)                   # player 座標
        prw = rect_player.w // 2                      # player 幅の半分
        prh = rect_player.h // 2                      # player 高の半分
    font = pygame.font.SysFont('Calibri', 20, True, False)  # size: 25, bold: True, italics: False
    while True:
        # マウスイベント処理（キャラクタの移動）
        x1, y1 = pygame.mouse.get_pos()
        x = int((x * 3 + x1) // 4)
        y = int((y * 3 + y1) // 4)
        screen.fill((255, 255, 255))     # 背景色の指定（RGB）
        if os.path.isfile(BG_FILE):
            screen.blit(bg, rect_bg)         # 背景画像の描画
        if os.path.isfile(CHARA_FILE):
            rect_player.center = (x, y)      # player 座標
            screen.blit(player, rect_player) # player の描画
            text = font.render(f'{x1}, {y1}', True, blue)
            screen.blit(text, [rect_player.x + space, rect_player.y + rect_player.h + space])
        pygame.time.wait(33)             # 更新間隔（ミリ秒） 30 FPS
        pygame.display.update()          # 画面更新
        for event in pygame.event.get(): # 終了処理
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
