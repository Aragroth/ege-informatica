def hodi(f, s=5, hod=0):
	if f + s >= 75 and hod == 2:
		return True

	if hod > 2:
		return False

	return 	hodi(f * 2, s, hod + 1) or \
			hodi(f + 2, s, hod + 1) or \
			hodi(f, s * 2, hod + 1) or \
			hodi(f, s + 2, hod + 1)


for i in range(1, 69 + 1):
	print(i) if hodi(i) else 0			
	
