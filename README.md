<h1 align="center">Welcome to Django Restaurant 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0-blue.svg?cacheSeconds=2592000" />
</p>

> A simple backend API for a restaurant

## Install

```sh
pip install -r requirements.py
```

## Usage

```sh
python manage.py runserver
```

## Author

👤 **Andrea Moguel Krause**

- Github: [@amoguelk](https://github.com/amoguelk)

## Improvements checklist

- [x] Print en cada request del user, usar middleware
- [x] Print del request en algún serializer (en el método `create` o `update`)
  - Modificar `CustomListCreateAPIView`
- [x] Traducciones en inglés y en español (ver doc Django)
- [x] Crear un empty migration para cambiar todos los datos en algún modelo (ej. cambiar el salario)
- [x] Hacer pruebas con un modelo usando [los tests de DRF](https://www.django-rest-framework.org/api-guide/testing/)
  - [x] GET
  - [x] POST
  - [x] DELETE
  - [x] PATCH
  - [x] Probar permisos de usuarios
- [ ] Agregar un template que muestre los objetos del menú
  - [ ] Usar tags
- [ ] Agregar throttling
- [ ] Agregar field para imágenes de productos
  - Integrar en DRF
- [ ] Agregar método en Order para enviar correo al cliente
  - Usa el `CustomListCreateAPIView`
  - El correo va en HTML

## Show your support

Give a ⭐️ if this project helped you!

---

_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
