import csv
things = []
with open('google.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		things = row
		print "done"
		break

# with open('test.csv', 'wb') as tofile:
# 	thingswriter = csv.writer(tofile, dialect='excel')
# 	thingswriter.writerow(things)
# 	print "finished"


# title = "Name,Given Name,Birthday,Gender,Location"
# subj  = "Liuyuelong,,1991,male,Shenzhen"

# dic = {}
# t_list = title.split(",")
# s_list = subj.split(",")

print "<table border='1'>"
print "<tr>" + "".join(["<td>%s</td>" % x for x in things]) + "</tr>"
print "</table>"

table = "<table border='1'>\n"
table += "<tr>\n" + "".join(["<td>%s</td>\n" % x for x in things]) + "</tr>\n"
table += "</table>"

with open('test.html', 'w+') as html:
	html.write(table)