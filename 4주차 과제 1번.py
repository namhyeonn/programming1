import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

animal_images = {
    "강아지": "C:/Users/남현/Desktop/school/1학년 2학기/컴퓨터 사고와 프로그래밍/jpeg파일/dog.jpg",
    "고양이": "cat.jpg",
  
}

def vote():
    selected_animal = var.get()
    if selected_animal:
        messagebox.showinfo("투표 결과", f"당신이 선택한 동물은 {selected_animal}입니다!")
        image_path = animal_images[selected_animal]
        img = Image.open(image_path)
        img = img.resize((200, 200), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        img_label.configure(image=img)
        img_label.image = img
    else:
        messagebox.showerror("오류", "동물을 선택해주세요!")

root = tk.Tk()
root.title("동물 투표 프로그램")

label = tk.Label(root, text="좋아하는 동물을 선택하세요:")
label.pack()

var = tk.StringVar()
for animal in animal_images.keys():
    radio_btn = tk.Radiobutton(root, text=animal, variable=var, value=animal)
    radio_btn.pack()

vote_btn = tk.Button(root, text="투표", command=vote)
vote_btn.pack()

img_label = tk.Label(root)
img_label.pack()
root.mainloop()