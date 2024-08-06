
#code for singular linear linked list
import tkinter as tk
from tkinter import messagebox

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.first = None

    def insert_first(self, data):
        new_node = Node(data)
        new_node.next = self.first
        self.first = new_node

    def insert_last(self, data):
        new_node = Node(data)
        if not self.first:
            self.first = new_node
        else:
            temp = self.first
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def delete_first(self):
        if not self.first:
            return
        self.first = self.first.next

    def delete_last(self):
        if not self.first:
            return
        if not self.first.next:
            self.first = None
        else:
            temp = self.first
            while temp.next.next:
                temp = temp.next
            temp.next = None

    def display(self):
        elements = []
        temp = self.first
        while temp:
            elements.append(temp.data)
            temp = temp.next
        return elements

    def count(self):
        temp = self.first
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Singly Linked List GUI")
        self.create_main_menu()

    def create_main_menu(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=10, pady=10)

        tk.Label(self.main_frame, text="Singly Linked List Operations", font=("Helvetica", 16)).pack(pady=10)

        # Button for Singly Linked List operations
        tk.Button(self.main_frame, text="Singly Linked List", command=self.show_singly_options, bg="#FF6F61", fg="white", width=30, height=2).pack(pady=10)

    def create_list_operations(self, frame, list_obj):
        self.entry_data = tk.Entry(frame)
        self.entry_data.pack(pady=5)
        
        # Operation buttons
        operations = [
            ("Insert First", lambda: self.insert_first(list_obj)),
            ("Insert Last", lambda: self.insert_last(list_obj)),
            ("Delete First", lambda: self.delete_first(list_obj)),
            ("Delete Last", lambda: self.delete_last(list_obj)),
            ("Display", lambda: self.display(list_obj)),
            ("Count", lambda: self.count(list_obj))
        ]
        
        for text, command in operations:
            button = tk.Button(frame, text=text, command=command, bg="#FFBF00", fg="black", width=15, height=2)
            button.pack(pady=5)

    def show_singly_options(self):
        self.clear_current_frame()
        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack()

        self.list = SinglyLinkedList()
        
        tk.Label(self.current_frame, text="Singly Linked List Operations", font=("Helvetica", 14)).pack(pady=10)
        self.create_list_operations(self.current_frame, self.list)

    def clear_current_frame(self):
        if hasattr(self, 'current_frame'):
            self.current_frame.pack_forget()
            del self.current_frame

    def insert_first(self, list_obj):
        data = self.entry_data.get()
        list_obj.insert_first(data)
        messagebox.showinfo("Insert First", "Inserted at the beginning")

    def insert_last(self, list_obj):
        data = self.entry_data.get()
        list_obj.insert_last(data)
        messagebox.showinfo("Insert Last", "Inserted at the end")

    def delete_first(self, list_obj):
        list_obj.delete_first()
        messagebox.showinfo("Delete First", "Deleted from the beginning")

    def delete_last(self, list_obj):
        list_obj.delete_last()
        messagebox.showinfo("Delete Last", "Deleted from the end")

    def display(self, list_obj):
        data = list_obj.display()
        messagebox.showinfo("Display", f"List: {data}")

    def count(self, list_obj):
        count = list_obj.count()
        messagebox.showinfo("Count", f"Count: {count}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()
