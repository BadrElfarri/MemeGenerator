"""Model for quotes."""


class QuoteModel:
    """Model for quotes will have body and author."""

    def __init__(self, body, author):
        """Pass body and Auther."""
        self.body = body
        self.author = author

    def __str__(self):
        """Implement str."""
        return f'{self.body} - {self.author}'

    def __repr__(self) -> str:
        """Return body and author."""
        return f'(body: {self.body}, author: {self.author})'
