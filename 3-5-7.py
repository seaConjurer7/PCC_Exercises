# This is a small program that will manage an ever-changing guest list and sends invitations to the diner party
# Carsen Weinzetl 02/19/2019 

# Initial guest list
guests = ["Billy", "Joe", "Smitty", "Lee"]

# Initial invitation messages
print(guests[0] + ", you are cordially invited to my dinner party!")
print("\n" + guests[1] + ", you are cordially invited to my dinner party!")
print("\n" + guests[2] + ", you are cordially invited to my dinner party!")
print("\n" + guests[3] + ", you are cordially invited to my dinner party!")

# Informing the guests that one has bailed and then removing him from the list
print("\nWell, it looks like " + guests[0] + " overdosed on cocaine. So he wont be showing up ...")
guests.remove("Billy")

# New invitations
print("\n" + guests[0] + ", you are STILL cordially invited to my dinner party!")
print("\n" + guests[1] + ", you are STILL cordially invited to my dinner party!")
print("\n" + guests[2] + ", you are STILL cordially invited to my dinner party!")

# Informing people I found this big ass table and adding more people to the list
print("\nYo I just found this big ass table on the side of the road! Bring the whole family!")

guests.insert(0, "Mrs. Joe")
guests.insert(2, "Mrs. Smitty")
guests.append("Mrs. Lee")

# Finding amount of guests and outputting it as a string
guest_amnt = str(len(guests))

print("\nSo it looks like there will be about, " + guest_amnt + " people coming!")

# Ok well, the table isnt going to arrive in time for the dinner, time to downsize
print("\n...Well, my table is still small...")
cut1 = guests.pop(0)
print("\nSorry " + cut1 + " I dont have room for anymore!")
cut2 = guests.pop(0)
print("\nSorry " + cut2 + " I dont have room for anymore!")
cut3 = guests.pop(0)
print("\nSorry " + cut3 + " I dont have room for anymore!")
cut4 = guests.pop(0)
print("\nSorry " + cut4 + " I dont have room for anymore!")

# Informing the last guests of their victory royale & del them off the list once-and-for-all

# Finding amount of guests and outputting it as a string
guest_amnt = str(len(guests))

print("\n" + guests[0] + " & " + guests[1] + ", you " + guest_amnt + " are the only ones left standing. Congratulations! Now lets eat!!")

del guests[0]
del guests[0]

# Checking to make sure the list is actually empty
print(guests)


