from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

class VirusScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.label = Label(text="🔴 Đang xóa dữ liệu...\nVui lòng không tắt máy!", font_size=24)
        self.add_widget(self.label)
        
        # Sau 5 giây đổi thông báo
        Clock.schedule_once(self.change_text, 5)
    
    def change_text(self, dt):
        self.label.text = "⚠️ Cảnh báo: Virus đã phát hiện!\nHãy khởi động lại ngay!"

class TrollApp(App):
    def build(self):
        return VirusScreen()

if __name__ == "__main__":
    TrollApp().run()