import cv2
import numpy as np
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly
import math
import plotly.graph_objs as go



#print("Enter the link of the video")
#zoom_0 (1).mp4
#link = "ishika2.mp4" #input()
#read_video(link)


def get_avg_points(all_points):
    index = 0
    all_points_avg_new = []
    while (index<len(all_points)):

        ### at point 0 
        counter = index + 1 ## at pt 1 
        end = counter + 3
        next_four = [all_points[index]]
        while (counter<len(all_points) and (counter<=end)): ## grab next 4 frames
            next_four.append(all_points[counter])
            counter+=1
        index += 1  ## skip by 5
        #print((next_four))
        all_points_avg_new.append(get_avg(next_four,6))
    return all_points_avg_new
def get_avg(next_four,number_tapes):
    avg_points = []
    for index in range(number_tapes):
        avg_points.append([0,0])
    #print (avg_points)
    #avg_points = [(0,0),(0,0),(0,0),(0,0)]
    for index in range (len(next_four)):
        frame_points = next_four[index]
        for tape in range(number_tapes):
            avg_points[tape][0]+= (frame_points[tape][0]/(len(next_four)))
            avg_points[tape][1]+= (frame_points[tape][1]/(len(next_four)))
    return avg_points
#print(avg_points)

def find_lowest_in_list(y_points_avg):
    #print(len(y_points_avg))
    lowest = []
    for index in range(len(y_points_avg)):
        lowest.append([])
    #print(lowest)
    for index in range(len(y_points_avg)):
        #print(y_points_avg[index])
        lowest[index] = min(y_points_avg[index])
    return min(lowest)


def get_avg_y(all_points_avg,number_tapes):
    y_points_avg = []
    for index in range(number_tapes):
        y_points_avg.append([])
    #print(y_points_avg)
    for index in range(len(all_points_avg)):
        frame_points = all_points_avg[index]
        for tape in range(number_tapes):
            y_points_avg[tape].append((frame_points[tape][1]*-1))
    lowest_avg = find_lowest_in_list(y_points_avg)
    #print (lowest_avg)
    #for index in range(len(all_points_avg)):
        #for tape in range(number_tapes):
            #y_points[tape][index]-=lowest_avg
    for tape in range(number_tapes):
        for index in range(len(all_points_avg)):
            y_points_avg[tape][index]=y_points_avg[tape][index] - lowest_avg
    return y_points_avg


#print(y_points_avg)
def find_dist(tape1,tape2):
    return (((tape1[0]-tape2[0])**2+(tape1[1]-tape2[1])**2)**0.5)
def find_angles(all_points_avg):
    angles_avg = []
    perf_avg = {"Good": 0, "Acceptable": 0, "Bad": 0}
    for point in all_points_avg:
        tape3 = point[2]
        tape2 = point[1]
        tape1 = point[0]
        # dist bw 6 and 4, 6 and 5, 4 and 5 
        dist_a = find_dist(tape2,tape3) ## mid->lowest
        dist_b = find_dist(tape1,tape2) ## highest->mid
        dist_c = find_dist(tape1,tape3) ## highest->lowest
        cos_c = (dist_c**2 - dist_a**2 -dist_b**2)/(-2*dist_a*dist_b)
        c = math.acos(cos_c)
        c_deg = (c * 180 /math.pi) -90
        if (c_deg>=0):
            angles_avg.append(c_deg)
            if (c_deg >=50):
                perf_avg["Good"]+=1
            elif (c_deg >=20):
                perf_avg["Acceptable"]+=1
            else:
                perf_avg["Bad"]+=1
    return angles_avg, perf_avg

def find_range(angles_avg):
    return (round(max(angles_avg)-min(angles_avg),2))
#print (find_range(angles_avg))
def find_avg_angle(angles_avg):
    sum=0
    for angle in angles_avg:
        sum+=angle
    return (round(sum/len(angles_avg),2))
#print (perf_avg)
##plot pie chart
##5 frame average for angle
#fig.show
def make_pie(perf_avg):
    trace = go.Pie(labels = ['Good','Acceptable','Bad'], values = [perf_avg['Good'],perf_avg['Acceptable'],perf_avg['Bad'],])
    data = [trace]
    fig1 = go.Figure(data = data)
    #fig1.show()
    return fig1

def draw_graph_y(y_points_avg,num_tapes):
    fig = go.Figure()
    for index in range(num_tapes):
        fig.add_trace(go.Scatter(y=y_points_avg[index],
                        mode='lines+markers',
                        name= 'tape ' + str(index+1)))
    return fig


def draw_graph_angles(angles_avg):
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=angles_avg,
                    mode='lines+markers',
                    name='angles'))
    return fig





