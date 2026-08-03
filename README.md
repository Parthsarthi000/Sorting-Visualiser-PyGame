<div align="center">
  <video src="https://github.com/user-attachments/assets/86a3668b-ccca-4301-80b6-0f688ce809dd" width="650" autoplay loop muted playsinline></video>
</div>

# 📊 Sorting Visualizer (Pygame)

An interactive sorting algorithm visualizer built in Python using the **Pygame** framework. This application translates theoretical computer science sorting routines into live, step-by-step graphical displays, tracking arrays using real-time sprite mutations.

---

## 🏗️ Architecture & Component Logic

The system follows a modular architecture to isolate sorting logic from UI view routing:

* **Centralized Application Routing (`WindowState`):** Coordinates menu transitions using a dedicated application state manager. It maps mouse clicks to target view targets (`Bubble Sort`, `Selection Sort`, `Insertion Sort`) and routes control matrices seamlessly back to the home options deck upon completion.
* **Encapsulated Menu Elements (`displayScreenOptions`):** Inherits from `pygame.sprite.Sprite`. Groups the algorithmic menu text objects into automated option bounds to calculate vector hitboxes during runtime menu clicks (`colliderect`).
* **Dynamic Graphical Arrays (`Tile`):** Custom sprite components representing data metrics via varying pixel height parameters. Manages individual runtime properties including index positioning (`rect.x`), active verification indicators (`changeColorCurrentTile`), and comparator tracking (`changeColorCompareTile`).
* **Visual Sorting Implementation (`BubbleSort`):** Orchestrates procedural loop blocks that freeze execution streams using `pygame.time.delay(100)` milestones. This injects visual padding to display array data switches, comparison indicators, and sorting mutations live.

---

## 🛠️ Built With

* **Python 3**
* **Pygame Framework** (Utilizes `Sprite.Group` frameworks, automated layout rendering matrices, surface blitting controllers, and basic bounding box math)

---

## 🚀 How to Run Locally

Because this project relies on custom library configurations, launching within a stable environment configuration (like Python 3.10) ensures exact rendering accuracy.

1. **Clone the repository files:**
   ```bash
   git clone https://github.com
   cd Sorting-Visualiser-PyGame
   ```

2. **Verify/Install framework packages:**
   ```bash
   pip install pygame
   ```

3. **Execute the central runtime launcher:**
   ```bash
   python3 main.py
   ```
