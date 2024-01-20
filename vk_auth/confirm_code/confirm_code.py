import tkinter as tk


def show_message():
    def start():
        nonlocal user_input
        user_input = entry.get()  # сохраняем введенный текст в переменную
        root.destroy()  # закрываем окно

    root = tk.Tk()
    root.title("Ввод данных")

    # Размещаем окно по центру экрана
    window_width = 200
    window_height = 100
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    entry = tk.Entry(root)
    entry.pack()

    button = tk.Button(root, text="Показать введенный текст", command=start)
    button.pack()

    user_input = ""  # переменная для сохранения введенного текста

    root.mainloop()
    return user_input

if __name__ == "__main__":
    gg = show_message()
    print(type(gg))