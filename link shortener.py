import pyshorteners


while True:

  link = input("Enter the link or type q to exit: ")
  if link == "q":
    break

  shortener = pyshorteners.Shortener()

  print(shortener.tinyurl.short(link))
