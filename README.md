# Gavin 2.0

**The mini version of me that obeys me** 🤖

A personal assistant that can chat with Gavin and execute simple commands.

## Features (Phase 1)

- ✅ Text-based chat interface
- ✅ Open websites (YouTube, Google)
- ✅ Open applications (Chrome, File Explorer)
- ✅ Create folders and files
- ✅ Command help system

## Project Structure

```
gavin-2.0/
├── Python/
│   ├── assistant.py          # Main Python backend
│   └── requirements.txt       # Python dependencies
├── CSharp/
│   ├── MainWindow.xaml        # C# GUI
│   └── MainWindow.xaml.cs     # C# Code-behind
├── README.md
└── .gitignore
```

## Getting Started

### Python Backend

1. **Install Python** (3.8+)
2. **Install dependencies**:
   ```bash
   cd Python
   pip install -r requirements.txt
   ```
3. **Run the assistant**:
   ```bash
   python assistant.py
   ```

### Available Commands

- `open youtube` - Open YouTube in browser
- `open google` - Open Google in browser
- `open chrome` - Open Chrome browser
- `open file explorer` - Open File Explorer
- `create folder` - Create a new folder
- `create file` - Create a new file
- `help` - Show help message
- `exit` - Exit the assistant

## Phase 1 Roadmap

- [x] Setup Python backend chat loop
- [x] Implement website opening commands
- [x] Implement app launching commands
- [x] Implement file/folder creation
- [ ] Create C# GUI wrapper
- [ ] Testing and documentation

## License

MIT License - Feel free to use and modify!

---

**Built with Python & C# | Developed by Gavin**
