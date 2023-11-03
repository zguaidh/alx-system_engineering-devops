#!/usr/bin/env ruby
# regular expression that will match this cases
# hbttn
# hbtttn
# hbttttn
# hbtttttn
puts ARGV[0].scan(/hbt{2,5}n/).join
