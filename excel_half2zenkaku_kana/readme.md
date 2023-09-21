# Excelファイルの半角カナを全角カナに変換する

## コード参照先
ChatGPT(GPT-4)と相談しながらコード作成した。

[ChatGPT(GPT-4)プロンプト](https://chat.openai.com/share/5cf722fc-d5a2-4edb-a526-a0610b477b62)

## 確認環境
Windows10

## 準備
事前にopenpyxlのインストールが必要
```
>python -m pip install openpyxl
```

## 確認方法

```
> py .\excel_half2zenkaku_kana.py
```
* 変換対象ファイルに半角カナを含むExcelファイルを指定する
* 変換後のファイル名に半角カナから全角カナに変換したExcelファイル名を指定する
* 変換実行ボタンを押下する


## 確認バージョン
```
>py -V
Python 3.9.13
```