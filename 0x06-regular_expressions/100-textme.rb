#!/usr/bin/env ruby
# 100-textme.rb script
puts ARGV[0].scan(/\[from:([\w+]+)\] \[to:([\w+]+)\] \[flags:([\d\-:]+)\]/).join(",")
