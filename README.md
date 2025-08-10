PASTRIX Autotyper
<!-- Replace with a URL to your screenshot -->

PASTRIX is a modern, highly configurable autotyper designed to simulate human typing. It is built with a sleek user interface using CustomTkinter and a powerful backend that works effectively in restricted environments where standard copy-pasting is disabled.

✨ Features
Modern User Interface: A clean, dark-themed UI with intuitive controls.

Multiple Typing Modes: Includes "Normal" mode for standard text fields and a specialized "Ace-editor" mode for code editors.

Customizable Hotkeys: Choose your preferred shortcut key to trigger the typing action.

Advanced Typing Options:

Line Break: Automatically presses Enter after each line.

Clear Field Before Pasting: Simulates Ctrl+A + Backspace to clear existing text.

Remove Auto Brackets: Cleans up extra brackets that some editors add automatically.

Standalone Software: Packaged as a .exe file that runs on Windows without needing Python or any libraries installed.

🚀 How to Use (For Normal Users)
No installation is needed. Just download the software and run it.

Go to the Releases section of this repository.

Under the latest release, download the PASTRIX.zip file.

Unzip the downloaded file.

Double-click PASTRIX.exe to run the application.

Configure your desired settings in the app and press START.

Click into any text field and press your chosen shortcut key to start typing.

🛠️ Building from Source (For Developers)
If you want to modify the code or build the software yourself, follow these steps.

1. Setup the Environment
First, clone the repository and install the required Python packages.

# Clone the repository
git clone [https://github.com/akashsrathaur/Pastrix.git](https://github.com/akashsrathaur/Pastrix.git)
cd Pastrix

# Install dependencies
pip install -r requirements.txt

2. Run the Application
To run the application directly from the source code:

python main.py

3. Build the Executable
To package the application into a standalone .exe file, use the following PyInstaller command. Make sure you have PyInstaller installed (pip install pyinstaller).

pyinstaller --noconsole --name "PASTRIX" --icon="assets/icon.ico" --add-data="assets;assets" main.py

The final software will be located in the dist/PASTRIX folder.

📂 Project Structure
The source code is organized as follows:

PASTRIX/
├── assets/
│   ├── github.png
│   ├── icon.ico
│   ├── instagram.png
│   └── linkedin.png
├── .gitignore
├── main.py
├── Pastrix.py
├── README.md
└── requirements.txt

main.py: Contains the code for the CustomTkinter user interface.

Pastrix.py: The core backend logic for keyboard control and typing.

assets/: Contains all static images and icons used by the application.

requirements.txt: A list of all Python dependencies.

👤 Author & Contact
Akash Singh Rathaur

GitHub: @akashsrathaur

LinkedIn: [Akash Singh Rathaur](https://www.linkedin.
