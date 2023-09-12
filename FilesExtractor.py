if __name__ == '__main__':
    import os
    import shutil
    from zipfile import ZipFile

    directorio = input("Ruta del archivo: ")

    # directorio = r"D:\Descargas\P1IDSTM-Ejercicio 7 - Viaje de autobús-42677.zip"

    with ZipFile(directorio, 'r') as zipObj:
        # Extract all the contents of zip file in different directory
        directorio = os.path.join(os.path.dirname(directorio), os.path.splitext(os.path.basename(directorio))[0])
        if not os.path.exists(directorio):
            os.makedirs(directorio)
        zipObj.extractall(directorio)

    materia = input("A dónde se van a extraer: "
                    "\n1. Programación 1 TM"
                    "\n2. Programación 1 TV"
                    "\nOpción: ")

    if materia == "1":
        carpeta = "Programación 1\\TM"
    elif materia == "2":
        carpeta = "Programación 1\\TV"

    print("Extrayendo...")

    subdirectorios = [f.path for f in os.scandir(directorio) if f.is_dir()]
    nuevoDirectorio = os.path.join("D:\\Escritorio\\2023-I\\", carpeta)
    nombreDelDirectorioOriginal = os.path.split(directorio)[1]

    if not os.path.exists(os.path.join(nuevoDirectorio, nombreDelDirectorioOriginal)):
        os.makedirs(os.path.join(nuevoDirectorio, nombreDelDirectorioOriginal))

    for subdirectorio in subdirectorios:
        index = 0
        for file in os.listdir(subdirectorio):
            print("Copiando " + os.path.split(subdirectorio)[1] + "...")
            nombreArchivoNuevo = os.path.basename(subdirectorio).split("_")[0]

            if os.path.isfile(os.path.join(nuevoDirectorio+"\\"+nombreDelDirectorioOriginal, nombreArchivoNuevo+".cpp")):
                nombreArchivoNuevo = nombreArchivoNuevo + "(" + str(index) + ")"

            nombreArchivoNuevo = nombreArchivoNuevo + ".cpp"
            newFolder = os.path.join(nuevoDirectorio+"\\"+nombreDelDirectorioOriginal, nombreArchivoNuevo)
            shutil.copy(os.path.join(directorio, subdirectorio, file), newFolder)
            index = index + 1

    print("La copia ha terminado :)")