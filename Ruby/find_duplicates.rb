# Algorithm written in O(N) to find duplicate numbers in an array

array_one = [1, 2, 3, 4, 5, 6, 7, 8]
array_two = [1, 2, 3, 4, 1, 6, 7, 8]

def find_duplicates(array)
  duplicate_tracker = []
  for i in array
    p duplicate_tracker
    if duplicate_tracker[i] == i
      p "true"
      return true
    end
    duplicate_tracker[i] = i
  end
  p "false"
  return false
end

# find_duplicates(array_one)
# find_duplicates(array_two)

# Algorithm adjusted in O(N) to find duplicate letters in an array

array_three = ["a", "b", "c", "d", "e", "f", "g"]
array_four = ["a", "b", "c", "a", "e", "f", "g"]
array_five = [1, "a,", 2.0, 3, "Hello", 7, 2134]
array_six = [1, "a,", 2.0, 3, "Hello", "Hello", 7]

def find_duplicate_letters(array)
  letter_hash = {}
  steps = 0
  for i in array
    letter_hash[i] = 0
    steps += 1
  end
  for i in array
    letter_hash[i] += 1
    p letter_hash
    steps += 1
    if letter_hash[i] > 1
      p "true"
      p "Steps: #{steps}"
      return true
    end
  end
  p "false"
  p "Steps: #{steps}"
  return false
end

# find_duplicate_letters(array_three)
# find_duplicate_letters(array_four)
find_duplicate_letters(array_five)
find_duplicate_letters(array_six)
