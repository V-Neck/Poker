f = open("nums.txt").readlines()

print ["%s,"% str(i).strip()[5:] for i in f]