from kivymd.app import MDApp
from kivy.lang import Builder

KV = """
MDScreen:
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(10), dp(40)
        MDCard:
            size_hint: .9, None
            height: self.minimum_height
            radius: [dp(10)]
            orientation: "vertical"
            pos_hint: {"center_x": .5}
            padding: dp(10), dp(10)
            MDBoxLayout:
                size_hint_y: None
                height: dp(160)
                orientation: "vertical"
                padding: dp(25), dp(20)
                canvas.before:
                    Color:
                        rgb: 1,1,1
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [dp(10)]
                        source: "assets/image.png"
                MDLabel:
                    text: "Get started"
                    font_style: "H6"
                    adaptive_height: True
                    bold: True
                MDLabel:
                    text: "Let us create your account"
                    font_style: "Body1"
                    adaptive_height: True
                BoxLayout:
            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                padding: dp(10), dp(20)
                spacing: dp(10)
                MDBoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    MDTextField:
                        hint_text: "Full name"
                    MDTextField:
                        hint_text: "Email"
                    MDTextField:
                        hint_text: "Password"
                MDRaisedButton:
                    markup: True
                    size_hint_x: 1
                    md_bg_color: 0.47, 0.479, 0.67, 1
                    text: "[b]Get started[/b]"
                MDBoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    spacing: dp(3)
                    MDLabel:
                        text: "By signing up you are agreeing to our"
                        adaptive_height: True
                        font_size: sp(10)
                        color: .2,.2,.2
                        halign: "center"
                        font_name: "assets/NexaDemo-Light.ttf"
                    MDLabel:
                        text: "Terms and Conditions"
                        adaptive_height: True
                        font_size: sp(10)
                        color: 0,.2,1
                        halign: "center"
                        font_name: "assets/NexaDemo-Light.ttf"

"""


class MainScreenApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


if __name__ == "__main__":
    MainScreenApp().run()
