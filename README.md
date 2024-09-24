# ChessMate

![ChessMate Screenshot](#)

## Introduction

**ChessMate** is a Python-based chess game developed using the Pygame library. This game offers an experience of real chess gameplay where players can compete against each other in Player vs Player mode. The project adheres to the official rules of chess, including special moves, valid movements, check, and checkmate detection. The AI mode is currently under development due to challenges with complexity and time constraints.

This README provides an overview of the project, how to install and use it, and information on contributing.

### Links:
- **GitHub Repository**: [ChessMate](https://github.com/Bbr011/CHESSMATE)
- **Hamza Khadraoui LinkedIn**: [(https://www.linkedin.com/in/hamza0111/)](#)
- **Youssef Nassib LinkedIn**: [https://www.linkedin.com/in/youssef-nassib-90694b270/](#)
- **Project Blog**: [ChessMate Development Journey](#)

---

## Installation

To install and run ChessMate on your local machine, follow the steps below:

### Prerequisites:
- Python 3.x
- Pygame library

### Installation Steps:
1. Clone the repository:
    ```bash
    git clone https://github.com/Bbr011/CHESSMATE.git
    ```
2. Navigate into the project directory:
    ```bash
    cd CHESSMATE
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the game:
    ```bash
    python main.py
    ```

---

## Usage

ChessMate currently supports:

1. **Player vs. Player**: Traditional chess gameplay against another player.
2. **Player vs. AI (Under Development)**: AI functionality is in progress and expected to be added in future updates.

### How to Play:
- Select and move chess pieces using your mouse.
- The game follows standard chess rules for valid moves.
- Notifications appear when in check or checkmate.
- When a player takes out a piece it apears on the side of the screen

### Screenshot:
![ChessMate Gameplay Screenshot](#)

---

## Features

- **Player vs. Player Mode**: Enjoy a local match against another human player.
- **Check/Checkmate Detection**: Game notifies players when in check or checkmate.
- **Pawn upgarde**: Pawn upgrades to a queen when it reachs the lase row.

---

## Roadmap

### Completed Features:
- Chess piece movement with validation.
- Check and checkmate detection.
- Pawn upgrad.

### Incomplete Features:
- AI opponent (delayed due to the complexity and lack of experience with AI development).

---

## Contributing

Contributions to ChessMate are welcome! Whether you want to help build the AI, enhance the user interface, or fix bugs, feel free to contribute.

### Contribution Steps:
1. Fork the repository.
2. Create a new branch (`feature/your-feature` or `bugfix/your-bugfix`).
3. Push your changes to the branch.
4. Submit a pull request for review.

### Ideas for Contributions:
- **AI Development**: Implement an AI opponent using Minimax or Alpha-Beta pruning algorithms.
- **UI Enhancements**: Improve the game's UI/UX.
- **Additional Chess Features**: Implement special chess rules like pawn promotion, en passant, etc.

---

## Related Projects

Here are a few projects related to chess or game development that you might find interesting:

- [Chess.js](https://github.com/jhlywa/chess.js): A chess engine implemented in JavaScript.
- [Pygame Examples](https://github.com/pygame/pygame): A collection of Pygame examples and tutorials.

---

## Licensing

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Technical Challenges & Insights

### Challenges:
The biggest challenge we encountered was implementing the game's AI. Due to limited experience in AI development, we decided to delay this feature to future iterations. Another key challenge was managing the chess movement logic, particularly for special moves like castling and en passant. These moves required significant research to ensure the game adhered to official chess rules.

### Team & Collaboration:
Our team struggled with maintaining a consistent meetup schedule due to personal reasons. Despite this, we were able to make small but steady progress toward completing the core functionality of the game.

### What I Learned:
Developing ChessMate deepened my understanding of game development and Python's Pygame library. I now have a much better grasp of event handling, state management, and building game logic. Although we couldn’t implement the AI as planned, I’m proud of how the movement and game mechanics turned out.

---

## Future Plans

- **AI Implementation**: We plan to add AI functionality using well-known algorithms.
- **Online Multiplayer**: Expanding the game for online matches.
- **UI Improvements**: Enhancing the overall look and feel of the game.
- **Mobile Support**: Making ChessMate mobile-compatible.

---

Thank you for checking out **ChessMate**! Feel free to explore the code, contribute, or just enjoy playing the game.
