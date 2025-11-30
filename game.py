import pygame
from sys import exit
from random import randint, choice

#definition of player class
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        #player images/frames loading
        player_walk_1 = pygame.image.load('/Users/aliona/Desktop/app_number_2/graphics/player_walk_1.webp').convert_alpha()
        player_walk_2 = pygame.image.load('/Users/aliona/Desktop/app_number_2/graphics/player_walk_2.png').convert_alpha()
        player_jump = pygame.image.load('/Users/aliona/Desktop/app_number_2/graphics/player_jump.png').convert_alpha()

        #walking and jumping animation
        self.player_walk = [
            pygame.transform.scale(player_walk_1, (200, 200)),
            pygame.transform.scale(player_walk_2, (200, 200)),
        ]
        self.player_index = 0
        self.player_jump = pygame.transform.scale(player_jump, (200, 200))

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(190, 460))
        self.mask = pygame.mask.from_surface(self.image)

        #physics of jumping
        self.velocity = 0
        self.gravity = 0.3  
        self.jump_force = -11

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 460:
            self.velocity = self.jump_force

    def apply_gravity(self):
        self.velocity += self.gravity
        self.rect.y += self.velocity
        if self.rect.bottom >= 460:
            self.rect.bottom = 460
            self.velocity = 0

    #animation of the player
    def animation_state(self):
        if self.rect.bottom < 460:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk): 
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]
        self.mask = pygame.mask.from_surface(self.image)
    
    #update method function
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

#definition of obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type, ground_y=460):
        super().__init__()
        self.type = type

        #loading coffee, cake, donut, tea, chocolate, nut, rock, scissors images/frames and scaling
        if type == 'coffee':
            coffee_frame_1 = pygame.image.load('/Users/aliona/Desktop/app_number_2/graphics/coffee_frame_1.png').convert_alpha()
            coffee_frame_2 = pygame.image.load('/Users/aliona/Desktop/app_number_2/graphics/coffee_frame_2.png').convert_alpha()
            self.frames = [
                pygame.transform.scale(coffee_frame_1, (100, 100)),
                pygame.transform.scale(coffee_frame_2, (100, 100)),
            ]
            y_pos = ground_y
        elif type == 'cake':
            cake_frame_1 = pygame.image.load('/Users/aliona/Desktop/app_number_2/graphics/cake_frame_1.png').convert_alpha()
            cake_frame_2 = pygame.image.load('/Users/aliona/Desktop/app_number_2/graphics/cake_frame_2.png').convert_alpha()
            self.frames = [
                pygame.transform.scale(cake_frame_1, (100, 100)),
                pygame.transform.scale(cake_frame_2, (100, 100)),
            ]
            y_pos = 200
        elif type == 'donut':
            donut_frame_1 = pygame.image.load('/Users/aliona/Desktop/app_number_2/graphics/donut_frame_1.png').convert_alpha()
            donut_frame_2 = pygame.image.load('/Users/aliona/Desktop/app_number_2/graphics/donut_frame_2.png').convert_alpha()
            self.frames = [
                pygame.transform.scale(donut_frame_1, (80, 80)),
                pygame.transform.scale(donut_frame_2, (80, 80)),
            ]
            y_pos = 200
        elif type == 'tea':
            tea_frame_1 = pygame.image.load('/Users/aliona/Desktop/app_number_2/graphics/tea_frame_1.png').convert_alpha()
            tea_frame_2 = pygame.image.load('/Users/aliona/Desktop/app_number_2/graphics/tea_frame_2.png').convert_alpha()
            self.frames = [
                pygame.transform.scale(tea_frame_1, (80, 80)),
                pygame.transform.scale(tea_frame_2, (80, 80)),
            ]
            y_pos = ground_y - 20
        elif type == 'chocolate':
            chocolate_frame_1 = pygame.image.load('/Users/aliona/Desktop/app_number_2/graphics/chocolate_frame_1.png').convert_alpha()
            chocolate_frame_2 = pygame.image.load('/Users/aliona/Desktop/app_number_2/graphics/chocolate_frame_2.png').convert_alpha()
            self.frames = [
                pygame.transform.scale(chocolate_frame_1, (80, 80)),
                pygame.transform.scale(chocolate_frame_2, (80, 80)),
            ]
            y_pos = ground_y - 30
        elif type == 'nut':
            nut_frame_1 = pygame.image.load('/Users/aliona/Desktop/app_number_2/graphics/nut_frame_1.png').convert_alpha()
            nut_frame_2 = pygame.image.load('/Users/aliona/Desktop/app_number_2/graphics/nut_frame_2.png').convert_alpha()
            self.frames = [
                pygame.transform.scale(nut_frame_1, (80, 80)),
                pygame.transform.scale(nut_frame_2, (80, 80)),
            ]
            y_pos = ground_y - 50
        elif type == 'rock':
            rock_frame_1 = pygame.image.load('/Users/aliona/Desktop/app_number_2/graphics/rock_frame_1.png').convert_alpha()
            rock_frame_2 = pygame.image.load('/Users/aliona/Desktop/app_number_2/graphics/rock_frame_2.png').convert_alpha()
            self.frames = [
                pygame.transform.scale(rock_frame_1, (90, 90)),
                pygame.transform.scale(rock_frame_2, (90, 90)),
            ]
            y_pos = ground_y
        elif type == 'scissors':
            scissors_frame_1 = pygame.image.load('/Users/aliona/Desktop/app_number_2/graphics/scissors_frame_1.png').convert_alpha()
            scissors_frame_2 = pygame.image.load('/Users/aliona/Desktop/app_number_2/graphics/scissors_frame_2.png').convert_alpha()
            self.frames = [
                pygame.transform.scale(scissors_frame_1, (90, 90)),
                pygame.transform.scale(scissors_frame_2, (90, 90)),
            ]
            y_pos = 200
        else:
            raise ValueError(f"Unknown obstacle type: {type}")

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1250), y_pos))
        self.mask = pygame.mask.from_surface(self.image)

    #animation of obstacles
    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames): 
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]
        self.mask = pygame.mask.from_surface(self.image)

    #update function for obstacles
    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy
    
    #destroy function for obstacles w
    def destroy(self):
            if self.rect.right < -100:
                self.kill()

