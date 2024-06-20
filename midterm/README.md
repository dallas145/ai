# 期中作業-CLI翻譯軟體

使用 `groq` 的 api 進行翻譯。

`groq_1.py` 參考：
- [GroqCloud](https://console.groq.com/docs/quickstart)。

`translator.py` 參考：
- [Python File(文件) 方法 | 菜鸟教程](https://www.runoob.com/python/file-methods.html)
- [Python argparse 教學：比 sys.argv 更好用，讓命令列引數整潔又有序 • 好豪筆記](https://haosquare.com/python-argparse/)
- [使用 argparse 為 Python 腳本加入 CUI 參數 - zhung](https://zhung.com.tw/article/使用-argparse-為-python-腳本加入-cui-參數%2f)
- [datetime的各種時間格式轉換－Python 套件使用(一) - 量化通 QuantPass](https://quantpass.org/python_datetime/)

## 安裝

確認已安裝`conda`

1. 使用安裝腳本：
    * Windows(在`powershell 7`測試及`powershell 5.1`皆測試成功):
    ```
    ./install.ps1
    ```
    若無法執行，請參考 [Windows PowerShell 基本操作 - 執行 Windows PowerShell 腳本](https://ithelp.ithome.com.tw/m/articles/10028377)

    * Linux(在`wsl`測試成功)
    ```
    ./install.sh
    ```

2. 不安裝，用`python`執行

    安裝套件：
    ```
    pip install groq
    ```

    ```
    python translator.py -h
    ```

## 使用方式

```
usage: translator [-h] [-m [1 or 2 or 3 or 4]] [-o] (-c | -e) ["翻譯內容"]

使用 groq 的 api 進行翻譯

positional arguments:
  "翻譯內容"                輸入要翻譯的內容，若沒有輸入，則進入互動模式

options:
  -h, --help            show this help message and exit
  -m [1 or 2 or 3 or 4], --model [1 or 2 or 3 or 4]
                        選擇模型： 1 為 llama3-8b-8192, 2 為 llama3-70b-8192, 3 為
                        mixtral-8x7b-32768, 4 為 gemma-7b-it。預設為 1
  -o, --output          將互動模式的結果紀錄至[日期_時間].md。只在互動模式生效。
  -c, --chinese         翻譯成中文
  -e, --english         翻譯成英文
```

### 安裝 + 單句翻譯


https://github.com/dallas145/ai/assets/52619674/1fe06dbb-f6f8-4f6b-af62-56eabdad978e


### 互動式翻譯成中文並留下紀錄檔


https://github.com/dallas145/ai/assets/52619674/2c3e3528-e812-48ce-91e9-438e2ce429d4

