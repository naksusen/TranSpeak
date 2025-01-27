import flet as ft
from deep_translator import GoogleTranslator
import pyttsx3

def translate_text(text, target_language):
    try:
        language_map = {
            'english': 'en',
            'spanish': 'es',
            'french': 'fr',
            'german': 'de',
            'italian': 'it',
            'portuguese': 'pt',
            'russian': 'ru',
            'japanese': 'ja',
            'korean': 'ko',
            'chinese': 'zh',
            'filipino': 'tl',
            'hindi': 'hi',
            'tagalog': 'tl',
            'arabic': 'ar',
            'bengali': 'bn',
            'dutch': 'nl',
            'greek': 'el',
            'gujarati': 'gu',
            'indonesian': 'id',
            'thai': 'th',
            'turkish': 'tr',
            'ukrainian': 'uk',
            'vietnamese': 'vi',
            'tamil': 'ta',
            'telugu': 'te',
            'urdu': 'ur',
            'persian': 'fa',
            'polish': 'pl',
            'romanian': 'ro',
            'swedish': 'sv',
            'malay': 'ms',
            'kannada': 'kn',
            'marathi': 'mr',
            'afrikaans': 'af',
            'albanian': 'sq',
            'amharic': 'am',
            'armenian': 'hy',
            'azerbaijani': 'az',
            'basque': 'eu',
            'belarusian': 'be',
            'cebuano': 'ceb',
            'corsican': 'co',
            'croatian': 'hr',
            'czech': 'cs',
            'danish': 'da',
            'esperanto': 'eo',
            'estonian': 'et',
            'finnish': 'fi',
            'frisian': 'fy',
            'galician': 'gl',
            'georgian': 'ka',
            'haitian creole': 'ht',
            'hawaiian': 'haw',
            'hebrew': 'iw',
            'hmong': 'hmn',
            'hungarian': 'hu',
            'icelandic': 'is',
            'igbo': 'ig',
            'irish': 'ga',
            'javanese': 'jw',
            'kazakh': 'kk',
            'khmer': 'km',
            'kurdish': 'ku',
            'kyrgyz': 'ky',
            'lao': 'lo',
            'latin': 'la',
            'latvian': 'lv',
            'lithuanian': 'lt',
            'luxembourgish': 'lb',
            'macedonian': 'mk',
            'malagasy': 'mg',
            'maltese': 'mt',
            'maori': 'mi',
            'mongolian': 'mn',
            'myanmar': 'my',
            'nepali': 'ne',
            'norwegian': 'no',
            'nyanja': 'ny',
            'pashto': 'ps',
            'punjabi': 'pa',
            'samoan': 'sm',
            'scots gaelic': 'gd',
            'serbian': 'sr',
            'sesotho': 'st',
            'shona': 'sn',
            'sindhi': 'sd',
            'sinhala': 'si',
            'slovak': 'sk',
            'slovenian': 'sl',
            'somali': 'so',
            'sundanese': 'su',
            'swahili': 'sw',
            'tajik': 'tg',
            'welsh': 'cy',
            'xhosa': 'xh',
            'yiddish': 'yi',
            'yoruba': 'yo',
            'zulu': 'zu'
        }
        
        target_code = language_map.get(target_language.lower(), target_language.lower())
        translator = GoogleTranslator(source='auto', target=target_code)
        return translator.translate(text)
    except Exception as e:
        print(f"Translation error: {e}")
        return f"Translation error: Please use a valid language code or name. Error: {str(e)}"

def get_voice_for_language(engine, lang_code):
    voices = engine.getProperty('voices')
    
    language_voice_map = {
        'ja': ['ja', 'jp', 'japanese'],
        'ko': ['ko', 'kr', 'korean'],
        'zh': ['zh', 'cn', 'chinese'],
        'es': ['es', 'spanish'],
        'fr': ['fr', 'french'],
        'de': ['de', 'german'],
        'it': ['it', 'italian'],
        'pt': ['pt', 'portuguese'],
        'ru': ['ru', 'russian']
    }
    
    search_terms = language_voice_map.get(lang_code.lower(), [lang_code.lower()])
    
    for voice in voices:
        voice_name = voice.name.lower()
        voice_id = voice.id.lower()
        for term in search_terms:
            if term in voice_name or term in voice_id:
                return voice.id
    
    return voices[0].id if voices else None

