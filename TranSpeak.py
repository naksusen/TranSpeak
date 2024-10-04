import flet as ft
from googletrans import Translator
import pyttsx3

# para ma-translate yung text sa target language using google translate API
def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

# speak the given text sa specified language gamit ang pyttsx3 text-to-speech engine
def speak_text(text, lang):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  
        engine.setProperty('voice', f'{lang}mbrola')  
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error speaking text: {e}")

# class ng main content area with a chat ListView
class MainContentArea(ft.Container):
    def __init__(self, dark_mode=False) -> None:
        self.dark_mode = dark_mode
        super().__init__(
            width=320,
            height=400,
            bgcolor="#d5cdc4",
            border_radius=10,
            padding=10,
        )
        self.chat = ft.ListView(
            expand=True,
            height=130,
            spacing=10,
            auto_scroll=True
        )
        self.content = self.chat

    # method para mag-set ng dark mode for the main content area
    def set_dark_mode(self, dark_mode):
        self.dark_mode = dark_mode
        self.update_text_color()

    # method din ito para i-update ang text color based sa dark mode
    def update_text_color(self):
        text_color = "#000000" if self.dark_mode else "#ffffff"
        for control in self.chat.controls:
            if isinstance(control, CreateMessage):
                control.text.color = text_color
        self.update()

# class ng message sa chat with specified attributes
class CreateMessage(ft.Column):
    def __init__(self, name: str, message: str, lang: str, spoken_text: str, dark_mode=False) -> None:
        self.name: str = name
        self.message: str = message
        self.lang: str = lang
        self.spoken_text: str = spoken_text
        self.text_color = "#000000"
        self.text = ft.Text(self.message, color=self.text_color)
        super().__init__(spacing=2)
        self.controls = [ft.Text(self.name, opacity=0.6, color=self.text_color), self.text]

    # method para i-set ang dark mode for the message
    def set_dark_mode(self, dark_mode):
        pass

# class sa prompt input field with language and text output animation methods
class Prompt(ft.TextField):
    def __init__(self, appbar: ft.AppBar, main_area: MainContentArea) -> None:
        super().__init__(width=320, height=30, border_color="#c2926a", content_padding=5, cursor_color="#c2926a", on_submit=self.run_prompt)
        self.appbar = appbar
        self.main_area = main_area
        self.lang_prompt = ft.TextField(width=100, height=40, cursor_height=20, content_padding=5, on_submit=self.update_language)

    # method para i-update yung selected language
    def update_language(self, event):
        lang = self.lang_prompt.value.lower()
        self.lang_prompt.value = lang

    # method para sa animate text output sa chat based ng user input
    def animate_text_output(self, name: str, prompt: str):
        lang = self.lang_prompt.value
        translated_text = translate_text(prompt, lang)
        spoken_text = speak_text(translated_text, lang)
        user_msg = CreateMessage(name="You:", message=prompt, lang=lang, spoken_text=spoken_text, dark_mode=self.main_area.dark_mode)
        self.main_area.chat.controls.append(user_msg)

        translated_msg = CreateMessage(name="Translated Text:", message=translated_text, lang=lang, spoken_text=spoken_text, dark_mode=self.main_area.dark_mode)
        self.main_area.chat.controls.append(translated_msg)

        self.main_area.chat.update()

    # method para i-handle yung prompt input at mag-initiate ng text animation
    def run_prompt(self, event):
        text = event.control.value
        self.animate_text_output(name="You:", prompt=text)
        self.value = ""
        self.lang_prompt.value = ""
        self.update()

# ito yung main function para i-set up yung application UI at mag-handle ng events
def main(page: ft.Page) -> None:
    appbar = ft.AppBar(
        title=ft.Text(str("ᴛʀᴀɴꜱᴘᴇᴀᴋ"), size=23), # nag-install din pala ako ng pywhatkit module here, para sa text manipulation, kaya pwede nang mag-input ng generated fonts para maangas HAHAHA
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED, on_click=lambda e: toggle_theme(page, appbar, main_area)),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Log Out", on_click=lambda e: logout_action()),
                ]
            ),
        ],
    )

    main_area = MainContentArea()
    prompt = Prompt(appbar=appbar, main_area=main_area)

    page.appbar = appbar

    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.theme_mode = "light"

    created_by_text = ft.Text("𝗖𝗿𝗲𝗮𝘁𝗲𝗱 𝗯𝘆: ᴊᴀɴᴇᴛ ᴍ. ʙᴜʟᴀᴏ | 𝖢𝖲 3-1", size=12, weight="w500")
    footer = ft.Container(
        content=created_by_text,
        bgcolor=ft.colors.SURFACE_VARIANT,
        padding=10,
    )

    page.add(
        ft.Text(str("̲T̲̲r̲a̲̲n̲̲S̲̲p̲̲e̲a̲̲k̲"), size=30, weight="w900"),
        main_area,
        ft.Divider(height=4, color="transparent"),
        prompt.lang_prompt,
        prompt,
        footer,
    )

    update_created_by_text_color(created_by_text, page.theme_mode)

    page.update()

# function para sa switching ng light at dark themes/ mode
def toggle_theme(page, appbar, main_area):
    if page.theme_mode == "light":
        page.theme_mode = "dark"
        appbar.actions[0].icon = ft.icons.WB_SUNNY_OUTLINED
    else:
        page.theme_mode = "light"
        appbar.actions[0].icon = ft.icons.BRIGHTNESS_2_OUTLINED

    main_area.set_dark_mode(page.theme_mode == "dark")

    update_created_by_text_color(page.controls[-1].content, page.theme_mode)

    page.update()

# function para sa logout action
def logout_action():
    print("Logout action triggered.")

# function para i-update ang text color based sa theme mode
def update_created_by_text_color(created_by_text, theme_mode):
    text_color = "#ffffff" if theme_mode == "dark" else "#000000"
    created_by_text.color = text_color

# ito yung entry point para mag-start yung application/ GUI, yun lang HAHAHA maangas na 'to HAHAHA ayoko na, sabog na akoo HAHAHAHAHHAHA
if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
