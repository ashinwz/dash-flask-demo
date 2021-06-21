"""Plotly Dash HTML layout override."""

html_layout = """
<!DOCTYPE html>
    <html>
        <head>
            {%metas%}
            <title>{%title%}</title>
            {%favicon%}
            {%css%}
        </head>
        <body class="dash-template">
            <header>
              <div class="nav-wrapper">
                <a href="/">
                    <img src="/static/img/logo.png" class="logo" />
                    <h1>Dash-flask-demo</h1>
                  </a>
                <nav>
                    <a href="/logout">
                        Hi, {%title%}&nbsp;&nbsp;logout
                    </a>
                </nav>
                
            </div>
            </header>
            {%app_entry%}
            <footer>
                {%config%}
                {%scripts%}
                {%renderer%}
            </footer>
        </body>
    </html>
"""
