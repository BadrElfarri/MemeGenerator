"""Class for handling word documensts."""
from .quoteModel import QuoteModel
from typing import List
from .IngestorInterface import IngestorInterface
import subprocess
import os
import random


class PDFImporter(IngestorInterface):
    """Extracts data from a word document."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse word document if extension is correct."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        tmp = f'./tmp/{random.randint(0,1000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])

        try:
            file_ref = open(tmp, 'r')
        except FileNotFoundError:
            print("File not found")
            return []

        quotes = []

        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                line = line.split('"')
                quotes_inline = [
                    QuoteModel(quote, author.strip().replace('- ', ''))
                    for quote, author in zip(line[1::2], line[2::2])]
                quotes += quotes_inline

        file_ref.close()
        os.remove(tmp)

        return quotes


if __name__ == '__main__':
    import pathlib
    print(pathlib.Path(__file__).parent.resolve())
    # Working directory. where tmp file should be available
    print(pathlib.Path().resolve())
    path1 = '/Users/badrelfarri/Documents/Coding Languages/Python/' + \
            'Udacity Advanced Python/Meme Generator Project/_data/' + \
            'DogQuotes/DogQuotesPDF.pdf'
    path2 = '/Users/badrelfarri/Documents/Coding Languages/Python/' + \
            'Udacity Advanced Python/Meme Generator Project/_data/' + \
            'SimpleLines/SimpleLines.pdf'
    quotes = PDFImporter.parse(path1)
    print(quotes)
