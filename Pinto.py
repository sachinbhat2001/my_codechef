for t in range(int(input())):
	n,m=map(int,input().split())
	fruit_type=list(map(int,input().split()))
	cost=list(map(int,input().split()))

	minn = max(cost);
    
	for j in range(1,m+1):
		amt=0;
		for i in range(0,n):
			if fruit_type[i]==j:
				amt=amt+cost[i]
		if amt!=0 and amt<=minn:
			minn=amt
	print(minn)
