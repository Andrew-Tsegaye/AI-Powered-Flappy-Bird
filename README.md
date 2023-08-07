# AI Playing Flappy Bird Game

![screen_shot](https://i.imgur.com/ZkkhzVV.png)

## Introduction

> The repository `AI-Powered-Flappy-Bird` is a project that showcases an implementation of an AI (Artificial Intelligence) algorithm playing the famous Flappy Bird game. The main focus of this project is to demonstrate how the NEAT (NeuroEvolution of Augmenting Topologies) algorithm can be utilized to evolve neural networks that control the behavior of the birds in the game.

The repository includes the Python code for the Flappy Bird game, utilizing the Pygame library for graphics and game logic. Additionally, it contains the implementation of the NEAT algorithm, which allows the AI to learn and improve its performance over generations.

***The NEAT algorithm is applied to evolve a population of neural networks that control the birds in the game. These neural networks are subjected to natural selection, mutation, and crossover, enabling them to adapt and improve their performance at navigating the obstacles in the Flappy Bird game.***

The implementation utilizes Python and the Pygame library for graphics and game logic. The NEAT algorithm is employed to evolve a population of neural networks, allowing the AI to learn and improve its performance over generations.

## Features

- AI-powered Flappy Bird game using the NEAT algorithm.
- Neural networks are evolved to control the birds' behavior in the game.
- Natural selection, mutation, and crossover are used to improve the neural networks' performance.
- Score tracking and display for monitoring the AI's progress.

## Getting Started

To get started with the AI-Powered Flappy Bird game, follow these steps:

1. Clone the repository to your local machine:

```bash
git clone https://github.com/Andrew-Tsegaye/AI-Powered-Flappy-Bird.git
```
2. Install the required dependencies. You can use pip to install them:
```bash
pip install pygame
pip install neat-python
```
3. Run the game:
```bash
python game.py
```

## How It Works
- The AI-Powered Flappy Bird game works as follows:
- The game window displays the Flappy Bird game environment, including pipes and a bird.
- The NEAT algorithm creates a population of neural networks, each controlling a bird's actions.
- The neural networks are evaluated based on their performance in the game. Birds that perform well (score higher) have higher fitness.
- Natural selection, mutation, and crossover are applied to the neural networks, creating the next generation of birds with improved behaviors.
- The process of evaluation, selection, and evolution continues across multiple generations, with the AI getting better at playing the game.

## Contributing
Contributions to the AI-Powered Flappy Bird project are welcome! If you want to contribute, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push the changes to your forked repository.
5. Create a pull request to merge your changes into the main repository.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
The implementation of the NEAT algorithm in this project is based on the neat-python library developed by [CodeReclaimers](https://github.com/CodeReclaimers/neat-python).

Special thanks to CodeReclaimers for their contribution to the NEAT algorithm and the open-source community.

## Contact
If you have any questions or suggestions, feel free to contact the project owner:

Name: Andrew Tsegaye
Email: andrewtsegaye7@gmail.com
GitHub: https://github.com/Andrew-Tsegaye

Remember to customize the README with your project-specific details, such as a more detailed explanation of how the NEAT algorithm is used, the game controls, and any additional features or improvements you've made to the game.
