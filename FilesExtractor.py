if __name__ == '__main__':
    import os
    import shutil
    from zipfile import ZipFile, is_zipfile
    from dotenv import load_dotenv

    load_dotenv()

    directorio = input("Ruta del archivo: ")

    #Extraer todos los archivos
    with ZipFile(directorio, 'r') as zipObj:
        # Extract all the contents of zip file in different directory
        directorio = os.path.join(os.path.dirname(directorio), os.path.splitext(os.path.basename(directorio))[0])
        if not os.path.exists(directorio):
            os.makedirs(directorio)
        zipObj.extractall(directorio)

    materia = input("A dónde se van a extraer: "
                    "\n1. Programación 1 TM"
                    "\n2. Programación 1 TV"
                    "\n3. Programación 3 TM"
                    "\nOpción: ")

    if materia == "1":
        carpeta = "Programación 1 IDS TM"
        tipo = "cpp"
    elif materia == "2":
        carpeta = "Programación 1 IDS TV"
        tipo = "cpp"
    elif materia == "3":
        tipo = "java"
        carpeta = "Programación 3 IDS TM"

    print("Extrayendo...")

    #Ontener los subdirectorios que existen de lo extraído
    subdirectorios = [f.path for f in os.scandir(directorio) if f.is_dir()]
    nuevoDirectorio = os.path.join(os.getenv('MAIN_FILE_DIRECTORY'), carpeta)
    nombreDelDirectorioOriginal = os.path.split(directorio)[1]

    #Si no existe el directorio, crearlo.
    if not os.path.exists(os.path.join(nuevoDirectorio, nombreDelDirectorioOriginal)):
        os.makedirs(os.path.join(nuevoDirectorio, nombreDelDirectorioOriginal))

    #Por cada carpeta descargada se van a copiar los archivos con un nuevo nombre
    for subdirectorio in subdirectorios:
        #El indice es por si se repite el nombre de algún archivo, al final se coloca un (0)(1) etc.
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

            #Si lo que se copió es un archivo zip, se extrae en el directorio que le corresponde.
            if file.endswith('.zip'):
                with ZipFile(newFolder, 'r') as zipObj:
                    # Extract all the contents of zip file in different directory
                    dirSegundoZip = os.path.join(os.path.dirname(newFolder), os.path.splitext(os.path.basename(newFolder))[0])
                    if not os.path.exists(dirSegundoZip):
                        os.makedirs(dirSegundoZip)
                    zipObj.extractall(dirSegundoZip)
                os.remove(newFolder)

    if(tipo == "cpp"):
        shutil.copytree(".vscode", nuevoDirectorio+"\\"+nombreDelDirectorioOriginal+"\\.vscode\\")

    shutil.rmtree(directorio)

    print("La copia ha terminado :)")