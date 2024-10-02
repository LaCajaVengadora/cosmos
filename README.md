# Guía de Configuración del Proyecto "cosmos"

## Versiones
- **Versión de Python**: 3.9.4 (global)
- **Versión de Django**: 4.2.16 (entorno virtual)

Se ha creado un entorno virtual y allí se ha instalado Django.
Más explicitamente, los pasos (que yo, Lolo, hice) fueron:

## Pasos que yo (Lolo) ejecuté:
- Crear dir PROJECT
- Crear entorno virtual con venv (llamado "myenv") y ejecutar `activate`
- En el dir PROJECT crear dir 280924 (ahora en PROJECT están los dirs "myenv" y "280924")
- Ejecutar `>>> pip install Django `(ahora Django está instalado en el entorno virtual pero no en global)
- En el dir 280924 ejecutar `>>> (myenv) django-admin startproject cosmos`
- En el mismo dir ejecutar `>>> (myenv) git init`
- Luego `>>> (myenv) python cosmos/manage.py migrate` (luego se probó `runserver` y funcionó)
- `>>> (myenv) git commit -am "start"; git push`
- `>>> deactivate`
- Y así el proyecto fue guardado en github (ver https://github.com/LaCajaVengadora/cosmos)

## Pasos para editar el proyecto *POR PRIMERA VEZ*:
1. [Instalar python](https://www.python.org/ftp/python/3.12.7/python-3.12.7-amd64.exe) (junto con venv)
2. [Instalar git](https://github.com/git-for-windows/git/releases/download/v2.46.2.windows.1/Git-2.46.2-64-bit.exe)
3. Crear un dir PROJECT y dentro ejecutar `>>> python -m venv myenv`
4. `>>> cd myenv/Scripts; activate; cd ../..`
5. Crear en PROJECT el dir "280924"
6. `(myenv) >>> pip install Django`
7. En el dir 280924 ejecutar `(myenv) >>> git clone https://github.com/LaCajaVengadora/cosmos.git`
8. `(myenv) >>> cd cosmos; git checkout main`
9. Actualizar con `(myenv) >>> git pull origin main`
10. A partir de ahora, hacer todos los cambios que quieran en el proyecto
11. Cuando hayan terminado ejecuten `(myenv) >>> git commit -am "Descripción de los cambios"`
12. Y luego `(myenv) >>> git push origin main`
13. `>>> deactivate` (para desactivar el venv)
Si les da algún error de git, puede que tengan que ejecutar (al menos la primera vez) (uso de ejemplo a Valen)
`>>> git config user.name "Valen_Local"; git config user.email "valucomvaz@gmail.com"`

## *LA PRÓXIMA VEZ* que quieran editar el proyecto, los pasos serían:
1. Activar el venv con `>>>cd PROJECT/280924/myenv/Scripts; activate; cd ../..`
2. En el dir 280924 ejecutar `(myenv) >>> git pull origin main`
3. Hacer todos los cambios que quieran
4. Ejecutar `(myenv) >>> git commit -am "Descripción de los cambios"; git push origin main`
5. Desactivar el venv con `>>> deactivate`
