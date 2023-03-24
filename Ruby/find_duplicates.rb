# Algorithm written in O(N) to find duplicate numbers in an array

array_one = [1, 2, 3, 4, 1, 6, 7, 8]
array_two = [1, 2, 3, 4, 5, 6, 7, 8]

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

find_duplicates(array_one)
find_duplicates(array_two)
