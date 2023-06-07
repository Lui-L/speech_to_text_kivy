from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFloatingActionButton
from android.permissions import Permission, request_permissions
from android.storage import app_storage_path
import speech_recognition as sr


Builder.load_string('''
<AudioTool>:
    md_bg_color: "#196F3D"
    orientation: 'vertical'
    Label:
        size_hint: 1, .3
        id: display_label
        text: 'empty'
    MDFloatingActionButton:
        icon: "translate"
        id: translate_button
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint: 1, .4
        on_release: root.detectAudio()
''')
 
class MyRecorder:
    def __init__(self, filepath):
        pass
 
class TestApp(MDApp):
    def build(self):
        request_permissions([Permission.READ_EXTERNAL_STORAGE,
                             Permission.INTERNET,
                             Permission.RECORD_AUDIO,
                             Permission.WRITE_EXTERNAL_STORAGE],
                            )
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.material_style = "M3"
        return AudioTool()
 
 
class AudioTool(MDBoxLayout):
    def __init__(self, **kwargs):
        super(AudioTool, self).__init__(**kwargs)
        self.label = self.ids['display_label']
        self.translate_button = self.ids['translate_button']
 
    def detectAudio(self):
        r = sr.Recognizer()
        try:
            path_to_audio = f"{app_storage_path()}/app/16-122828-0002.wav"
            print(path_to_audio)
            audio_f = sr.AudioFile(path_to_audio)
        except Exception as e:
            print(e)
        try:
            with audio_f as source:
                audio = r.record(source)
            text = r.recognize_google(audio)
            self.label.text = text
        except Exception as e:
            print(e)
    
 
if __name__ == '__main__':
    TestApp().run()