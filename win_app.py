import sys
import os
import pygame
from pygame.locals import Rect, QUIT

game_dir = os.path.dirname(__file__)
img_dir = os.path.join(game_dir, "image")
BG_FILE = "bg.jpg"
CHARA_FILE = "foo.png"
BLUE  = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SPACE = 2
SCREEN = Rect(0, 0, 600, 400)

class Player(pygame.sprite.Sprite):
    # sprite for the Player
    def __init__(self, scr_rect):
        super().__init__()
        self.scr_rect = scr_rect
        self.image = pygame.image.load(
            os.path.join(img_dir, CHARA_FILE)).convert()           # CHARA_FILE: キャラクタ画像ファイル
        self.image = pygame.transform.scale(self.image, (73, 73))  # 73 x 73 に縮小
        self.image.set_colorkey(BLACK)                             # 透過色を黒に設定する
        self.rect = self.image.get_rect()
        self.rect.center = (self.scr_rect.w // 2, self.scr_rect.h // 2)  # player 座標
        self.speed = 5
    def update(self):
        # マウスイベント処理（キャラクタの移動）
        x1, y1 = pygame.mouse.get_pos()
        self.rect.center = ((self.rect.centerx * 3 + x1) // 4,
                            (self.rect.centery * 3 + y1) // 4)     # player 座標
        self.rect.clamp_ip(self.scr_rect)         # ゲーム画面内のみで移動

def main():
    pygame.init()                                 # pygame 初期化
    x, y = SCREEN.width//2, SCREEN.height//2
    screen = pygame.display.set_mode((SCREEN.width, SCREEN.height))  # ウィンドウサイズ（幅, 高）の指定
    pygame.display.set_caption("Pygame Sample")   # タイトル
    bg_image = pygame.image.load(
        os.path.join(img_dir, BG_FILE)).convert() # 背景画像の指定
    rect_bg = bg_image.get_rect()                 # 背景画像のサイズ取得
    all_sprites = pygame.sprite.Group()
    player = Player(SCREEN)
    all_sprites.add(player)
    font = pygame.font.SysFont('Calibri', 20, True, False)  # size: 25, bold: True, italics: False
    while True:
        screen.fill(WHITE)               # 背景色の指定（RGB）
        screen.blit(bg_image, rect_bg)   # 背景画像の描画
        all_sprites.update()
        all_sprites.draw(screen)
        x1, y1 = pygame.mouse.get_pos()  # マウス座標
        text = font.render(f'{x1}, {y1}', True, BLUE)
        screen.blit(text, [player.rect.x + SPACE, player.rect.y + player.rect.h + SPACE])
        pygame.time.wait(33)             # 更新間隔（ミリ秒） 30 FPS
        pygame.display.update()          # 画面更新
        for event in pygame.event.get(): # 終了処理
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()

