def count_characters(array, chars = array[0].length)
  if array.length == 1
    return chars
  end
  count = count_characters(array[1, array.length - 1], chars + array[1].length)
end

array = ["ab", "c", "def", "ghij"]
array = ["ab", "c", "def", "ghij", "klmn", "o", "pqr", "stuv", "wx", "y", "z"]

p count_characters(array)
