from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class AdventureGame(App):

    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        self.message = Label(
            text="Welcome to the Castle!",
            font_size=25
        )

        red = Button(text="Red Door", font_size=22)
        blue = Button(text="Blue Door", font_size=22)

        red.bind(on_press=self.red_door)
        blue.bind(on_press=self.blue_door)

        layout.add_widget(self.message)
        layout.add_widget(red)
        layout.add_widget(blue)

        return layout

    def red_door(self, instance):
        self.message.text = "You found a treasure!"

    def blue_door(self, instance):
        self.message.text = "A monster appeared!"


AdventureGame().run()
