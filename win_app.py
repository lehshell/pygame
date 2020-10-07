import sys
import os
import pygame
from pygame.locals import Rect, QUIT

game_dir = os.path.dirname(__file__)
img_dir = os.path.join(game_dir, "image")
BG_FILE = "bg.jpg"
CHARA_FILE = "foo.png"
blue = (0, 0, 255)
space = 2

class Player(pygame.sprite.Sprite):
    # sprite for the Player
    def __init__(self, scr_rect):
        super().__init__()
        self.scr_rect = scr_rect
        self.image = pygame.image.load(
            os.path.join(img_dir, CHARA_FILE)).convert()
        self.image = pygame.transform.scale(self.image, (73, 73))
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (self.scr_rect.w // 2, self.scr_rect.h // 2)  # player 座標
        self.speed = 5
    def update(self, x, y):
        self.rect.center = (x, y)                # player 座標

def main():
    pygame.init()                                # pygame 初期化
    (w, h) = (600, 400)
    (x, y) = (w//2, h//2)
    screen = pygame.display.set_mode((w, h))     # ウィンドウサイズ（幅, 高）の指定
    scr_rect = Rect(0, 0, screen.get_width(), screen.get_height())
    pygame.display.set_caption("Pygame Sample")  # タイトル
    bg_image = pygame.image.load(
        os.path.join(img_dir, BG_FILE)).convert() # 背景画像の指定
    rect_bg = bg_image.get_rect()                      # 背景画像のサイズ取得
    all_sprites = pygame.sprite.Group()
    player = Player(scr_rect)
    all_sprites.add(player)
    font = pygame.font.SysFont('Calibri', 20, True, False)  # size: 25, bold: True, italics: False
    while True:
        # マウスイベント処理（キャラクタの移動）
        x1, y1 = pygame.mouse.get_pos()
        x = int((x * 3 + x1) // 4)
        y = int((y * 3 + y1) // 4)
        screen.fill((255, 255, 255))     # 背景色の指定（RGB）
        screen.blit(bg_image, rect_bg)   # 背景画像の描画
        all_sprites.update(x, y)
        all_sprites.draw(screen)
        text = font.render(f'{x1}, {y1}', True, blue)
        screen.blit(text, [player.rect.x + space, player.rect.y + player.rect.h + space])
        pygame.time.wait(33)             # 更新間隔（ミリ秒） 30 FPS
        pygame.display.update()          # 画面更新
        for event in pygame.event.get(): # 終了処理
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
