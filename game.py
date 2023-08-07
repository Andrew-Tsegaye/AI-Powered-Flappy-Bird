import pygame
import neat
import os
from graphics_ui.bird import Bird
from graphics_ui.pipe import Pipe
from graphics_ui.base import Base

# Initialize pygame and the font for displaying text on the game window
pygame.font.init()

# Constants for the game window dimensions and generation number
WIN_WIDTH = 500
WIN_HEIGHT = 800

GEN = 0

# Font for displaying score and generation number on the game window
STAT_FONT = pygame.font.SysFont("comicsans", 50)

# Load the background image and scale it to fit the game window
BACKGROUND_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))

# Function to draw the game window
def draw_window(win, birds, pipes, base, score, gen):
    # Draw the background image at the top-left corner of the window
    win.blit(BACKGROUND_IMAGE, (0, 0))

    # Draw each pipe on the game window
    for pipe in pipes:
        pipe.draw(win)

    # Render and display the score and generation number on the game window
    score_text = STAT_FONT.render("Score: " + str(score), 1, (255, 255, 255))
    win.blit(score_text, (WIN_WIDTH - 10 - score_text.get_width(), 10))

    gen_text = STAT_FONT.render("Gen: " + str(gen), 1, (255, 255, 255))
    win.blit(gen_text, (10, 10))

    # Draw each bird on the game window
    for bird in birds:
        bird.draw(win)

    # Draw the base (ground) on the game window
    base.draw(win)

    # Update the game window to display the changes
    pygame.display.update()

# Main function that runs the game for each generation
def main(genomes, config):
    global GEN
    GEN += 1

    # Lists to store the neural networks, genomes, and bird objects for each generation
    nets = []
    ge = []
    birds = []

    # Loop through each genome in the genomes list
    for _, genome in genomes:
        # Create a feedforward neural network for the genome using the NEAT configuration
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)

        # Create a Bird object and add it to the birds list
        birds.append(Bird(230, 350))

        # Set the fitness of the genome to 0 initially
        genome.fitness = 0

        # Add the genome to the ge list
        ge.append(genome)

    # Create the base (ground) and the first pipe for the game
    base = Base(730)
    pipes = [Pipe(600)]

    # Initialize the game window and clock
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()

    # Initialize the score and run flag for the game loop
    score = 0
    run = True

    # Main game loop
    while run:
        # Limit the frame rate to 30 frames per second
        clock.tick(30)

        # Event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

        # Determine which pipe to use for the neural network's input
        pipe_ind = 0
        if len(birds) > 0:
            if len(pipes) > 1 and birds[0].x > pipes[0].x + pipes[0].PIPE_TOP.get_width():
                pipe_ind = 1
        else:
            run = False
            break

        # Neural network evaluation loop
        for bird_index, bird in enumerate(birds):
            # Move the bird
            bird.move()

            # Increase the fitness of the genome for the bird
            ge[bird_index].fitness += 0.1

            # Activate the neural network to get the output for the current bird's input
            output = nets[bird_index].activate((bird.y, abs(bird.y - pipes[pipe_ind].height), abs(bird.y - pipes[pipe_ind].bottom)))

            # If the output value is greater than 0.5, make the bird jump
            if output[0] > 0.5:
                bird.jump()

        # Pipe handling loop
        add_pipe = False
        remove_pipes = []
        for pipe in pipes:
            # Check for bird-pipe collisions
            for bird_index, bird in enumerate(birds):
                if pipe.collide(bird):
                    # If a bird collides with a pipe, remove it from the lists
                    birds.pop(bird_index)
                    nets.pop(bird_index)
                    ge.pop(bird_index)

                # If a bird passes a pipe, increase its fitness and add a new pipe
                if not pipe.passed and pipe.x < bird.x:
                    pipe.passed = True
                    add_pipe = True

            # If a pipe moves off the screen, mark it for removal
            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                remove_pipes.append(pipe)

            # Move the pipe
            pipe.move()

        # Add a new pipe if needed
        if add_pipe:
            score += 1
            for genome in ge:
                genome.fitness += 5
            pipes.append(Pipe(600))

        # Remove pipes that have moved off the screen
        for pipe_to_remove in remove_pipes:
            pipes.remove(pipe_to_remove)

        # Remove birds that hit the ground or fly too high
        for bird_index, bird in enumerate(birds):
            if bird.y + bird.image.get_height() >= 730 or bird.y < 0:
                birds.pop(bird_index)
                nets.pop(bird_index)
                ge.pop(bird_index)

        # Move the base (ground)
        base.move()

        # Draw the game window with the updated game elements
        draw_window(win, birds, pipes, base, score, GEN)

# Function to run the NEAT algorithm for the Flappy Bird game
def run(config_path):
    # Load the NEAT configuration from the given config file
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

    # Create a NEAT population
    population = neat.Population(config)

    # Add reporters to display information during the evolution process
    population.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    population.add_reporter(stats)

    # Run the NEAT algorithm with the main function as the fitness function
    winner = population.run(main, 50)

# Entry point of the program
if __name__ == "__main__":
    # Get the path to the NEAT configuration file
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config-feedforward.txt")

    # Start the NEAT algorithm with the specified configuration
    run(config_path)