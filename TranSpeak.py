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
            'tagalog': 'tl',
            'arabic': 'ar',
            'bengali': 'bn',
            'dutch': 'nl',
            'greek': 'el',
            'gujarati': 'gu',
            'hindi': 'hi',
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

def speak_text(text, lang):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.setProperty('voice', f'{lang}mbrola')
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error speaking text: {e}")

class MainContentArea(ft.Container):
    def __init__(self, dark_mode=False) -> None:
        super().__init__(
            width=600,
            expand=True,
            bgcolor="#d5cdc4",
            border_radius=15,
            padding=20,
            margin=ft.margin.symmetric(vertical=10),
            border=ft.border.all(1, "#c2926a"),
        )
        self.dark_mode = dark_mode
        self.chat = ft.ListView(
            expand=True,
            spacing=15,
            auto_scroll=True,
            height=400
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
        super().__init__(spacing=5)
        self.name = name
        self.message = message
        self.lang = lang
        self.spoken_text = spoken_text
        self.text_color = "#ffffff" if dark_mode else "#000000"
        self.text = ft.Text(self.message, color=self.text_color, size=14, selectable=True)
        
        self.controls = [
            ft.Text(self.name, 
                   size=16,
                   opacity=0.8,
                   color=self.text_color,
                   weight=ft.FontWeight.BOLD),
            self.text
        ]

class Prompt(ft.Column):
    def __init__(self, appbar: ft.AppBar, main_area: MainContentArea) -> None:
        super().__init__()
        self.appbar = appbar
        self.main_area = main_area
        
        self.text_field = ft.TextField(
            width=400,
            height=45,
            border_color="#c2926a",
            border_width=2,
            content_padding=10,
            cursor_color="#c2926a",
            hint_text="Enter text to translate...",
            bgcolor="#ffffff",
            focused_border_color="#a06d47",
        )
        
        self.lang_field = ft.TextField(
            width=150,
            height=45,
            border_width=2,
            cursor_height=20,
            content_padding=10,
            hint_text="Enter language...",
            bgcolor="#ffffff",
            border_color="#c2926a",
            focused_border_color="#a06d47",
        )
        
        self.translate_button = ft.ElevatedButton(
            text="Translate",
            bgcolor="#c2926a",
            color="#ffffff",
            on_click=self.run_prompt,
            height=45,
        )

        self.controls = [
            ft.Row(
                controls=[
                    self.lang_field,
                    ft.Container(width=10),
                    self.text_field,
                    ft.Container(width=10),
                    self.translate_button
                ],
                alignment=ft.MainAxisAlignment.CENTER
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
    page.window_height = 700
    page.padding = 20
    page.bgcolor = "#ffffff"
    page.scroll = "auto"
    
    appbar = ft.AppBar(
        title=ft.Text("TRANSPEAK", size=30, weight=ft.FontWeight.BOLD),
        center_title=True,
        bgcolor="#c2926a",
        actions=[
            ft.IconButton(
                ft.icons.WB_SUNNY_OUTLINED, 
                on_click=lambda e: toggle_theme(page, appbar, main_area),
                icon_color="#ffffff"
            ),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Log Out", on_click=lambda e: logout_action()),
                ]
            ),
        ],
    )

    main_area = MainContentArea()
    prompt = Prompt(appbar=appbar, main_area=main_area)

    title_container = ft.Container(
        content=ft.Text(
            "TranSpeak",
            size=40,
            weight=ft.FontWeight.BOLD,
            color="#c2926a",
            text_align=ft.TextAlign.CENTER,
        ),
        margin=ft.margin.only(bottom=10, top=10),
        alignment=ft.alignment.center
    )

    input_container = ft.Container(
        content=prompt,
        margin=ft.margin.only(top=10, bottom=10),
        padding=10,
        bgcolor="#f0f0f0",
        border_radius=10,
        border=ft.border.all(1, "#c2926a")
    )

    footer = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(
                    "Created by:",
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    color="#c2926a"
                ),
                ft.Text(
                    "JANET M. BULAO | CS 3-1",
                    size=14,
                    color="#666666",
                    weight=ft.FontWeight.BOLD
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=5
        ),
        padding=15,
        margin=ft.margin.only(top=10),
        bgcolor="#f5f5f5",
        border_radius=10,
        border=ft.border.all(1, "#c2926a")
    )

    content = ft.Column(
        controls=[
            title_container,
            main_area,
            input_container,
            footer
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10,
        scroll=ft.ScrollMode.AUTO
    )

    page.appbar = appbar
    page.add(content)
    page.update()

def toggle_theme(page, appbar, main_area):
    if page.theme_mode == "light":
        page.theme_mode = "dark"
        page.bgcolor = "#1a1a1a"
        appbar.bgcolor = "#2d2d2d"
        appbar.actions[0].icon = ft.icons.WB_SUNNY_OUTLINED
    else:
        page.theme_mode = "light"
        page.bgcolor = "#ffffff"
        appbar.bgcolor = "#c2926a"
        appbar.actions[0].icon = ft.icons.BRIGHTNESS_2_OUTLINED

    main_area.set_dark_mode(page.theme_mode == "dark")
    page.update()

def logout_action():
    print("Logout action triggered.")

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)