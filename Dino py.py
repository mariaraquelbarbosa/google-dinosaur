import pygame
import os
import random
pygame.init()

# Criando a tela
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Carrega as animações
RUNNING = [pygame.image.load(os.path.join('C:\\Users\\maria\\projetos\\IA\\google-dinosaur-main\\Images\\Dino', 'DinoRun1.png')),
           pygame.image.load(os.path.join('C:\\Users\\maria\\projetos\\IA\\google-dinosaur-main\\Images\\Dino', 'DinoRun2.png'))]

DUCKING = [pygame.image.load(os.path.join('C:\\Users\\maria\\projetos\\IA\\google-dinosaur-main\\Images\\Dino', 'DinoDuck1.png'))]

JUMPING = pygame.image.load(os.path.join('C:\\Users\\maria\\projetos\\IA\\google-dinosaur-main\\Images\\Dino', 'DinoJump.png'))

SMALL_CACTUS = [pygame.image.load(os.path.join('C:\\Users\\maria\\projetos\\IA\\google-dinosaur-main\\Images\\Cactus', 'SmallCactus1.png')),
                pygame.image.load(os.path.join('C:\\Users\\maria\\projetos\\IA\\google-dinosaur-main\\Images\\Cactus', 'SmallCactus2.png')),
                pygame.image.load(os.path.join('C:\\Users\\maria\\projetos\\IA\\google-dinosaur-main\\Images\\Cactus', 'SmallCactus3.png'))]

LARGE_CACTUS = [pygame.image.load(os.path.join('C:\\Users\\maria\\projetos\\IA\\google-dinosaur-main\\Images\\Cactus', 'LargeCactus1.png')),
                pygame.image.load(os.path.join('C:\\Users\\maria\\projetos\\IA\\google-dinosaur-main\\Images\\Cactus', 'LargeCactus2.png')),
                pygame.image.load(os.path.join('C:\\Users\\maria\\projetos\\IA\\google-dinosaur-main\\Images\\Cactus', 'LargeCactus3.png'))]

BIRD = [pygame.image.load(os.path.join('C:\\Users\\maria\\projetos\\IA\\google-dinosaur-main\\Images\\Bird', 'Bird1.png')),
        pygame.image.load(os.path.join('C:\\Users\\maria\\projetos\\IA\\google-dinosaur-main\\Images\\Bird', 'Bird2.png'))]

CLOUD = pygame.image.load(os.path.join('C:\\Users\\maria\\projetos\\IA\\google-dinosaur-main\\Images\\Other', 'Cloud.png'))

BG = pygame.image.load(os.path.join("C:\\Users\\maria\\projetos\\IA\\google-dinosaur-main\\Images\\Other", "Track.png"))

class Dinosaur:
    X_POS = 80  # Coordenada x do dinossauro
    Y_POS = 310  # Coordenada y do dinossauro
    # Lembrando que nesse jogo, o dinossauro não se move na tela
    Y_POS_DUCK = 340  # Coordenada y do dinossauro agachado. Por algum motivo, o dinossauro agachado é um pouco mais alto que o normal ???
    JUMP_VEL = 8.5  # Velocidade do pulo do dinossauro

    def __init__(self):
        self.run_img = RUNNING
        self.duck_img = DUCKING
        self.jump_img = JUMPING
        
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]  # Imagem inicial do dinossauro
        self.dino_rect = self.image.get_rect()  # Pega a hitbox do dinossauro
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self, userInput):
        """
        Função que atualiza o dinossauro baseado no input do usuário
        """
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:  # Para ficar mais fácil de animar o dinossauro
            self.step_index = 0        

        if userInput[pygame.K_UP] and not self.dino_jump:  # Se o usuário aperta para a cima e o dino não está pulando, pula
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False
        elif userInput[pygame.K_DOWN] and not self.dino_jump:  # Se o usuário aperta para baixo e o dino não está agachado, agacha
            self.dino_jump = False
            self.dino_run = False
            self.dino_duck = True
        elif not(self.dino_jump or userInput[pygame.K_DOWN]):  # Se o usuário não está apertando nada, o dino corre
            self.dino_jump = False
            self.dino_run = True
            self.dino_duck = False

    def run(self):
        """
        Atualiza a imagem do dinossauro de modo a parecer que ele está se movendo
        """
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1
    

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]    
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4  # Diminui a coordenada y do dino (o que significa que aumenta a posição dele na tela)    
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)  # A nuvem aparece em algum lugar entre 800 e 1000 pixels da direita da tela
        self.y = random.randint(50, 100)  # A nuvem aparece em algum lugar entre 50 e 100 pixels do topo da tela
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed  # A nuvem se move para a esquerda
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type # Número inteiro entre 0 e 2 que determina o tipo de cactus
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self): 
        """
        Move o obstáculo pela tera
        """
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width: # Remover o obstáculo assim que ele sai da tela principal
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)


class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325


class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300


class Bird(Obstacle): # Pterodáctilo
    def __init__(self, image):
        self.type = 0 # Só há um tipo de pterodáctilo
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, SCREEN): # Diferente do método draw da classe genérica Obstacle porque o pterodáctilo é "animado"
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1
        # Quando o index é 0-4, aparece uma imagem, de 5-9 aparece outra, no 10 ele reseta o index


def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()
    cloud = Cloud()
    game_speed = 20
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0 
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = []
    death_count = 0

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1  # Aumenta a velocidade do jogo a cada 100 pontos

        text = font.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()  # Tudo nessa porra precisa de coordenadas
        textRect.center = (1000, 40)
        SCREEN.blit(text, textRect)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:                                # A ideia é que o background vá se movendo, e quando a imagem acabar, põe outra imagem
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    # Loop para permitir sair do jogo no X
    while run:  # As paradas no pygame são sempre em while loop
        for event in pygame.event.get(): # event é qualquer ação realizada pelo usuário
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255, 255, 255)) # Preenche a tela com a cor branca
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)  # Atualiza o dinossauro baseado no input do usuário

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            if player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(2000)
                death_count += 1
                menu(death_count)

        background()

        cloud.draw(SCREEN)
        cloud.update()

        score()
        
        clock.tick(30)
        pygame.display.update()

def menu(death_count):
    global points
    run = True
    while run:
        SCREEN.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if death_count == 0:
            text = font.render("Press any Key to Start", True, (0, 0, 0))
        elif death_count > 0:
            text = font.render("Press any Key to Restart", True, (0, 0, 0))
            score = font.render("Your Score: " + str(points), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)
        SCREEN.blit(RUNNING[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main()


menu(death_count = 0)