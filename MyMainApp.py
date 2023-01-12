from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.carousel import MDCarousel
from kivy.uix.image import Image
from kivymd.uix.list import MDList, TwoLineAvatarListItem, ImageLeftWidget, TwoLineListItem, IRightBodyTouch
from kivymd.uix.label import MDLabel
from kivy.clock import Clock
from kivymd.uix.imagelist.imagelist import MDSmartTile
from kivymd.uix.button import MDRaisedButton
from kivy.properties import ObjectProperty


class CounterContainer(IRightBodyTouch, MDBoxLayout):
    adaptive_width = True

class MySmartTile(MDSmartTile):
    def __init__(self, **kwargs):
        super().__init__(
            radius = 24,
            box_radius = [0,0,24,24], 
            box_color = (0.5, 0.5, 0.5, 0.7),
            lines = 2,
            size_hint= (None, None),
            size = (300, 300),
            pos_hint = {'center_x': 0.5, 'center_y': 0.5},
            **kwargs
        )
            
    def design(self, id_no=1, desc_line_1 = 'Line-1', desc_line_2 = 'Line-2', price = 500):
        self.source = f'images/{id_no}.png'

        description = TwoLineListItem(
            text = desc_line_1,
            secondary_text = desc_line_2, 
        )

        btn = MDRaisedButton(
            text = str(price),
            pos_hint = {'center_x': 0.17, 'center_y': -0.1},
            rounded_button = True,
            padding = [0,0,0,0],
            line_width = 3,
            line_color = (0.07, 0.07, 0.07, 1),
        )

        description.add_widget(btn)
        self.add_widget(description)

    def include_count(self, pcs=0):
        btn = MDRaisedButton(
            text = f'{pcs} pcs',
            pos_hint = {'right': 1.03, 'top': 3.7},
            padding = [0,0,0,0]
        )

        self.children[0].children[0].add_widget(btn)

    def on_release(self, *args):
        super().on_release(*args)
        MyApp.root.ids.top_app_bar.title = 'Product ID xyz'
        MyApp.root.ids.screen_content_manager.current = 'product details'



class MyShowcaseCarousel(MDCarousel):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_content()

    def auto_rotate(self, interval=5.0):
        print('scrolling...')
        Clock.schedule_interval(self.load_next, interval)

    def load_content(self):
        self.clear_widgets()

        for i in range(5):
            item = MySmartTile()
            item.design(i)
            self.add_widget(item)
        


class MyMainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Red"
        return Builder.load_file('MyMainApp.kv')

    def on_start(self):
        for i in range(20):
            item = TwoLineAvatarListItem(text= "Two-line item with avatar", secondary_text= "Secondary text here")
            img  = ImageLeftWidget(source=f'images/{i%5}.png')

            item.add_widget(img)
            self.root.ids.dashboard_list.add_widget(item)

        for i in range(10):
            item = MySmartTile()
            item.design(i%5, 'lorem ipsum dolor sit amet polka polka dot dot')
            item.include_count(5000)
            self.root.ids.inventory_list.add_widget(item)

    def update_db(self, formInput):
        print(formInput)



from kivy.core.window import Window
Window.size = (430, 930)

MyApp = MyMainApp()
MyApp.run()