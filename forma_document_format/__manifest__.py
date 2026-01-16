{
    "name": "Forma Document Format",
    "category": "Report",
    "version": "19.0.1.0.6",
    'author': 'Guillermo Bárcena López',
    'website': 'https://www.xtendoo.es',
    "depends": [
        "base",
        "account",
        "account_payment_mode",
    ],
    "license": "AGPL-3",
    "application": True,
    "description": """
        Módulo para editar el formato base de los documentos
        """,
    "data": [
        "views/invoice/invoice_document.xml",
    ],

    "installable": True,
}
