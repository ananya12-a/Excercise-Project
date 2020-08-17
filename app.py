import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly
import math
import plotly.graph_objs as go
import os
from flask import Flask, Response

all_points = [[(439.5, 93.0), (431.5, 91.0), (437.5, 36.0), (425.0, 33.0), (421.0, 27.5), (434.5, 33.5)], [(449.5, 454.5), (424.5, 324.5), (350.0, 145.0), (362.5, 139.5), (370.5, 91.5), (358.0, 89.5)], [(349.0, 444.5), (344.5, 442.0), (343.5, 435.0), (347.0, 322.5), (352.5, 322.0), (323.0, 154.5)], [(332.5, 431.0), (341.5, 318.0), (303.5, 171.0), (315.0, 168.0), (307.0, 23.0), (318.0, 19.5)], [(331.0, 430.5), (327.5, 424.0), (343.0, 319.5), (338.0, 317.0), (301.5, 170.0), (311.0, 167.0)], [(300.0, 476.5), (311.0, 470.5), (294.0, 169.0), (304.5, 167.0), (310.5, 128.5), (302.0, 125.0)], [(310.5, 472.5), (293.0, 170.0), (304.0, 169.0), (311.0, 128.5), (301.5, 125.0), (309.0, 21.5)], [(311.0, 472.5), (304.0, 166.0), (310.0, 128.0), (298.5, 121.5), (301.0, 25.5), (308.0, 22.5)], [(303.5, 478.0), (314.0, 471.5), (325.5, 322.5), (302.0, 170.0), (294.0, 170.5), (306.0, 131.0)], [(304.0, 477.5), (312.5, 472.0), (328.0, 323.0), (324.5, 316.5), (301.5, 174.5), (307.5, 136.0)], [(301.5, 477.5), (308.5, 477.0), (313.0, 472.5), (327.0, 322.0), (303.0, 176.5), (312.0, 139.0)], [(309.0, 472.0), (327.5, 322.0), (299.5, 179.0), (308.0, 177.0), (311.0, 141.5), (309.5, 45.5)], [(309.0, 471.5), (312.5, 411.0), (324.5, 320.5), (303.0, 183.0), (312.5, 181.5), (312.0, 145.0)], [(308.5, 469.5), (310.5, 414.0), (318.5, 320.0), (315.5, 185.0), (305.5, 187.0), (314.0, 149.0)], [(307.5, 466.5), (311.0, 409.0), (321.5, 316.0), (305.5, 188.0), (315.5, 186.5), (316.0, 151.5)], [(308.5, 460.5), (313.5, 408.5), (310.5, 400.5), (327.0, 315.5), (313.0, 185.5), (315.5, 150.0)], [(309.0, 460.5), (314.5, 407.0), (311.0, 400.5), (327.5, 316.0), (312.0, 186.0), (315.5, 150.5)], [(311.0, 463.5), (312.0, 409.0), (322.5, 319.0), (313.5, 188.5), (317.0, 151.5), (312.0, 67.0)], [(311.5, 464.5), (311.5, 408.5), (320.5, 319.0), (313.5, 188.5), (317.0, 152.0), (310.5, 66.5)], [(310.5, 464.5), (311.5, 407.5), (318.0, 319.5), (313.0, 188.0), (316.5, 151.5), (312.0, 65.5)], [(311.0, 464.5), (311.0, 407.5), (315.0, 319.0), (313.0, 188.0), (316.5, 151.5), (308.0, 66.0)], [(310.0, 464.5), (309.0, 409.0), (314.0, 319.0), (314.0, 187.5), (316.5, 151.0), (309.5, 65.0)], [(309.5, 465.5), (307.0, 409.0), (313.5, 319.0), (311.5, 186.0), (314.5, 148.5), (307.5, 62.0)], [(331.5, 477.0), (310.0, 465.5), (307.0, 408.5), (310.5, 185.0), (313.5, 147.5), (304.5, 61.0)], [(330.5, 477.5), (309.5, 465.5), (329.0, 322.0), (300.0, 188.0), (307.0, 150.0), (309.0, 60.0)], [(330.5, 477.5), (311.0, 465.5), (330.0, 323.0), (298.0, 190.0), (306.5, 152.5), (311.5, 62.5)], [(330.0, 477.5), (311.0, 465.5), (342.5, 330.0), (289.0, 208.5), (301.5, 173.5), (318.5, 82.0)], [(329.0, 477.5), (312.5, 465.5), (347.5, 334.0), (287.5, 214.5), (300.5, 179.5), (320.0, 89.5)], [(329.5, 477.5), (313.5, 465.0), (364.0, 356.5), (268.0, 297.0), (297.5, 278.5), (294.5, 270.5)], [(329.5, 477.5), (313.5, 467.5), (316.5, 459.0), (365.0, 357.5), (268.0, 302.0), (294.0, 278.0)], [(313.0, 467.5), (365.0, 359.5), (266.0, 348.0), (299.0, 334.0), (293.5, 326.0), (340.0, 248.0)], [(331.0, 477.5), (312.5, 465.0), (368.0, 359.5), (269.0, 344.0), (296.5, 325.0), (343.0, 243.0)], [(331.0, 477.5), (313.0, 465.0), (368.5, 359.5), (269.5, 338.5), (296.5, 320.5), (344.0, 238.0)], [(331.0, 478.0), (313.5, 465.0), (369.0, 360.0), (270.0, 332.0), (298.5, 314.5), (344.0, 231.5)], [(330.5, 477.5), (315.0, 465.0), (371.5, 357.5), (270.5, 324.5), (298.5, 308.0), (344.5, 224.5)], [(330.5, 477.5), (316.5, 465.0), (371.0, 356.5), (272.0, 318.5), (300.0, 300.0), (344.5, 217.5)], [(331.0, 477.5), (316.5, 464.0), (373.0, 356.5), (273.5, 310.0), (299.0, 292.0), (344.5, 209.5)], [(331.5, 477.5), (316.5, 465.0), (373.0, 357.0), (276.0, 304.0), (300.0, 284.0), (343.5, 199.5)], [(332.0, 477.5), (314.5, 465.5), (374.5, 355.0), (276.0, 296.5), (301.5, 276.5), (342.5, 191.5)], [(332.0, 477.5), (314.5, 465.0), (373.5, 357.0), (278.0, 289.5), (302.0, 268.5), (343.0, 181.5)], [(331.0, 478.0), (314.5, 465.0), (369.5, 355.0), (279.0, 282.0), (303.5, 259.5), (341.5, 171.5)], [(331.5, 478.0), (314.5, 464.5), (368.5, 355.5), (283.5, 266.5), (305.5, 242.0), (338.0, 152.0)], [(313.0, 461.5), (330.5, 324.0), (299.5, 186.5), (320.0, 153.5), (315.5, 148.5), (325.0, 56.0)], [(313.0, 464.0), (325.5, 323.5), (303.5, 182.0), (321.0, 145.5), (315.0, 141.5), (323.0, 50.0)], [(312.0, 464.0), (306.0, 180.0), (323.5, 145.0), (317.0, 141.0), (520.0, 114.0), (319.0, 48.5)], [(312.5, 464.5), (308.0, 178.5), (325.0, 144.5), (323.5, 140.5), (315.0, 139.5), (319.5, 46.5)], [(312.0, 463.5), (317.5, 323.5), (310.0, 179.0), (323.5, 143.5), (315.5, 138.5), (315.5, 46.5)], [(312.0, 463.5), (316.0, 323.5), (309.5, 179.0), (323.0, 137.5), (320.0, 140.5), (315.5, 47.0)], [(311.5, 463.5), (313.5, 324.5), (311.5, 179.0), (323.0, 137.5), (320.0, 140.0), (313.5, 48.0)], [(311.5, 463.5), (312.5, 324.5), (312.0, 179.0), (323.0, 137.5), (320.0, 140.0), (312.5, 48.0)], [(311.5, 463.5), (314.5, 411.5), (305.0, 405.0), (312.0, 180.5), (320.0, 140.5), (311.5, 49.5)], [(311.0, 463.5), (312.0, 413.0), (311.0, 180.0), (324.5, 141.5), (316.0, 139.5), (311.5, 49.5)], [(310.0, 465.5), (313.0, 412.5), (306.0, 404.5), (311.5, 180.0), (320.0, 141.0), (311.5, 49.5)], [(311.0, 466.5), (312.0, 413.0), (306.0, 404.5), (311.0, 180.0), (320.0, 141.0), (311.5, 50.5)], [(311.5, 465.5), (311.0, 414.0), (313.0, 320.5), (309.5, 180.0), (319.0, 141.0), (312.5, 50.0)], [(311.5, 465.5), (312.5, 412.0), (315.0, 320.0), (309.5, 180.0), (319.0, 141.5), (312.5, 49.5)], [(312.0, 467.0), (314.5, 405.5), (322.5, 320.0), (305.5, 182.0), (318.0, 143.5), (316.0, 50.5)], [(314.0, 463.5), (327.5, 321.5), (302.5, 184.5), (317.0, 148.5), (525.0, 112.0), (319.0, 54.0)], [(331.5, 478.0), (314.0, 464.0), (338.5, 328.0), (297.5, 196.5), (314.0, 163.5), (326.0, 68.5)], [(331.0, 477.5), (314.0, 464.0), (340.5, 329.0), (295.5, 202.5), (313.5, 170.0), (329.0, 75.5)], [(331.0, 477.5), (317.5, 462.5), (347.5, 339.0), (289.0, 222.0), (310.0, 191.0), (334.5, 100.0)], [(331.5, 477.5), (316.0, 464.0), (353.0, 345.0), (286.0, 238.0), (309.0, 208.5), (341.0, 119.5)], [(331.5, 477.5), (314.5, 465.0), (369.5, 346.0), (280.0, 263.0), (307.0, 236.5), (346.5, 149.0)], [(331.5, 478.0), (313.0, 465.0), (370.0, 360.5), (366.5, 356.0), (280.0, 306.0), (305.0, 282.0)], [(331.5, 478.0), (314.0, 465.0), (367.0, 363.0), (275.5, 325.0), (304.5, 302.0), (356.0, 226.5)], [(329.5, 478.0), (313.0, 467.0), (367.0, 364.5), (278.5, 340.5), (306.0, 321.0), (357.0, 242.5)], [(331.0, 478.0), (312.5, 467.0), (366.5, 365.5), (278.5, 342.5), (306.5, 321.0), (357.0, 244.5)], [(329.5, 478.0), (311.5, 467.5), (366.5, 365.0), (278.0, 342.5), (307.0, 320.0), (357.0, 244.5)], [(329.5, 478.0), (311.5, 466.0), (367.5, 365.5), (278.5, 339.5), (307.5, 319.0), (357.0, 240.5)], [(332.0, 477.5), (315.5, 467.0), (368.5, 365.5), (278.5, 335.5), (306.0, 315.5), (354.5, 236.0)], [(332.5, 477.5), (315.5, 466.5), (368.0, 363.5), (279.0, 329.5), (307.0, 311.0), (356.0, 230.0)], [(332.5, 477.5), (314.0, 466.5), (367.5, 362.0), (279.5, 316.5), (309.5, 302.0), (303.5, 294.5)], [(310.5, 468.0), (316.0, 461.0), (354.0, 332.0), (292.5, 212.0), (301.0, 213.0), (317.0, 181.5)], [(311.5, 465.0), (325.0, 322.5), (325.5, 317.0), (319.0, 177.5), (331.5, 139.5), (323.5, 45.5)], [(330.5, 477.5), (313.0, 465.0), (311.5, 404.5), (324.5, 178.0), (333.0, 139.0), (319.5, 47.5)], [(330.5, 477.5), (312.5, 464.0), (315.5, 411.5), (324.5, 178.0), (332.5, 139.5), (318.5, 48.5)], [(330.5, 477.5), (312.5, 464.0), (308.0, 404.5), (325.0, 178.5), (331.0, 140.0), (320.0, 48.5)], [(313.0, 464.0), (315.5, 412.5), (307.5, 404.5), (325.0, 178.5), (331.5, 140.0), (319.0, 49.0)], [(313.0, 464.0), (314.5, 412.5), (306.5, 404.5), (324.5, 178.5), (331.5, 140.0), (319.0, 49.0)], [(313.0, 464.0), (313.0, 411.0), (306.0, 404.5), (324.5, 179.0), (332.5, 140.0), (319.0, 49.0)], [(313.0, 464.0), (312.0, 412.5), (307.0, 404.5), (323.5, 179.0), (330.5, 140.0), (319.0, 49.0)], [(312.5, 464.0), (311.5, 411.0), (306.5, 404.5), (321.5, 179.0), (330.0, 140.5), (321.0, 47.5)], [(312.5, 464.0), (313.0, 411.0), (320.0, 180.0), (321.5, 177.0), (330.0, 140.5), (322.0, 46.5)], [(330.0, 478.0), (312.0, 464.0), (324.5, 316.5), (314.0, 179.0), (326.5, 142.5), (326.0, 48.0)], [(331.0, 477.5), (313.5, 464.5), (332.5, 319.5), (307.5, 186.0), (323.5, 152.5), (330.5, 56.5)], [(331.0, 477.5), (313.0, 465.0), (337.5, 322.5), (305.5, 190.5), (321.0, 156.0), (330.0, 62.5)], [(331.0, 477.5), (314.0, 465.0), (339.5, 323.5), (303.5, 197.5), (320.0, 162.0), (332.0, 68.5)], [(331.0, 477.5), (314.5, 464.0), (345.0, 328.0), (300.0, 204.0), (317.5, 169.5), (334.0, 77.5)], [(331.0, 477.5), (315.5, 464.0), (347.0, 329.0), (297.5, 211.5), (317.0, 178.0), (333.5, 85.5)], [(331.0, 477.5), (315.5, 464.0), (352.5, 332.5), (295.0, 219.5), (315.0, 188.5), (338.0, 94.5)], [(331.0, 478.0), (315.5, 464.5), (361.5, 350.5), (291.0, 260.0), (280.0, 258.0), (311.0, 232.5)], [(331.0, 478.0), (314.5, 464.5), (362.5, 356.5), (285.0, 277.0), (277.5, 275.5), (309.0, 253.0)], [(331.0, 478.0), (313.5, 465.0), (365.5, 359.0), (277.5, 308.5), (305.5, 290.0), (305.5, 284.5)], [(330.0, 478.0), (312.5, 465.0), (366.5, 359.0), (276.5, 323.0), (305.0, 306.5), (306.0, 304.0)], [(330.0, 478.0), (312.5, 465.0), (366.5, 358.5), (274.5, 329.5), (304.5, 314.0), (305.5, 310.5)], [(311.5, 467.0), (362.0, 360.5), (274.0, 348.0), (268.0, 349.0), (301.5, 329.0), (346.0, 246.5)], [(312.5, 468.0), (308.5, 462.5), (365.0, 358.5), (272.0, 344.0), (301.0, 326.0), (345.0, 242.5)], [(306.0, 465.0), (314.0, 466.0), (362.5, 356.5), (271.0, 318.5), (301.5, 302.5), (347.0, 214.5)], [(331.0, 477.0), (315.0, 464.0), (353.5, 332.5), (289.5, 216.0), (299.0, 216.0), (315.0, 188.5)], [(331.0, 478.0), (313.5, 464.5), (340.5, 330.0), (299.0, 192.5), (297.5, 191.0), (319.0, 160.5)], [(330.5, 477.5), (314.0, 462.5), (316.5, 317.5), (320.0, 176.0), (330.5, 142.0), (312.0, 45.5)], [(331.0, 477.5), (314.0, 463.5), (316.0, 316.5), (319.0, 178.0), (321.0, 174.0), (333.5, 142.5)], [(331.0, 477.5), (314.0, 463.5), (314.5, 316.5), (322.0, 177.5), (321.5, 173.5), (332.5, 142.5)], [(330.5, 477.5), (317.0, 464.0), (312.0, 465.0), (323.0, 178.0), (332.5, 142.0), (317.0, 47.5)], [(331.0, 477.5), (313.5, 465.0), (314.0, 411.0), (324.0, 177.0), (333.0, 142.0), (316.5, 47.5)], [(331.0, 477.5), (313.5, 465.0), (314.0, 411.0), (323.5, 178.0), (332.5, 142.0), (319.0, 48.0)], [(313.0, 465.5), (313.5, 409.5), (317.5, 320.0), (324.5, 177.0), (332.5, 141.5), (317.0, 49.5)], [(313.0, 465.5), (313.5, 409.5), (318.0, 320.0), (324.5, 177.5), (333.0, 142.5), (317.0, 48.0)], [(313.0, 465.5), (311.5, 410.0), (319.5, 320.0), (323.5, 178.0), (333.0, 142.5), (320.5, 45.0)], [(313.0, 465.5), (314.0, 412.0), (320.0, 320.0), (323.5, 177.0), (333.0, 142.5), (322.0, 45.0)], [(313.0, 465.0), (313.0, 410.0), (320.0, 320.0), (322.0, 176.5), (332.5, 142.5), (324.0, 43.5)], [(313.0, 465.0), (316.5, 412.0), (322.0, 320.0), (320.5, 176.5), (332.5, 142.5), (324.5, 44.0)], [(312.5, 465.0), (318.5, 416.5), (326.0, 320.0), (318.5, 176.0), (331.0, 142.5), (327.5, 44.0)], [(313.0, 465.5), (339.5, 327.5), (310.0, 186.0), (326.0, 156.5), (327.5, 154.0), (333.0, 54.5)], [(331.5, 478.0), (313.0, 465.5), (338.0, 322.5), (307.5, 190.5), (327.5, 160.0), (335.0, 59.5)], [(330.5, 477.5), (313.5, 465.5), (350.0, 337.5), (301.5, 203.5), (324.0, 174.5), (340.0, 73.5)], [(331.0, 478.0), (313.0, 464.5), (373.0, 365.0), (310.0, 319.0), (316.5, 315.5), (284.0, 312.5)], [(331.0, 478.0), (314.5, 465.5), (376.5, 363.5), (375.5, 361.0), (316.0, 313.5), (286.0, 305.0)], [(331.5, 477.5), (314.0, 463.0), (333.0, 324.5), (333.5, 319.0), (327.0, 242.0), (301.0, 181.0)], [(331.5, 477.5), (313.5, 464.0), (331.0, 322.0), (325.5, 320.0), (328.0, 241.5), (303.0, 182.5)], [(331.5, 477.5), (314.5, 463.0), (324.0, 319.0), (330.5, 250.5), (316.0, 177.0), (305.0, 178.5)], [(331.0, 477.5), (315.0, 464.0), (307.0, 409.0), (311.5, 322.5), (312.0, 182.5), (322.5, 54.0)], [(331.0, 477.5), (314.5, 464.0), (307.0, 410.0), (313.5, 324.5), (311.0, 182.5), (323.0, 55.0)]]
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
number_tapes = 6
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
all_points_avg = get_avg_points(all_points)
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

