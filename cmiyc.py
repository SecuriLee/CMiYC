import tkinter as tk
from tkinter import messagebox
import random

class ElusiveDialog:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Important Message")
        self.root.resizable(False, False)
        
        # Remove window decorations for a more authentic dialog look
        self.root.overrideredirect(True)
        
        # Dialog dimensions
        self.width = 300
        self.height = 120
        
        # Get screen dimensions
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        
        # Initial position (center of screen)
        x = (self.screen_width - self.width) // 2
        y = (self.screen_height - self.height) // 2
        self.root.geometry(f"{self.width}x{self.height}+{x}+{y}")
        
        # Make window stay on top
        self.root.attributes('-topmost', True)
        
        # Create dialog-like frame
        main_frame = tk.Frame(self.root, bg='#f0f0f0', relief='raised', borderwidth=2)
        main_frame.pack(fill='both', expand=True)
        
        # Title bar
        title_frame = tk.Frame(main_frame, bg='#0078d7', height=30)
        title_frame.pack(fill='x')
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(title_frame, text="Important Message", 
                              bg='#0078d7', fg='white', font=('Segoe UI', 9))
        title_label.pack(side='left', padx=8, pady=5)
        
        # Message area
        message_frame = tk.Frame(main_frame, bg='white')
        message_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        message = tk.Label(message_frame, text="Click OK to Close", 
                          bg='white', font=('Segoe UI', 10))
        message.pack(pady=15)
        
        # Button
        self.ok_button = tk.Button(message_frame, text="OK", width=10, 
                                   command=self.on_ok_click,
                                   relief='raised', borderwidth=1)
        self.ok_button.pack(pady=5)
        
        # Movement parameters
        self.escape_distance = 100  # Distance to flee from cursor
        self.speed = 30  # How far to move each time
        
        # Start monitoring mouse position
        self.check_mouse_position()
        
    def check_mouse_position(self):
        """Check mouse position and move window if too close"""
        try:
            # Get current mouse position
            mouse_x = self.root.winfo_pointerx()
            mouse_y = self.root.winfo_pointery()
            
            # Get window position
            win_x = self.root.winfo_x()
            win_y = self.root.winfo_y()
            
            # Calculate center of window
            win_center_x = win_x + self.width // 2
            win_center_y = win_y + self.height // 2
            
            # Calculate distance from mouse to window center
            dx = win_center_x - mouse_x
            dy = win_center_y - mouse_y
            distance = (dx**2 + dy**2)**0.5
            
            # If mouse is too close, move away
            if distance < self.escape_distance:
                # Calculate direction to move (away from mouse)
                if distance > 0:
                    move_x = int((dx / distance) * self.speed)
                    move_y = int((dy / distance) * self.speed)
                else:
                    # If mouse is exactly at center, move randomly
                    move_x = random.choice([-self.speed, self.speed])
                    move_y = random.choice([-self.speed, self.speed])
                
                # Calculate new position
                new_x = win_x + move_x
                new_y = win_y + move_y
                
                # Bounce off screen edges
                if new_x < 0:
                    new_x = 0
                if new_y < 0:
                    new_y = 0
                if new_x + self.width > self.screen_width:
                    new_x = self.screen_width - self.width
                if new_y + self.height > self.screen_height:
                    new_y = self.screen_height - self.height
                
                # Move the window
                self.root.geometry(f"{self.width}x{self.height}+{new_x}+{new_y}")
            
            # Continue checking (every 10ms for smooth movement)
            self.root.after(10, self.check_mouse_position)
        except tk.TclError:
            # Window was destroyed
            pass
    
    def on_ok_click(self):
        """Handle OK button click"""
        # Show a congratulatory message and close
        self.root.destroy()
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Success!", "You caught me! Well done!")
        root.destroy()
    
    def run(self):
        """Start the application"""
        self.root.mainloop()

if __name__ == "__main__":
    app = ElusiveDialog()
    app.run()
