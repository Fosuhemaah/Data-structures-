import numpy as np
L=12 #length of beam in metres
w=10 #intensity of load in kilo newton per meter
#question a
#bending moment(m) and shear force(v) at x=0
x=0
m=(w*(-6*x**2+6*L*x-L**2))/12
v=w*(L/2-x)
d='bending moment at x=0'
e='shear force at x=0'
print(d+str(m))
print(e+str(v))
#bending moment(m) and shear force(v) at x=l
x=10
m=(w*(-6*x**2+6*L*x-L**2))/12
v=w*(L/2-x)
f='bending moment at x=L'
g='shear force at x=L'
print(f+str(m))
print(g+str(v))
#question b
#an expression for distance when bending moment is zero is
'x**2-Lx+L**2/6'
#from the expression
a=1
b=-L
c=L**2/6
#finding the roots using the almighty formula
h=(b**2-4*a*c)/2*a
root1b=(-b+np.sqrt(h))
root2b=(-b-np.sqrt(h))
i='points of contraflexure are {0} and {1}'
print(i.format(root1b,root2b))
#question c
#when the shear force is zero
x=L/2
j='point at which shear force is zero'
print(j.format(x))
#question d
s=0.01 #step in meters
x=np.arange(0,(L+s),s)
m=(w*(-6*x**2+6*L*x-L**2))/12
k='the bending moment at each step in the array is{0} using the initialised variable'
print(d.format(m))
#question e
v=w*(L/2-x)
n='shear force for each step along the span is{}'
print(n.format(v))
#question f
o='absolute value of bending moment array'
p='minimum value for absolute value of bending moment array'
o=abs(m)
p=min(o)
'expression for when bending moment is p'
'x**2-Lx+(L**2/6)+(2*p)/w=0'
#from the expression
a=1
b=-L
c=(L**2/6)+(2*p)/w
#finding the roots using the almighty formula
h=(b**2-4*a*c)/2*a
root1f=(-b+np.sqrt(h))
root2f=(-b-np.sqrt(h))
q='points along L where absolute values of bending moment array is minumum are {0} and {1}'
print(q.format(root1f,root2f))
#question g
'relative errors betwwen estimated points of contraflexure in question b and question f'
relerror1=((root1b-root1f)/root1b*100)
relerror2=((root2f-root2b)/root2f*100)
r='relative errors betwwen estimated points of contraflexure are {0}% and {1}%'
print(r.format(relerror1,relerror2))
#question h
'maximum and minimum bending moment are t and u respectively'
t=max(m)
u=min(m)
#maximum
'for maximum bending moment x**2-Lx+(L**2/6)+(2*t)/w=0'
#from the expression
a=1
b=-L
c=(L**2/6)+(2*t)/w
#finding the roots using the almighty formula
h=(b**2-4*a*c)/2*a
root1h=(-b+np.sqrt(h))
root2h=(-b-np.sqrt(h))
v='points at which maximum bending moment occur are {0} and {1}'
print(v.format(root1h,root2h))
#minimum
'for minimum bending moment x**2-Lx+(L**2/6)+(2*u)/w=0'
#from the expression
a=1
b=-L
c=(L**2/6)+(2*u)/w
#finding the roots using the almighty formula
h=(b**2-4*a*c)/2*a
root1hi=(-b+np.sqrt(h))
root2hi=(-b-np.sqrt(h))
y='points at which maximum bending moment occur are {0} and {1}'
print(y.format(root1hi,root2hi))
# https://github.com/Fosuhemaah
