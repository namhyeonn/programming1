import tkinter as tk
import sqlite3

db_name = "md_학번.db"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS 사용자 (
                  id INTEGER PRIMARY KEY,
                  사용자ID TEXT,
                  사용자이름 TEXT,
                  이메일 TEXT,
                  출생년도 TEXT)''')
conn.commit()

root = tk.Tk()
root.title("데이터 입력 및 조회")

label1 = tk.Label(root, text="사용자 ID:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="사용자 이름:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

label3 = tk.Label(root, text="이메일:")
label3.pack()
entry3 = tk.Entry(root)
entry3.pack()

label4 = tk.Label(root, text="출생년도:")
label4.pack()
entry4 = tk.Entry(root)
entry4.pack()

def insert_data():
    user_id = entry1.get()
    user_name = entry2.get()
    email = entry3.get()
    birth_year = entry4.get()
    
    cursor.execute("INSERT INTO 사용자 (사용자ID, 사용자이름, 이메일, 출생년도) VALUES (?, ?, ?, ?)",
                   (user_id, user_name, email, birth_year))
    conn.commit()
    
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)

def search_data():
    user_id = entry1.get()
    cursor.execute("SELECT * FROM 사용자 WHERE 사용자ID=?", (user_id,))
    result = cursor.fetchall()
    
    if not result:
        result_label.config(text="데이터가 없습니다.")
    else:
        result_label.config(text="검색 결과: " + str(result))

insert_button = tk.Button(root, text="데이터 입력", command=insert_data)
insert_button.pack()

search_button = tk.Button(root, text="데이터 조회", command=search_data)
search_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()