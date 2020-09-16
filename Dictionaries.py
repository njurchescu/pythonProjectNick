
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Nov": "November",
    "Oct": "October",
    "Dec": "December",
    5: 7,
}


print(monthConversions["Dec"])  # prints the dictionary
print(monthConversions.get("Luv", "Not a valid key"))
print(monthConversions[5])
