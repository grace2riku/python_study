import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import PyPDF2
import threading
from tqdm import tqdm

class PDFConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF to TXT コンバータ")

        # ウィンドウの初期サイズを設定
        self.root.geometry("300x150")
        
        self.convert_btn = tk.Button(root, text="PDFをテキストに変換", command=self.start_conversion)
        self.convert_btn.pack(pady=20)

        self.progress = ttk.Progressbar(root, orient="horizontal", mode="determinate")
        self.progress.pack(pady=20, fill=tk.X)

    def start_conversion(self):
        self.pdf_file_path = filedialog.askopenfilename(filetypes=[("PDFファイル", "*.pdf")])
        if self.pdf_file_path:
            self.progress["value"] = 0
            self.convert_btn["state"] = "disabled"
            thread = threading.Thread(target=self.convert_pdf_to_txt)
            thread.start()

    def update_progress(self, value):
        self.progress["value"] = value
        self.root.update_idletasks()

    def convert_pdf_to_txt(self):
        try:
            with open(self.pdf_file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = ''
                for page_num in tqdm(range(len(reader.pages)), unit="page"):
                    text += reader.pages[page_num].extract_text()
                    self.update_progress((page_num+1) / len(reader.pages) * 100)
                self.save_as_txt(text)
        except Exception as e:
            messagebox.showerror("エラー", f"PDFの読み込み中にエラーが発生しました: {e}")
        finally:
            self.convert_btn["state"] = "normal"

    def save_as_txt(self, text):
        txt_file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("テキストファイル", "*.txt")])
        if txt_file_path:
            with open(txt_file_path, 'w', encoding="utf-8") as file:
                file.write(text)
            messagebox.showinfo("成功", "テキストファイルとして保存しました。")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFConverter(root)
    root.mainloop()
