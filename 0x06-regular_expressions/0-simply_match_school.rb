#!/usr/bin/env ruby
# This script accepts one argument and prints matches of the word "School"

input = ARGV[0]
matches = input.scan(/School/)
