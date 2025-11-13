{
    'name': 'Inventory Access for Sales Users',
    'version': '1.0',
    'category': 'Inventory',
    'summary': 'Allow Sales users with Own Documents Only to access inventory reporting',
    'description': """
        This module allows users with 'Sales / User: Own Documents Only' role to:
        - Access the menu Inventory → Reporting → Stock
        - View stock data (quantities, moves, etc.) in read-only mode
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['sale', 'stock'],
    'data': [
        'views/stock_menu_views.xml',
        'views/stock_readonly_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
