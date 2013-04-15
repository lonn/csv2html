from sys import argv
import csv

script, filename = argv
table = ""

#open .csv file
with open(filename, 'rb') as csvfile:
	reader = csv.reader(csvfile)
	
	#generate table
	table += "<table border='1'>"

	#get every row in .csv
	for row in reader:
		#get every item in row
		table += "<tr>\n" + "".join(["<td>%s</td>\n" % item for item in row]) + "</tr>\n"

	table += "</table>"

#write to .html
tofile = filename + ".html"
with open(tofile, 'w+') as htmlfile:
	htmlfile.write(table)

print "All done.."
