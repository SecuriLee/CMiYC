import tkinter as tk
from tkinter import messagebox
import random

class ElusiveDialog:
    def __init__(self):
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        
        # Win98 Colors
        self.W98_GREY = "#c0c0c0"
        self.W98_BLUE = "#000080"
        self.W98_WHITE = "#ffffff"
        self.W98_DARK_GREY = "#808080"
        
        self.width = 320
        self.height = 140
        
        # Center Window
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        x = (sw - self.width) // 2
        y = (sh - self.height) // 2
        self.root.geometry(f"{self.width}x{self.height}+{x}+{y}")
        self.root.attributes('-topmost', True)
        
        # Main Border (Classic 3D effect)
        self.outer_frame = tk.Frame(self.root, bg=self.W98_GREY, highlightthickness=2, 
                                   highlightbackground=self.W98_WHITE, 
                                   highlightcolor=self.W98_DARK_GREY, relief='raised', bd=2)
        self.outer_frame.pack(fill='both', expand=True)
        
        # Title Bar
        self.title_bar = tk.Frame(self.outer_frame, bg=self.W98_BLUE, height=22)
        self.title_bar.pack(fill='x', padx=2, pady=2)
        self.title_bar.pack_propagate(False)
        
        self.title_label = tk.Label(self.title_bar, text="System Error", 
                                   bg=self.W98_BLUE, fg='white', 
                                   font=('MS Sans Serif', 8, 'bold'))
        self.title_label.pack(side='left', padx=5)

        # Fake Close Button (Non-functional, for aesthetics)
        self.close_btn = tk.Label(self.title_bar, text="×", bg=self.W98_GREY, fg='black',
                                 font=('Arial', 10, 'bold'), width=2, relief='raised', bd=1)
        self.close_btn.pack(side='right', padx=2, pady=2)
        
        # Content Area
        self.content = tk.Frame(self.outer_frame, bg=self.W98_GREY)
        self.content.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Classic Icon Placeholder (A blue circle with a '?')
        self.icon_lbl = tk.Label(self.content, text="?", font=('Times New Roman', 24, 'bold'),
                                fg='white', bg='#0000ff', width=2, relief='sunken', bd=2)
        self.icon_lbl.pack(side='left', padx=(5, 15))
        
        self.message = tk.Label(self.content, text="An unknown error occurred.\nPress OK to ignore.", 
                               bg=self.W98_GREY, font=('MS Sans Serif', 8), justify='left')
        self.message.pack(side='left', pady=5)
        
        # OK Button
        self.ok_button = tk.Button(self.outer_frame, text="OK", width=10, 
                                  command=self.on_ok_click,
                                  bg=self.W98_GREY, activebackground=self.W98_GREY,
                                  font=('MS Sans Serif', 8),
                                  relief='raised', bd=2)
        self.ok_button.pack(side='bottom', pady=15)
        
        self.escape_distance = 120
        self.speed = 40
        self.check_mouse_position()

    def check_mouse_position(self):
        try:
            mx, my = self.root.winfo_pointerxy()
            wx, wy = self.root.winfo_x(), self.root.winfo_y()
            
            cx, cy = wx + self.width // 2, wy + self.height // 2
            dx, dy = cx - mx, cy - my
            distance = (dx**2 + dy**2)**0.5
            
            if distance < self.escape_distance:
                move_x = int((dx / distance) * self.speed) if distance > 0 else random.randint(-50, 50)
                move_y = int((dy / distance) * self.speed) if distance > 0 else random.randint(-50, 50)
                
                nx = max(0, min(wx + move_x, self.root.winfo_screenwidth() - self.width))
                ny = max(0, min(wy + move_y, self.root.winfo_screenheight() - self.height))
                
                self.root.geometry(f"+{nx}+{ny}")
            
            self.root.after(10, self.check_mouse_position)
        except: pass

    def on_ok_click(self):
        self.root.destroy()
        messagebox.showinfo("Win98", "Error successfully ignored.")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ElusiveDialog()
    app.run()
