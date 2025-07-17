import tkinter as tk
from tkinter import messagebox


class ToDoApp:
    def  __init__(self, master):
        self.master=master
        self.master.configure(bg="light green")
        self.master.title("ToDo App")
        self.master.geometry("350x500")

        self.task_list = []

        # UI Components
        self.enter_task_label=tk.Label(master, text="Enter your task:", bg="light green")
        self.enter_task_field=tk.Entry(master)
        self.submit_button = tk.Button(master, text="Submit", command=self.insert_task, bg="red", fg="black")
        self.text_area = tk.Text(master, height=10, width=30, font="lucida 13")
        self.delete_label = tk.Label(master, text="Delete task number:", bg="light blue")
        self.task_number_field=tk.Entry(master, width=5, font="lucida 13")
        self.delete_button = tk.Button(master, text="Delete", command=self.delete_task, bg="red", fg="black")
        self.sort_button = tk.Button(master, text="Sort Tasks", command=self.sort_tasks, bg="green", fg="black")
        self.exit_button = tk.Button(master, text="Exit", command=master.quit, bg="red", fg="black")

        # Layout using grid
        # self.enter_task_label.grid(row=0, column=2)
        # self.enter_task_field.grid(row=1, column=2, ipadx=50)
        # self.submit_button.grid(row=2, column=2)
        # self.submit_button.grid(row=2, column=2)
        # self.text_area.grid(row=3, column=2, padx=10, sticky=tk.W)
        # self.delete_label.grid(row=4, column=2, pady=5)
        # self.task_number_field.grid(row=5, column=2)
        # self.delete_button.grid(row=6, column=2, pady=5)
        # self.sort_button.grid(row=7, column=2, pady=5)
        # self.exit_button.grid(row=8, column=2, pady=5)  

        self.enter_task_label.grid(row=0, column=2, pady=(10, 0), padx=20, sticky="ew")
        self.enter_task_field.grid(row=1, column=2, ipadx=50, pady=5, padx=20, sticky="ew")
        self.submit_button.grid(row=2, column=2, pady=5) 
        self.text_area.grid(row=3, column=2, padx=20, pady=10, sticky="nsew") # This will expand with window resize
        self.delete_label.grid(row=4, column=2, pady=(10, 0), padx=20, sticky="ew")
        self.task_number_field.grid(row=5, column=2, pady=5)
        self.delete_button.grid(row=6, column=2, pady=5)
        self.sort_button.grid(row=7, column=2, pady=5)
        self.exit_button.grid(row=8, column=2, pady=5)

    def _update_task_display(self):
        """Refreshes the display of all tasks in the text area."""
        self.text_area.delete(1.0, tk.END)
        for i, task in enumerate(self.task_list,1):
            self.text_area.insert(tk.END, f"[ {i} ]. {task}\n")

    def insert_task(self):
        """Adds a new task to the list and updates the display."""
        task_content=self.enter_task_field.get().strip()
        if not task_content:
            messagebox.showerror("Input Error","Please enter a task.")
            return
        self.task_list.append(task_content)
        self.enter_task_field.delete(0, tk.END)
        self._update_task_display()

    def sort_tasks(self):
        """Sorts the tasks alphabetically and updates the display."""
        if not self.task_list:
            messagebox.showinfo("Info", "No tasks to sort.")
            return
        
        self.task_list.sort()
        self._update_task_display()

    def delete_task(self):
        """Deletes a task by its number and updates the display."""
        if not self.task_list:
            messagebox.showerror("Error", "No tasks to delete.")
            return
        
        try:
            task_number = int(self.task_number_field.get())
            if 1 <= task_number <= len(self.task_list):
                self.task_list.pop(task_number - 1)
                self.task_number_field.delete(0, tk.END)
                self._update_task_display()
            else:
                messagebox.showerror("Input Error", "Invalid task number.")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number.")


if __name__ == "__main__":
    root=tk.Tk()
    app=ToDoApp(root)
    root.mainloop()