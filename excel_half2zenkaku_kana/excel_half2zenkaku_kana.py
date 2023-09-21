import openpyxl
import tkinter as tk
from tkinter import filedialog, messagebox

def convert_half_to_full_katakana(s):
    conversions = {
        "ｱ": "ア", "ｲ": "イ", "ｳ": "ウ", "ｴ": "エ", "ｵ": "オ",
        "ｶ": "カ", "ｷ": "キ", "ｸ": "ク", "ｹ": "ケ", "ｺ": "コ",
        "ｻ": "サ", "ｼ": "シ", "ｽ": "ス", "ｾ": "セ", "ｿ": "ソ",
        "ﾀ": "タ", "ﾁ": "チ", "ﾂ": "ツ", "ﾃ": "テ", "ﾄ": "ト",
        "ﾅ": "ナ", "ﾆ": "ニ", "ﾇ": "ヌ", "ﾈ": "ネ", "ﾉ": "ノ",
        "ﾊ": "ハ", "ﾋ": "ヒ", "ﾌ": "フ", "ﾍ": "ヘ", "ﾎ": "ホ",
        "ﾏ": "マ", "ﾐ": "ミ", "ﾑ": "ム", "ﾒ": "メ", "ﾓ": "モ",
        "ﾔ": "ヤ", "ﾕ": "ユ", "ﾖ": "ヨ",
        "ﾗ": "ラ", "ﾘ": "リ", "ﾙ": "ル", "ﾚ": "レ", "ﾛ": "ロ",
        "ﾜ": "ワ", "ｦ": "ヲ", "ﾝ": "ン",
        "ｧ": "ァ", "ｨ": "ィ", "ｩ": "ゥ", "ｪ": "ェ", "ｫ": "ォ",
        "ｬ": "ャ", "ｭ": "ュ", "ｮ": "ョ", "ｯ": "ッ",
        "ｶﾞ": "ガ", "ｷﾞ": "ギ", "ｸﾞ": "グ", "ｹﾞ": "ゲ", "ｺﾞ": "ゴ",
        "ｻﾞ": "ザ", "ｼﾞ": "ジ", "ｽﾞ": "ズ", "ｾﾞ": "ゼ", "ｿﾞ": "ゾ",
        "ﾀﾞ": "ダ", "ﾁﾞ": "ヂ", "ﾂﾞ": "ヅ", "ﾃﾞ": "デ", "ﾄﾞ": "ド",
        "ﾊﾞ": "バ", "ﾋﾞ": "ビ", "ﾌﾞ": "ブ", "ﾍﾞ": "ベ", "ﾎﾞ": "ボ",
        "ﾊﾟ": "パ", "ﾋﾟ": "ピ", "ﾌﾟ": "プ", "ﾍﾟ": "ペ", "ﾎﾟ": "ポ",
        "ｰ": "ー"
    }

    for k, v in sorted(conversions.items(), key=lambda x: -len(x[0])):
        s = s.replace(k, v)
    return s

    
def convert_excel_file(input_filename, output_filename):
    wb = openpyxl.load_workbook(input_filename)

    # 全てのワークシートをループ
    for ws in wb:
        for row in ws:
            for cell in row:
                if cell.value and isinstance(cell.value, str):
                    cell.value = convert_half_to_full_katakana(cell.value)

    # 変更を保存
    wb.save(output_filename)
    
def browse_input_file():
    file_name = filedialog.askopenfilename(title="変換対象のExcelファイルを選択", filetypes=[("Excel files", "*.xlsx")])
    input_var.set(file_name)

def browse_output_file():
    file_name = filedialog.asksaveasfilename(title="変換後のExcelファイル名を選択", filetypes=[("Excel files", "*.xlsx")], defaultextension=".xlsx")
    output_var.set(file_name)

def execute_conversion():
    input_file = input_var.get()
    output_file = output_var.get()

    if not input_file or not output_file:
        messagebox.showerror("エラー", "ファイル名を指定してください。")
        return
    
    convert_excel_file(input_file, output_file)
    messagebox.showinfo("完了", "変換完了!")

app = tk.Tk()
app.title("Excel変換ツール")

input_var = tk.StringVar()
output_var = tk.StringVar()

tk.Label(app, text="変換対象ファイル:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
tk.Entry(app, textvariable=input_var, width=40).grid(row=0, column=1, padx=10, pady=5)
tk.Button(app, text="参照", command=browse_input_file).grid(row=0, column=2, padx=10, pady=5)

tk.Label(app, text="変換後のファイル名:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
tk.Entry(app, textvariable=output_var, width=40).grid(row=1, column=1, padx=10, pady=5)
tk.Button(app, text="参照", command=browse_output_file).grid(row=1, column=2, padx=10, pady=5)

tk.Button(app, text="変換実行", command=execute_conversion).grid(row=2, columnspan=3, pady=20)

app.mainloop()
