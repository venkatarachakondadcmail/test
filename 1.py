#Program to print all duplicates and their counts 
# Programming - print g:2, r:2, m:2

class Duplicates:
    def print_duplicates(self,input):
        counts = {}
        for i in input:
            if i in counts:
                counts[i]+=1
            else:
                counts[i] = 1
        for key, value in counts.items():
            if value > 1:
                print(f"{key}: {value}")

d = Duplicates()
d.print_duplicates('prop')
