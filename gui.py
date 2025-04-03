import tkinter as tk
from PIL import Image, ImageTk
from tkinter import PhotoImage
import requests
from io import BytesIO
import main as api

class DogMatcherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dog Matcher")
        self.root.geometry("800x700")
        self.root.configure(bg="#E8F5E9")  # Jasnozielone tło
        self.root.iconphoto(False, PhotoImage(file='dog.png'))

        self.start_screen()

    def start_screen(self):
        self.clear_screen()

        # Tytuł
        title_label = tk.Label(
            self.root,
            text="Welcome to Dog Matcher!",
            font=("Comic Sans MS", 28, "bold"),
            bg="#388E3C",  # Ciemnozielony
            fg="white",
            pady=10
        )
        title_label.pack(fill="x", pady=(20, 10))

        # Podtytuł
        subtitle_label = tk.Label(
            self.root,
            text="Find your perfect furry friend!",
            font=("Comic Sans MS", 16),
            bg="#66BB6A",  # Średniozielony
            fg="white",
            pady=5,
        )
        subtitle_label.pack(fill="x", pady=(0, 20))

        # Obrazek psa
        image_path = "dog.jpeg"
        original_image = Image.open(image_path)
        resized_image = original_image.resize((300, 250))  # Zmniejszony obrazek
        self.image = ImageTk.PhotoImage(resized_image)

        image_label = tk.Label(self.root, image=self.image, bg="#E8F5E9")
        image_label.pack(pady=20)

        # Przycisk Start
        start_button = tk.Button(
            self.root,
            text="Start",
            font=("Comic Sans MS", 20),
            bg="#4CAF50",  # Zielony
            fg="white",
            command=self.main_screen,
            relief="solid",
            bd=3,
            padx=40,
            pady=10
        )
        start_button.config(
            highlightthickness=0,
            activebackground="#2E7D32",  # Ciemniejszy zielony
            activeforeground="white",
            borderwidth=0
        )
        start_button.pack(pady=30)  # Większy odstęp od góry

    def main_screen(self):
        self.clear_screen()

        # Tytuł
        title_label = tk.Label(
            self.root,
            text="Answer the Questions Below!",
            font=("Comic Sans MS", 24, "bold"),
            bg="#388E3C",  # Ciemnozielony
            fg="white",
            pady=10
        )
        title_label.pack(fill="x", pady=(20, 10))

        # Sekcja pytań i odpowiedzi
        qa_frame = tk.Frame(self.root, bg="white", bd=3, relief="solid")
        qa_frame.place(relx=0.5, rely=0.3, relwidth=0.8, relheight=0.2, anchor="n")

        self.question_label = tk.Label(
            qa_frame,
            text="Click 'Submit' to begin!",
            font=("Comic Sans MS", 14),
            bg="white",
            anchor="w"
        )
        self.question_label.place(relwidth=1, relheight=0.4)

        self.answer_entry = tk.Entry(qa_frame, font=("Comic Sans MS", 14), bd=3, relief="solid")
        self.answer_entry.place(rely=0.5, relwidth=0.7, relheight=0.4)

        self.answer_entry.bind("<Return>", self.next_question)

        submit_button = tk.Button(
            qa_frame,
            text="Submit",
            font=("Comic Sans MS", 12),
            bg="#4CAF50",  # Zielony
            fg="white",
            command=self.next_question,
            relief="solid",
            bd=3,
            padx=20,
            pady=10
        )
        submit_button.config(
            highlightthickness=0,
            activebackground="#2E7D32",  # Ciemniejszy zielony
            activeforeground="white",
            borderwidth=0
        )
        submit_button.place(relx=0.72, rely=0.5, relwidth=0.25, relheight=0.4)

        # Sekcja wyświetlania odpowiedzi
        data_frame = tk.Frame(self.root, bg="#E8F5E9", bd=3, relief="solid")
        data_frame.place(relx=0.5, rely=0.6, relwidth=0.8, relheight=0.3, anchor="n")

        scrollbar = tk.Scrollbar(data_frame)
        scrollbar.pack(side="right", fill="y")

        self.data_display = tk.Text(
            data_frame,
            font=("Comic Sans MS", 12),
            bg="#F1F8E9",  # Jasnozielony
            state="disabled",
            wrap="word",
            yscrollcommand=scrollbar.set,  # Powiązanie z paskiem przewijania
            padx=10,
            pady=10
        )
        self.data_display.pack(side="left", fill="both", expand=True)

        scrollbar.config(command=self.data_display.yview)

        self.answers = []
        self.questions = [q[0] for q in api.filters]
        self.current_question = 0

        self.start_quiz()

    def start_quiz(self):
        self.question_label.config(text=self.questions[0])

    def next_question(self, event=None):
        answer = self.answer_entry.get().strip()
        self.answers.append(answer)
        self.answer_entry.delete(0, tk.END)

        # Wyświetlanie odpowiedzi w czasie rzeczywistym
        self.data_display.config(state="normal")
        self.data_display.insert(tk.END, f"Q: {self.questions[self.current_question]}\nA: {answer}\n\n")
        self.data_display.config(state="disabled")

        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
            self.question_label.config(text=self.questions[self.current_question])
        else:
            self.final_screen()

    def final_screen(self):
        self.clear_screen()

        title_label = tk.Label(
            self.root,
            text="Your Perfect Match!",
            font=("Comic Sans MS", 28, "bold"),
            bg="#388E3C",
            fg="white",
            pady=10
        )
        title_label.pack(fill="x", pady=(20, 10))

        result = api.process_user_input(self.answers)

        if result and isinstance(result, tuple) and len(result) >= 3:
            breed, description, image_url = result[:3]
        else:
            breed, description, image_url = "No Results", "No matching breed found.", None

        result_label = tk.Label(
            self.root,
            text=f"Best Match: {breed}\n{description}",
            font=("Comic Sans MS", 14),
            bg="#F1F8E9",
            fg="black",
            wraplength=600,
            justify="center"
        )
        result_label.pack(pady=20)

        if image_url:
            response = requests.get(image_url)
            img_data = Image.open(BytesIO(response.content))
            img_data = img_data.resize((300, 300))
            self.dog_image = ImageTk.PhotoImage(img_data)
            image_label = tk.Label(self.root, image=self.dog_image, bg="#F1F8E9")
            image_label.pack(pady=20)

        home_button = tk.Button(
            self.root,
            text="Home",
            font=("Comic Sans MS", 14),
            bg="#4CAF50",
            fg="white",
            command=self.start_screen,
            relief="solid",
            bd=3,
            padx=20,
            pady=10
        )
        home_button.pack(pady=10)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = DogMatcherApp(root)
    root.mainloop()