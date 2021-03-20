import click
import pygame
import random
import math
import time
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((798, 600))

pygame.mixer.init()

pygame.display.set_caption("Rajpath Wheels")
logo = pygame.image.load('car game/nitclogo.bmp')
pygame.display.set_icon(logo)

introfont = pygame.font.SysFont("agencyfb.ttf", 60)


def introimg():
    intro = pygame.image.load("car game/RAJTPATH2 copy.jpg")

    screen.blit(intro, (0, 0))


def instructionimg():
    instruct = pygame.image.load("car game/instruction copy.jpg")
    run = True
    while run:
        screen.blit(instruct, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False


def aboutimg():
    aboutimg = pygame.image.load("car game/about copy.jpg")
    run = True
    while run:
        screen.blit(aboutimg, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False


def play(x, y):
    playtext = introfont.render("PLAY", True, (255, 0, 0))
    screen.blit(playtext, (x, y))


def about(x, y):
    abouttext = introfont.render("ABOUT", True, (255, 0, 0))
    screen.blit(abouttext, (x, y))


def instruction(x, y):
    instructiontext = introfont.render("INSTRUCTION", True, (255, 0, 0))
    screen.blit(instructiontext, (x, y))


def show(a, x):
    screen.blit(a, (0, 0))
    pygame.display.update()

    screen.blit(x, (380, 250))
    pygame.display.update()
    time.sleep(1)


def introscreen():
    run = True
    pygame.mixer.music.load("car game/upbeat.mp3")
    pygame.mixer.music.play()
    while run:
        screen.fill((0, 0, 0))
        introimg()
        play(100, 220)
        instruction(270, 220)
        about(615, 220)

        x, y = pygame.mouse.get_pos()

        button1 = pygame.Rect(60, 210, 175, 50)
        button2 = pygame.Rect(260, 210, 320, 50)
        button3 = pygame.Rect(600, 210, 165, 50)

        pygame.draw.rect(screen, (255, 255, 255), button1, 6)
        pygame.draw.rect(screen, (255, 255, 255), button2, 6)
        pygame.draw.rect(screen, (255, 255, 255), button3, 6)

        if button1.collidepoint(x, y):
            pygame.draw.rect(screen, (155, 0, 0), button1, 6)
            if click:
                countdown()

        if button2.collidepoint(x, y):
            pygame.draw.rect(screen, (155, 0, 0), button2, 6)
            if click:
                instructionimg()

        if button3.collidepoint(x, y):
            pygame.draw.rect(screen, (155, 0, 0), button3, 6)
            if click:
                aboutimg()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()


def countdown():
    font2 = pygame.font.SysFont('agencyfb.ttf', 200)
    countdownbg = pygame.image.load('car game/RAJTPATH2.jpg')
    three = font2.render('3', True, (187, 30, 16))
    two = font2.render('2', True, (255, 255, 0))
    one = font2.render('1', True, (51, 165, 50))
    go = font2.render('GO', True, (0, 255, 0))

    show(countdownbg, three)
    show(countdownbg, two)
    show(countdownbg, one)
    countdownbg = pygame.image.load('car game/Road.jpg')
    show(countdownbg, go)

    def gameloop():
        pygame.mixer.music.load('car game/gamemusic.mp3')
        pygame.mixer.music.play()

        crash_sound = pygame.mixer.Sound('car game/car_crash.wav')
        font1 = pygame.font.SysFont("agencyfb.ttf", 50)

        def show_score(x, y):
            score = font1.render("SCORE: " + str(score_value), True, (255, 0, 0))
            screen.blit(score, (x, y))

        score_value = 0

        with open("car game/highscore.txt", "r") as f:
            highscore = f.read()

        def show_highscore(x, y):
            Hiscore_text = font1.render("HIGH SCORE :" + str(highscore), True, (255, 0, 0))
            screen.blit(Hiscore_text, (x, y))
            pygame.display.update()

        def gameover():
            gameoverimg = pygame.image.load("car game/gameoverraj.png")
            run = True
            while run:
                screen.blit(gameoverimg, (0, 0))
                time.sleep(0.5)
                show_score(100, 500)
                time.sleep(0.5)
                show_highscore(500, 500)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        pygame.quit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            introscreen()
                        if event.key == pygame.K_ESCAPE:
                            run = False
                            pygame.quit()

        bg = pygame.image.load("car game/Road.jpg")

        maincar = pygame.image.load("car game/Usercar.png")
        maincarX = 315
        maincarY = 495
        maincarX_change = 0
        maincarY_change = 0

        car1 = pygame.image.load("car game/Car_1second2.png")
        car1X = random.randint(210, 500)
        car1Y = -200

        car2 = pygame.image.load("car game/car_2second.png")
        car2X = random.randint(210, 500)
        car2Y = -400

        car3 = pygame.image.load("car game/car_3scnd.png")
        car3X = random.randint(210, 500)
        car3Y = -600

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        maincarX_change += 2
                    if event.key == pygame.K_LEFT:
                        maincarX_change -= 2
                    if event.key == pygame.K_UP:
                        maincarY_change += 2
                    if event.key == pygame.K_DOWN:
                        maincarY_change -= 2
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        maincarX_change = 0
                    if event.key == pygame.K_LEFT:
                        maincarX_change = 0
                    if event.key == pygame.K_UP:
                        maincarY_change = 0
                    if event.key == pygame.K_DOWN:
                        maincarY_change = 0

            if maincarX < 210:
                maincarX = 210
            if maincarX > 500:
                maincarX = 500

            if maincarY < 0:
                maincarY = 0
            if maincarY > 495:
                maincarY = 495

            screen.fill((0, 0, 0))

            screen.blit(bg, (0, 0))

            screen.blit(maincar, (maincarX, maincarY))

            screen.blit(car1, (car1X, car1Y))
            screen.blit(car2, (car2X, car2Y))
            screen.blit(car3, (car3X, car3Y))

            maincarX += maincarX_change
            maincarY -= maincarY_change

            car1Y += 2
            car2Y += 2
            car3Y += 2

            if car1Y > 670:
                car1Y = -100
                car1X = random.randint(210, 500)
                score_value += 1
            if car2Y > 670:
                car2Y = -100
                car2X = random.randint(210, 500)
                score_value += 1
            if car3Y > 670:
                car3Y = -100
                car3X = random.randint(210, 500)
                score_value += 1

            if score_value > int(highscore):
                highscore = int(score_value)

            def iscollision(car1X, car1Y, maincarX, maincarY):
                distance = math.sqrt(
                    math.pow((car1X + 25) - (maincarX + 25), 2) + math.pow((car1Y + 30) - (maincarY + 30), 2))

                # checking if distance is smaller than 50 after then collision will occur

                if distance < 50:
                    return True
                else:
                    return False

            coll1 = iscollision(car1X, car1Y, maincarX, maincarY)
            coll2 = iscollision(car2X, car2Y, maincarX, maincarY)
            coll3 = iscollision(car3X, car3Y, maincarX, maincarY)

            if coll1:
                screen.fill((200, 215, 250))
                car1Ychange = 0
                car2Ychange = 0
                car3Ychange = 0
                maincarX_change = 0
                maincarY_change = 0
                pygame.mixer.music.stop()
                crash_sound.play()
                time.sleep(1)
                gameover()

            # if coll2 occur
            if coll2:
                screen.fill((200, 215, 250))
                car1Ychange = 0
                car2Ychange = 0
                car3Ychange = 0
                maincarX_change = 0
                maincarY_change = 0
                pygame.mixer.music.stop()
                crash_sound.play()
                time.sleep(1)
                gameover()

            # if coll3 occur
            if coll3:
                screen.fill((200, 215, 250))
                car1Ychange = 0
                car2Ychange = 0
                car3Ychange = 0
                maincarX_change = 0
                maincarY_change = 0
                pygame.mixer.music.stop()
                crash_sound.play()
                time.sleep(1)
                gameover()

            show_score(570, 280)
            show_highscore(0, 0)
            with open("car game/highscore.txt", "w") as f:
                f.write(str(highscore))

            pygame.display.update()

    gameloop()


introscreen()
