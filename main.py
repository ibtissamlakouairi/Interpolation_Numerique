import numpy as np
import matplotlib.pyplot as plt
from interpolation import lagrange, newton, hermite

def f1(x):
    return x ** 2
def df1(x):
    return 2 * x
def f2(x):
    return 1 / (1 + 25 * x ** 2)
def df2(x):
    return -50 * x / (1 + 25 * x ** 2) ** 2
def erreur_max(f,P,a,b):
    x = np.linspace(a, b, 1000)
    erreur = np.abs(f(x)-P(x))
    return np.max(erreur)
def etude_fonction(f, df, a, b, nom):
    print("\n")
    print(nom)
    nombres_points = [3, 5, 7, 9]
    for nombre in nombres_points:
        x_points = np.linspace(a, b, nombre)
        y_points = f(x_points)
        dy_points = df(x_points)
        P_lagrange = lambda x: lagrange(
            x_points, y_points, x )
        
        P_newton = lambda x: newton( x_points, y_points, x )
        P_hermite = lambda x: hermite( x_points, y_points, dy_points, x)

        erreur_lagrange = erreur_max( f, P_lagrange, a, b )
        erreur_newton = erreur_max( f, P_newton, a, b )
        erreur_hermite = erreur_max( f, P_hermite, a, b )
        
        print("\nnombre de points:", nombre)
        print( "erreur Lagrange:", erreur_lagrange )
        print( "erreur Newton:", erreur_newton )
        print( "erreur Hermite:", erreur_hermite )

        # Graphique
        x = np.linspace(a, b, 500)
        plt.figure()
        plt.plot( x,f(x),label="fonction originale" )
        plt.plot( x,P_lagrange(x),"--", label="lagrange")
        plt.plot(x,P_newton(x),":",label="newton" )
        plt.plot(x,P_hermite(x),"-.",label="hermite")
        plt.scatter(x_points,y_points,label="points" )
        plt.title( nom + " - " + str(nombre) + " points" )
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.legend()
        plt.grid()
        plt.show()
print("Interpolation polinomial")
etude_fonction(f1,df1,-1,1,"f(x) = x^2")
etude_fonction(f2,df2,-1,1,"f(x) = 1 / (1 + 25x^2)")
