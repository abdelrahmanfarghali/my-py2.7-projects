import urllib2
website_address = raw_input("Enter Website Address: ")
website = urllib2.urlopen(website_address)
information = website.read()
website.close()
print "Done, configure variable information!"
