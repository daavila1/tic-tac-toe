# Tic-Tac-Toe AI (Minimax & Pygame)
An AI implementation for the Tic-Tac-Toe game using the Minimax algorithm. The AI evaluates possible moves recursively to make optimal decisions, ensuring the best outcome. Additionally, it allows player vs player gameplay. 

✅ Built with Pygame for the game interface

✅ Optimal decision-making for unbeatable AI

<p align="center">
  <img src="https://i.imgur.com/8H1Gi3i.png" width="200" />
  <img src="https://i.imgur.com/xM6obj7.png" width="200" />
  <img src="https://i.imgur.com/cUG3x42.png" width="200" />
  <img src="https://i.imgur.com/gXzfUqz.png" width="200" />
</p>

## Minimax Algorithm in This Implementation
The AI uses the Minimax algorithm to evaluate all possible moves and choose the best one. The algorithm works by simulating all future board states and assigning a score to each move based on the likelihood of winning or losing.

### Utility function
The utility function determines the score of a board state and is defined as:

$$
U(w) = w \times (n + 1)
$$

Where:

- $w$ is the winner of the board (`1` for X, `-1` for O, `0` for a tie).
- $n$ is the number of empty spaces left on the board.

The function rewards quicker victories by assigning a higher score for fewer remaining spaces, pushing the AI to finish the game as soon as possible.

# Installation and usage
Prerequisites: Python 3.8 or higher, pip.

1. Clone this repository:
```bash
git clone ...
cd tic-tac-toe
```

2. Create virtual environment (optionally but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
Or set it up via [VS Code](https://code.visualstudio.com/docs/python/environments)


3. Install required dependencies
```bash
pip install -r requirements.txt
```

4. Run the game with:
```bash
python runner.py
```

