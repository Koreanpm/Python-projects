import os
import pygame
#########################################################
#기본 초기화(반드시 해야 하는 것들)
pygame.init()

#화면 크기 설정
screen_width = 640 #가로 크기
screen_height = 480 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Nado Pang") #게임 이해

#FPS
clock = pygame.time.Clock()

#########################################################

#1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
current_path = os.path.dirname(__file__) #현재 파일의 위치 반환
image_path = os.path.join(current_path, "images") #images 폴더 위치 반환

#배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

#스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] #스테이지 높이 위에 캐릭터를 두기 위해 사용

#캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character2.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - stage_height - character_height

running = True #게임이 진행중인가?
while running:
  dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정

  #2. 이벤트 처리(키보드, 마우스 등)
  print("fps: " + str(clock.get_fps()))
  for event in pygame.event.get(): #어떤 이벤트가 발생하였는가?
      if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생했는가?
        running = False #게임이 진행중이 아님

  #3. 게임 캐릭터 위치 정의

  

  #4. 충돌 처리

  #5. 화면에 그리기
  screen.blit(background, (0, 0))
  screen.blit(stage, (0, screen_height - stage_height))
  screen.blit(character, (character_x_pos, character_y_pos))

  pygame.display.update() #게임화면을 다시 그리기!


#pygame 종료
pygame.quit()