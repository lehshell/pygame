import pygame
from pygame.locals import QUIT
import sys

def main():
    pygame.init()                                # pygame 初期化
    screen = pygame.display.set_mode((600, 400)) # ウィンドウサイズ（幅, 高）の指定
    pygame.display.set_caption("Pygame Sample")  # タイトル

    while True:
        screen.fill((180, 220, 248))     # 背景色の指定。RGB
        pygame.display.update()          # 画面更新
        pygame.time.wait(33)             # 更新間隔（ミリ秒） 30 FPS(Frames Per Second)

        for event in pygame.event.get(): # 終了処理
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
