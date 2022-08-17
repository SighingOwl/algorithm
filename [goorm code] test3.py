def check_Prime(num):
	for i in range(2, int(num**(1/2)) + 1):
		if num % i == 0:
			return False
	
	return True

def make_prime(target):
	if target == 1:
		Prime_List = []
		Prime_List.append(2)
		Prime_List.append(3)
		Prime_List.append(5)
		Prime_List.append(7)
		return Prime_List
	
	prev_Prime_List = make_prime(target - 1)
	
	new_Prime_List = []
	add_num = [1, 3, 7 ,9]
	for i in range(len(prev_Prime_List)):
		prev_Prime = prev_Prime_List[i] * 10
		for j in range(len(add_num)):
			tmp = prev_Prime + add_num[j]
			if check_Prime(tmp) == True:
				new_Prime_List.append(tmp)
				
	return new_Prime_List


n = int(input())
print(make_prime(n))