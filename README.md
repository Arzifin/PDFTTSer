# PDFTTSer
A lightweight program for converting PDF files to Speech.
The app is containerized for my own convinience.

## Launch instructions
- Make sure you have Python installed, if you don't have it, then download it from here: 
  - https://www.python.org/downloads/
- Download/clone the contents of this application onto your computer. 
- Open terminal from the directory where you downloaded the application.
- Install required packages with:
  - pip install -r requirements.txt
- If all above steps are done, then you can start the application with the command:
  - python app.py

Now you can open your web browser and head to http://localhost:5000 to access the application.
Enjoy! Alternatively you can launch the program with Docker, if you so desire.

### Launching with Docker
- For this option you'll need to have Docker installed.
  - https://docs.docker.com/get-docker/ 
- Upon having downloaded the application, head to its root directory with the terminal.
- Type into terminal:
  - docker-compose up 

Now the containers and images should be up and working.
You should see the application at http://localhost:5000.
