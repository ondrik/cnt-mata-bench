#!/bin/bash
cat bench-twain.txt | ./pycobench pattern_match.yaml >&2
cat pycobench.tasks | ./san_output.sh > sanitized.txt
cat sanitized.txt | ./proc_results.py
