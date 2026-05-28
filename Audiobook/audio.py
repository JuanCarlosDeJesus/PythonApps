# Audiobook
import pyttsx3
import PyPDF2

with open('loremipsum.pdf', 'rb') as book:

    full_text = ""

    reader = PyPDF2.PdfReader(book)

    audio_reader = pyttsx3.init()
    audio_reader.setProperty("rate", 100)

    for page in range(len(reader.pages)):
        next_page = reader.pages[page]
        content = next_page.extract_text()
        full_text += content

        # .say = audio reader
        # audio_reader.say(content)
        # audio_reader.runAndWait()

    # .save_to_file = saves read file to text
    audio_reader.save_to_file(full_text, "myaudio.mp3")
    audio_reader.runAndWait()