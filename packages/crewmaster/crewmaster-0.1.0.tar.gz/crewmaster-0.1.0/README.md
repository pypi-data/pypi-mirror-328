# Crewmaster

## Instalar dependencias

1. Activar entorno virtual
```
poetry env use python
```
2. Instalar
```
poetry install
```

## Ejecutar los test 

1. Ejecutar todos los test
```
poetry run pytest
```

2. Se puede utilizar pytest para hacer los tests:
```
poetry run pytest ./ruta/a/probar --capture=no
```

3. Pytest no ofrece un modo "watch".  Si quiere utilizar un modo watch debes  ejecutar:
```
poetry run ptw ./ruta/a/monitorear ./ruta/a/probar --capture=no
```

4. Si se quiere probar sólo algún test, se puede agregar la marca `@pytest.mark.mi_marca` y luego ejecutar con el parámetro -k=mi_marca.

```
# test.py
@pytest.mark.mi_marca
def test_check...

# console
poetry run ptw ./ruta/a/monitorear ./ruta/a/probar --capture=no -k=mi_marca
```

## Publicar libreria

1. Crear cuenta en pypi
2. Crear credenciales
3. Ir a "Configurar cuenta"
3. Dar scroll hasta "Anadir una ficha api" y crear token(si es necesario)
4. Agregar token a poetry
```
poetry config pypi-token.pypi your-api-token
```
5. Construir el paquete
```
poetry build
```
6. Publicar el paquete
```
poetry publish
```

* Tambien puedes crear y publicar el paquete en un solo paso
```
poetry publish --build
```