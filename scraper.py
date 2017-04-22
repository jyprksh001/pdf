# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".


# 1. Add some necessary libraries
import scraperwiki
import urllib2, lxml.etree

# 2. The URL/web address where we can find the PDF we want to scrape
# url = 'http://cdn.varner.eu/cdn-1ce36b6442a6146/Global/Varner/CSR/Downloads_CSR/Fabrikklister_VarnerGruppen_2013.pdf'
url='http://git.macropus.org/2011/11/pdftotext/example/journal.pone.0026738.pdf'
# 3. Grab the file and convert it to an XML document we can work with
pdfdata = urllib2.urlopen(url).read()
xmldata = scraperwiki.pdftoxml(pdfdata)
root = lxml.etree.fromstring(xmldata)

# 4. Have a peek at the XML (click the "more" link in the Console to preview it).
print lxml.etree.tostring(root, pretty_print=True)

# 5. How many pages in the PDF document?
pages = list(root)
print "There are",len(pages),"pages"
