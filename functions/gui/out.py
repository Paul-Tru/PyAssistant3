import customtkinter as ctk


def answer(title, text):
    root = ctk.CTk()
    root.geometry("400x250")

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    # title
    label = ctk.CTkLabel(master=frame, text=title, font=("Roboto", 24))
    label.pack(pady=5, padx=10)

    # text
    text_widget = ctk.CTkTextbox(root, wrap="word")
    text_widget.pack(fill="both", expand=True)
    text_widget.insert("0.0", text)
    text_widget.configure(state="disabled", font=("Arial", 15))
    root.mainloop()