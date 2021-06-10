import os
import requests
import time
import config
from flask import request
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_extensions as de
from dash.dependencies import Input, Output, State
import base64

external_stylesheets = [
    "https://use.fontawesome.com/releases/v5.0.7/css/all.css",
    'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css',
    'https://fonts.googleapis.com/css?family=Roboto&display=swap'
]

intro_page_url = "https://assets10.lottiefiles.com/packages/lf20_eprctl58.json"
disclaimer_page_url = "https://assets4.lottiefiles.com/packages/lf20_j6fywzxe.json"
questions_page_url = "https://assets3.lottiefiles.com/packages/lf20_klBrF0.json"
awaiting_results_url = "https://assets7.lottiefiles.com/packages/lf20_y6h1lr1b.json"
evil_animation_url = "https://assets7.lottiefiles.com/packages/lf20_7qcbuqgk.json"
good_animation_url = "https://assets1.lottiefiles.com/packages/lf20_bP7KzP.json"
options = dict(loop=True, autoplay=True, rendererSettings=dict(
    preserveAspectRatio='xMidYMid slice'))

options2 = dict(loop=False, autoplay=True, rendererSettings=dict(
    preserveAspectRatio='xMidYMid slice'))

# external_script = "https://raw.githubusercontent.com/MarwanDebbiche/post-tuto-deployment/master/src/dash/assets/gtag.js"

app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],
    suppress_callback_exceptions=True
)

server = app.server


app.title = 'Cap Attack'

colors = {
    'background': '#111111',
    'text': '#FF0000'
}

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])
image_filename = 'mushroom_spin.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())
home_layout = html.Div(
    [
        html.Div(
            [
                html.Img(
                    src='data:image/png;base64,{}'.format(
                        encoded_image.decode()),
                    style={
                        'height': '500px',
                        'width': '500px',
                    },
                )
            ], style={'textAlign': 'center'}
        ),


        html.H1(
            'MUSHROOM EDIBILLITY',
            style={'textAlign': 'center'}
        ),

        dbc.Nav(
            [
                dbc.NavItem(dbc.NavLink(
                    "Tobby's Site", active=True, href='https://tobbylie.com')),
            ],
            horizontal='center',
        ),

        dbc.Nav(
            [
                dbc.NavItem(dbc.NavLink(
                    "START >>", active=True, href='/intro_page')),
            ],
            horizontal='center',
        ),
    ],
    className="form-review",
)

intro_page = html.Div(
    [
        dbc.Row(
            [
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.Div(de.Lottie(options=options, width="100%",
                                     height="100%", url=intro_page_url)),
                            html.H4(
                                "EXPERIMENTAL classifier of edible/poisonous mushrooms 🍄 via a Neural Network"),
                        ]
                    ),
                    className="w-30",
                    color="primary",
                    outline=True,
                    style={
                        "width": "18rem",
                        "border-radius": "2%",
                        "background": "PowderBlue",
                    },


                ),
            ], justify='center'
        ),
        dbc.Nav(
            [
                dbc.NavItem(dbc.NavLink(
                            "NEXT >>", active=True, href='/disclaimer_page')),
            ],
            horizontal='center',
        ),
        dbc.Nav(
            [
                dbc.NavItem(dbc.NavLink(
                            "<< BACK", active=True, href='/')),
            ],
            horizontal='center',
        ),
    ], style={"margin-top": "50px"}

)

disclaimer_page = html.Div(
    [
        dbc.Row(
            [
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.Div(de.Lottie(options=options, width="50%",
                                     height="50%", url=disclaimer_page_url)),
                            html.H4(
                                "DISCLAIMER: This model is EXPERIMENTAL! Do NOT consume anything solely based on it's results."),
                            dbc.Nav(
                                [
                                    dbc.NavItem(dbc.NavLink(
                                        "NEXT >>", active=True, href='/questions')),
                                ],
                                horizontal='center',
                            ),

                            dbc.Nav(
                                [
                                    dbc.NavItem(dbc.NavLink(
                                        "<< BACK", active=True, href='/intro_page')),
                                ],
                                horizontal='center',
                            ),
                        ]
                    ),
                    className="w-30",
                    color="primary",
                    outline=True,
                    style={
                        "width": "18rem",
                        "border-radius": "2%",
                        "background": "PowderBlue",
                    },


                ),
            ], justify='center'
        ),

    ], style={"margin-top": "50px"}
)

