0.0.40
Se vuelve a la version 0.0.39 por conflictos en la función "Select browser"
0.0.41
Se agrega linea 125 
options.add_argument("--profile-directory=Temporal")
0.0.42
Se modifica el nombre de la variable de entorno de jenkins para que siempre se tome en minuscula y se corrige browser para que se pueda ejecutar con firefox
0.0.43
Se actualiza funcion **open browser** por conflictos para la ejecucion local 
0.0.44
Se agrega dependencia Andreani-QA-Jmeter
0.0.45
Se realizan varios cambios (ver historial)
0.0.46
Se agrega psutil a las dependencias
0.0.47
Se agrega la linea 472 y se modifica de la linea 234 a la 237
0.0.48
Se agrega carpeta de tests, gitignore y requirements
0.0.49
Se actualiza .init
0.0.50
Se realizan varios cambios (ver historial)
0.0.51
Se agregan logueos por consola
Adhesión de imports url3lib (para manejo de warnings), loggin
Adhesión de las lineas 80 a la 83, para la instanciación del logger y configuración del mismo.
Aplicación del sistema de loggeo en todas las lineas necesarias (ver historial).
Linea 244, se adisiona Selenium.driver.close() para el correcto cierre del mismo.
0.0.52
Actualización con variable de entorno para su ejecución en server y local
Actualiación de lineas para loggeo con la LoggingFeature proveniente de Functions
0.0.53
Se comenta linea 133 y 134 por conflictos con firefox
0.0.54
ver historial (chrome for testing)
0.0.55
ver historial
* 0.0.56
* Se reactivo el debugger. Debugger ahora recibe un diccionario con los pasos realizados y sus capturas. 
* Se eliminaron algunas variables que no se utilizaban o se utilizaban mal.
* Se creo la funcion close browser reemplazando a tear_down en algunos contextos.
* Se realizaron modificaciones menores para que se pueda operar con el framework bajo diferentes contextos, (recorder, script y testing)
* Se elimino el uso de variables de entorno llamadas desde Selenium. 
* Se reemplazo Chromium por ChromeForTesting para el servidor.
0.0.57
Se actualizan options de Chrome para poder realizar descargas desde el modo incognito
0.0.58
* Se vuelve a actualizar options de Chrome
0.0.59
* Se vuelve a actualizar options de Chrome