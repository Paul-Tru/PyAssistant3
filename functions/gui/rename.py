import customtkinter as ctk


def tools_rename():

    def on_enter(event):
        keyword_enter = entry.get()
        print(f"on_enter called with keyword: {keyword_enter}")
        if keyword_enter.strip():
            entry.delete(0, 'end')

    # size
    root = ctk.CTk()
    root.geometry("300x250")

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    # title
    label = ctk.CTkLabel(master=frame, text="Rename", font=("Roboto", 24))
    label.pack(pady=12, padx=10)

    # input
    entry = ctk.CTkEntry(master=frame, placeholder_text="Path")
    entry.pack(pady=12, padx=10)

    entry.bind('<Return>', on_enter)

    # buttons
    button = ctk.CTkButton(master=frame, text="Quit", command=root.destroy)
    button.pack(pady=12, padx=10)
    root.mainloop()
