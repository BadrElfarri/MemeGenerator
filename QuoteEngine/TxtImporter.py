"""Class for handling document."""
from .IngestorInterface import IngestorInterface
from .quoteModel import QuoteModel
from typing import List


class TxtImporter(IngestorInterface):
    """Extracts data from a document."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse Text document if extension is correct."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []

        try:
            file_ref = open(path, 'r')

            for line in file_ref.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parse = line.split(' - ')
                    new_quote = QuoteModel(parse[0], parse[1])
                    quotes.append(new_quote)

            file_ref.close()

        except FileNotFoundError:
            print(f'CSV File not found at {path}')

        return quotes


if __name__ == '__main__':
    path1 = '/Users/badrelfarri/Documents/Coding Languages/Python/' + \
            'Udacity Advanced Python/Meme Generator Project/_data/' + \
            'DogQuotes/DogQuotesTXT.txt'
    path2 = '/Users/badrelfarri/Documents/Coding Languages/Python/' + \
            'Udacity Advanced Python/Meme Generator Project/_data/' + \
            'SimpleLines/SimpleLines.txt'

    quotes = TxtImporter.parse(path1)
    print(quotes)
