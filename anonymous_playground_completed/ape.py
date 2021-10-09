s="hEzAdCfHzA::hEzAdCfHzAhAiJzAeIaDjBcBhHgAzAfHfN"
# convert to numeric a=1 Z=26 a+z=26+1=27
a=[8,5,26,1,4,3,6,8,26,1,8,5,26,1,4,3,6,8,26,1,8,1,9,10,26,1,5,9,1,4,10,2,3,2,8,8,7,1,26,1,6,8,6,14]

for i in range(0,len(a),2):
	# print(a[i],a[i+1])
	c=((a[i]+a[i+1])%26)
	c=c+96
	print(chr(c),end='')

