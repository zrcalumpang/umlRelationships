class Document:
    def __init__(self):
        self.content = "Hello, World!"


class Printer:
    def print_document(self, document):
        print(document.content)


document = Document()
printer = Printer()

printer.print_document(document)
