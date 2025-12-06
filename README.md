# 🚀 Pastrix

> **Paste anywhere, even where it’s blocked** — Pastrix is a Python-based GUI tool that simulates keystrokes to bypass paste restrictions (perfect for ACE Editor and similar environments).

---

## ✨ Features
- 🖱 **Bypass paste restrictions** on websites & editors.
- ⚙ **Two Modes**: Normal & ACE Editor.
- ⌨ **Custom Shortcut Key** (default: Right Ctrl).
- 📝 Options:
  - Line break after each line.
  - Remove everything before pasting.
  - Remove auto-completion brackets.
- 📦 Can be converted into a **standalone .exe** (no Python required).

---

## 📦 Requirements
Install dependencies:
```bash
pip install -r requirements.txt
```
**Dependencies:**
- [`pynput`](https://pypi.org/project/pynput/)
- [`pyperclip`](https://pypi.org/project/pyperclip/)

---

## 🚀 How to Run
1. **Clone the repo**:
   ```bash
   git clone https://github.com/akashsrathaur/pastrix.git
   cd pastrix
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the GUI**:
   ```bash
   python main.py
   ```
4. **Usage**:
   - Select mode, shortcut key, and options.
   - Click **START**.
   - Copy text and press your shortcut key to paste anywhere.

---

## 📂 Directory Structure
```
Pastrix/
├── assets/                # Icons and images
│   ├── icon.ico
│   ├── icon.png
│   ├── icon.py
├── main.py                 # GUI entry point
├── Pastrix.py              # Core paste logic
├── requirements.txt        # Dependencies
├── build.sh                # Build script (PyInstaller)
├── README.md               # Documentation
├── .gitignore
```

---

## 🛠 Build to EXE
To create a standalone `.exe`:
```bash
pip install pyinstaller
pyinstaller --noconsole --onefile --icon=assets/icon.ico main.py
```
- Your `.exe` will be in the `dist` folder.
- You can run it without Python installed.

---

## 👤 Author

**Akash Singh Rathaur**  

[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/akashsrathaur/)  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/akashsrathaur/)  
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/akashsrathaur)

---

💡 *Feel free to fork, contribute, or open issues to improve Pastrix.*

## License

This project is open source and available under the MIT License.


## Testing

To run tests, use the built-in test suite included with the project.
