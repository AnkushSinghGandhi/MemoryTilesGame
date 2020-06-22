import pygame
from pygame import display, event, image
import game_config as gc
from animal import Animal
from time import sleep

total_skipped = 0


def find_index(x, y):
    row = y // gc.image_size
    col = x // gc.image_size
    index = row * gc.num_tiles_side + col
    return index


pygame.init()

display.set_caption('Memory game @ankush_singh_gandhi')

# set title of window

screen = display.set_mode((512, 512))

# making a window of 512X512 pixels

matched = image.load('other_assets/matched.png')

# load the matched image

running = True
tiles = [Animal(i) for i in range(0, gc.num_tiles_total)]
current_images = []

while running:
    current_events = event.get()

    # to get the state of various input devices, you can forego the event queue and access the input devices

    for e in current_events:

    # loop through all events

        if e.type == pygame.QUIT:

        # check event type

            running = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            (x, y) = pygame.mouse.get_pos()
            index = find_index(x, y)
            if index not in current_images:
                current_images.append(index)
            if len(current_images) > 2:
                current_images = current_images[1:]

    r = (255, 255, 255)
    screen.fill(r)
    for (_, tile) in enumerate(tiles):
        image_i = (tile.image if tile.index
                   in current_images else tile.box)
        if not tile.skip:
            screen.blit(image_i, (tile.col * gc.image_size + gc.margin,
                        tile.row * gc.image_size + gc.margin))

    display.flip()

    if len(current_images) == 2:
        (idx1, idx2) = current_images
        if tiles[idx1].name == tiles[idx2].name:
            tiles[idx1].skip = True
            tiles[idx2].skip = True
            total_skipped += 2
            sleep(0.4)
            screen.blit(matched, (0, 0))

            # display matched image starting from (0,0) wich is corner of the screen

            display.flip()

            # update the display to show the image

            sleep(0.4)
            current_images = []

    if total_skipped == len(tiles):
        running = False

print ('goodbye dear')
