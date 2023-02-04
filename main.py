import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkFont
# import pandas as pd             #DataFrameを使う
# from openpyxl import Workbook   #Excelに書き込む
import os                       #パソコンの情報を使用する
from functools import partial   #関数やメソッドの操作

# 
# 変数
# 
C_symptoms = ["発熱","咳","倦怠感","味覚または嗅覚の消失"]   # チェックボタンのテキスト
O_symptoms = ["喉の痛み","頭痛","痛み","下痢","皮膚の発疹、または手足の指の変色","眼の充血または炎症"]  # チェックボタンのテキストに応じたポイント
S_symptoms  = ["呼吸が苦しい、または息切れ","発話障害、運動障害、錯乱","胸の痛み"]
score = 0   # コロナかどうか判定する点数
check_v1 = []
check_v2 = []
check_v3 = []


# 
# 関数
# 
def adobaisu():
    global score
    score = 0
    for i in range(len(C_symptoms)):
        # チェックボタンがCheckされているとき
        if check_v1[i].get():
            score += 3  # 点数に 1加算
    
    for i in range(len(O_symptoms)):
        # チェックボタンがCheckされているとき
        if check_v2[i].get():
            score += 1  # 点数に 1加算

    for i in range(len(S_symptoms)):
        # チェックボタンがCheckされているとき
        if check_v3[i].get():
            score += 5  # 点数に 1加算

    if score >= 10:
        messagebox.showinfo('メッセージ','コロナ可能性があります。')
    else:
        messagebox.showinfo('メッセージ','コロナ可能性がありません。')

def check_page():
    global root,cframe,check_v1, check_v2, check_v3

    # root = tk.Tk()
    root.title('コロナ検査SE')
    root.geometry('500x600+200+100')

    lframe.destroy()

    cframe = tk.Frame(root)
    cframe.pack(fill=tk.BOTH)

    # check_v = tk.BooleanVar()
    
    checkFont = tkFont.Font(family='Helvetica', size=10)
    labelFont = tkFont.Font(family='Helvetica', size=30)
    buttonFont = tkFont.Font(family='Helvetica', size=20)

    label = tk.Label(
        cframe,
        text='体状態',
        font=labelFont
    ) 
    label.pack(ipadx=10, ipady=10, pady=20)

    frame = tk.Frame(cframe, pady=20, padx=100, relief=tk.GROOVE, bd=4)
    frame.pack()

    # CheckButtonの状態
    for i in range(len(C_symptoms)):
        check_v1.append(tk.BooleanVar(value=False))
    for i in range(len(O_symptoms)):
        check_v2.append(tk.BooleanVar(value=False))
    for i in range(len(S_symptoms)):
        check_v3.append(tk.BooleanVar(value=False))
    # CheckButtonの作成
    for i in range(len(C_symptoms)):
        check = tk.Checkbutton(
            frame,
            text=C_symptoms[i],
            variable=check_v1[i],
            onvalue=True,
            offvalue=False,
            font=checkFont
        )
        check.pack(anchor=tk.W)
    for i in range(len(O_symptoms)):
        check = tk.Checkbutton(
            frame,
            text=O_symptoms[i],
            variable=check_v2[i],
            onvalue=True,
            offvalue=False,
            font=checkFont
        )
        check.pack(anchor=tk.W)
    for i in range(len(S_symptoms)):
        check = tk.Checkbutton(
            frame,
            text=S_symptoms[i],
            variable=check_v3[i],
            onvalue=True,
            offvalue=False,
            font=checkFont
        )
        check.pack(anchor=tk.W)

    button = tk.Button(
        cframe,
        text='結論', 
        relief=tk.GROOVE, 
        bd=4, 
        command=adobaisu,
        font=buttonFont
        )

    button.pack(ipadx=10, ipady=10, pady=20)

def login_page():
    global root,lframe
    root.title('コロナ検査SE ログイン')
    root.geometry('500x250+200+100')

    rframe.destroy()

    lframe = tk.Frame(root)
    lframe.pack(fill=tk.BOTH)

    u_frame = tk.Frame(lframe, pady=0, padx=100, relief=tk.FLAT, bd=4)
    u_frame.pack()

    p_frame = tk.Frame(lframe, pady=0, padx=100, relief=tk.FLAT, bd=4)
    p_frame.pack()

    checkFont = tkFont.Font(family='Helvetica', size=10)
    labelFont = tkFont.Font(family='System', size=15, weight="bold")
    buttonFont = tkFont.Font(family='System', size=10,weight="bold")

    user_label = tk.Label(u_frame, text="ユーザー名", font=labelFont)
    user_label.grid(row=0, column=0, padx=15, pady=0)
    user_entry = tk.Entry(u_frame)
    user_entry.grid(row=0, column=1, padx=15, pady=5, ipadx=40, ipady=5)

    password_label = tk.Label(p_frame, text="Password   ", font=labelFont)
    password_label.grid(row=0, column=0, padx=15, pady=5)
    password_entry = tk.Entry(p_frame,show= "*")
    password_entry.grid(row=0, column=1, padx=15, pady=5, ipadx=40, ipady=5)

    # login_button = tk.Button(lframe,text="ログイン",font=buttonFont)
    login_button = tk.Button(lframe,text="ログイン",font=buttonFont, command=check_page)
    login_button.pack(ipadx=10, ipady=10, pady=5)
    regiter_button = tk.Button(lframe,text="新規登録",font=buttonFont, command=register_page)
    regiter_button.pack(ipadx=10, ipady=10, pady=5)

