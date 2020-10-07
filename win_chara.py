import pygame
from pygame.locals import Rect, QUIT, K_LEFT, K_RIGHT, K_UP, K_DOWN
import sys
import os

game_dir = os.path.dirname(__file__)
img_dir = os.path.join(game_dir, "image")
BG_FILE = "bg.jpg"
CHARA_FILE = "foo.png"
bg_file = os.path.join(img_dir, BG_FILE)
char_file = os.path.join(img_dir, CHARA_FILE)
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
    if os.path.isfile(bg_file):
        bg = pygame.image.load(bg_file).convert() # 背景画像の指定
        rect_bg = bg.get_rect()                   # 背景画像のサイズ取得
    if os.path.isfile(char_file):
        img = pygame.image.load(char_file).convert_alpha() # キャラ画像の指定
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
        if os.path.isfile(bg_file):
            screen.blit(bg, rect_bg)         # 背景画像の描画
        if os.path.isfile(char_file):
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
