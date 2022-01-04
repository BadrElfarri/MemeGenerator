import random
import os
import requests
from QuoteEngine import Ingestor
from MemeGenerator import MemeEngine
from flask import Flask, render_template, abort, request

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # quote_files variable
    quotes = []
    for path in quote_files:
        quote = Ingestor.parse(path)
        quotes.append(quote)
    # flaten quotes
    quotes = [quote for sublist in quotes for quote in sublist]

    images_path = "./_data/photos/dog/"

    # images within the images images_path directory
    imgs = None
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    body = request.form.get('body', '')
    author = request.form.get('author', '')
    image_url = request.form.get('image_url', '')
    if image_url:
        get_image = requests.get(image_url, allow_redirects=True)
        tmp = f'./temp_{random.randint(0, 1000000)}.jpg'
        with open(tmp, 'wb') as img_f:
            img_f.write(get_image.content)
        img = tmp

        path = meme.make_meme(img, body, author)
        os.remove(tmp)
    else:
        img = random.choice(imgs)
        path = meme.make_meme(img, body, author)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
