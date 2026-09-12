import numpy as np
import matplotlib.pyplot as plt

def generate_airfoil(naca):
    #All calculationss
    #Chord length 
    c = 1.0

    m = int(naca[0]) / 100
    p = int(naca[1]) / 10
    t = int(naca[2:]) / 100
    #Generate 200 points from leading edge (0) to trailing edge (1)
    x = np.linspace(0, c, 200)
    yc = np.zeros_like(x)
    dyc_dx = np.zeros_like(x)
    if m == 0:
        yc = np.zeros_like(x)
        dyc_dx = np.zeros_like(x)
    else:
        yc = np.zeros_like(x)
        dyc_dx = np.zeros_like(x)

        #Calculate camber line
        for i in range(len(x)):
            if x[i] <= p:
                yc[i] = (m / p**2) * (2 * p * x[i] - x[i]**2)
            else:
                yc[i] = (m / (1 - p)**2) * ((1 - 2 * p)+ 2 * p * x[i] - x[i]**2)
        for i in range(len(x)):
            if x[i] <= p:
                dyc_dx[i] = (2 * m / p**2) * (p - x[i])
            else:
                dyc_dx[i] = (2 * m / (1-p)**2) * (p - x[i])

    theta = np.arctan(dyc_dx)

    #Thickness distribution
    yt = 5*t*(0.2969 * np.sqrt(x)
            -0.1260 * x
            -0.3516 * x**2
            +0.2843 * x**3
            -0.1015 * x**4)
    xu = x - yt * np.sin(theta)
    yu = yc + yt * np.cos(theta)

    xl = x + yt * np.sin(theta)
    yl = yc - yt * np.cos(theta)
    return xu,yu,xl,yl,x,yc

def plot_airfoil(xu,yu,xl,yl,x,yc,naca):
    # Plot the Airfoil
    plt.plot(xu, yu, label = "Upper Surface")
    plt.plot(xl, yl, label = "Lower Surface")
    plt.plot(x, yc, '--', color='black' , label = 'Camber line')        
    plt.title(f"NACA {naca} Airfoil")
    plt.xlabel("Chord Position")
    plt.ylabel("Vertical Position")
    plt.axis("equal")
    plt.grid(True)
    plt.legend()
    filename = f"NACA{naca}_airfoil.png"
    plt.savefig(filename)

    plt.show()

def export_csv(xu,yu,xl,yl,naca):
    filename = f"NACA{naca}_coordinates.csv"
    with open(filename , "w") as file:
        file.write("Upper X, Upper Y, Lower X, Lower Y\n")
        for i in range (len(xu)):
            file.write(f"{xu[i]},{yu[i]},{xl[i]},{yl[i]}\n")

def main():
    naca = input("Enter NACA 4 digit code: ")

    while len(naca) != 4 or not naca.isdigit():
        print("Invalid NACA code. Please enter exactly 4 digits.")
        naca = input("Enter NACA 4 digit code:")

    xu,yu,xl,yl,x,yc = generate_airfoil(naca)
    export_csv(xu,yu,xl,yl,naca)
    plot_airfoil(xu,yu,xl,yl,x,yc,naca)

main()
