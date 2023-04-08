# Jan -> January
# Mar -> March


monthConversion = {0: "January", "Feb": "February", "Mar": "March", "Apr": "April", "May": "May", "Jun": "June",
                   "Jul": "July", "Aug": "August", "Sep": "September", "Oct": "October", "Nov": "November",
                   "Dec": "December"}
print(monthConversion["Dec"])
print(monthConversion.get(0, "Not a valid key"))
print(monthConversion)
print(*monthConversion)
