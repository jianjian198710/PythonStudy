#10.3.8
from re import *
#match from first character
print match("p","python")
print match("p","www.python.org")

#split
some_text="alpha, beta,,,,gamma delta"
print split("[, ]+",some_text)

some_text="alpha, beta,,,,gamma delta"
print split("[, ]+",some_text,maxsplit=2)

#findall
pat="[a-zA-Z]+"
text='"Hm... Err -- are you sure?" he said, sounding insecure.'
print findall(pat,text)

#sub
pat="{name}"
text="Dear {name}..."
print sub(pat,"Mr.Gumby",text)

#group
m=match("www\\.(.*)\\..{3}","www.python.org")
print "m.group(1) is: "+str(m.group(1))
#"python" start location in "www.python.org"
print "m.start(1) is: "+str(m.start(1))
print "m.end(1) is: "+str(m.end(1))
print "m.span(1) is: "+str(m.span(1))

#greedy
emphasis_pattern="\\*(.+)\\*"
print sub(emphasis_pattern, "<em>\\1</em>","*This* is *it*!")
#not greedy with "?"
emphasis_pattern2="\\*(.+?)\\*"
print sub(emphasis_pattern2, "<em>\\1</em>","*This* is *it*!")