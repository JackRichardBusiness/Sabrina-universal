# Sabrina on Ruby (1.5)
# by Sabrina Technologies Inc.
require 'firebase'
def talk(input = 'default/unknown')
  firebase = Firebase::Client.new('https://sabrina-415a1.firebaseio.com/')
  resp = firebase.get("conversation/#{input.tr!(' ', '+')}")
  if resp.success? && resp.body != ''
    puts resp.body
  else
    firebase.set("unknown/#{input}", '?')
  end
end
while TRUE
  talk(gets.chomp)
end