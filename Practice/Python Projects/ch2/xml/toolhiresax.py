__author__ = 'Stuart'

import xml.sax
import xml.sax.handler
# Sax goes through the document line by line.

class ToolHireHandler(xml.sax.handler.ContentHandler):
    """
    Typically, use ContentHandler to create your own handler. For simple tasks, write own versions of
    startElement() and endElement(), and maybe character() method
    Then create a parser object, passing the handler as an argument.

    Handler processes an event sequence between startElement(), then Characters, then endElement()
    """
    def __init__(self):
        super().__init__()
        self.dates = []
        self.dateLent = ''
        self.dateCounter = 0
        self.isDate = False

    def startElement(self, name, attributes):
        """
        looks for Data elements, when found, refines search for only selecting those with ss:type of DateTime
        (have to inspect XML file for those manually)

        Looks cell by cell?

        If data type isn't DateTime, we've reached a new row, so reset date counter.

        If the ss:Type is DateTime, we flag it as such, so that within the character() method, which is called next,
        we know we are looking at the type of data we want.
        :param name: name of element type
        :param attributes:
        :return:
        """
        if name == 'Data':
            data = attributes.get('ss:Type', None)
            if data == 'DateTime':
                self.isDate = True
                self.dateCounter += 1
            else:
                self.dateCounter = 0

    def endElement(self, name):
        """
        resets flag to false for next trigger event
        :param name:
        :return:
        """
        self.isDate = False

    def characters(self, data):
        """
        DO NOT MISTYPE THIS OR IT DOES NOT WORK INSIDE THE PARSER OBJECT
        characters() is called whenever content outside a tag element is encountered. So when self.isDate is True,
        and we aren't in the tag, but the content between, we grab the date lent, or if it is the second date,
        we append a tuple to the dates.

        If only lent data available, will not add any tuples to the dates list. Since we can't calculate duration with
        only one date.
        :param data:
        :return:
        """
        if self.isDate:
            if self.dateCounter == 1:
                self.dateLent = data
            else:
                self.dates.append((self.dateLent, data))

if __name__ == '__main__':
    handler = ToolHireHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse('toolhire.xml')
    print(handler.dates)