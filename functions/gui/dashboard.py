import customtkinter as ctk


def dashboard():
    # size
    root = ctk.CTk()
    root.geometry("300x250")

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    # title
    label = ctk.CTkLabel(master=frame, text="PyAssistant", font=("Roboto", 24))
    label.pack(pady=12, padx=10)

    # buttons
    button = ctk.CTkButton(master=frame, text="Rename", command=print("test"))
    button.pack(pady=12, padx=10)
    root.mainloop()