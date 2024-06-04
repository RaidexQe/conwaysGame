import pygame


pygame.init()

BLACK = (0,0,0)
GREY = (128,128,128)
YELLOW = (255,255,0)


WIDTH, HEIGHT = 800 , 800
TILE_SIZE = 20
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT// TILE_SIZE
FPS  = 60

screen = pygame.display.set_mode((WIDTH,HEIGHT))

clock = pygame.time.Clock()

def draw_grid(positions):
    for row in range(GRID_HEIGHT):
        pygame.draw.line(screen, BLACK, (0, row * TILE_SIZE), (WIDTH, row * TILE_SIZE))

    for col in range(GRID_WIDTH):
        pygame.draw.line(screen, BLACK, (col * TILE_SIZE, 0), (col * TILE_SIZE, HEIGHT))

    # Draw colored cells based on positions
    for pos in positions:
        x, y, color = pos
        pygame.draw.rect(screen, color, pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

def main():
    running = True
    positions = set()

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get mouse position and calculate grid cell
                x, y = pygame.mouse.get_pos()
                grid_x, grid_y = x // TILE_SIZE, y // TILE_SIZE
                positions.add((grid_x, grid_y, YELLOW))  # Add color to the clicked cell

        screen.fill(GREY)
        draw_grid(positions)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
