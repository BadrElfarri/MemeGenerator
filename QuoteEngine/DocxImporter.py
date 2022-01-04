"""Class for handling word documensts."""
import docx
from .IngestorInterface import IngestorInterface
from .quoteModel import QuoteModel
from typing import List


class DocxImporter(IngestorInterface):
    """Extracts data from a word document."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse word document if extension is correct."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        try:
            doc = docx.Document(path)

            for para in doc.paragraphs:
                if para.text != "":
                    parse = para.text.split(' - ')
                    new_quote = QuoteModel(parse[0], parse[1])
                    quotes.append(new_quote)

        except docx.opc.exceptions.PackageNotFoundError:
            print(f'Word file not found {path}')
            return []

        except IndexError:
            print('Error inncosistence file structure')
            return []

        return quotes


if __name__ == '__main__':
    path1 = '/Users/badrelfarri/Documents/Coding Languages/Python/' + \
            'Udacity Advanced Python/Meme Generator Project/_data/' + \
            'DogQuotes/DogQuotesDOCX.docx'
    path2 = '/Users/badrelfarri/Documents/Coding Languages/Python/' + \
            'Udacity Advanced Python/Meme Generator Project/_data/' + \
            'SimpleLines/SimpleLines.docx'
    quotes = DocxImporter.parse(path1)
    print(quotes)
