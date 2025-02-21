### ⚙️ **CoreEase** — Simplify Your Workflow  

CoreEase is a robust Python package designed to automate repetitive tasks, manage threads efficiently, and provide easy utilities for system operations. Whether you are handling files, automating browsers, or working with system resources, CoreEase helps you streamline your workflow with powerful, ready-to-use functions.  

---

### 🚀 **What's New in Version 0.3.0**  
- 🆕 **Compiler Support:** Convert your `.py` scripts into `.exe` files easily.  
- 🆕 **Streamlined Code Formatting:** Compact and efficient module structures.  
- 🆕 **Enhanced Thread Management:** Improved load-buffer animations and task submission.  

---

### 📌 **Key Features**  

#### 🧵 Thread Management  
- Submit tasks to threads with automatic CPU-based worker allocation.  
- Built-in animated load buffer to indicate progress.  
- Non-blocking and blocking task submission options.  

#### 🌐 Browser Automation  
- Start and control web browsers for form filling, button clicking, and link scraping.  
- Headless browsing option for fast, invisible automation.  
- Automatic detection and interaction with login fields and buttons.  

#### 📂 File and Directory Operations  
- Perform essential file operations: check existence, create, read, append, and delete.  
- Manage directories: list contents, create nested structures, and remove folders.  
- Simplified path joining for cross-platform compatibility.  

#### 💻 Compiler Support (New in v0.3.0)  
- Build `.exe` files from your `.py` scripts for easy sharing.  
- Supports multiple compilers with automatic detection and installation prompts.  

#### 🖥️ Console and System Utilities  
- Retrieve system information such as CPU count, console size, and current time.  
- Display centered output or enumerated lists directly in the terminal.  
- Execute console commands and clear the terminal easily.  

---

### 🛠️ **Installation**  

#### From PyPI:  
```bash
pip install CoreEase
```  

#### From GitHub:  
```bash
pip install git+https://github.com/Casbian/CoreEase.git
```  

---

### 📖 **Quickstart Guide**  

#### 🧵 Run Tasks with Threads  
```python
from CoreEase.executor import INIT, SUBMIT_WB

def my_task():
    print("Processing task...")

INIT()  
SUBMIT_WB(my_task)
```  

#### 🌐 Automate Browser Actions  
```python
from CoreEase.webdriver import BROWSER_START, BROWSER_GOURL, PARS_LINKS, BROWSER_CLOSE

BROWSER_START(hidden=True)  
BROWSER_GOURL("https://example.com")  
http_links, https_links = PARS_LINKS()  
print("HTTP Links:", http_links)  
print("HTTPS Links:", https_links)  
BROWSER_CLOSE()
```  

#### 📂 Manage Files  
```python
from CoreEase.explorer import FILE_EXIST, FILE_CREATE, FILE_APPEND

file_name = "data.txt"

if not FILE_EXIST(file_name):
    FILE_CREATE(file_name)

FILE_APPEND(file_name, "Appending new line to the file.")
```  

#### 💻 Compile Python Scripts (New in v0.3.0)  
```bash
python -m compiler --onefile script.py
```  

#### 🖥️ Get System Information  
```python
from CoreEase.system import ENV_CPUCOUNT, TIME_CURRENT

print("CPU Cores:", ENV_CPUCOUNT())  
print("Current Time:", TIME_CURRENT())
```  

---

### 📂 **File Structure Overview**  
```
CoreEase/
├── CoreEase/
│   ├── __init__.py
│   ├── compiler.py
│   ├── executor.py
│   ├── explorer.py
│   ├── output.py
│   ├── system.py
│   └── webdriver.py
├── README.md
├── LICENSE
└── setup.py
```  

---

### 💾 **Dependencies**  
CoreEase requires:  
- Python >= 3.7  

---

### 🧩 **Contributing**  
Contributions are welcome! Follow these steps to contribute:  
1. Fork the repository.  
2. Clone it:  
   ```bash
   git clone https://github.com/Casbian/CoreEase.git
   ```  
3. Create a new branch for your feature.  
4. Commit and push your changes.  
5. Submit a pull request.  

---

### 📜 **License**  
CoreEase is released under the **MIT License**.  
- You are free to use, modify, and distribute this software.  
- We are not liable for any damages resulting from the use of this software.  