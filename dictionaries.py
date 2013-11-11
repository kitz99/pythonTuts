d = {"nume" : "Timofte", "prenume" : "Bogdan"}
print d["nume"]
# KeyError -> print d["cnp"]
del d["prenume"] #STERGERE
d["cnp"] = "1930614270037"
print d
d["nume"] = "timofte"
print d
print "~~~~~~~~More ops~~~~~~~~"
print "\tkeys: "
print d.keys()
print "\tvalues:"
print d.values()
print "\titems"
print d.items()
print "\tverificarea cheilor \"nume\" si \"grupa\""
print d.has_key("nume")
print d.has_key("grupa")

