# lee_naca.py
# este programa, abre un archivo externo generado por otros medios
# donde la invormacion contenida representa para cada angulo d eincidencia
# caracteristicas aerodinamicas de un perfil NACA
# se filtran del archivo las lineas que comuenzan con el simbolo/
# posteriormente se almacenan dichos datos en listas y se los grafica

import matplotlib.pyplot as plt

f = open("NACA2412.txt", 'r')  # el archivo debe estar en la misma carpeta que el programa
alfa = []  # armo listas vacias para llenar las caracct. aerod.
cl = []
cd = []
cdp = []
cm = []
top = []
bot = []
for linea in f.readlines():  # este for desgrana una a una la lista de lineas que lee readlines
    if not linea.find("/") == 0:  # me fijo si empieza con /
        # print linea
        dumm = linea.split("  ")  # separo la linea en una lista de nombre dumm buscando las ocurrencias de "  "
        print
        "-", dumm[0], "-", float(dumm[1])
        alfa.append(float(dumm[1]))  # lleno las listas previamente definidas vacias mediante append
        cl.append(float(dumm[2]))
        cd.append(float(dumm[3]))
        cdp.append(float(dumm[4]))
        cm.append(float(dumm[5]))
        top.append(float(dumm[6]))
        bot.append(float(dumm[7]))
f.close()  # cierro el archivo

# grafico

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(alfa, cl, color='lightblue', linewidth=1)
ax.plot(alfa, cd, color='red', linewidth=1)
ax.plot(alfa, cm, color='green', linewidth=1)

plt.show()
