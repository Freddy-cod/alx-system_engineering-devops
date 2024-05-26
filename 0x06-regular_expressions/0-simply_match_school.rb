#!/usr/bin/env ruby
# This script accepts one argument and prints matches of the word "School"
puts ARGV[0].scan(/School/).join
