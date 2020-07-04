import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(external_stylesheets=[dbc.themes.LITERA])
jumbotron = dbc.Jumbotron(
    [
        dbc.Container(
            [
                html.H1("Exercise Project", className="display-3"),
                html.P(
                    "Coming soon",
                    className="lead",
                ),
                html.P(
                    "",
                    className="lead",
                ),
                html.P(
                    html.A(
                        "Learn More",
                        className="btn btn-primary btn-lg",
                        href="#link_input",
                        role="button",
                    ),
                    className="lead",
                )
            ],
            fluid=True,
            
        )
    ],
    fluid=True,
    #style=JUMBOTRON_STYLE,
    #style={'background': 'url(https://pixabay.com/get/51e3d4464a54b108feda8460da2932771637d8e65b5171_1920.jpg)'}
)

link_input = dbc.FormGroup(
    dbc.Container(
        [
        dbc.Label("Enter a link and press submit",),
        dbc.Input( type="text", bs_size="lg",className="form-control form-control-lg", placeholder="your link",id="inputLarge"),
        dbc.FormText(""),
        html.Button('Submit', id='submit-val',className='btn btn-info',type="submit"),
        
        dbc.Container(
            dbc.Container(
                dbc.Input(type="file", className="custom-file-input", id="inputGroupFile02"),
                dbc.Label(className="custom-file-label", "Choose File")
            ),
            className="custom-file",
            dbc.Container(
                dbc.Span(
                    "Upload"
                ),
                className = "input-group-text",
                id = "",
            ),
            className="input-group-append"
        ),
    ]
)


#imagee = html.Div(
#    html.Img(src=app.get_asset_url('img1.jpg'), style={'height':'10%', 'width':'45%','margin' : '3%'})
#)
app.layout = html.Div([dcc.Location(id="url"), jumbotron, link_input])

if __name__ == "__main__":
    app.run_server()
ß