#score display
def display_score():
    score_surf = test_font.render(f'{score}', False, 'Black')
    score_rect = score_surf.get_rect(center=(670, 70))
    screen.blit(score_surf, score_rect)

#collision detection
def collision_sprite():
    global score
    collided = pygame.sprite.spritecollide(player.sprite, obstacle_group, False, collided=pygame.sprite.collide_mask)
    #change score after collision
    for obstacle in collided:
        if obstacle.type == 'coffee':
            score += 5
            obstacle.kill()
        elif obstacle.type == 'cake':
            score += 10
            obstacle.kill()
        elif obstacle.type == 'donut':
            score += 15
            obstacle.kill()
        elif obstacle.type == 'chocolate':
            score += 20
            obstacle.kill()
        elif obstacle.type == 'tea':
            score += 100
            obstacle.kill()
        elif obstacle.type == 'nut':
            score -= 30
            obstacle.kill()
            if score < 0:
                obstacle_group.empty()
                return False
        elif obstacle.type == 'rock':
            score -= 100
            obstacle.kill()
            if score < 0:
                obstacle_group.empty()
                return False
        elif obstacle.type == 'scissors':
                obstacle_group.empty()
                return False
    return True

#setup screen
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Aliona's game")
clock = pygame.time.Clock()
test_font = pygame.font.Font('/Users/aliona/Desktop/app_number_2/font/font.ttf', 50)
button_font = pygame.font.Font('/Users/aliona/Desktop/app_number_2/font/font.ttf', 40)
game_active = False
showing_rules = False
start_time = 0
score = 0

#groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

background_surface = pygame.image.load('/Users/aliona/Desktop/app_number_2/graphics/background.jpg').convert_alpha()
background_surface = pygame.transform.scale(background_surface, (800, 600))
text_surface = test_font.render('Coffe shop', False, 'deeppink4')

