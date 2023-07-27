import tkinter as tk
from tkinter import messagebox

class PayScaleCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PayScale Calculator")
        self.geometry("400x200")

        self.pay_per_hour = tk.DoubleVar()
        self.monthly_payment = tk.DoubleVar()
        self.yearly_payment = tk.DoubleVar()

        self.create_widgets()

    def create_widgets(self):
        # Labels
        tk.Label(self, text="Pay per hour:").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self, text="Monthly payment:").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(self, text="Yearly payment:").grid(row=2, column=0, padx=10, pady=5)

        # Entry fields
        tk.Entry(self, textvariable=self.pay_per_hour).grid(row=0, column=1, padx=10, pady=5)
        tk.Entry(self, textvariable=self.monthly_payment).grid(row=1, column=1, padx=10, pady=5)
        tk.Entry(self, textvariable=self.yearly_payment).grid(row=2, column=1, padx=10, pady=5)

        # Calculate and Reset buttons
        tk.Button(self, text="Calculate", command=self.calculate_payment).grid(row=3, column=0, padx=10, pady=10)
        tk.Button(self, text="Reset", command=self.reset_values).grid(row=3, column=1, padx=10, pady=10)

    def calculate_payment(self):
        # Calculate monthly and yearly payments based on available inputs
        pay_per_hour = self.pay_per_hour.get()
        monthly_payment = self.monthly_payment.get()
        yearly_payment = self.yearly_payment.get()

        if not pay_per_hour:
            if monthly_payment and not yearly_payment:
                pay_per_hour = monthly_payment / 160
                yearly_payment = monthly_payment * 12
            elif yearly_payment and not monthly_payment:
                pay_per_hour = yearly_payment / 1920
                monthly_payment = yearly_payment / 12
        elif not monthly_payment:
            monthly_payment = pay_per_hour * 160
            yearly_payment = monthly_payment * 12
        elif not yearly_payment:
            yearly_payment = monthly_payment * 12
            pay_per_hour = yearly_payment / 1920

        self.pay_per_hour.set(pay_per_hour)
        self.monthly_payment.set(monthly_payment)
        self.yearly_payment.set(yearly_payment)

    def reset_values(self):
        # Reset all input and output fields
        self.pay_per_hour.set(0)
        self.monthly_payment.set(0)
        self.yearly_payment.set(0)


if __name__ == "__main__":
    app = PayScaleCalculator()
    app.mainloop()
