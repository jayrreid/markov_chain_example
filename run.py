__author__ = 'jrreid'
from markov_python.cc_markov import MarkovChain
from bs4 import BeautifulSoup
import fetch_data

title1 =  fetch_data.fetch('http://www.netlingo.com/acronyms.php')
title2 =  fetch_data.fetch('http://www.cnn.com')
title3 =  fetch_data.fetch('http://google.com')

mc = MarkovChain()
mc.add_string(title1)
mc.add_string(title2)
mc.add_string(title3)

print "random text generator: "
list1= mc.generate_text()
print " ".join(list1)

list2= mc.generate_text()
print " ".join(list2)

list3= mc.generate_text()
print " ".join(list3)