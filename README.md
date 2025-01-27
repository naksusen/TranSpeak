# <div align="center" style="background: linear-gradient(to right, brown, brown); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 2.5em;">T̲̲r̲a̲̲n̲̲S̲̲p̲e̲a̲̲k̲</div>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A **Mobile-Based Translator** application built with Python, enabling users to translate text into multiple languages and have the translated text spoken aloud using text-to-speech capabilities.
    
## Features

- **Multi-Language Translation:** Translate text into over 100 languages.
- **Text-to-Speech:** Speak translated text with language-specific voices.
- **Responsive Design:** Enjoy light and dark mode themes for the user interface.
- **Real-Time Translation:** Instant translations with smooth speech output.

## Demo

### Welcome Screen:
A sleek landing page with a start button to launch the application.

### Main Interface:
- Input fields for entering text and selecting target languages.
- A chat-like area for displaying translations and original messages.
- Text-to-speech functionality for translated text.

## Installation Instructions

### Prerequisites

Before you begin, ensure you have the following installed on your local machine:
- Python
- Required Python libraries: `flet`, `deep-translator`, `pyttsx3`

### Steps to Install

1. **Clone the Repository**
    ```bash
    git clone https://github.com/naksusen/TranSpeak.git
    ```

2. **Navigate to the Project Directory**
    ```bash
    cd TranSpeak
    ```

3. **Install Dependencies**
    ```bash
    pip install flet deep-translator pyttsx3
    ```

4. **Run the Application**
    ```bash
    python TranSpeak.py
    ```

## How to Use

1. Launch the application by running `python TranSpeak.py`.
2. Enter text in the input field and specify the target language.
3. Click the "Translate" button to see the translated text in the chat area.
4. Listen to the translated text spoken aloud using the app's text-to-speech feature.

## Supported Languages

TranSpeak supports a wide variety of languages, including but not limited to:
- English
- Spanish
- French
- German
- Chinese
- Hindi
- Tagalog
- And many more...

Refer to the code for the full list of supported languages.

## Technology Stack

- **Python:** Core programming language.
- **Flet:** Framework for building the user interface.
- **Deep Translator:** For accurate and fast text translations.
- **Pyttsx3:** For text-to-speech functionality.

## Contributing

I welcome contributions to improve TranSpeak! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
    ```bash
    git checkout -b feature-name
    ```
3. Commit your changes:
    ```bash
    git commit -m "Add feature-name"
    ```
4. Push to the branch:
    ```bash
    git push origin feature-name
    ```
5. Open a pull request.
