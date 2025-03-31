import tkinter as tk
HEIGHT = 700
WIDTH = 800

root = tk.Tk()
root.title("Dog Matcher")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

label = tk.Label(root, text="Welcome to the Dog Finder!", font=("Helvetica", 24, "bold"), bg="lightblue")
label.place(relx=0.5, rely=0.05, anchor='n', relwidth=0.9, relheight=0.1)

label = tk.Label(root, text="A perfect place to find your lifelong friend", font=("Helvetica", 16), bg="lightblue")
label.place(relx=0.5, rely=0.15, anchor='n', relwidth=0.9, relheight=0.05)

#logo = tk.PhotoImage(file='dog.png')
#logo_label = tk.Label(root, image=logo)
#logo_label.place(relx=0.6, rely=0.6, anchor='n', relwidth=0.9, relheight=0.05)

start_button = tk.Button(root, text="Let's get started", font=("Helvetica", 14), anchor='n', bg='red')
start_button.place(relx=0.5, rely=0.2, anchor='n', relwidth=0.5, relheight=0.05)

qa_frame = tk.Frame(root, bg="white", bd=5)
qa_frame.place(relx=0.5, rely=0.25, relwidth=0.9, relheight=0.2, anchor="n")

question_label = tk.Label(qa_frame, text="Question will appear here", font=("Helvetica", 14), anchor="w", bg="white")
question_label.place(relwidth=1, relheight=0.4)

answer_entry = tk.Entry(qa_frame, font=("Helvetica", 14))
answer_entry.place(rely=0.5, relwidth=0.7, relheight=0.4)

submit_button = tk.Button(qa_frame, text="Submit", font=("Helvetica", 12), bg="lightblue", command=lambda: update_data())
submit_button.place(relx=0.72, rely=0.5, relwidth=0.25, relheight=0.4)

data_frame = tk.Frame(root, bg="white", bd=5)
data_frame.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.4, anchor="n")

data_display = tk.Text(data_frame, font=("Helvetica", 12), bg="lightgray", state="disabled")
data_display.place(relwidth=1, relheight=1)


def update_data():
    user_answer = answer_entry.get()
    if user_answer:
        data_display.config(state="normal")
        data_display.insert(tk.END, f"User Answer: {user_answer}\n")
        data_display.config(state="disabled")
        answer_entry.delete(0, tk.END)

        question_label.config(text="Next question will appear here")



root.mainloop()