#!/usr/bin/env ruby
#output: [SENDER],[RECEIVER],[FLAGS]
#Sender phone num or name (including country code if present)
#Receiver phone num or name (including country code if present)
#The flags that were used
puts ARGV[0].scan(/\[from:([^\]]*)\] \[to:([^\]]*)\] \[flags:([^\]]*)\]/).join(",")
