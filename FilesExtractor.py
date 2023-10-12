if __name__ == '__main__':
    import os
    import shutil
    from zipfile import ZipFile
    from dotenv import load_dotenv

    load_dotenv()

    directorio = input("Ruta del archivo: ")

    with ZipFile(directorio, 'r') as zipObj:
        # Extract all the contents of zip file in different directory
        directorio = os.path.join(os.path.dirname(directorio), os.path.splitext(os.path.basename(directorio))[0])
        if not os.path.exists(directorio):
            os.makedirs(directorio)
        zipObj.extractall(directorio)

    materia = input("A dónde se van a extraer: "
                    "\n1. Programación 2 TM"
                    "\n2. Programación 2 TV"
                    "\n3. Estructura de Datos TM"
                    "\n4. Estructura de Datos TV"
                    "\nOpción: ")

    if materia == "1":
        carpeta = "Programación 2\\TM"
    elif materia == "2":
        carpeta = "Programación 2\\TV"
    elif materia == "3":
        carpeta = "Estructura de Datos\\TM"
    elif materia == "4":
        carpeta = "Estructura de Datos\\TV"

    print("Extrayendo...")

    subdirectorios = [f.path for f in os.scandir(directorio) if f.is_dir()]
    nuevoDirectorio = os.path.join(os.getenv('MAIN_FILE_DIRECTORY'), carpeta)
    nombreDelDirectorioOriginal = os.path.split(directorio)[1]

    if not os.path.exists(os.path.join(nuevoDirectorio, nombreDelDirectorioOriginal)):
        os.makedirs(os.path.join(nuevoDirectorio, nombreDelDirectorioOriginal))

    for subdirectorio in subdirectorios:
        index = 0
        for file in os.listdir(subdirectorio):
            print("Copiando " + os.path.split(subdirectorio)[1] + "...")
            nombreArchivoNuevo = os.path.basename(subdirectorio).split("_")[0] + " " + os.path.splitext(file)[0]
            extension = os.path.splitext(file)[1]

            if os.path.isfile(os.path.join(nuevoDirectorio+"\\"+nombreDelDirectorioOriginal, nombreArchivoNuevo+extension)):
                nombreArchivoNuevo = nombreArchivoNuevo + "(" + str(index) + ")"

            nombreArchivoNuevo = nombreArchivoNuevo + extension
            newFolder = os.path.join(nuevoDirectorio+"\\"+nombreDelDirectorioOriginal, nombreArchivoNuevo)
            shutil.move(os.path.join(directorio, subdirectorio, file), newFolder)
            #index = index + 1

    shutil.rmtree(directorio)

    print("La copia ha terminado :)")