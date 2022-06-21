"""
Input	                                                                    Output
Join WebStars now for free, at www.web-stars.com                            www.web-stars.com
You can also support our partners:                                          www.internet.com
Internet - www.internet.com                                                 www.webspiders101.com
WebSpiders - www.webspiders101.com
Sentinel - www.sentinel.-ko

Need information about cheap hotels in London?                              www.indigo.bloggers.com
You can check us at www.london-hotels.co.uk !                               www.rebel21.sedecrem.moc
We provide the best services in London.
Here are some reviews in some blogs:
London Hotels are awesome! - www.indigo.bloggers.com
I am very satisfied with their services - ww.ivan.bg
Best Hotel Services! - www.rebel21.sedecrem.moc
www.london-hotels.co.uk
"""
import re
output = list()

while True:
    text = input()

    if not text:
        break

    expression = r"w{3}\.[a-zA-Z0-9\-]+(\.[a-z]+)+"
    matches = re.finditer(expression, text)

    for match in matches:
        output.append(match.group())

if len(output) > 0:
    print("\n".join(output))