questions = html.Div(
    [
        html.Div(de.Lottie(options=options, width="25%",
                           height="25%", url=questions_page_url)),
        dbc.Row(
            dbc.Card(
                dbc.CardBody(
                    [

                        dbc.FormGroup(
                            [
                                dbc.Label("Cap Shape"),
                                dbc.RadioItems(
                                    options=[
                                        {"label": "Bell (b)", "value": 'b'},
                                        {"label": "Conical (c)", "value": 'c'},
                                        {"label": "Convex (x)", "value": 'x'},
                                        {"label": "Flat (f)", "value": 'f'},
                                        {"label": "Knobbed (k)", "value": 'k'},
                                        {"label": "Sunken (s)", "value": 's'},
                                    ],
                                    value=1,
                                    id="capshape-input",
                                ),
                            ]
                        ),

                        dbc.FormGroup(
                            [
                                dbc.Label("Cap Surface"),
                                dbc.RadioItems(
                                    options=[
                                        {"label": "Fibrous (f)", "value": 'f'},
                                        {"label": "Grooves (g)", "value": 'g'},
                                        {"label": "Scaly (y)", "value": 'y'},
                                        {"label": "Smooth (s)", "value": 's'},
                                    ],
                                    value=1,
                                    id="capsurface-input",
                                ),
                            ],
                        ),

                        dbc.FormGroup(
                            [
                                dbc.Label("Cap Color"),
                                dbc.RadioItems(
                                    options=[
                                        {"label": "Brown (n)", "value": 'n'},
                                        {"label": "Buff (b)", "value": 'b'},
                                        {"label": "Cinnamon (c)",
                                         "value": 'c'},
                                        {"label": "Gray (g)", "value": 'g'},
                                        {"label": "green (g)", "value": 'r'},
                                        {"label": "Pink (p)", "value": 'p'},
                                        {"label": "Purple (u)", "value": 'u'},
                                        {"label": "Red (e)", "value": 'e'},
                                        {"label": "White (w)", "value": 'w'},
                                        {"label": "Yellow (y)", "value": 'y'},
                                    ],
                                    value=1,
                                    id="capcolor-input",
                                ),
                            ],
                        ),

                        dbc.FormGroup(
                            [
                                dbc.Label("Bruises"),
                                dbc.RadioItems(
                                    options=[
                                        {"label": "Yes (t)", "value": 't'},
                                        {"label": "No (f)", "value": 'f'},
                                    ],
                                    value=1,
                                    id="bruises-input",
                                ),
                            ],
                        ),

                        dbc.FormGroup(
                            [
                                dbc.Label("Odor"),
                                dbc.RadioItems(
                                    options=[
                                        {"label": "Almond (a)", "value": 'a'},
                                        {"label": "Anise (l)", "value": 'l'},
                                        {"label": "Creosote (c)",
                                         "value": 'c'},
                                        {"label": "Fishy (y)", "value": 'y'},
                                        {"label": "Foul (f)", "value": 'f'},
                                        {"label": "Musty (m)", "value": 'm'},
                                        {"label": "None (n)", "value": 'n'},
                                        {"label": "Pungent (p)", "value": 'p'},
                                        {"label": "Spicy (s)", "value": 's'},
                                    ],
                                    value=1,
                                    id="odor-input",
                                ),
                            ],
                        ),

                        dbc.FormGroup(
                            [
                                dbc.Label("Gill Attachment"),
                                dbc.RadioItems(
                                    options=[
                                        {"label": "Attached (a)",
                                         "value": 'a'},
                                        {"label": "Free (f)", "value": 'f'},
                                    ],
                                    value=1,
                                    id="gillattachment-input",
                                ),
                            ],
                        ),

                        dbc.FormGroup(
                            [
                                dbc.Label("Gill Spacing"),
                                dbc.RadioItems(
                                    options=[
                                        {"label": "Close (c)", "value": 'c'},
                                        {"label": "Crowded (w)", "value": 'w'},
                                    ],
                                    value=1,
                                    id="gillspacing-input",
                                ),
                            ],
                        ),

                        dbc.FormGroup(
                            [
                                dbc.Label("Gill Size"),
                                dbc.RadioItems(
                                    options=[
                                        {"label": "Broad (b)", "value": 'b'},
                                        {"label": "Narrow (n)", "value": 'n'},
                                    ],
                                    value=1,
                                    id="gillsize-input",
                                ),
                            ],
                        ),

                        dbc.FormGroup(
                            [
                                dbc.Label("Gill Color"),
                                dbc.RadioItems(
                                    options=[
                                        {"label": "Black (k)", "value": 'k'},
                                        {"label": "Brown (n)", "value": 'n'},
                                        {"label": "Buff (b)", "value": 'b'},
                                        {"label": "Chocolate (h)",
                                         "value": 'h'},
                                        {"label": "Gray (g)", "value": 'g'},
                                        {"label": "Green (r)", "value": 'r'},
                                        {"label": "Orange (o)", "value": 'o'},
                                        {"label": "Pink (p)", "value": 'p'},
                                        {"label": "Purple (u)", "value": 'u'},
                                        {"label": "Red (e)", "value": 'e'},
                                        {"label": "White (w)", "value": 'w'},
                                        {"label": "Yellow (y)", "value": 'y'},
                                    ],
                                    value=1,
                                    id="gillcolor-input",
                                ),
                            ],
                        ),

                        dbc.FormGroup(
                            [
                                dbc.Label("Stalk Shape"),
                                dbc.RadioItems(
                                    options=[
                                        {"label": "Enlarging (e)",
                                         "value": 'e'},
                                        {"label": "Tapering (t)",
                                         "value": 't'},
                                    ],
                                    value=1,
                                    id="stalkshape-input",
                                ),
                            ],
                        ),

                        dbc.FormGroup(
                            [
                                dbc.Label("Stalk Root"),
                                dbc.RadioItems(
                                    options=[
                                        {"label": "Bulbous (b)", "value": 'b'},
                                        {"label": "Club (c)", "value": 'c'},
                                        {"label": "Equal (e)", "value": 'e'},
                                        {"label": "Rooted (r)", "value": 'r'},
                                        {"label": "Missing (?)", "value": '?'},
                                    ],
                                    value=1,
                                    id="stalkroot-input",
                                ),
                            ],
                        ),

                        dbc.FormGroup(
                            [
                                dbc.Label("Stalk Surface Above Ring"),
                                dbc.RadioItems(
                                    options=[
                                        {"label": "Fibrous (f)", "value": 'f'},
                                        {"label": "Scaly (y)", "value": 'y'},
                                        {"label": "Silky (k)", "value": 'k'},
                                        {"label": "Smooth (s)", "value": 's'},
                                    ],
                                    value=1,
                                    id="stalksurfaceabovering-input",
                                ),
                            ],
                        ),

                        dbc.FormGroup(
                            [
                                dbc.Label("Stalk Surface Below Ring"),
                                dbc.RadioItems(
                                    options=[
                                        {"label": "Fibrous (f)", "value": 'f'},
                                        {"label": "Scaly (y)", "value": 'y'},
                                        {"label": "Silky (k)", "value": 'k'},
                                        {"label": "Smooth (s)", "value": 's'},
                                    ],
                                    value=1,
                                    id="stalksurfacebelowring-input",
                                ),
                            ],
                        ),

                        dbc.FormGroup(
                            [
                                dbc.Label("Stalk Color Above Ring"),
                                dbc.RadioItems(
                                    options=[
                                        {"label": "Brown (n)", "value": 'n'},
                                        {"label": "Buff (b)", "value": 'b'},
                                        {"label": "Cinnamon (c)",
                                         "value": 'c'},
                                        {"label": "Gray (g)", "value": 'g'},
                                        {"label": "Orange (o)", "value": 'o'},
                                        {"label": "Pink (p)", "value": 'p'},
                                        {"label": "Red (e)", "value": 'e'},
                                        {"label": "White (w)", "value": 'w'},
                                        {"label": "Yellow (y)", "value": 'y'},
                                    ],
                                    value=1,
                                    id="stalkcolorabovering-input",
                                ),
                            ],
                        ),

                        dbc.FormGroup(
                            [
                                dbc.Label("Stalk Color Below Ring"),
                                dbc.RadioItems(
                                    options=[
                                        {"label": "Brown (n)", "value": 'n'},
                                        {"label": "Buff (b)", "value": 'b'},
                                        {"label": "Cinnamon (c)",
                                         "value": 'c'},
                                        {"label": "Gray (g)", "value": 'g'},
                                        {"label": "Orange (o)", "value": 'o'},
                                        {"label": "Pink (p)", "value": 'p'},
                                        {"label": "Red (e)", "value": 'e'},
                                        {"label": "White (w)", "value": 'w'},
                                        {"label": "Yellow (y)", "value": 'y'},
                                    ],
                                    value=1,
                                    id="stalkcolorbelowring-input",
                                ),
                            ],
                        ),

                        dbc.FormGroup(
                            [
                                dbc.Label("Veil Color"),
                                dbc.RadioItems(
                                    options=[
                                        {"label": "Brown (n)", "value": 'n'},
                                        {"label": "Orange (o)", "value": 'o'},
                                        {"label": "White (w)", "value": 'w'},
                                        {"label": "Yellow (y)", "value": 'y'},
                                    ],
                                    value=1,
                                    id="veilcolor-input",
                                ),
                            ],
                        ),

                        dbc.FormGroup(
                            [
                                dbc.Label("Ring Number"),
                                dbc.RadioItems(
                                    options=[
                                        {"label": "None (n)", "value": 'n'},
                                        {"label": "One (o)", "value": 'o'},
                                        {"label": "Two (t)", "value": 't'},
                                    ],
                                    value=1,
                                    id="ringnumber-input",
                                ),
                            ],
                        ),

                        dbc.FormGroup(
                            [
                                dbc.Label("Ring Type"),
                                dbc.RadioItems(
                                    options=[
                                        {"label": "Evanescent (e)",
                                         "value": 'e'},
                                        {"label": "Flaring (f)", "value": 'f'},
                                        {"label": "Large (l)", "value": 'l'},
                                        {"label": "None (n)", "value": 'n'},
                                        {"label": "Pendant (p)", "value": 'p'},
                                    ],
                                    value=1,
                                    id="ringtype-input",
                                ),
                            ],
                        ),

                        dbc.FormGroup(
                            [
                                dbc.Label("Spore Print Color"),
                                dbc.RadioItems(
                                    options=[
                                        {"label": "Black (k)", "value": 'k'},
                                        {"label": "Brown (n)", "value": 'n'},
                                        {"label": "Buff (b)", "value": 'b'},
                                        {"label": "Chocolate (h)",
                                         "value": 'h'},
                                        {"label": "Green (r)", "value": 'r'},
                                        {"label": "Orange (o)", "value": 'o'},
                                        {"label": "Purple (u)", "value": 'u'},
                                        {"label": "White (w)", "value": 'w'},
                                        {"label": "Yellow (y)", "value": 'y'},
                                    ],
                                    value=1,
                                    id="sporeprintcolor-input",
                                ),
                            ],
                        ),

                        dbc.FormGroup(
                            [
                                dbc.Label("Population"),
                                dbc.RadioItems(
                                    options=[
                                        {"label": "Abundant (a)",
                                         "value": 'a'},
                                        {"label": "Clustered (c)",
                                         "value": 'c'},
                                        {"label": "Numerous (n)",
                                         "value": 'n'},
                                        {"label": "Scattered (s)",
                                         "value": 's'},
                                        {"label": "Several (v)", "value": 'v'},
                                        {"label": "Solitary (y)",
                                         "value": 'y'},
                                    ],
                                    value=1,
                                    id="population-input",
                                ),
                            ],
                        ),

                        dbc.FormGroup(
                            [
                                dbc.Label("Habitat"),
                                dbc.RadioItems(
                                    options=[
                                        {"label": "Grasses (g)", "value": 'g'},
                                        {"label": "Leaves (l)", "value": 'l'},
                                        {"label": "Meadows (m)", "value": 'm'},
                                        {"label": "Paths (p)", "value": 'p'},
                                        {"label": "Urban (u)", "value": 'u'},
                                        {"label": "Waste (w)", "value": 'w'},
                                        {"label": "Woods (d)", "value": 'd'},
                                    ],
                                    value=1,
                                    id="habitat-input",
                                ),
                            ],
                        ),

                        html.Div(
                            [
                                dbc.Button("SUBMIT", id="submit_link",
                                           className="mr-2", color="primary", outline=True),
                            ],
                        ),

                        html.Div(
                            [
                                dbc.Button(
                                    "RESTART", href='/', className="mr-2", color="primary", outline=True),
                            ],
                        ),


                        dbc.FormGroup(
                            [
                                html.Div(id='submit_button_lottie'),
                                html.H4(id='submit_button_display')
                            ],
                        ),

                    ],
                    style={'margin-left': "100px"}
                ),
                className="w-25",
                color="primary",
                outline=True,
                style={
                    "width": "18rem",
                    "border-radius": "2%",
                    # "background": "PowderBlue",
                },
            ), justify="center"
        ),

    ],
    className="form-review",
    style={"margin-top": "50px"},
)


