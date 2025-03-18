import gym
import pygame
import numpy as np
import random
from gym import spaces

WIDTH, HEIGHT = 600, 400
PLAYER_SIZE = 30
OBSTACLE_SIZE = 20
PLAYER_SPEED = 10
OBSTACLE_SPEED = 15
FPS = 60

class AvoidanceEnv(gym.Env):
    def __init__(self):
        super(AvoidanceEnv, self).__init__()

        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("AI Avoidance Game")

        self.action_space = spaces.Discrete(3)
        self.observation_space = spaces.Box(low=0, high=max(WIDTH, HEIGHT),
                                            shape=(4,), dtype=np.float32)
        

        self.reset()

    def reset(self):
        self.player_x = 50
        self.player_y = HEIGHT // 2
        self.obstacle_x = WIDTH
        self.obstacle_y = random.randint(self.player_y - 20, self.player_y + 30)
        self.done = False
        return np.array([self.player_x, self.player_y, self.obstacle_x, self.obstacle_y], dtype=np.float32)

    def step(self, action):

        self.clock.tick(FPS)

        if action == 1 and self.player_y > 10:
            self.player_y -= PLAYER_SPEED
        elif action == 2 and self.player_y < HEIGHT - PLAYER_SIZE - 10:
            self.player_y += PLAYER_SPEED

        reward = 1
        self.obstacle_x -= OBSTACLE_SPEED
        if self.obstacle_x < 0:
            self.obstacle_x = WIDTH
            self.obstacle_y = random.randint(self.player_y - 20, self.player_y + 30)
            reward += 3
            print("Né thành công, +3 điểm")

        if pygame.Rect.colliderect(pygame.Rect(self.player_x, self.player_y, PLAYER_SIZE, PLAYER_SIZE), pygame.Rect(self.obstacle_x, self.obstacle_y, OBSTACLE_SIZE, OBSTACLE_SIZE)):
            reward -= 10
            self.done = True
            print("Trúng đạn, -10 điểm")

        if self.player_y > HEIGHT - 50 or self.player_y < 50:  
            reward -= 5  # Phạt nếu ở quá gần rìa màn hình
            print("Quá gần mép, -5 điểm")

        return np.array([self.player_x, self.player_y, self.obstacle_x, self.obstacle_y], dtype=np.float32), reward, self.done, {}

    def render(self):
        self.screen.fill((255, 255, 255))
        pygame.draw.rect(self.screen, (0, 0, 255), (self.player_x, self.player_y, PLAYER_SIZE, PLAYER_SIZE))
        pygame.draw.rect(self.screen, (255, 0, 0), (self.obstacle_x, self.obstacle_y, OBSTACLE_SIZE, OBSTACLE_SIZE))
        pygame.display.update()

    def close(self):
        pygame.quit()
