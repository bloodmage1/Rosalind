import math

ros = "ACGATACAA"

# print(math.log10(0.783))

gc_con = (ros.count("G") + ros.count("C")) / len(ros)

print(math.log10(gc_con))




