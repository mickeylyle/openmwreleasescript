#!/usr/bin/python
#
# Usage: ./process.py inputfile.txt
# Result will be written to output.txt
#

import sys
import re

with open (sys.argv[1], "r") as myinputfile:
    rawtext = myinputfile.read().rstrip()

htmltext = "<p>" + rawtext.replace("\n\n", "</p>\n\n<p>") + "</p>"
htmltext = htmltext.replace("Downloads Page (https://openmw.org/downloads/)", "<a href=\"https://openmw.org/downloads/\">Downloads Page</a>")
htmltext = htmltext.replace("Known Issues:\n- ", "<b>Known Issues:</b><br>\n<ul><li>")
htmltext = htmltext.replace("Changelog:\n- ", "<b>Changelog:</b><br>\n<ul><li>")
htmltext = htmltext.replace("\n- ", "</li>\n<li>")

htmltext = re.sub(re.compile('(<p>.*?<ul>.*?)</p>', re.DOTALL), '\\1</li></ul></p>', htmltext)
htmltext = re.sub('(.*?)release video(.*?) http.*?(watch.*?)</p>', '\\1<a href="http://www.youtube.com/\\3\">release video</a>\\2</p>', htmltext)
htmltext = htmltext.replace("WeirdSexy:", "WeirdSexy.")

bbtext = htmltext.replace("<p>", "")
bbtext = bbtext.replace("</p>", "")
bbtext = bbtext.replace("<br>", "")
bbtext = bbtext.replace("<a href=\"", "[url=")
bbtext = bbtext.replace("\">", "]")
bbtext = bbtext.replace("</a>", "[/url]")
bbtext = bbtext.replace("<", "[")
bbtext = bbtext.replace(">", "]")
bbtext = bbtext.replace("[li]", "[*]")
bbtext = bbtext.replace("[/li]", "")
bbtext = bbtext.replace("ul]", "list]")

with open ("output.txt", "w") as myoutputfile:
    myoutputfile.write("[code]" + rawtext + "[/code]\n\n[code]" + htmltext + "[/code]\n\n[code]" + bbtext + "[/code]")
