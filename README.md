# 🐍💧🔫 Snake, Water, Gun Game

A simple, interactive command-line game written in Python. This game is a fun variation of the classic "Rock, Paper, Scissors" game, played against the computer.

## 📜 Description

The game consists of 5 rounds where you play against the computer. In each round, you can choose either Snake, Water, or Gun. The computer will randomly make its own choice, and the winner of the round is decided based on a simple set of rules. At the end of the 5 rounds, the overall winner is announced based on the final score.

## ⚖️ Rules of the Game

* **Snake vs. Water:** Snake drinks the water **(Snake wins)**.
* **Water vs. Gun:** The gun sinks in the water **(Water wins)**.
* **Gun vs. Snake:** The gun shoots the snake **(Gun wins)**.
* If both the player and the computer choose the same item, the round is a **Tie**.

## ✨ Features

* **Interactive Gameplay:** Easy-to-use text prompts for user inputs.
* **Automated Opponent:** The computer uses Python's `random` library to make unpredictable moves.
* **Score Tracking:** Keeps track of both the player's and the computer's scores across all rounds.
* **Input Validation:** Handles invalid inputs gracefully without crashing the game.

## 🛠️ Prerequisites

To run this game, you need to have Python installed on your system. 
* Python 3.x (Recommended)

## 🚀 How to Play

1. **Clone the repository** (or download the script directly):
   ```bash
   git clone [https://github.com/your-username/snake-water-gun.git](https://github.com/your-username/snake-water-gun.git)
Navigate to the project directory:

Bash
cd snake-water-gun
Run the Python script:

Bash
python game.py
Follow the on-screen instructions to choose your move:

Press s for Snake

Press w for Water

Press g for Gun

💻 Example Output
Plaintext
Welcome to Snake, Water, Gun Game!
Let's play 5 rounds.

--- Round 1 ---
Choose (s)nake, (w)ater, or (g)un: s
You chose: Snake
Computer chose: Water
Result: You win this round!
...
=== Game Over ===
Final Score -> You: 3 | Computer: 1
Congratulations! You won the game! 🎉
🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page if you want to contribute.

📝 License
This project is open-source and available under the MIT License.


---
