import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from calculator_ui import Ui_Calculator


class CalculatorApp(QMainWindow, Ui_Calculator):
    def __init__(self, *args, **kwargs):
        super(QMainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.equation_line = "0"
        self.answer.setText(self.equation_line)
        self.equation.setText(self.equation_line)

        self.plus.clicked.connect(self.add_plus)
        self.minus.clicked.connect(self.add_minus)
        self.equal.clicked.connect(self.add_equal)
        self.divide.clicked.connect(self.add_division)
        self.multiply.clicked.connect(self.add_multiplication)

        self.number0.clicked.connect(self.add_number_0)
        self.number1.clicked.connect(self.add_number_1)
        self.number2.clicked.connect(self.add_number_2)
        self.number3.clicked.connect(self.add_number_3)
        self.number4.clicked.connect(self.add_number_4)
        self.number5.clicked.connect(self.add_number_5)
        self.number6.clicked.connect(self.add_number_6)
        self.number7.clicked.connect(self.add_number_7)
        self.number8.clicked.connect(self.add_number_8)
        self.number9.clicked.connect(self.add_number_9)
        self.del_last.clicked.connect(self.delete_last)
        self.clear.clicked.connect(self.clear_everything)
        self.numberdot.clicked.connect(self.add_number_dot)
        self.percent.clicked.connect(self.add_percent)

    def clear_everything(self):
        self.equation.setText("0")
        self.answer.setText("0")

    def delete_last(self):
        self.equation_line = self.equation_line[:-1]

        if self.equation_line == "":
            self.equation_line = "0"

        self.equation.setText(self.equation_line)
        self.solve_expression()

    def add_plus(self):
        if self.equation_line != "0":
            if not (self.equation_line[-1] in ["+", "-", "x", "/"]):
                self.equation_line += "+"
        self.equation.setText(self.equation_line)

    def add_minus(self):
        if self.equation_line == "0":
            self.equation_line = "-"
        elif not (self.equation_line[-1] in ["+", "-", "x", "/"]):
            self.equation_line += "-"
        self.equation.setText(self.equation_line)

    def add_multiplication(self):
        if self.equation_line != "0":
            if not (self.equation_line[-1] in ["+", "-", "x", "/"]):
                self.equation_line += "x"
        self.equation.setText(self.equation_line)

    def add_division(self):
        if self.equation_line != "0":
            if not (self.equation_line[-1] in ["+", "-", "x", "/"]):
                self.equation_line += "/"
        self.equation.setText(self.equation_line)

    def add_equal(self):
        self.equation_line = self.solve()
        self.equation.setText(self.equation_line)
        self.answer.setText(self.equation_line)

    def solve(self):
        try:
            equation = self.equation_line[:-1] if self.equation_line[-1] in ["+", "-", "x", "/"] else self.equation_line
            format_equation = equation.replace("x", "*").replace("%", "*0.01")
            return str(eval(format_equation))
        except ZeroDivisionError:
            return "Division By Zero"
        except Exception as e:
            return "Bad Expression"

    def solve_expression(self):
        self.equation.setText(self.equation_line)
        solution = self.solve()
        self.answer.setText(solution)

    def add_number_0(self):
        if self.equation_line != "0":
            self.equation_line += "0"
        self.solve_expression()

    def add_number_1(self):
        if self.equation_line == "0":
            self.equation_line = "1"
        else:
            self.equation_line += "1"
        self.solve_expression()

    def add_number_2(self):
        if self.equation_line == "0":
            self.equation_line = "2"
        else:
            self.equation_line += "2"
        self.solve_expression()

    def add_number_3(self):
        if self.equation_line == "0":
            self.equation_line = "3"
        else:
            self.equation_line += "3"
        self.solve_expression()

    def add_number_4(self):
        if self.equation_line == "0":
            self.equation_line = "4"
        else:
            self.equation_line += "4"
        self.solve_expression()

    def add_number_5(self):
        if self.equation_line == "0":
            self.equation_line = "5"
        else:
            self.equation_line += "5"
        self.solve_expression()

    def add_number_6(self):
        if self.equation_line == "0":
            self.equation_line = "6"
        else:
            self.equation_line += "6"
        self.solve_expression()

    def add_number_7(self):
        if self.equation_line == "0":
            self.equation_line = "7"
        else:
            self.equation_line += "7"
        self.solve_expression()

    def add_number_8(self):
        if self.equation_line == "0":
            self.equation_line = "8"
        else:
            self.equation_line += "8"
        self.solve_expression()

    def add_number_9(self):
        if self.equation_line == "0":
            self.equation_line = "9"
        else:
            self.equation_line += "9"
        self.solve_expression()

    def add_number_dot(self):
        add = False
        dot_present = self.equation_line.split(".")

        if len(dot_present) == 1:
            self.equation_line += "."

        for symbol in ["+", "-", "x", "/"]:
            if symbol in dot_present[-1]:
                add = True
        if add:
            if self.equation_line[-1] in ["+", "-", "x", "/", "%"]:
                self.equation_line += "0."
            elif self.equation_line[-1] != ".":
                self.equation_line += "."
        self.equation.setText(self.equation_line)

    def add_percent(self):
        if self.equation_line != "0":
            if not (self.equation_line[-1] in ["+", "-", "x", "/"]):
                self.equation_line += "%"
        self.solve_expression()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec())
