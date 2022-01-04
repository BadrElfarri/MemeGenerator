"""Class for handling document."""
from .IngestorInterface import IngestorInterface
from .quoteModel import QuoteModel
from typing import List
from pandas import read_csv


class CSVImporter(IngestorInterface):
    """Extracts data from a document."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse Text document if extension is correct."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        try:
            df = read_csv(path, header=0)
            # print(df)
            quotes = []

            for index, row in df.iterrows():
                quote = QuoteModel(row['body'], row['author'])
                quotes.append(quote)

        except FileNotFoundError:
            print(f'CSV File not found at {path}')

        except KeyError:
            print('Header Schema error expect header with names: body, author')

        return quotes


if __name__ == '__main__':
    path1 = '/Users/badrelfarri/Documents/Coding Languages/Python/' + \
            'Udacity Advanced Python/Meme Generator Project/_data/' + \
            'DogQuotes/DogQuotesCSV.csv'
    path2 = '/Users/badrelfarri/Documents/Coding Languages/Python/' + \
            'Udacity Advanced Python/Meme Generator Project/_data/' + \
            'SimpleLines/SimpleLines.csv'

    quotes = CSVImporter.parse(path1)
    print(quotes)
