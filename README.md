MANUAL TECNICO:
https://docs.google.com/document/d/1wRlIfKXUIfM3_aOxIpX07rx6rIwu5A9ilTJBhEeXpS0/edit?usp=sharing


---INSTALAR EL PROYECTO---
Clonar el repositorio 
dentro del repositorio ejecutar
py -m venv venv
pip install -r requirements.txt
crear un archivo .env basado en el envexample


---CREAR UNA MIGRACION---
prisma migrate dev --name nombre de la migracion

---MIGRAR LA BASE DE DATOS--
prisma migrate deploy

---VER EL ESTATUS DE LAS MIGRACIONES--
prisma migrate status

---GENERAR EL CLIENTE DE PRISMA---
prisma generate


---EJECUTAR EL PROYECTO---
uvicorn main:app --reload

---VISUALIZAR API---
Ingresar a localhost:8000


sucursal.
Busqueda para