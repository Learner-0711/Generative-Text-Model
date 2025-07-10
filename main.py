import tkinter as tk
from tkinter import ttk, messagebox
from gpt_utils import get_ai_reply

# ---------------- Window Configuration ----------------
window = tk.Tk()
window.title("AI Prompt Assistant")
window.geometry("880x560")
window.configure(bg="#f5f7fa")
window.minsize(720, 500)

# ---------------- Styling ----------------
style = ttk.Style()
style.theme_use("clam")
style.configure("Gen.TButton", font=("Verdana", 11, "bold"), padding=6)
style.configure("TLabel", font=("Verdana", 11), background="#f5f7fa")
style.configure("TEntry", font=("Verdana", 11))
style.configure("TText", font=("Verdana", 11))

style.map("Gen.TButton",
          background=[("active", "#204080")],
          foreground=[("active", "white")])

# ---------------- Functions ----------------
def process_query():
    query_text = input_field.get().strip()
    if not query_text:
        messagebox.showwarning("Input Required", "Please enter a question or prompt.")
        return
    output_area.delete("1.0", tk.END)
    output_area.insert(tk.END, "Processing...\n")
    window.update()
    result = get_ai_reply(query_text)
    output_area.delete("1.0", tk.END)
    output_area.insert(tk.END, result)

# ---------------- Widgets ----------------
heading = ttk.Label(window, text="Ask Your AI Assistant", font=("Verdana", 17, "bold"), foreground="#204080")
heading.pack(pady=18)

input_label = ttk.Label(window, text="Write your query here:")
input_label.pack()

input_field = tk.Entry(window, font=("Verdana", 11), width=88, bd=2, relief="groove")
input_field.pack(pady=10, padx=20)

generate_btn = ttk.Button(window, text="Get Response", style="Gen.TButton", command=process_query)
generate_btn.pack(pady=10)

output_label = ttk.Label(window, text="AI Response:")
output_label.pack(pady=5)

output_area = tk.Text(window, height=12, width=100, font=("Verdana", 10), wrap="word",
                      relief="sunken", bd=2, bg="white", fg="#222")
output_area.pack(padx=20, pady=10)

footer = tk.Label(window, text="Developed by Yash Sharma", font=("Verdana", 9, "bold"),
                  bg="#f5f7fa", fg="#777")
footer.pack(side=tk.BOTTOM, pady=6)

# ---------------- Run App ----------------
window.mainloop()
