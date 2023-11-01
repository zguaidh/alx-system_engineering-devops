#!/usr/bin/env ruby
# Get the argument from the command line
args = ARGV[0]

# Define the regular expression pattern
regexp = /School/

# Find all matches in the input
matches = args.scan(regexp)

# Join the matches together
result = matches.join

# Print the result or a new line if no match found
if args =~ regexp
  puts result
else
  puts
end
