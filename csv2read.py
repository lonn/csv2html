from sys import argv
import csv

script, filename = argv
table = ""

with open(filename, 'rb') as csvfile:
	reader = csv.reader(csvfile)

	table += "<table border='1'>"

	for row in reader:
		table += "<tr>\n" + "".join(["<td>%s</td>\n" % item for item in row]) + "</tr>\n"

	table += "</table>"

tofile = filename + ".html"
with open(tofile, 'w+') as htmlfile:
	htmlfile.write(table)

print "All done.."