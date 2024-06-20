import argparse
import os
import groq_1
from sys import exit
from datetime import datetime

# parse command line arguments.
parser = argparse.ArgumentParser(prog="translator", description="使用 groq 的 api 進行翻譯")
parser.add_argument("content", metavar="\"翻譯內容\"", nargs='?', type=str, help="輸入要翻譯的內容，若沒有輸入，則進入互動模式" )
parser.add_argument("-m", "--model",\
    nargs='?', type=int,choices=[1, 2, 3, 4], default=1, metavar="1 or 2 or 3 or 4",\
    help="選擇模型： 1 為 llama3-8b-8192, 2 為 llama3-70b-8192, 3 為 mixtral-8x7b-32768, 4 為 gemma-7b-it。預設為 1")
parser.add_argument("-o", "--output", action='store_true', help="將互動模式的結果紀錄至[日期_時間].md。只在互動模式生效。")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-c", "--chinese", action='store_true', help="翻譯成中文")
group.add_argument("-e", "--english", action='store_true', help="翻譯成英文")

args = parser.parse_args()

# Use datetime as log filename.
time_now = datetime.now().strftime("%Y%m%d_%H%M")

language = "english" if args.english else "chinese"

try:
    if os.environ.get("GROQ_API_KEY") is None:
        raise
except:
    print("Can't get GROQ_API_KEY...")
    print("Exiting...")
    exit()

if args.content is None:
    print("")
    print("Interactive mode")
    if args.output:
        print("")
        print(f"Log file: ./logs/{time_now}.md")
    print("")
    print(f"Translate to {language.capitalize()}")
    print("")
    groq_1.main_loop(args.model, language, time_now, args.output)

else:
    print("")
    print(f"Translate to {language.capitalize()}")
    groq_1.main_noloop(args.model, args.content, language)