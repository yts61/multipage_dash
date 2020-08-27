import dash

#external_stylesheets = ['https://codepen.io/lorenzoyeung/pen/zYqxNQg']
#external_stylesheets = ['assets/style.css']
#custom = ['https://codepen.io/lorenzoyeung/pen/LYNNLKJ.css']



app = dash.Dash(__name__,
                #external_stylesheets=external_stylesheets,
                #assets_ignore='.*ignored.*'
                meta_tags=[
                    # A description of the app, used by e.g.
                    # search engines when displaying search results.
                    {
                        'name': 'template, WebApp designed and created by Lorentz Yeung',
                        'content': 'write sth'
                    },
                    # A tag that tells the browser not to scale
                    # desktop widths to fit mobile screens.
                    # Sets the width of the viewport (browser)
                    # to the width of the device, and the zoom level
                    # (initial scale) to 1.
                    #
                    # Necessary for "true" mobile support.
                    {
                      'name': 'viewport',
                      'content': 'width=device-width, initial-scale=1.0'
                    }]
                )
app.config.suppress_callback_exceptions = True
server = app.server
