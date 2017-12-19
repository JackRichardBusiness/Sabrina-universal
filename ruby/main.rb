puts "\nSabrina on Ruby (1.0)"
puts 'By Unyfi Technologies Inc.'
puts "\nHi! I'm Sabrina"
puts "What's your name?"
name = gets.chomp
if name != ''
  puts "Hello #{name}!"
else
  puts 'Hi!'
end
puts 'How are you today?'
feeling = gets.chomp
if feeling != ''
  puts "That's #{feeling}"
else
  puts 'Ok.'
end
puts 'Can you ask me some math, please.'
def math(num1, num2, operation)
  if operation == 0
    puts "I think that is #{num1 + num2}"
  elsif operation == 1
    puts "I think that is #{num1 - num2}"
  end
end
puts 'So, addition or subtraction?'
operation = gets.chomp
if operation == 'addition' || operation == 'subtraction'
  puts "Ok! What's the first number?"
  numOne = Integer(gets.chomp)
  puts 'And now, the second?'
  numTwo = Integer(gets.chomp)
  if operation == 'addition'
    math(numOne, numTwo, 0)
  else
    math(numOne, numTwo, 1)
  end
else
  puts "I didn't understand that..."
end