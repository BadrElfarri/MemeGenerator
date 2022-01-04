"""Ingestor class."""
from .quoteModel import QuoteModel
from typing import List
from .IngestorInterface import IngestorInterface
from .PDFImporter import PDFImporter
from .TxtImporter import TxtImporter
from .DocxImporter import DocxImporter
from .CSVImporter import CSVImporter


class Ingestor(IngestorInterface):
    """Class used to ingest data from different file types."""
    
    ingestors = [PDFImporter, CSVImporter, TxtImporter, DocxImporter]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse all file types."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
            else:
                continue

        raise Exception("File is not of type, PDF, CSV, Txt or Docx")


if __name__ == '__main__':
    path1 = '/Users/badrelfarri/Documents/Coding Languages/Python/' + \
            'Udacity Advanced Python/Meme Generator Project/_data/' + \
            'DogQuotes/DogQuotesCSV.csv'
    path2 = '/Users/badrelfarri/Documents/Coding Languages/Python/' + \
            'Udacity Advanced Python/Meme Generator Project/_data/' + \
            'DogQuotes/DogQuotesDOCX.docx'
    path3 = '/Users/badrelfarri/Documents/Coding Languages/Python/' + \
            'Udacity Advanced Python/Meme Generator Project/_data/' + \
            'DogQuotes/DogQuotesPDF.pdf'
    path4 = '/Users/badrelfarri/Documents/Coding Languages/Python/' + \
            'Udacity Advanced Python/Meme Generator Project/_data/' + \
            'DogQuotes/DogQuotesTXT.txt'

    print(Ingestor.parse(path1))
    print(Ingestor.parse(path2))
    print(Ingestor.parse(path3))
    print(Ingestor.parse(path4))
