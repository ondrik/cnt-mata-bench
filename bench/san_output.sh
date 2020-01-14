#!/bin/bash
grep -v 'Error parsing' |\
	grep -v 'pattern too large' |\
	sed 's/Error[^;]*###/Error ###/' |\
	sed 's/Unhandled Exception[^;]*###/Unhandled Exception ###/' |\
	sed 's/Not supported[^;]*###/Not supported ###/' |\
	sed 's/;[^;]*Time: \([^ ]*\)[^;]*Matching lines: \([0-9]*\)[^;]*;/;\2;/' |\
	sed 's/;[^;]*Time: \([^ ]*\)[^;]*Matching lines: \([0-9]*\)[^;]*;/;\2;/'

# grep -v 'FATAL UNHANDLED EXCEPTION' | \
# 	# sed 's/;[^;]*--chipmunk[^;]*Time: \([^ ]*\)[^;]*Matching lines: \([0-9]*\)[^;]*;/;\2;/' |
# 	# sed 's/;[^;]*--margus[^;]*Time: \([^ ]*\)[^;]*Matching lines: \([0-9]*\)[^;]*;/;\2;/'
# 	sed 's/;[^;]*Time: \([^ ]*\)[^;]*Matching lines: \([0-9]*\)[^;]*;/;\2;/' |
# 	sed 's/;[^;]*Time: \([^ ]*\)[^;]*Matching lines: \([0-9]*\)[^;]*;/;\2;/'
