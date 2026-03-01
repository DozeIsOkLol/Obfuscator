"""
GUI Interface for Lua Obfuscator
Simple and intuitive interface for obfuscating Lua scripts
"""

import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext, messagebox
import threading
from lua_obfuscator import LuaObfuscator
from advanced_obfuscator import apply_advanced_obfuscation

class ObfuscatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Lua Obfuscator - Pro Edition")
        self.root.geometry("1000x700")
        self.root.configure(bg='#1e1e1e')
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TButton', background='#0d7377', foreground='white', borderwidth=0, focuscolor='none')
        style.map('TButton', background=[('active', '#14a085')])
        style.configure('TLabel', background='#1e1e1e', foreground='#ffffff')
        style.configure('TFrame', background='#1e1e1e')
        
        self.create_widgets()
        
    def create_widgets(self):
        # Title
        title = tk.Label(
            self.root,
            text="🔒 Advanced Lua Obfuscator",
            font=('Arial', 20, 'bold'),
            bg='#1e1e1e',
            fg='#0d7377'
        )
        title.pack(pady=10)
        
        # Main container
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Left panel - Input
        left_frame = ttk.Frame(main_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        tk.Label(
            left_frame,
            text="Input Lua Script:",
            font=('Arial', 12, 'bold'),
            bg='#1e1e1e',
            fg='#ffffff'
        ).pack(anchor=tk.W)
        
        self.input_text = scrolledtext.ScrolledText(
            left_frame,
            wrap=tk.WORD,
            font=('Consolas', 10),
            bg='#2d2d2d',
            fg='#ffffff',
            insertbackground='white'
        )
        self.input_text.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Right panel - Output
        right_frame = ttk.Frame(main_frame)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5)
        
        tk.Label(
            right_frame,
            text="Obfuscated Output:",
            font=('Arial', 12, 'bold'),
            bg='#1e1e1e',
            fg='#ffffff'
        ).pack(anchor=tk.W)
        
        self.output_text = scrolledtext.ScrolledText(
            right_frame,
            wrap=tk.WORD,
            font=('Consolas', 10),
            bg='#2d2d2d',
            fg='#00ff00',
            insertbackground='white'
        )
        self.output_text.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Control panel
        control_frame = ttk.Frame(self.root)
        control_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Options frame
        options_frame = ttk.Frame(control_frame)
        options_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # Obfuscation level
        tk.Label(
            options_frame,
            text="Obfuscation Level:",
            font=('Arial', 10, 'bold'),
            bg='#1e1e1e',
            fg='#ffffff'
        ).grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        
        self.level_var = tk.StringVar(value="extreme")
        level_combo = ttk.Combobox(
            options_frame,
            textvariable=self.level_var,
            values=["basic", "advanced", "extreme", "paranoid"],
            state="readonly",
            width=15
        )
        level_combo.grid(row=0, column=1, padx=5, pady=5)
        
        # Advanced options checkboxes
        self.anti_debug_var = tk.BooleanVar(value=True)
        tk.Checkbutton(
            options_frame,
            text="Anti-Debug",
            variable=self.anti_debug_var,
            bg='#1e1e1e',
            fg='#ffffff',
            selectcolor='#2d2d2d',
            activebackground='#1e1e1e',
            activeforeground='#ffffff'
        ).grid(row=1, column=0, padx=5, pady=2, sticky=tk.W)
        
        self.vm_wrapper_var = tk.BooleanVar(value=True)
        tk.Checkbutton(
            options_frame,
            text="VM Wrapper",
            variable=self.vm_wrapper_var,
            bg='#1e1e1e',
            fg='#ffffff',
            selectcolor='#2d2d2d',
            activebackground='#1e1e1e',
            activeforeground='#ffffff'
        ).grid(row=1, column=1, padx=5, pady=2, sticky=tk.W)
        
        self.junk_code_var = tk.BooleanVar(value=True)
        tk.Checkbutton(
            options_frame,
            text="Junk Code",
            variable=self.junk_code_var,
            bg='#1e1e1e',
            fg='#ffffff',
            selectcolor='#2d2d2d',
            activebackground='#1e1e1e',
            activeforeground='#ffffff'
        ).grid(row=2, column=0, padx=5, pady=2, sticky=tk.W)
        
        self.control_flow_var = tk.BooleanVar(value=True)
        tk.Checkbutton(
            options_frame,
            text="Control Flow",
            variable=self.control_flow_var,
            bg='#1e1e1e',
            fg='#ffffff',
            selectcolor='#2d2d2d',
            activebackground='#1e1e1e',
            activeforeground='#ffffff'
        ).grid(row=2, column=1, padx=5, pady=2, sticky=tk.W)
        
        # Buttons frame
        buttons_frame = ttk.Frame(control_frame)
        buttons_frame.pack(side=tk.RIGHT, padx=5)
        
        ttk.Button(
            buttons_frame,
            text="📂 Load File",
            command=self.load_file
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            buttons_frame,
            text="🔒 Obfuscate",
            command=self.obfuscate_script
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            buttons_frame,
            text="💾 Save Output",
            command=self.save_file
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            buttons_frame,
            text="🗑️ Clear",
            command=self.clear_all
        ).pack(side=tk.LEFT, padx=5)
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready")
        status_bar = tk.Label(
            self.root,
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            anchor=tk.W,
            bg='#0d7377',
            fg='#ffffff',
            font=('Arial', 9)
        )
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
    def load_file(self):
        """Load a Lua file into the input text area"""
        filename = filedialog.askopenfilename(
            title="Select Lua Script",
            filetypes=[("Lua files", "*.lua"), ("All files", "*.*")]
        )
        if filename:
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    content = f.read()
                self.input_text.delete(1.0, tk.END)
                self.input_text.insert(1.0, content)
                self.status_var.set(f"Loaded: {filename}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load file:\n{str(e)}")
    
    def save_file(self):
        """Save the obfuscated output to a file"""
        content = self.output_text.get(1.0, tk.END).strip()
        if not content:
            messagebox.showwarning("Warning", "No output to save!")
            return
        
        filename = filedialog.asksaveasfilename(
            title="Save Obfuscated Script",
            defaultextension=".lua",
            filetypes=[("Lua files", "*.lua"), ("All files", "*.*")]
        )
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(content)
                self.status_var.set(f"Saved: {filename}")
                messagebox.showinfo("Success", f"File saved successfully!\n{filename}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file:\n{str(e)}")
    
    def clear_all(self):
        """Clear both input and output text areas"""
        self.input_text.delete(1.0, tk.END)
        self.output_text.delete(1.0, tk.END)
        self.status_var.set("Cleared")
    
    def obfuscate_script(self):
        """Obfuscate the script in a separate thread"""
        script = self.input_text.get(1.0, tk.END).strip()
        if not script:
            messagebox.showwarning("Warning", "Please enter a script to obfuscate!")
            return
        
        self.status_var.set("Obfuscating...")
        self.root.config(cursor="wait")
        
        def obfuscate_thread():
            try:
                # Basic obfuscation
                obfuscator = LuaObfuscator(script)
                result = obfuscator.obfuscate(level=self.level_var.get())
                
                # Apply advanced techniques if selected
                if any([
                    self.anti_debug_var.get(),
                    self.vm_wrapper_var.get(),
                    self.junk_code_var.get(),
                    self.control_flow_var.get()
                ]):
                    options = {
                        'anti_debug': self.anti_debug_var.get(),
                        'vm_wrapper': self.vm_wrapper_var.get(),
                        'junk_code': self.junk_code_var.get(),
                        'control_flow': self.control_flow_var.get()
                    }
                    result = apply_advanced_obfuscation(result, options)
                
                # Update GUI in main thread
                self.root.after(0, lambda: self.update_output(result))
            except Exception as e:
                self.root.after(0, lambda: self.show_error(str(e)))
        
        thread = threading.Thread(target=obfuscate_thread)
        thread.daemon = True
        thread.start()
    
    def update_output(self, result):
        """Update output text area with obfuscated result"""
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(1.0, result)
        self.root.config(cursor="")
        self.status_var.set(f"✓ Obfuscated successfully! ({len(result)} bytes)")
    
    def show_error(self, error_msg):
        """Show error message"""
        self.root.config(cursor="")
        self.status_var.set("Error during obfuscation")
        messagebox.showerror("Obfuscation Error", f"An error occurred:\n{error_msg}")


def launch_gui():
    """Launch the GUI application"""
    root = tk.Tk()
    app = ObfuscatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    launch_gui()
