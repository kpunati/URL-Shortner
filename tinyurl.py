import pyshorteners

link = input("enter link: ")
shortener = pyshorteners.Shortener()
new_link = shortener.tinyurl.short(link)
print(new_link)
