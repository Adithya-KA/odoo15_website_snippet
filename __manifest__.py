{
    'name': 'Website Snippet',
    'version': '15.0.0.1.0',
    'description': 'Dynamic Snippet in Website',
    'depends': [
        'base', 'website', 'contacts'
    ],
    'assets': {
        'web.assets_frontend': [
            '/website_snippet/static/src/js/dynamic_snippet.js'],
    },

    'data': [
        'views/snippet_view.xml',
        'views/sale_count.xml',
    ],

    'installable': True,
    'application': True

}