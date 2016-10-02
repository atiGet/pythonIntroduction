hrs = raw_input("Enter Hours:")
rhrs = raw_input("Enter Rate Hours:")

h=float(hrs)
r=float(rhrs)
if h<=40:
    gp=h*r
else:
	gp=(40*r)+(1.5*(h-40)*r)
print gp    