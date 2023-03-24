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

def find_duplicate_letters(array)
  letter_hash = {}
  for i in array
    letter_hash[i] = 0
  end
  for i in array
    letter_hash[i] += 1
    p letter_hash
    if letter_hash[i] > 1
      p "true"
      return true
    end
  end
  p "false"
  return false
end

find_duplicate_letters(array_three)
find_duplicate_letters(array_four)
