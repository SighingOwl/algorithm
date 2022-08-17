def merge_sort(A):
	if len(A) == 1:
		return A
	
	center_index = len(A) // 2
	
	left = merge_sort(A[center_index:])
	right = merge_sort(A[:center_index])
	
	sorted_num = []
	l_index, r_index = 0, 0
	while l_index < len(left) and r_index < len(right):
		if left[l_index] < right[r_index]:
			sorted_num.append(left[l_index])
			l_index += 1
		elif left[l_index] >= right[r_index]:
			sorted_num.append(right[r_index])
			r_index += 1
			
	sorted_num += left[l_index:]
	sorted_num += right[r_index:]
	return sorted_num

n = int(input())
num = [int(x) for x in input().split()]
for i in range(n):
	print(merge_sort(num)[i], end=" ")
    