def register_page():
    global root,rframe
    global user_entry, password_entry, birthday_entry, address_entry, tel_entry, account_entry
    root.title('コロナ検査SE 新規登録')
    root.geometry('500x325+200+100')

    lframe.destroy()

    rframe = tk.Frame(root)
    rframe.pack(fill=tk.BOTH)

    u_frame = tk.Frame(rframe, pady=0, padx=100, relief=tk.FLAT, bd=4)
    u_frame.pack()

    p_frame = tk.Frame(rframe, pady=0, padx=100, relief=tk.FLAT, bd=4)
    p_frame.pack()

    checkFont = tkFont.Font(family='Helvetica', size=10)
    labelFont = tkFont.Font(family='System', size=15, weight="bold")
    buttonFont = tkFont.Font(family='System', size=10,weight="bold")

    user_label = tk.Label(u_frame, text="ユーザー名", font=labelFont)
    user_label.grid(row=0, column=0, padx=15, pady=0)
    user_entry = tk.Entry(u_frame)
    user_entry.grid(row=0, column=1, padx=15, pady=5, ipadx=40, ipady=5)

    password_label = tk.Label(p_frame, text="Password   ", font=labelFont)
    password_label.grid(row=1, column=0, padx=15, pady=0)
    password_entry = tk.Entry(p_frame,show= "*")
    password_entry.grid(row=1, column=1, padx=15, pady=5, ipadx=40, ipady=5)

    birthday_label = tk.Label(u_frame, text="生年月日", font=labelFont)
    birthday_label.grid(row=2, column=0, padx=15, pady=0)
    birthday_entry = tk.Entry(u_frame)
    birthday_entry.grid(row=2, column=1, padx=15, pady=5, ipadx=40, ipady=5)

    address_label = tk.Label(u_frame, text="住所", font=labelFont)
    address_label.grid(row=3, column=0, padx=15, pady=0)
    address_entry = tk.Entry(u_frame)
    address_entry.grid(row=3, column=1, padx=15, pady=5, ipadx=40, ipady=5)

    tel_label = tk.Label(u_frame, text="電話番号", font=labelFont)
    tel_label.grid(row=4, column=0, padx=15, pady=0)
    tel_entry = tk.Entry(u_frame)
    tel_entry.grid(row=4, column=1, padx=15, pady=5, ipadx=40, ipady=5)

    account_label = tk.Label(u_frame, text="アカウント", font=labelFont)
    account_label.grid(row=5, column=0, padx=15, pady=0)
    account_entry = tk.Entry(u_frame)
    account_entry.grid(row=5, column=1, padx=15, pady=5, ipadx=40, ipady=5)
    regiter_button = tk.Button(
        rframe,text="新規登録", font=buttonFont,
        command=register_process
    )
    regiter_button.pack(ipadx=10, ipady=10, pady=5)

user_entry, password_entry, birthday_entry, address_entry, tel_entry, account_entry = None, None, None, None, None, None
def register_process():
    global user_entry, password_entry, birthday_entry, address_entry, tel_entry, account_entry
    # Excel読み込み
    df = pd.read_excel(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'acount_data.xlsx'), index_col=None)
    # print("パスワード：", df["Password"])
    # 末尾に一行追加
    # df = df.append({"ユーザー名": "user", "生年月日":"2000/1/1", "住所":"xxx-xx-xx", "電話番号":"xxx-xx-xxxx", "アカウント":"bbbb", "Password":"password2"}, ignore_index=True)
    list1 = []
    list1 = list1.append([user_entry.get(), birthday_entry.get(), address_entry.get(), tel_entry.get(), account_entry.get(), password_entry.get()], ignore_index=True)
    df = pd.concat(list1)
    # Excelに書き込み
    df.to_excel(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'acount_data.xlsx'),index=False)
    login_page()


if __name__ == "__main__":
    root = tk.Tk()
    rframe = tk.Frame(root)
    rframe.pack(fill=tk.BOTH)
    login_page()
    root.mainloop()

# check_page()