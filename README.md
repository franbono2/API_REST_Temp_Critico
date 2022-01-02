# API_REST_Temp_Critico
El único requisito es tener instalado docker en la máquina.
Una vez descargado el repositorio abrimos una terminal en la carpeta del repositorio.
Ejecutamos el siguiente comando:
docker-compose up -d --scale=web=3
Este comando realizará el compose del proyecto usando la imagen del docker hub y abrirá 3 réplicas de web.
Si se cambia este número se pueden añadir más replicas.
Para acceder al servidor desde el navegador realizaremos lo siguiente:
docker ps 
Para mostrarnos los contenedores con la imagen de “franbono2/dsc_crit” y el de “mongo”
docker container inspect <CONTAINER ID> | grep -i IPAddress
Nos mostrará la IP del contenedor con la id seleccionada.
Con la IP podremos acceder desde el navegador poniendo lo siguiente en la URL:
http://<IPAddress>:8000/temp/
Esto nos mostrará el listado de todas las temperaturas en la template por defecto del django rest framework.
