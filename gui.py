import tkinter as tk
import main as api

root = tk.Tk()
root.title("Dog Matcher")
root.geometry("800x700")
root.configure(bg="#f0f8ff")  

title_label = tk.Label(
    root,
    text="Welcome to Dog Matcher!",
    font=("Helvetica", 24, "bold"),
    bg="#4682b4", 
    fg="white",  
    pady=10
)
title_label.pack(fill="x")

subtitle_label = tk.Label(
    root,
    text="Find your perfect furry friend!",
    font=("Helvetica", 16),
    bg="#5f9ea0",  
    fg="white",
    pady=5
)
subtitle_label.pack(fill="x")

qa_frame = tk.Frame(root, bg="white", bd=5, relief="groove")
qa_frame.place(relx=0.5, rely=0.25, relwidth=0.9, relheight=0.2, anchor="n")

question_label = tk.Label(
    qa_frame,
    text="Click 'Start' to begin!",
    font=("Helvetica", 14),
    bg="white",
    anchor="w"
)
question_label.place(relwidth=1, relheight=0.4)

answer_entry = tk.Entry(qa_frame, font=("Helvetica", 14))
answer_entry.place(rely=0.5, relwidth=0.7, relheight=0.4)

submit_button = tk.Button(
    qa_frame,
    text="Submit",
    font=("Helvetica", 12),
    bg="#4682b4",
    fg="white",
    command=lambda: next_question()
)
submit_button.place(relx=0.72, rely=0.5, relwidth=0.25, relheight=0.4)

data_frame = tk.Frame(root, bg="white", bd=5, relief="groove")
data_frame.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.4, anchor="n")

data_display = tk.Text(
    data_frame,
    font=("Helvetica", 12),
    bg="#f5f5f5", 
    state="disabled",
    wrap="word",
    padx=10,
    pady=10
)
data_display.place(relwidth=1, relheight=1)

answers = []
questions = [q[0] for q in api.filters]
current_question = 0

def next_question():
    global current_question
    answer = answer_entry.get()
    answers.append(answer)
    answer_entry.delete(0, tk.END)

    if current_question < len(questions) - 1:
        current_question += 1
        question_label.config(text=questions[current_question])
    else:
        breed, description = api.process_user_input(answers) or ("No results found", "")
        data_display.config(state="normal")
        data_display.insert(tk.END, f"Best Match: {breed}\n{description}\n")
        data_display.config(state="disabled")

start_button = tk.Button(
    root,
    text="Start",
    font=("Helvetica", 14),
    bg="#32cd32",  
    fg="white",
    command=lambda: question_label.config(text=questions[0])
)
start_button.place(relx=0.5, rely=0.2, anchor="n", relwidth=0.3, relheight=0.05)

root.mainloop()