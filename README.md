# monday
A Meme Generator Porject


For an overview of the Project, [click here](https://www.udacity.com/course/intermediate-python-nanodegree--nd303).


### Requirements
- Python = 3.8

### Background
Python is well suited for solving both web and data problems. This project is based on building a service that demonstrates these domains. Quote data imported from different data types (PDF, DOCX, CSV, TXT). Then, the Strategy Object design pattern is used to write clean, modular code to handle these different file types. The application will resize images and overlay a quote onto the resized graphics. the application interface is throug a command line utility and a deployable web service.

### Getting started
Make sure to have all dependencies installed
- `pip install flask`
- `pip install pandas`
- `pip install Pillow`
- `pip install docx`

for mac:
called via subprocess to parse PDF.
- `brew install --cask pdftotext`

pictures to be consumed by the application must be added to _data -> Photos

### Structure
The project consist of the following files and modules:
- _data: holdes the quote files and images
- fonts: holdes the fonts used
- MemeGenerator: Module that loads an image, resize it and overlays the image with a quote
- QuoteEngine: Parse the quote files of type CSV, PDF, TXT and DOCX
- templates: HTML templates
- tmp: Used to store output data from image MemeGenerator and PDFImporter

### How to run
run python3 app.py to start the webpage
run python3 meme.py ImagePath BodyQuote AuthorQuote to interface through the CLI. picute will be exported to tmp folder.