__author__ = 'Stuart'

import html.parser


class ToolHireParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.dates = []
        self.dateLent = ''
        self.isDate = False
        self.dateCounter = 0

    def handle_starttag(self, tag, attributes):
        """
        attributes would be: class=, height=, align, style, whatever. Value is the part after.
        The tags attributes are listed as tuples.
        :param tag:
        :param attributes:
        :return:
        """
        if tag == 'td':
            for key, value in attributes:
                if key == 'class' and value == 'xl65':  # xL not xONE
                    self.isDate = True
                    self.dateCounter += 1
                    break
        else:
            self.dateCounter = 0

    def handle_endtag(self, tag):
        self.isDate = False

    def handle_data(self, data):
        if self.isDate:
            if self.dateCounter == 1:
                self.dateLent = data
            else:
                self.dates.append((self.dateLent,data))


if __name__ == '__main__':
    htm = open('toolhire_files/sheet001.htm').read()
    parser = ToolHireParser()
    parser.feed(htm)
    print(parser.dates)