#!/usr/bin/env ruby
#regex must match a string that stars with h ends with n
#and can have any single character in between 
puts ARGV[0].scan(/h.n/).join
