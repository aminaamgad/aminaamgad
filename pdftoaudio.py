# https://www.youtube.com/watch?v=LXsdt6RMNfY (tiffany in tech)

import pyttsx3, PyPDF2

# prompt the user for the name of the PDF file
def file_name():
    filename = input("Enter the name of your PDF file: ")
    return filename

# prompt the user for the name of the audio file
def audio_file_name():
    audiofile = input("Enter the name of your audio file: ")
    return audiofile

# convert the PDF to audio
def convert_pdf_to_audio(file_name, audio_file_name):
    pdfreader = PyPDF2.PdfFileReader(open(file_name, 'rb'))
    speaker = pyttsx3.init()

    # repeat for every page in the pdf
    for page_num in range(pdfreader.numPages):
        text = pdfreader.getPage(page_num).extractText()
        clean_text = text.strip().replace('\n', ' ')
        print(clean_text)
        speaker.save_to_file(clean_text, audio_file_name)
        speaker.runAndWait()

    speaker.stop()

if __name__ == "__main__":
    filename = file_name()
    audiofile = audio_file_name()
    convert_pdf_to_audio(filename, audiofile)
