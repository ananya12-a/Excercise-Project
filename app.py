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
        dbc.Label("Enter a link and press submit", className= "col-form-label col-form-label-lg", ),
        dbc.Row(
            [
                html.Div(
                    [
                        dbc.Input(placeholder="Your link", type="text", bs_size="lg"),
                        dbc.FormText(""),
                    ]
                ),
                html.Div(
                    [
                        html.Button('Submit', id='submit-val',className='btn btn-info',type="submit"),
                    ]
                ),
            ]
        )
        
        ]
    ),
    id="link_input"
)

file_input = html.Div(
    html.Div(
        [
            html.Div(
                [dbc.Input(type="file", className = "custom-file-input", id = "inputGroupFile02"),
                dbc.Label("Choose File", className="custom-file-label", html_for="inputGroupFile02")],
                className = "custom-file"
            ),
            html.Span(
                
                    ["Upload",],
                    
                    id=""
                ,className="input-group-text", 
            ),
        ]
    )
    ,className = "form-group",
)

images = html.Div(
    html.Img(src=app.get_asset_url('img1.jpg'), style={'height':'10%', 'width':'45%','margin' : '3%'})
)
app.layout = html.Div([dcc.Location(id="url"), jumbotron, link_input,images,file_input])

if __name__ == "__main__":
    app.run_server()