def read_video_red(link):
    cap = cv2.VideoCapture(link)
    fps = cap.get(cv2.CAP_PROP_FPS)
    print ("read")
    all_points = []
    drawn_frame_list = []
    width = 0
    height = 0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            color = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            lower_red = np.array([169, 100, 100]) #[161, 155, 84]
            upper_red = np.array([189, 255, 255]) #[179, 255, 255]
            mask = cv2.inRange(color, lower_red, upper_red)
            res = cv2.bitwise_and(frame,frame, mask= mask)
            height = frame.shape[0]
            width = frame.shape[1]
            #cv2.imshow('frame', mask)
            drawn_frame= get_contours(res, frame, all_points)
            drawn_frame_list.append(drawn_frame)
            """LUV = cv2.cvtColor(res, cv2.COLOR_BGR2LUV)
            edges = cv2.Canny(LUV, 10, 100)
            contours, hierarchy = cv2.findContours(edges,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            print("Number of Contours is: " + str(len(contours)))
            print(contours)"""
            #cv2.imshow('Contours', image)
            #cv2.waitKey(0)
            # & 0xFF is required for a 64-bit system
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    out = cv2.VideoWriter("assets/result.mp4",cv2.VideoWriter_fourcc(*'X264'), fps, (width,height))
    for i in range(len(drawn_frame_list)):
        # writing to a image array
        out.write(drawn_frame_list[i])
    out.release()
    print("Read video function called for " + str(link))
    number_tapes = 6
    all_points_avg = get_avg_points(all_points)
    y_points_avg = get_avg_y(all_points_avg,number_tapes)
    angles_avg, perf_avg = find_angles(all_points_avg)
    fig = make_pie(perf_avg)
    fig1 = draw_graph_y(y_points_avg,6)
    fig2 = draw_graph_angles(angles_avg)
    #fig.show()
    cv2.destroyAllWindows()
    return (all_points, fig, fig1, fig2, str(find_range(angles_avg)) + u"\N{DEGREE SIGN}", str(find_avg_angle(angles_avg)) + u"\N{DEGREE SIGN}", str(round(min(angles_avg),2)) + u"\N{DEGREE SIGN}")  
    





def get_contours(mask, frame, all_points):
    LUV = cv2.cvtColor(mask, cv2.COLOR_BGR2LUV)
    edges = cv2.Canny(LUV, 10, 100)
    contours, hierarchy = cv2.findContours(edges,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    #print("Number of Contours is: " + str(len(contours)))
    contours_final = []
    for contour in contours:
        x_left, y_up, width, height= cv2.boundingRect(contour)
        if ((width*height)>20):
            contours_final.append(contour)
            x_left, y_up, width, height= cv2.boundingRect(contour)
            #print("Area", width*height)
    #print(contours)
    #print("Number of Contours is: " + str(len(contours_final)))
    useful_points = [ ]
    if (len(contours_final)==6):
        for contour in contours_final:
            #print("Bounding Rect", cv2.boundingRect(contour))
            x_left, y_up, width, height= cv2.boundingRect(contour)
            ## find midpoint 
            ### useful_points.append(mid_point)
            #print("Area: ", width*height)
            cv2.rectangle(frame,(x_left, y_up), (x_left + width, y_up+height), (0,0,255), 3)
            x_mid = int(x_left+(width/2))
            y_mid = int(y_up+(height/2))
            cv2.circle(frame, (x_mid, y_mid),9,(0,255,0),12)
            useful_points.append((x_left+(width/2),y_up+(height/2)))
        """for contour in contours_final:
            x_left, y_up, width, height= cv2.boundingRect(contour)
        """ 
    if (len(useful_points)==6):
        all_points.append(useful_points) 
    if (len(useful_points)==2):
        #all_points.append(useful_points) 

        cv2.line(frame, (int(useful_points[0][0]),int(useful_points[0][1])), (int(useful_points[1][0]),int(useful_points[1][1])), (255,255,255),4)
    #cv2.imshow('Found Red', frame)
    return frame

#def get_cordinates()

#cvtColor()

#video1: IMG_4229.mov
#video2: IMG_4230.mov
#video3: IMG_4231.mov


"""all_points, fig = read_video_red(link)
all_points_avg = get_avg_points(all_points)
y_points_avg = get_avg_y(all_points_avg,6)
angles_avg, perf_avg = find_angles(all_points_avg)
#fig = make_pie(perf_avg)
fig1 = draw_graph_y(y_points_avg,6)
fig2 = draw_graph_angles(angles_avg)"""

#figure = dcc.Graph(id="piechart")
#figure1 = dcc.Graph(id="yvalues")
figure2 = dcc.Graph(id="angles")

cardfig = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Angles", className="card-title"),
            html.Div(id = "piechart",children=[]
            )
            
        ]
    )
)
cardfig1 = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Y", className="card-title"),
            html.Div(id = "yvalues",children=[])
        ]
    ),className="my-4"
)
cardfig2 = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Angles", className="card-title"),
            html.Div(id = "angles",children=[])
        ]
    ),className="my-4"
)



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
                        href="#card",
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
)

