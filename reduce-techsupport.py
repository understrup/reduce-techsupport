#!/usr/local/bin/python
# latin-1
import argparse

__author__ = "JPUnderstrup"


def check_cmd(cmdline):
    for i in range(len(output)):
        if cmdline.find(output[i]) != -1:
            return True
    return False


def get_filter(new_filter):
    try:
        filters = new_filter.split(";")
    except AttributeError:
        filters = []

    output = []
    try:
        ptr_add = open('.reduce-techsupport', 'r')
        for line in ptr_add:
            output = line.split(";")
        ptr_add.close()
    except IOError:
        print "No old filter defined"

    ptr_add = open('.reduce-techsupport', 'a')
    for line2 in filters:
        DontAdd = False
        for line in output:
            if line == line2:
                DontAdd = True
        if DontAdd is False:
            if not output:
                s = line2
            else:
                s = ";" + line2
            output.append(line2)
            ptr_add.write(s)
    if not output:
        output = filters
        try:
            ptr_add.write(new_filter)
        except TypeError:
            print "No new or old filters"
    ptr_add.close()
    return output


def remove_filter(filters, remove):
    try:
        rm = remove.split(";")
    except AttributeError:
        print "No filters to remove"
        return filters

    i = 0
    for f1 in filters:
        i = i + 1
        for f2 in rm:
            if f2 == f1:
                print i
                filters.remove(f1)
    return filters


def write_filers(filters):
    try:
        ptr_out = open('.reduce-techsupport', 'w')
        first = True
        for line in filters:
            if first:
                s = line
                first = False
            else:
                s = ";" + line
            ptr_out.write(s)
        ptr_out.close()
    except IOError:
        print "No old filter defined"


parser = argparse.ArgumentParser(prog='reduce-techsupport.py')
parser.add_argument('FILE', nargs='+', help='<tech-support> file to input')
parser.add_argument('--add', nargs='?', help="Add a filter to file .reduce-techsupport."
                                             " More filters can de added ex."
                                             "\"cdp neighbor:ip route:hostname\"")
parser.add_argument('--remove', nargs='?', help="Remove a filter from file .reduce-techsupport."
                                                " More filters can de remove ex. "
                                                "\"inventory:system internal dcbx info global\"")

args = parser.parse_args()


output = get_filter(args.add)
output = remove_filter(output, args.remove)

try:
    ptr_in = open(args.FILE[0])
except IOError:
    print args.FILE[0] + ": File not found"
    parser.print_help()
    exit(0)

print_cmd = False
for line in ptr_in:
    if line.find("`show ") != -1:
        if check_cmd(line) is True:
            print_cmd = True
        else:
            print_cmd = False
        print line
    elif print_cmd is True:
        print "    " + line,

ptr_in.close()
write_filers(output)