def speak_text(text, lang):
    try:
        engine = pyttsx3.init()
        
        engine.setProperty('rate', 150)
        
        voice_id = get_voice_for_language(engine, lang)
        if voice_id:
            engine.setProperty('voice', voice_id)
        
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error speaking text: {e}")

class WelcomePage(ft.Container):
    def __init__(self, switch_to_main):
        super().__init__(expand=True)
        self.switch_to_main = switch_to_main

        main_content = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        "T̲̲r̲a̲̲n̲̲S̲̲p̲̲e̲a̲̲k̲",
                        size=30,
                        weight=ft.FontWeight.BOLD,
                        color="#c2926a",
                        text_align=ft.TextAlign.CENTER,
                        font_family="Roboto",
                    ),
                    ft.Container(height=20),
                    ft.ElevatedButton(
                        text="Start",
                        bgcolor="#c2926a",
                        color="#ffffff",
                        on_click=self.handle_start,
                        width=200,
                        height=50,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True
            ),
            alignment=ft.alignment.center,
            expand=True
        )

        footer = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        "© 2025 TranSpeak. All Rights Reserved.",
                        size=12,
                        weight=ft.FontWeight.BOLD,
                        color="#666666",
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Text(
                        "Developed by Janet Bulao",
                        size=12,
                        color="#666666",
                        text_align=ft.TextAlign.CENTER,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=2,
            ),
            padding=ft.padding.symmetric(vertical=20),
        )

        self.content = ft.Column(
            controls=[
                main_content,
                footer,
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        )

    def handle_start(self, e):
        self.switch_to_main()

class MainContentArea(ft.Container):
    def __init__(self, dark_mode=False) -> None:
        super().__init__(
            expand=True,
            bgcolor="#d5cdc4",
            border_radius=15,
            padding=10,
            margin=ft.margin.symmetric(vertical=5, horizontal=10),
            border=ft.border.all(1, "#c2926a"),
        )
        self.dark_mode = dark_mode
        self.chat = ft.ListView(
            expand=True,
            spacing=10,
            auto_scroll=True,
            height=200
        )
        self.content = self.chat

    def set_dark_mode(self, dark_mode):
        self.dark_mode = dark_mode
        self.bgcolor = "#2d2d2d" if dark_mode else "#d5cdc4"
        self.update_text_color()

    def update_text_color(self):
        text_color = "#ffffff" if self.dark_mode else "#000000"
        for control in self.chat.controls:
            if isinstance(control, CreateMessage):
                control.text.color = text_color
        self.update()

class CreateMessage(ft.Column):
    def __init__(self, name: str, message: str, lang: str, spoken_text: str, dark_mode=False) -> None:
        super().__init__(spacing=3)
        self.name = name
        self.message = message
        self.lang = lang
        self.spoken_text = spoken_text
        self.text_color = "#ffffff" if dark_mode else "#000000"
        
        label_color = (
           "#c2926a" if name == "You:" else "#8B4513"  
        )

        self.text = ft.Text(
            self.message,
            color=self.text_color,
            size=14,
            selectable=True,
            width=None,
            max_lines=None,
        )

        self.controls = [
            ft.Text(
                self.name,
                size=16,
                opacity=1.0,
                color=label_color,
                weight=ft.FontWeight.BOLD,
            ),
            self.text,
        ]

class Prompt(ft.Column):
    def __init__(self, appbar: ft.AppBar, main_area: MainContentArea) -> None:
        super().__init__()
        self.appbar = appbar
        self.main_area = main_area
        
        self.lang_field = ft.TextField(
            expand=True,
            height=45,
            border_width=2,
            cursor_height=20,
            content_padding=10,
            hint_text="Enter language...",
            bgcolor="#ffffff",
            border_color="#c2926a",
            focused_border_color="#a06d47",
            text_style=ft.TextStyle(color="#000000"),
        )
        
        self.text_field = ft.TextField(
            expand=True,
            height=45,
            border_color="#c2926a",
            border_width=2,
            content_padding=10,
            cursor_color="#c2926a",
            hint_text="Enter text to translate...",
            bgcolor="#ffffff",
            focused_border_color="#a06d47",
            text_style=ft.TextStyle(color="#000000"),
            multiline=True,
        )
        
        self.translate_button = ft.ElevatedButton(
            text="Translate",
            bgcolor="#c2926a",
            color="#ffffff",
            on_click=self.run_prompt,
            width=200,
            height=35,
        )

        self.controls = [
            ft.ResponsiveRow(
                controls=[ 
                    ft.Column(
                        controls=[
                            self.lang_field,
                            ft.Container(height=10),  
                            self.text_field,
                            ft.Container(height=15),  
                            self.translate_button 
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=0,
                        col={"sm": 12, "md": 8, "lg": 6},
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        ]

    def animate_text_output(self, name: str, prompt: str):
        lang = self.lang_field.value.lower() if self.lang_field.value else 'en'
        translated_text = translate_text(prompt, lang)
        
        user_msg = CreateMessage(
            name="You:", 
            message=prompt, 
            lang=lang, 
            spoken_text="", 
            dark_mode=self.main_area.dark_mode
        )
        self.main_area.chat.controls.append(user_msg)

        translated_msg = CreateMessage(
            name="Translated Text:", 
            message=translated_text, 
            lang=lang, 
            spoken_text="", 
            dark_mode=self.main_area.dark_mode
        )
        self.main_area.chat.controls.append(translated_msg)
        self.main_area.chat.update()
        
        speak_text(translated_text, lang)

    def run_prompt(self, e):
        if self.text_field.value:
            self.animate_text_output(name="You:", prompt=self.text_field.value)
            self.text_field.value = ""
            self.lang_field.value = ""
            self.text_field.update()
            self.lang_field.update()

def main(page: ft.Page) -> None:
    page.window_width = 800
    page.window_height = 600
    page.padding = 10
    page.bgcolor = "#ffffff"
    page.scroll = "auto"
    
    page.window_resizable = True
    page.window_maximizable = True
    page.fonts = {
        "Roboto": "https://github.com/google/fonts/raw/main/apache/roboto/static/Roboto-Regular.ttf"
    }
    
    def switch_to_welcome():
        page.clean()
        page.appbar = None 
        welcome = WelcomePage(switch_to_main)
        page.add(welcome)
        page.update()
    
    def switch_to_main():
        page.clean()
        
        appbar = ft.AppBar(
            center_title=True,
            bgcolor="#c2926a",
            toolbar_height=50,
            leading=ft.IconButton(
                ft.icons.WB_SUNNY_OUTLINED,
                on_click=lambda e: toggle_theme(page, appbar, main_area),
                icon_color="#ffffff"
            ),
            actions=[
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(text="Log Out", on_click=lambda e: switch_to_welcome()),
                    ]
                ),
            ],
        )

        main_area = MainContentArea()

        title_container = ft.Container(
            content=ft.Text(
                "T̲̲r̲a̲̲n̲̲S̲̲p̲e̲a̲̲k̲",
                size=30,
                weight=ft.FontWeight.BOLD,
                color="#c2926a",
                text_align=ft.TextAlign.CENTER,
                font_family="Roboto"
            ),
            margin=ft.margin.only(bottom=5, top=5),
            alignment=ft.alignment.center
        )

        prompt = Prompt(appbar=appbar, main_area=main_area)

        content = ft.ResponsiveRow(
            controls=[
                ft.Column(
                    controls=[
                        title_container,
                        main_area,
                        prompt,
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=5,
                    scroll=ft.ScrollMode.AUTO,
                    col={"sm": 12, "md": 12, "lg": 12}
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        page.appbar = appbar
        page.add(content)
        page.update()
    
    switch_to_welcome()

def toggle_theme(page, appbar, main_area):
    if page.theme_mode == "light":
        page.theme_mode = "dark"
        page.bgcolor = "#1a1a1a"
        appbar.bgcolor = "#2d2d2d"
        appbar.leading.icon = ft.icons.WB_SUNNY_OUTLINED
    else:
        page.theme_mode = "light"
        page.bgcolor = "#ffffff"
        appbar.bgcolor = "#c2926a"
        appbar.leading.icon = ft.icons.BRIGHTNESS_2_OUTLINED

    main_area.set_dark_mode(page.theme_mode == "dark")
    page.update()

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)