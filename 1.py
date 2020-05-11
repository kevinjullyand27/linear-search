
def search(arr, n, x): 

	for i in range (0, n): 
		if (arr[i] == x): 
			return i; 
	return -1; 


print('data array')
print('[ 2, 3, 4, 10, 40 ]')
x = input('data yang dicari: ')
arr = [ 2, 3, 4, 10, 40 ];  
n = len(arr); 
result = search(arr, n, int(x)) 
if(result == -1): 
	print('data yang dicari tidak ditemukan') 
else: 
	print(x+" ada di array ke "+str(result))
	
