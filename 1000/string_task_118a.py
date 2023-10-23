def main():
  string = input().lower()
  vowels = "aoyeui"
  output = ""

  for char in string:
    if vowels.find(char) == -1:
      output = output + "." + char

  print(output)

if __name__ == "__main__":
  main()