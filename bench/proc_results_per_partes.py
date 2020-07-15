#!/usr/bin/env python3

import csv
import re
import sys
from tabulate import tabulate

# fmt = 'text'
fmt = 'csv'


###########################################
def proc_res(fd):
    """proc_res(fd) -> _|_

    processes results from file descriptor 'fd'
"""
    reader = csv.reader(
        fd, delimiter=';', quotechar='"', doublequote=False, quoting=csv.QUOTE_MINIMAL)

    engines = list()
    engines_match = list()
    results = dict()
    for row in reader:
        eng, pattern, fl = row[1], row[2], row[3]
        ptrn_fl = (pattern, fl)
        if ptrn_fl not in results:
            results[ptrn_fl] = dict()
        if eng not in engines:
            engines.append(eng)
            engines_match.append(eng + '-matches')
            engines_match.append(eng + '-time-nca')
            engines_match.append(eng + '-time-dca')
            engines_match.append(eng + '-time-match')
            engines_match.append(eng + '-time-total')

        if row[0] == 'finished':
            if (re.search('Unhandled Exception', row[6])):
                row[0] = 'error'
            else:
                retcode = row[4]
                nca_time = row[5]
                dca_time = row[6]
                match_time = row[7]
                total_time = row[8]
                count_lines = row[9]
                user_time = row[11]

                results[ptrn_fl][eng] = user_time
                results[ptrn_fl][eng + '-matches'] = count_lines
                results[ptrn_fl][eng + '-time-nca'] = nca_time
                results[ptrn_fl][eng + '-time-dca'] = dca_time
                results[ptrn_fl][eng + '-time-match'] = match_time
                results[ptrn_fl][eng + '-time-total'] = total_time

        if row[0] == 'error':
            results[ptrn_fl][eng] = 'ERR'
            results[ptrn_fl][eng + '-matches'] = 'ERR'
            results[ptrn_fl][eng + '-time-nca'] = 'ERR'
            results[ptrn_fl][eng + '-time-dca'] = 'ERR'
            results[ptrn_fl][eng + '-time-match'] = 'ERR'
            results[ptrn_fl][eng + '-time-total'] = 'ERR'

        if row[0] == 'timeout':
            results[ptrn_fl][eng] = 'TO'
            results[ptrn_fl][eng + '-matches'] = 'TO'

    list_ptrns = list()
    for ptrn_fl in results:
        pattern, fl = ptrn_fl
        ls = [pattern, fl]
        for eng in engines:
            if eng in results[ptrn_fl]:
                ls.append(results[ptrn_fl][eng])
            else:
                ls.append(None)
        for eng in engines_match:
            if eng in results[ptrn_fl]:
                ls.append(results[ptrn_fl][eng])
            else:
                ls.append(None)
        list_ptrns.append(ls)

    header = ['pattern', 'file'] + engines + engines_match

    if fmt == 'html':
        print(tabulate(list_ptrns, header, tablefmt='html'))
    elif fmt == 'text':
        print(tabulate(list_ptrns, header, tablefmt='text'))
    elif fmt == 'csv':
        writer = csv.writer(
            sys.stdout, delimiter=';', quotechar='"', escapechar='\\',
            doublequote=False, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        writer.writerows(list_ptrns)
    else:
        raise Exception('Invalid output format: "{}"'.format(fmt))
    return


###############################
if __name__ == '__main__':
    argc = len(sys.argv)
    if argc == 1:
        fd = sys.stdin
    elif argc == 2:
        fd = open(sys.argv[1], "r")
    else:
        print("Invalid number of arguments: either 0 or 1 required")
        sys.exit(1)

    proc_res(fd)
    if argc == 2:
        fd.close()
