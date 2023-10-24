import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import PyPDF2
from pdfminer.high_level import extract_text
import threading
from tqdm import tqdm
import traceback  # エラーの詳細を取得するためのモジュール

class PDFConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF to TXT コンバータ")

        # ウィンドウの初期サイズを設定
        self.root.geometry("300x200")
        
        self.library_choice = tk.StringVar(value="PyPDF2")
        tk.Radiobutton(root, text="PyPDF2", variable=self.library_choice, value="PyPDF2").pack()
        tk.Radiobutton(root, text="pdfminer.six", variable=self.library_choice, value="pdfminer.six").pack()

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
            text = ''
            if self.library_choice.get() == "PyPDF2":
                with open(self.pdf_file_path, 'rb') as file:
                    reader = PyPDF2.PdfReader(file)
                    for page_num in tqdm(range(len(reader.pages)), unit="page"):
                        text += reader.pages[page_num].extract_text()
                        self.update_progress((page_num+1) / len(reader.pages) * 100)
            else:
                text = extract_text(self.pdf_file_path)
            
            self.save_as_txt(text)
        except Exception as e:
            # エラーの詳細を取得して表示
            error_detail = traceback.format_exc()
            messagebox.showerror("エラー", f"PDFの読み込み中にエラーが発生しました: {e}\n\n詳細:\n{error_detail}")
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
