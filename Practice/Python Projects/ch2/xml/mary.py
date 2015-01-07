__author__ = 'Stuart'

text = """mary had a little lamb
its fleece was white as snow
and everywhere that mary went
the lamb was sure to go"""

def has_mary(aLine):
    print("We found: {}".format(aLine))

def parse_text(theText, aPattern, function):
    for line in theText.split('\n'):
        if aPattern in line:
            function(line)

parse_text(text,'mary',has_mary)