@ app.callback(
    Output('submit_button_display', 'children'),
    Output('submit_button_lottie', 'children'),
    Input('submit_link', 'n_clicks'),

    [
        State('capshape-input', 'value'),
        State('capsurface-input', 'value'),
        State('capcolor-input', 'value'),
        State('bruises-input', 'value'),
        State('odor-input', 'value'),
        State('gillattachment-input', 'value'),
        State('gillspacing-input', 'value'),
        State('gillsize-input', 'value'),
        State('gillcolor-input', 'value'),
        State('stalkshape-input', 'value'),
        State('stalkroot-input', 'value'),
        State('stalksurfaceabovering-input', 'value'),
        State('stalksurfacebelowring-input', 'value'),
        State('stalkcolorabovering-input', 'value'),
        State('stalkcolorbelowring-input', 'value'),
        State('veilcolor-input', 'value'),
        State('ringnumber-input', 'value'),
        State('ringtype-input', 'value'),
        State('sporeprintcolor-input', 'value'),
        State('population-input', 'value'),
        State('habitat-input', 'value'),
    ]
)
def get_edibility(submit_click_ts, capshape, capsurface, capcolor,
                  bruises, odor, gillatachment, gillsapcing, gillsize,
                  gillcolor, stalkshape, stalkroot, stalksurfaceabovering,
                  stalksurfacebelowring, stalkcolorabovering, stalkcolorbelowring,
                  veilcolor, ringnumber, ringtype, sporeprintcolor, population,
                  habitat):

    print('in callback')
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'submit_link' in changed_id:

        # print(capshape)
        data = {"class": "p", "cap-shape": capshape, "cap-surface": capsurface,
                "cap-color": capcolor, "bruises": bruises, "odor": odor,
                "gill-attachment": gillatachment, "gill-spacing": gillsapcing,
                "gill-size": gillsize, "gill-color": gillcolor, "stalk-shape": stalkshape,
                "stalk-root": stalkroot, "stalk-surface-above-ring": stalksurfaceabovering,
                "stalk-surface-below-ring": stalksurfacebelowring, "stalk-color-above-ring": stalkcolorabovering,
                "stalk-color-below-ring": stalkcolorbelowring, "veil-color": veilcolor, "ring-number": ringnumber,
                "ring-type": ringtype, "spore-print-color": sporeprintcolor, "population": population,
                "habitat": habitat}

        # data = {"data": data}
        print('data')
        print(data)
        # print(f"{config.API_URL}/predict", data=data)
        response = requests.post(
            f"{config.API_URL}/predict", data=data)

        print(response)
        prediction = f"{response.json()}"

        if prediction == 'poisonous':
            msg = f"Our model predicts that this mushroom is {prediction}!"
            lottie_animation = de.Lottie(options=options2, width="100%",
                                         height="100%", url=evil_animation_url)
        elif prediction == 'edible':
            msg = f"Our model predicts that this mushroom is {prediction}!"
            lottie_animation = lottie_animation = de.Lottie(options=options2, width="100%",
                                                            height="100%", url=good_animation_url)
        else:
            msg = 'AWAITING VALID INPUT'
            lottie_animation = de.Lottie(options=options, width="100%",
                                         height="100%", url=awaiting_results_url)

    else:
        msg = 'AWAITING VALID INPUT'
        lottie_animation = de.Lottie(options=options, width="100%",
                                     height="100%", url=awaiting_results_url)
    return msg, lottie_animation


# Update page layout


@ app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/':
        return home_layout
    if pathname == "/questions":
        return questions
    if pathname == "/intro_page":
        return intro_page
    if pathname == "/disclaimer_page":
        return disclaimer_page
    if pathname == "/results":
        return results_page
    else:
        return [
            html.Div(
                [
                    html.Img(
                        src="./assets/404.png",
                        style={
                            "width": "50%"
                        }
                    ),
                ],
                className="form-review"
            ),
            dcc.Link("Go to Home", href="/"),
        ]


if __name__ == '__main__':
    app.run_server(debug=config.DEBUG, host=config.HOST)
    # app.run()
