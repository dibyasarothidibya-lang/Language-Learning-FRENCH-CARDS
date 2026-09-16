# 🗂️ Flashy - Flash Card Language Learning App

An interactive language learning flashcard desktop application built in Python using **Tkinter** and **Pandas**. Test and reinforce your vocabulary with timed card flips and automatic progress tracking!

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![GUI](https://img.shields.io/badge/GUI-Tkinter-brightgreen)
![Data](https://img.shields.io/badge/Library-Pandas-150458?logo=pandas&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue)

---

## 📖 Overview

Flashy presents frequently used French words on clean, rounded flashcards. 
- You have **3 seconds** to recall the English translation before the card automatically flips.
- If you already know the word, click the **Checkmark (✔)** button: the word is marked as mastered, saved, and removed from future practice rounds.
- If you don't know it yet, click the **Cross (✖)** button: the card stays in your study rotation for continuous practice.

---

## ✨ Features

- **⚡ Automatic 3-Second Flip**: Cards automatically turn over from French to English after 3 seconds using asynchronous Tkinter timer callbacks (`window.after`).
- **👆 Manual Flip on Click**: In a rush? Simply click the card directly at any time to flip it immediately.
- **💾 Smart Progress Tracking**: 
  - Tracks known words and writes remaining vocabulary to `data/words_to_learn.csv`.
  - Automatically picks up where you left off on next app launch.
  - Gracefully handles initial setups, empty lists, and completion states.
- **🎨 Polished Modern Interface**:
  - Consistent `#B1DDC6` mint theme.
  - Borderless, translucent rounded card images and circular buttons.
  - Dynamic text color transitions (black on front, white on back).

---

## 🕹️ Controls & Interaction

| Control | Action | Function |
| :--- | :--- | :--- |
| **Cross Button (✖)** | Click | Don't know the word yet; keeps it in rotation and pulls next card. |
| **Check Button (✔)** | Click | Know the word; removes it from `words_to_learn.csv` and pulls next card. |
| **Card Face** | Click | Instantly flips between French and English. |

---

## 📋 Prerequisites

Ensure you have **Python 3.7+** installed. You will also need `pandas`:

```bash
pip install pandas
```

*(Note: `tkinter`, `os`, and `random` are built directly into Python's standard library).*

---

## 🚀 How to Run

1. **Navigate to the project directory**:
   ```bash
   cd DAY-31/flash-card-project-start
   ```

2. **Launch the application**:
   ```bash
   python main.py
   ```

---

## 📁 Project Structure

```text
flash-card-project-start/
├── data/
│   ├── french_words.csv      # Default vocabulary dataset (French to English)
│   └── words_to_learn.csv    # Dynamic user progress file (auto-generated)
├── images/
│   ├── card_front.png        # Front card background
│   ├── card_back.png         # Back card background (flipped)
│   ├── right.png             # Known word button icon (green check)
│   └── wrong.png             # Unknown word button icon (red cross)
├── .gitignore                # Ignores bytecache, virtual environments, and progress CSV
├── main.py                   # Main application code and Tkinter GUI loop
└── README.md                 # Project documentation
```

---

## 🤝 Contributing

Contributions, feedback, and pull requests are welcome! You can expand this project with:
- Additional language datasets (Spanish, German, Japanese, etc.)
- Customizable countdown timer lengths
- Pronunciation audio playback using `gTTS` or `playsound`

---

## 📜 License

This project is open-source and licensed under the [MIT License](LICENSE).