link_input = dbc.FormGroup(
        [
        html.H4("Enter a link and press submit", className= "card-title mx-1", ),
        dbc.Row(
            [
                html.Div(
                    [
                        dbc.Input(placeholder="Your link", type="text", bs_size="lg", id="link", className="my-2 mx-3"),
                    ]
                ),
                html.Div(
                    [
                        html.Button('Submit', className='btn btn-info mx-3', id='submitbtn', n_clicks = 0),
                    ]
                ),
            ]
        )
        
        ],
)
file_input = html.Div(
    html.Div(
        [
            html.Div(
                [dbc.Input(type="file", className = "custom-file-input", id = "inputGroupFile02"),
                dbc.Label("Choose File", className="custom-file-label", html_for="inputGroupFile02")],
                className = "custom-file mb-4"
            ),
            dbc.Button("Submit", color="primary", className="mr-1", id='submitbtn', n_clicks = 0),
        ]
    )
    ,className = "form-group", id="file_input"
)
popup = dbc.Modal(
            [
                dbc.ModalHeader("Header"),
                dbc.ModalBody("This is the content of the modal"),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close", className="ml-auto")
                ),
            ],
            id="modal",
        ),
fnameDict = {'Cardio': ['Walking', 'Running', 'Jogging'], 'Lower Body': ['High Knee', 'Squat', 'Lunge']}

names = list(fnameDict.keys())
nestedOptions = fnameDict[names[0]]

dropdown_set = html.Div(
    [
        html.H4("Select type of exercise", className="card-title"),
        dcc.Dropdown(
            id='name-dropdown',
            options=[{'label':name, 'value':name} for name in names],
            value = list(fnameDict.keys())[0],className = 'mb-4'
            ),
        html.H4("Select exercise", className="card-title"),
        dcc.Dropdown(
            id='opt-dropdown',className = 'mb-4'
            ),

    ]
)

card = dbc.Card(
    dbc.CardBody(
        [
            
            dropdown_set,
            link_input,
        ]
    )
)



stat_range = dbc.Card(
                    [
                        html.H4("Range of angles:", className="card-title ml-2 mt-2"),
                        html.H4(children = [], className="card-title ml-2", id="rangestat"),
                    ]
                )

stat_avg_ang = dbc.Card(
                    [
                        html.H4("Average angle:", className="card-title ml-2 mt-2"),
                        html.H4(children=[], className="card-title ml-2", id="avgstat"),
                    ]
                )
stat_smallest_ang = dbc.Card(
                    [
                        html.H4("Smallest angle:", className="card-title ml-2 mt-2"),
                        html.H4(children=[], className="card-title ml-2", id="smalleststat"),
                    ]
                )

row_stats = dbc.Row(
    [
        dbc.Col(stat_range,width=4),
        dbc.Col(stat_avg_ang,width=4),
        dbc.Col(stat_smallest_ang,width=4)
        
    ], className = "mb-4"
)

row = dbc.Row(
    [
        dbc.Col(card,width=3),
        dbc.Col(
            [
                row_stats, cardfig
            ]
        ),
    ]
)


images = html.Div(
    html.Img(src=app.get_asset_url('img1.jpg'), style={'height':'10%', 'width':'45%','margin' : '3%'})
)

video = html.Center (
    html.Video(id="resultvid", src="assets/result.mp4",controls=True) 
)



modal = html.Div(
    [
        dbc.Button("Open modal", id="open"),
        dbc.Modal(
            [
                dbc.ModalHeader("Guidelines"),
                dbc.ModalBody(),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close", className="mx-5", style="display:none")
                ),
            ],
            id="modal",
        ),
    ]
)




app.layout = html.Div([dcc.Location(id="url"), jumbotron, html.Div([row, cardfig1,cardfig2,modal,video],className="mx-5")])

@app.callback(
    dash.dependencies.Output('opt-dropdown', 'options'),
    [dash.dependencies.Input('name-dropdown', 'value')]
)
def update_date_dropdown(name):
    return [{'label': i, 'value': i} for i in fnameDict[name]]



@app.callback(
    [Output('piechart', 'children'),Output('yvalues', 'children'),Output('angles', 'children'), Output('resultvid', 'src'),Output('rangestat', 'children'),Output('avgstat', 'children'),Output('smalleststat', 'children')], ##add video as output and return same thing + graph call backs + stats call backs
    [Input('submitbtn', 'n_clicks')], 
    [State('opt-dropdown', 'value'),  State('link', 'value'), State('resultvid', 'src')], 
)
def analyze_video(n,exercise, link, src):
    print("click")
    print(link)
    print(n)
    if (link!=None):
        all_points, fig, fig1, fig2, anglerange, angleavg, smallestang = read_video_red(link)
        #fig.show()
        ##update result video
        #return fig
        figure = dcc.Graph(figure=fig)
        figure1 = dcc.Graph(figure=fig1)
        figure2 = dcc.Graph(figure=fig2)
        html.Video(id="resultvid", src="assets/result.mp4",controls=True) 
        return figure, figure1, figure2, src, anglerange, angleavg, smallestang
    else:
        print ("prevent update called")
        return dash.no_update
    



@app.callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open





if __name__ == "__main__":
    app.run_server(debug=False)

#video upload
#return stats in functions
