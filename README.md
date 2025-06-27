# Day 4 – Rock, Paper, Scissors

This project is a beginner-friendly Python implementation of the classic game Rock, Paper, Scissors. The player competes against the computer, which randomly selects its move. The game also includes basic ASCII art to visualize each choice.

## 🎮 How It Works

- The user is prompted to enter a number: 0 for Rock, 1 for Paper, or 2 for Scissors.
- The computer makes a random choice.
- The result is displayed using ASCII art along with the winner of the round.

## 🔢 Game Logic

- Rock (0) beats Scissors (2)
- Scissors (2) beats Paper (1)
- Paper (1) beats Rock (0)
- If both choices are the same, it's a draw

## 💡 Skills Learned

- Using the `random` module
- Creating and indexing Python lists
- ASCII art implementation
- Input validation and error handling

## 🖥 Example Output

<pre>
Welcome to Rock Paper Scissors!
What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.
1
You chose:
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

PC chose: 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
You loose. PC won. Better luck next time.</pre>
