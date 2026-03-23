import os
import sys
import subprocess
import webbrowser
from pathlib import Path

class GavinAssistant:
    def __init__(self):
        self.name = "Gavin 2.0"
        self.commands = {
            "open youtube": self.open_youtube,
            "open google": self.open_google,
            "open chrome": self.open_chrome,
            "open file explorer": self.open_file_explorer,
            "create folder": self.create_folder,
            "create file": self.create_file,
            "help": self.show_help,
            "exit": self.exit_assistant,
        }
    
    def start(self):
        """Start the chat loop"""
        print(f"\n{'='*50}")
        print(f"Welcome to {self.name}")
        print(f"Type 'help' for available commands")
        print(f"{'='*50}\n")
        
        while True:
            try:
                user_input = input("You: ").strip().lower()
                
                if not user_input:
                    continue
                
                self.process_command(user_input)
            except KeyboardInterrupt:
                print("\n\nGavin 2.0: Goodbye!")
                break
            except Exception as e:
                print(f"Gavin 2.0: Error - {str(e)}")
    
    def process_command(self, command):
        """Process user commands"""
        # Check for exact match first
        if command in self.commands:
            self.commands[command]()
            return
        
        # Check for commands with parameters
        for cmd_key in self.commands:
            if command.startswith(cmd_key):
                if cmd_key == "create folder":
                    folder_name = command.replace("create folder", "").strip()
                    if folder_name:
                        self.create_folder(folder_name)
                    else:
                        self.create_folder()
                elif cmd_key == "create file":
                    file_name = command.replace("create file", "").strip()
                    if file_name:
                        self.create_file(file_name)
                    else:
                        self.create_file()
                return
        
        print(f"Gavin 2.0: I don't understand that command. Type 'help' for available commands.")
    
    def open_youtube(self):
        """Open YouTube"""
        print("Gavin 2.0: Opening YouTube...")
        webbrowser.open("https://www.youtube.com")
    
    def open_google(self):
        """Open Google"""
        print("Gavin 2.0: Opening Google...")
        webbrowser.open("https://www.google.com")
    
    def open_chrome(self):
        """Open Chrome browser"""
        print("Gavin 2.0: Opening Chrome...")
        try:
            if sys.platform == "win32":
                subprocess.Popen("chrome")
            elif sys.platform == "darwin":
                subprocess.Popen(["open", "-a", "Google Chrome"])
            else:
                subprocess.Popen("google-chrome")
        except Exception as e:
            print(f"Gavin 2.0: Could not open Chrome - {str(e)}")
    
    def open_file_explorer(self):
        """Open File Explorer"""
        print("Gavin 2.0: Opening File Explorer...")
        try:
            if sys.platform == "win32":
                subprocess.Popen("explorer")
            elif sys.platform == "darwin":
                subprocess.Popen(["open", "-a", "Finder"])
            else:
                subprocess.Popen("nautilus")
        except Exception as e:
            print(f"Gavin 2.0: Could not open File Explorer - {str(e)}")
    
    def create_folder(self, folder_name=None):
        """Create a new folder"""
        if not folder_name:
            folder_name = input("Gavin 2.0: What should I name the folder? ").strip()
        
        if not folder_name:
            print("Gavin 2.0: Folder name cannot be empty.")
            return
        
        try:
            Path(folder_name).mkdir(parents=True, exist_ok=True)
            print(f"Gavin 2.0: Folder '{folder_name}' created successfully!")
        except Exception as e:
            print(f"Gavin 2.0: Could not create folder - {str(e)}")
    
    def create_file(self, file_name=None):
        """Create a new file"""
        if not file_name:
            file_name = input("Gavin 2.0: What should I name the file? ").strip()
        
        if not file_name:
            print("Gavin 2.0: File name cannot be empty.")
            return
        
        try:
            Path(file_name).touch(exist_ok=True)
            print(f"Gavin 2.0: File '{file_name}' created successfully!")
        except Exception as e:
            print(f"Gavin 2.0: Could not create file - {str(e)}")
    
    def show_help(self):
        """Display available commands"""
        print("\nGavin 2.0: Available commands:")
        print("  - open youtube       : Open YouTube in browser")
        print("  - open google        : Open Google in browser")
        print("  - open chrome        : Open Chrome browser")
        print("  - open file explorer : Open File Explorer")
        print("  - create folder      : Create a new folder")
        print("  - create file        : Create a new file")
        print("  - help               : Show this help message")
        print("  - exit               : Exit the assistant\n")
    
    def exit_assistant(self):
        """Exit the assistant"""
        print("Gavin 2.0: Goodbye!")
        sys.exit(0)


if __name__ == "__main__":
    assistant = GavinAssistant()
    assistant.start()