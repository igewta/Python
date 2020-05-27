for i in range(0,21):
	for j in range(0,34):
		for k in range(0,201):
			if i*5 + j*3 +k*0.5 == 100 and i + j + k ==100:
				print(i,j,k)