import tkinter as tk
from tkinter import ttk, messagebox

class StudentSurveyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Centennial College")
        self.geometry("420x360")
        self.configure(bg="light green")
        
        self.style = ttk.Style()
        self.style.configure("LightGreen.TFrame", background="light green")
        self.style.configure("LightGreen.TLabel", background="light green", font=("Arial", 10))
        
        self.create_widgets()
        self.reset_form()
    
    def create_widgets(self):
        frame = ttk.Frame(self, padding=15, relief="ridge", style="LightGreen.TFrame")
        frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        ttk.Label(frame, text="ICET Student Survey", font=("Arial", 12, "bold"), style="LightGreen.TLabel").grid(row=0, column=0, columnspan=2, pady=10)
        
        ttk.Label(frame, text="Full name:", style="LightGreen.TLabel").grid(row=1, column=0, sticky="w", pady=5)
        self.name_var = tk.StringVar()
        self.name_entry = ttk.Entry(frame, textvariable=self.name_var, width=30)
        self.name_entry.grid(row=1, column=1, sticky="ew", pady=5)
        
        ttk.Label(frame, text="Residency:", style="LightGreen.TLabel").grid(row=2, column=0, sticky="w", pady=5)
        self.residency_var = tk.StringVar(value="Domestic")
        ttk.Radiobutton(frame, text="Domestic", variable=self.residency_var, value="Domestic").grid(row=2, column=1, sticky="w")
        ttk.Radiobutton(frame, text="International", variable=self.residency_var, value="International").grid(row=3, column=1, sticky="w", pady=5)
        
        ttk.Label(frame, text="Program:", style="LightGreen.TLabel").grid(row=4, column=0, sticky="w", pady=5)
        self.program_var = tk.StringVar()
        self.program_combobox = ttk.Combobox(frame, textvariable=self.program_var, values=["AI", "Gaming", "Health", "Software"], width=27)
        self.program_combobox.grid(row=4, column=1, sticky="ew", pady=5)
        
        ttk.Label(frame, text="Courses:", style="LightGreen.TLabel").grid(row=5, column=0, sticky="w", pady=5)
        self.course1_var = tk.BooleanVar()
        self.course2_var = tk.BooleanVar()
        self.course3_var = tk.BooleanVar()
        
        ttk.Checkbutton(frame, text="Programming I", variable=self.course1_var).grid(row=5, column=1, sticky="w")
        ttk.Checkbutton(frame, text="Web Page Design", variable=self.course2_var).grid(row=6, column=1, sticky="w")
        ttk.Checkbutton(frame, text="Software Engineering", variable=self.course3_var).grid(row=7, column=1, sticky="w", pady=5)
        
        button_frame = ttk.Frame(frame)
        button_frame.grid(row=8, column=0, columnspan=2, pady=40)
        
        ttk.Button(button_frame, text="Reset", command=self.reset_form).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Ok", command=self.show_info).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Exit", command=self.quit).pack(side="left", padx=5)
    
    def reset_form(self):
        self.name_var.set("")
        self.residency_var.set("Domestic")
        self.program_var.set("Health")
        self.course1_var.set(False)
        self.course2_var.set(False)
        self.course3_var.set(False)
    
    def show_info(self):
        name = self.name_var.get()
        residency = self.residency_var.get()
        program = self.program_var.get()
        courses = []
        if self.course1_var.get(): courses.append("Programming I")
        if self.course2_var.get(): courses.append("Web Page Design")
        if self.course3_var.get(): courses.append("Software Engineering")
        courses_text = ", ".join(courses) if courses else "None"
        
        messagebox.showinfo("Student Information", f"Name: {name}\nResidency: {residency}\nProgram: {program}\nCourses: {courses_text}")

if __name__ == "__main__":
    app = StudentSurveyApp()
    app.mainloop()
