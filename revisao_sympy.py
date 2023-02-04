import sympy as sp

x = sp.symbols('x')

x*x


sp.init_printing()

Lista_simbolos = ['y', 'x']
y,x = sp.symbols(Lista_simbolos)

f_x_y = x**2 + y **2 + x*y
f_x_y


resposta = f_x_y.subs(x,1).subs(y,2)
resposta


f_xy = (x+y)**2 + y**2 + 2*x*y + y**2
sp.simplify(f_xy)

x<=y

a = sp.Matrix([[1,2,3],[4,5,6]])
a.shape

I = sp.zeros(3)

lista_E = [7,8,9]

E = sp.diag(*lista_E)

E.det()

x1,x2,x3 = sp.symbols(['x1','x2','x3'])

X = sp.Matrix([x1,x2,x3])
E = sp.Matrix([[1,2,3], [4,5,6],[7,8,9]])
R = sp.Matrix([11,22,33])

#EX = R

E*X - R


