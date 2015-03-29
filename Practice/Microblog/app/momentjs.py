__author__ = 'Stuart'

from jinja2 import Markup

class momentjs(object):
    def __init__(self, timestamp):
        self.timestamp = timestamp

    def render(self, format):
        """
        Doesn't directly return a string, but wraps the string inside a Markup obj. Jinja escapes all strings by default
        So <script> tag would reach client as &lt;script&gt;, so we put it in the obj to tell Jinja that it shouldn't
        be escaped
        :param format:
        :return:
        """
        return Markup("<script>\ndocument.write(moment({}).{});\n</script>".format(self.timestamp.strftime("'%Y-%m-%d %H:%M:%S Z'"),format))


    def format(self, fmt):
        return self.render("format(\"{}\")".format(fmt))

    def calendar(self):
        return self.render("calendar()")

    def fromNow(self):
        return self.render("fromNow()")

