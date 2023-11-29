import customtkinter as ctk
import functions.tools.tools as t

def on_enter(event):
    keyword_enter = entry.get()
    print(f"on_enter called with keyword: {keyword_enter}")
    if keyword_enter.strip():
        try:
            t.his(title=keyword_enter)
            t.keyword(key_var=keyword_enter)
        except Exception as e:
            print(f"Error when calling t.his or t.keyword: {e}")
        entry.delete(0, 'end')


# size
root = ctk.CTk()
root.geometry("300x250")

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

# title
label = ctk.CTkLabel(master=frame, text="PyAssistant", font=("Roboto", 24))
label.pack(pady=12, padx=10)

# input
entry = ctk.CTkEntry(master=frame, placeholder_text="Keyword")
entry.pack(pady=12, padx=10)

entry.bind('<Return>', on_enter)

# buttons
button = ctk.CTkButton(master=frame, text="Quit", command=root.destroy)
button.pack(pady=12, padx=10)
root.mainloop()