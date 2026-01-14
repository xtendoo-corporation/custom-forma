{
    "name": "Document format forma",
    "category": "Report",
    "version": "19.0.1.0.4",
    'author': 'Guillermo Bárcena López',
    'website': 'https://www.xtendoo.es',
    "depends": [
        "base",
        "account",
    ],
    "license": "AGPL-3",
    "application": True,
    "description": """
        Modulo para editar el formato base de los documentos
        """,
    "data": [
        "views/invoice/invoice_document.xml",
        "views/layout/layout_inherit.xml",
    ],

    "installable": True,
}
