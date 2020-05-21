import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-m', '--match', required=True,
                    help='String to match of the website when the query is TRUE', dest='match')
parser.add_argument('-s', '--sql', required=True, nargs="+",
                    help='Subselect to run on the database.  Must return a string (use concat and group_concat)', dest='sql')

args = parser.parse_args()
sqlstatement = " ".join(args.sql)

print "\nCommand line read:\n"
print "sql statement = ", sqlstatement
print "match string = ", args.match
