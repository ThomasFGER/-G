from kivy.config import Config
Config.set("graphics","resizable", '0')

from decimal import *

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window


Window.size = (275, 290)


class BoxApp(App):
    result = Label(text="0")

    def build(self):

        label_print = BoxLayout(orientation="vertical")

        label_print.add_widget(BoxApp.result)

        button_kal = GridLayout(rows=5, cols=4)
        button_kal.add_widget(Button(text="C", on_press=self.clear))
        button_kal.add_widget(Button(text="C1", on_press=self.clear_one_num))
        button_kal.add_widget(Button(text="%", on_press=self.percent))
        button_kal.add_widget(Button(text="/", on_press=self.operator_add))

        n = 9
        for i in range(3):
            n -= 3
            for _ in range(3):
                n += 1
                button_kal.add_widget(Button(text=str(n), on_press=self.numbers_add))

            button_kal.add_widget(Button(text=("*", "-", "+")[i], on_press=self.operator_add))
            n -= 3

        button_kal.add_widget(Button())
        button_kal.add_widget(Button(text="0", on_press=self.numbers_add))
        button_kal.add_widget(Button(text=".", on_press=self.operator_add))
        button_kal.add_widget(Button(text="=", on_press=self.suma))


        label_print.add_widget(button_kal)

        return label_print

    def numbers_add(self, instance):
        if self.result.text[0] == "0" and len(self.result.text) == 1:
            self.result.text = instance.text
        else:
            self.result.text += instance.text


    def clear(self, instance):
        self.result.text = "0"

    def clear_one_num(self, instance):
        if len(self.result.text) > 1:
            self.result.text = self.result.text[:-1]
        else:
            self.result.text = "0"


    def operator_add(self, instance):
        if not self.result.text[-1] in ["*", ".", "/", "+", "-"]:
            self.result.text += instance.text


    def percent(self, instance):
        result = self.result.text
        if all(map(lambda x: not x in result, ["*", "/", "+", "-"])):
            self.result.text = str(Decimal(result) * Decimal("0.01"))
        elif not result[-1] in ["*", ".", "/", "+", "-"]:
            result = list(result)[::-1]
            for i in range(len(result)):
                if result[i] in ["*", "/", "+", "-"]:
                    result[i] = "#"
                    break

            result = "".join(result[::-1]).split("#")
            percent_num = str(eval(result[0]) * Decimal("0.01") * Decimal(result[1]))
            result = self.result.text[::-1].replace(result[1][::-1], percent_num[::-1], 1)
            self.result.text = result[::-1].rstrip(".0")

    def suma(self, instance):
        if not self.result.text[-1] in ["*", ".", "/", "+", "-"]:
            try:
                self.result.text = str(eval(self.result.text))
            except ZeroDivisionError:
                self.result.text = "0"














if __name__ == '__main__':
    BoxApp().run()
