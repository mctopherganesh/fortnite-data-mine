# https://www.youtube.com/watch?v=F7UKmK9eQLY&list=PLdNh1e1kmiPP4YApJm8ENK2yMlwF1_edq
# https://kivy.org/doc/stable/tutorials/crashcourse.html
# https://github.com/kivy/kivy/wiki
# links i was working from


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class DegWidget(BoxLayout):
    pass



class DegApp(App):
    def build(self):
        return DegWidget()


if __name__=="__main__":
    DegApp().run()
