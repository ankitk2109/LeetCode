
class solution():
	def countPairs(self, s: String) -> int
	#s = 'abad' -> valid pairs would be ab, ad, bd, ad
	from collections import Counter
	counter = Counter(s)
	#print (counter)
	count = 0
	for c in s:
	  #print('Value of ',c,'is :',dict_[c])
	  if(counter[c]!= 0):
	    for k,v in counter.items():
	      if c<k and v!=0:
	        count += 1
	    counter[c] -= 1     

	return (count)