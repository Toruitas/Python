__author__ = 'Stuart'
"""
Challenge #19 will use The Adventures of Sherlock Holmes[1] from Project Gutenberg[2] .
Write a program that counts the number of alphanumeric characters there are in The Adventures of Sherlock Holmes.
 Exclude the Project Gutenberg header and footer, book title, story titles, and chapters. Post your code and the
 alphanumeric character count.

 Use Regex for matching the chapters and whatnot
"""

if __name__ == "__main__":
    import re, string
    linenum = 1
    ascii_count = 0
    pattern1 = '^X?(IX|IV|V?I{0,3})\.$'
    pattern2 = '^X?(IX|IV|V?I{0,3})\. THE'
    pattern3 = '^ADVENTURE X?(IX|IV|V?I{0,3})\.'
    with open("DP19Sherlock.txt") as file:
        for line in file:
            if linenum < 58:
                pass
            elif linenum > 12681:
                pass
            elif re.match(pattern1,line):
                print(line)
            elif re.match(pattern2,line):
                print(line)
            elif re.match(pattern3,line):
                print(line)
            else:
                for letter in line:
                    if letter in (string.ascii_letters + string.digits):
                        ascii_count +=1
                        #print(letter)
            linenum+=1
    print(ascii_count)
    print(linenum)