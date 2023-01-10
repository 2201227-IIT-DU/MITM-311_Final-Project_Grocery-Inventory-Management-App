from kivy.lang import Builder

from kivymd.app import MDApp

from kivymd.uix.boxlayout import MDBoxLayout

from kivymd.uix.carousel import MDCarousel

from kivy.uix.image import Image




class MyMainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Red"
        return Builder.load_file('MyMainApp.kv')



from kivy.core.window import Window
Window.size = (430, 930)



MyMainApp().run()