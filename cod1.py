#ATM
n, k= map(float, input().split())


if k>(n+0.5) and n%5.0==0:
	k=k-(n+0.5)

	


precision = 2
print( "{:.{}f}".format( k, precision ) )