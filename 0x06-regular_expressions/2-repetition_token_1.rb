#!/usr/bin/env ruby
#regular expression that will match the following cases:
#htn
#hbtn
puts ARGV[0].scan(/hb{0,1}tn/).join
