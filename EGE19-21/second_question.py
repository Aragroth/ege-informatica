def hodi(f, s=5, hod=0):
	if f + s >= 75 and hod == 3:
		return True
	if hod > 3:
		return False
	
	if hod % 2 == 1:
		return 	hodi(f * 2, s, hod + 1) and \
			hodi(f + 2, s, hod + 1) and \
			hodi(f, s * 2, hod + 1) and \
			hodi(f, s + 2, hod + 1)
	else:
		return 	hodi(f * 2, s, hod + 1) or \
			hodi(f + 2, s, hod + 1) or \
			hodi(f, s * 2, hod + 1) or \
			hodi(f, s + 2, hod + 1)
		


for i in range(1, 69 + 1):
	print(i) if hodi(i) else 0
			
	
