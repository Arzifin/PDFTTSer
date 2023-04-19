from flask import Flask, request, redirect, url_for, send_file, render_template
from PyPDF2 import PdfFileReader
from gtts import gTTS
from io import BytesIO
import threading

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            # start the conversion process in a separate thread
            thread = threading.Thread(target=convert_pdf_to_speech, args=(file,))
            thread.start()
            # show the loading spinner while conversion is in progress
            return render_template('./loading.html')
    return render_template('./index.html')

def convert_pdf_to_speech(file):
    pdf_reader = PdfFileReader(file)
    full_text = ''
    for page in range(pdf_reader.getNumPages()):
        full_text += pdf_reader.getPage(page).extractText()
    speech = gTTS(text=full_text, lang='en', slow=False)
    file_obj = BytesIO()
    speech.write_to_fp(file_obj)
    file_obj.seek(0)
    # send the speech file to the user for download
    return send_file(file_obj, attachment_filename='output.mp3', as_attachment=True)


if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = '/path/to/save/uploads'
    app.run(host='0.0.0.0', port=5000)
