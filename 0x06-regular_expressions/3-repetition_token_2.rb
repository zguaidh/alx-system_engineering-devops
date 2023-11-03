#!/usr/bin/env ruby
#Regexp that match the following cases:
#hbtn
#hbttn
#hbtttn
#hbttttn
puts ARGV[0].scan(/hbt+n/).join
