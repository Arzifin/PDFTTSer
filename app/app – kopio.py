from io import BytesIO
from flask import Flask, request, send_file
from gtts import gTTS
from PyPDF2 import PdfFileReader

app = Flask(__name__)


def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf = PdfFileReader(file)
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
        return text


def generate_audio(text, file_path):
    tts = gTTS(text=text, lang='en')
    tts.save(file_path)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            pdf_reader = PdfFileReader(file)
            full_text = ''
            for page in range(pdf_reader.getNumPages()):
                full_text += pdf_reader.getPage(page).extractText()
            speech = gTTS(text=full_text, lang='en', slow=False)
            file_obj = BytesIO()
            speech.write_to_fp(file_obj)
            file_obj.seek(0)
            return send_file(file_obj, attachment_filename='output.mp3', as_attachment=True)
    return '''
    <!doctype html>
    <html>
    <body>
    <h1>Upload PDF</h1>
    <form method="POST" enctype="multipart/form-data">
    <input type="file" name="file">
    <input type="submit" value="Convert to Speech">
    </form>
    </body>
    </html>
    '''


if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = '/path/to/save/uploads'
    app.run(host='0.0.0.0', port=5000)
