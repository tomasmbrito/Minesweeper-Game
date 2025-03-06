# Minesweeper-Game
A full Python implementation of the classic Minesweeper game using custom data structures and logic.

# Minesweeper Game Engine 💣🪖

This project is a complete implementation of the classic **Minesweeper** game, developed in **Python** as part of the **Fundamentals of Programming** course at **Instituto Superior Técnico (IST)**.

The goal is to recreate the traditional gameplay mechanics using custom Abstract Data Types (ADTs) and to manage the entire game logic, from board generation to player interactions.

---

## 🧩 Game Overview

The Minesweeper game consists of a rectangular grid of cells (parcels), some of which hide mines. The objective is to reveal all safe cells without detonating any mines. Players receive hints via numbers indicating the count of mines in adjacent cells.

Key gameplay mechanics include:
- Cleaning cells (revealing if they are safe or detonating a mine).
- Marking suspected cells with flags.
- Automatic cleaning of adjacent cells when no neighboring mines are present.
- Random mine placement after the first move, ensuring a safe initial play.

---

## 🚀 Features

- **Custom Data Structures (ADTs)**  
  Implementation of abstract data types for:
  - Pseudo-random number generator (Xorshift).
  - Board coordinates.
  - Parcels (cells) with state management.
  - The game board itself.

- **Core Game Functions**  
  - Dynamic mine generation.
  - Automatic cell reveal logic.
  - Victory detection and game-ending conditions.

- **Interactive Gameplay**  
  Turn-based player input to clean or flag cells, with real-time board updates.

---

<img width="424" alt="image" src="https://github.com/user-attachments/assets/0097b358-ec73-4dc1-b276-9bf4368628d7" />

---

## 📥 Input

The game receives parameters to set up the board:
- The last column (character).
- The last row (integer).
- The total number of mines.
- The bit size of the random number generator (32 or 64).
- The seed for random generation.

### Example:

```python
minas('Z', 5, 6, 32, 2)
```

---

## 📤 Output

The game runs interactively in the console, displaying the board after each move and checking for victory or defeat.

---

## ⚙️ How to Run

No external libraries are required. Simply execute the `.py` file with Python 3:

```bash
python3 minesweeper.py
```

Make sure you have **Python 3.7+** installed.

---

## 🧰 Technologies

- **Language:** Python 3
- **Built-in modules only:** No external dependencies (except `functools.reduce`).