chair_surface = pygame.image.load('/Users/aliona/Desktop/app_number_2/graphics/chair.png').convert_alpha()
chair_surface = pygame.transform.scale(chair_surface, (300, 400))
mirror_chair = pygame.transform.flip(chair_surface, True, False)

#intro screen
player_stand = pygame.image.load('/Users/aliona/Desktop/app_number_2/graphics/player_walk_1.webp').convert_alpha()
player_stand = pygame.transform.scale(player_stand, (200, 250))
player_stand_rect = player_stand.get_rect(center=(350, 250))

game_name = test_font.render('Aliona\'s Coffee Run', False, '#663399')
game_name_rect = game_name.get_rect(center=(400, 80))

game_message = test_font.render('Press space to run', False, "#000000")
game_message_rect = game_message.get_rect(center=(400, 400))

button_text = test_font.render('Read rules', True, "#000000", "#CAE5FF")
button_rect = button_text.get_rect(center=(400, 530))

#Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

obstacle_types = (
    ['coffee'] * 2 + ['cake'] * 2 + ['donut'] * 2 + 
    ['tea'] + ['chocolate'] + ['nut'] * 5 + ['rock'] * 5 + ['scissors']
)

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        #handle rules button click
        if not game_active and not showing_rules:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    showing_rules = True

        elif showing_rules:
            #exit rules on any key press or mouse click
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                showing_rules = False

        #start  game
        if not showing_rules:
            if game_active:
                if event.type == obstacle_timer:
                    obstacle_group.add(Obstacle(choice(obstacle_types)))
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_active = True
                    start_time = int(pygame.time.get_ticks() / 1000)
                    score = 0
                    obstacle_group.empty()
                    player.sprite.rect.midbottom = (190, 460)
                    player.sprite.velocity = 0

    #game logic
    if game_active:
        screen.blit(background_surface, (0, 0))
        screen.blit(text_surface, (300, 10))
        screen.blit(mirror_chair, (60, 240))
        
        display_score()

        player.draw(screen)
        player.update()

        if obstacle_group:
            if not collision_sprite():
                game_active = False

        if score >= 1000:
            game_active = False

        obstacle_group.draw(screen)
        obstacle_group.update()
    else:   
        screen.fill('lightpink')
        screen.blit(player_stand, player_stand_rect)
        obstacle_group.empty()
        player.sprite.rect.midbottom = (190, 460)
        player.sprite.velocity = 0      

        score_message = test_font.render(f'Your score: {score}', False, "#098F51")
        score_message_rect = score_message.get_rect(center=(200, 450))
        screen.blit(game_name, game_name_rect)

        if score == 0:
            screen.blit(game_message, game_message_rect)
        #win/lose messages
        elif score >= 1000:
            win_message = test_font.render('You win', False, "#009900")
            win_message_rect = win_message.get_rect(center=(400, 450))
            screen.blit(score_message, score_message_rect)
            screen.blit(win_message, win_message_rect)
        else:
            lost_message = test_font.render('You lost', False, "#0676bc")
            lost_message_rect = lost_message.get_rect(center=(600, 450))
            screen.blit(score_message, score_message_rect)
            screen.blit(lost_message, lost_message_rect)

        if not showing_rules:
            screen.blit(button_text, button_rect)

    #display rules screen
    if showing_rules:
        overlay = pygame.Surface((800, 600))
        overlay.set_alpha(230)
        overlay.fill('white')
        screen.blit(overlay, (0, 0))

        rules = [
            "RULES:",
            "- Use SPACE to jump",
            "- Collect coffee, cake, donut, tea, chocolate",
            "- Touching them gives points",
            "- Avoid nuts and rocks: they SUBTRACT points!",
            "- If points drop below 0, you lose.",
            "- If you hit scissors, you lose instantly.",
            "- Get 1000 points to win!",
            "- Press SPACE or click to return."
        ]
        for i, rule in enumerate(rules):
            line = button_font.render(rule, True, "#220044")
            screen.blit(line, (100, 100 + 50 * i))

    pygame.display.update()
    clock.tick(60)