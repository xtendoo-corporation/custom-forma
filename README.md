# **CUSTOM-FORMA**

Repositorio de módulos personalizados para el cliente Forma.

## Módulos

### forma_document_format

**Versión:** 19.0.1.0.6
**Autor:** Guillermo Bárcena López
**Website:** https://www.xtendoo.es

Módulo para personalizar el formato base de los documentos de Forma.

**Características:**
- Personalización del formato de facturas
- Diseño de layout personalizado con cabecera tipo folder
- Modificación de campos de pago en facturas
- Mostrar cuentas bancarias de la compañía

**Dependencias:**
- base
- account

**Instalación:**
```bash
# Actualizar lista de aplicaciones desde Odoo
# Buscar "Forma Document Format" e instalar
```

## Notas de desarrollo

- **Rama principal:** 19.0
- **Licencia:** AGPL-3

## Historial de cambios

### 2026-01-15 (v19.0.1.0.6)
- Simplificado el layout_inherit.xml: mantenida la herencia pero sin aplicar cambios por ahora
- Layout preparado para futuras personalizaciones cuando sean necesarias

### 2026-01-15 (v19.0.1.0.5)
- Agregada condición para mostrar "Forma de pago" solo cuando está configurada

### 2026-01-15 (v19.0.1.0.4)
- Renombrado el módulo `document_format` a `forma_document_format` para mejor identificación y evitar conflictos

## Autor

Xtendoo - https://www.xtendoo.es