y_points_avg = get_avg_y(all_points_avg,6)
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
angles_avg, perf_avg = find_angles(all_points_avg)
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
fig = make_pie(perf_avg)
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

fig1 = draw_graph_y(y_points_avg,6)
fig2 = draw_graph_angles(angles_avg)

figure = dcc.Graph(figure=fig,id="piechart")
figure1 = dcc.Graph(figure=fig1)
figure2 = dcc.Graph(figure=fig2)
cardfig = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Angles", className="card-title"),
            figure
        ]
    )
)
cardfig1 = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Y", className="card-title"),
            figure1
        ]
    ),className="my-4"
)
cardfig2 = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Angles", className="card-title"),
            figure2
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
                        html.Button('Submit', className='btn btn-info', type="submit"),
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
                className = "custom-file mb-4"
            ),
            dbc.Button("Submit", color="primary", className="mr-1", id='submitbtn', n_clicks = 0),
        ]
    )
    ,className = "form-group ",
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
            file_input,
        ]
    )
)



stat_range = dbc.Card(
                    [
                        html.H4("Range of angles:", className="card-title ml-2 mt-2"),
                        html.H4(str(find_range(angles_avg)) + u"\N{DEGREE SIGN}", className="card-title ml-2"),
                    ]
                )

stat_avg_ang = dbc.Card(
                    [
                        html.H4("Average angle:", className="card-title ml-2 mt-2"),
                        html.H4(str(find_avg_angle(angles_avg)) + u"\N{DEGREE SIGN}", className="card-title ml-2"),
                    ]
                )

row_stats = dbc.Row(
    [
        dbc.Col(stat_range,width=4),
        dbc.Col(stat_avg_ang,width=4),
        dbc.Col(stat_range,width=4)
        
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

video = html.Video(src="assets/result.mp4",controls=True) ##center video and fix style, try to put in card



modal = html.Div(
    [
        dbc.Button("Open modal", id="open"),
        dbc.Modal(
            [
                dbc.ModalHeader("Guidelines"),
                dbc.ModalBody(),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close", className="ml-auto", style="display:none")
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
    Output('piechart', 'figure'),
    [Input('submitbtn', 'n_clicks')],
    [State('opt-dropdown', 'value')], #state of exercise they chose
)
def analyze_video(n,exercise):
    print("click") #use fig.show
    print(exercise)
    return fig



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
    app.run_server(debug=True)

#video upload
#return stats in functions