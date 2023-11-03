#!/usr/bin/env ruby
#Regexp that match the following cases:
#hbtn
#hbttn
#hbtttn
#hbttttn
puts ARGV[0].scan(/hbt{1,4}n/).join
