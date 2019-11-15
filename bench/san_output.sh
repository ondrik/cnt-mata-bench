#!/bin/bash
grep -v 'FATAL UNHANDLED EXCEPTION' | \
	# sed 's/;[^;]*--chipmunk[^;]*Time: \([^ ]*\)[^;]*Matching lines: \([0-9]*\)[^;]*;/;\2;/' |
	# sed 's/;[^;]*--margus[^;]*Time: \([^ ]*\)[^;]*Matching lines: \([0-9]*\)[^;]*;/;\2;/'
	sed 's/;[^;]*Time: \([^ ]*\)[^;]*Matching lines: \([0-9]*\)[^;]*;/;\2;/' |
	sed 's/;[^;]*Time: \([^ ]*\)[^;]*Matching lines: \([0-9]*\)[^;]*;/;\2;/'
