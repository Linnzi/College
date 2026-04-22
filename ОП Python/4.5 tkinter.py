import tkinter as tk
from tkinter import font as tkfont


class SequenceSumApp:
    def __init__(self, root):
        self.root = root
        self.root.title("4.5 — Сумма последовательности")
        self.root.geometry("520x420")
        self.root.resizable(False, False)
        self.root.configure(bg="#0f1117")

        self._build_ui()

    def _build_ui(self):
        # ── Header ──────────────────────────────────────────────
        header = tk.Frame(self.root, bg="#1a1d27", pady=14)
        header.pack(fill="x")

        badge = tk.Label(
            header, text="4.5", bg="#e63946", fg="white",
            font=("Courier New", 13, "bold"), padx=10, pady=4
        )
        badge.pack(side="left", padx=(18, 10))

        title = tk.Label(
            header,
            text="ВВОД И ОБРАБОТКА ПОСЛЕДОВАТЕЛЬНОСТЕЙ",
            bg="#1a1d27", fg="#f1faee",
            font=("Courier New", 11, "bold")
        )
        title.pack(side="left")

        # ── Task label ──────────────────────────────────────────
        task_frame = tk.Frame(self.root, bg="#0f1117", pady=18)
        task_frame.pack(fill="x", padx=24)

        tk.Label(
            task_frame,
            text="Задача 1. Найти сумму элементов последовательности.",
            bg="#0f1117", fg="#a8dadc",
            font=("Courier New", 10), anchor="w", justify="left"
        ).pack(fill="x")

        # ── Input ────────────────────────────────────────────────
        input_frame = tk.Frame(self.root, bg="#0f1117")
        input_frame.pack(fill="x", padx=24)

        tk.Label(
            input_frame,
            text="Введите числа через пробел (для дробных используйте точку):",
            bg="#0f1117", fg="#cdd6f4",
            font=("Courier New", 9), anchor="w", justify="left"
        ).pack(fill="x", pady=(0, 6))

        entry_bg = tk.Frame(input_frame, bg="#e63946", padx=2, pady=2)
        entry_bg.pack(fill="x")

        self.entry = tk.Entry(
            entry_bg,
            font=("Courier New", 13),
            bg="#1e2130", fg="#cdd6f4",
            insertbackground="#e63946",
            relief="flat", bd=0
        )
        self.entry.pack(fill="x", ipady=8, padx=1, pady=1)
        self.entry.bind("<Return>", lambda e: self._calculate())
        self.entry.focus()

        # ── Button ───────────────────────────────────────────────
        btn_frame = tk.Frame(self.root, bg="#0f1117", pady=16)
        btn_frame.pack()

        self.calc_btn = tk.Button(
            btn_frame,
            text="  ВЫЧИСЛИТЬ  ",
            font=("Courier New", 11, "bold"),
            bg="#e63946", fg="white",
            activebackground="#c1121f", activeforeground="white",
            relief="flat", bd=0, padx=20, pady=8,
            cursor="hand2",
            command=self._calculate
        )
        self.calc_btn.pack()

        clear_btn = tk.Button(
            btn_frame,
            text="Очистить",
            font=("Courier New", 9),
            bg="#1a1d27", fg="#6b7280",
            activebackground="#252836", activeforeground="#a8dadc",
            relief="flat", bd=0, padx=12, pady=4,
            cursor="hand2",
            command=self._clear
        )
        clear_btn.pack(pady=(8, 0))

        # ── Result box ───────────────────────────────────────────
        result_outer = tk.Frame(self.root, bg="#0f1117", padx=24)
        result_outer.pack(fill="x")

        self.result_frame = tk.Frame(
            result_outer, bg="#1a1d27",
            padx=16, pady=14,
            highlightbackground="#2a2d3e", highlightthickness=1
        )
        self.result_frame.pack(fill="x")

        self.result_label = tk.Label(
            self.result_frame,
            text="Результат появится здесь...",
            bg="#1a1d27", fg="#4b5263",
            font=("Courier New", 10),
            justify="left", anchor="w"
        )
        self.result_label.pack(fill="x")

    def _calculate(self):
        raw = self.entry.get().strip()

        if not raw:
            self._show_error("Ошибка: Вы ничего не ввели. Попробуйте ещё раз.")
            return

        try:
            numbers = [float(x) for x in raw.split()]
        except ValueError:
            self._show_error(
                "Ошибка: Обнаружен некорректный символ.\n"
                "Вводите только числа через пробел."
            )
            return

        total = sum(numbers)
        count = len(numbers)

        # Format nicely: drop .0 for whole results
        total_str = f"{total:g}" if total == int(total) else f"{total}"

        self._show_success(count, total_str)

    def _show_success(self, count, total_str):
        self.result_frame.configure(
            highlightbackground="#2a9d8f", highlightthickness=1
        )
        self.result_label.configure(
            fg="#a8dadc",
            text=(
                f"  Успешно!\n\n"
                f"   Элементов в последовательности:  {count}\n"
                f"   Сумма последовательности:         {total_str}"
            )
        )

    def _show_error(self, message):
        self.result_frame.configure(
            highlightbackground="#e63946", highlightthickness=1
        )
        self.result_label.configure(
            fg="#e63946",
            text=f"  {message}"
        )

    def _clear(self):
        self.entry.delete(0, "end")
        self.result_frame.configure(
            highlightbackground="#2a2d3e", highlightthickness=1
        )
        self.result_label.configure(
            text="Результат появится здесь...",
            fg="#4b5263"
        )
        self.entry.focus()


if __name__ == "__main__":
    root = tk.Tk()
    app = SequenceSumApp(root)
    root.mainloop()
