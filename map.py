import plotly.offline as py
import pandas as pd

df_airports = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/2011_february_us_airport_traffic.csv')
df_airports.head()

df_flight_paths = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/2011_february_aa_flight_paths.csv')
df_flight_paths.head()
longitudes=[]
latitudes=[]
a=[(20.4942, 53.7799), (120.3408, 16.0475), (36.33, 41.2867), (34.5581, 38.5797), (16.6818, 53.2303), (27.4265, 38.612), (9.491, 51.2993), (13.4062, 52.5155), (28.9684, 41.0214), (-79.3716, 43.6319), (34.5581, 38.5797), (-70.4, -23.65), (-6.8443000000000005, 34.0138), (31.2109, 30.0081), (-43.8988, -19.9553), (-57.9489, -34.9314), (31.3792, 30.1088), (31.2109, 30.0081), (28.9521, 41.0483), (14.5939, 53.4395), (-97.822, 37.751), (-56.1708, -34.8581), (31.2859, 30.0771), (116.0802, 5.9342), (9.0, 34.0), (31.223, 30.0355), (28.9684, 41.0214), (28.9684, 41.0214), (-66.0, 8.0), (107.6186, -6.9039), (27.4292, 37.0383), (28.9684, 41.0214), (28.9948, 41.0214), (29.0359, 41.0843), (166.45, -22.15), (77.2, 28.6), (29.27, 40.9656), (-71.6406, 10.6317), (29.9553, 31.2156), (28.9684, 41.0214), (28.9684, 41.0214), (31.2859, 30.0771), (-67.45, 10.1833), (28.3665, 37.2181), (28.9948, 41.0214), (27.2931, 38.5351), (8.5977, 53.5887), (151.5616, -33.1124), (36.1572, 36.2066), (21.0362, 52.2394), (-0.7667, 51.6333), (-50.4667, -27.1333), (28.9948, 41.0214), (34.6559, 31.7361), (29.9833, 39.4242), (33.5188, 40.1498), (28.8822, 40.3753), (28.8397, 41.0065), (32.8378, 39.923), (9.0167, 51.3667), (34.5581, 38.5797), (28.9684, 41.0214), (21.4314, 41.9965), (-37.4, -6.6667), (33.5064, 39.8453), (-58.3816, -34.6033), (29.9833, 39.4242), (34.765, 32.0666), (31.1786, 30.4591), (-3.0333, 48.8), (29.5764, 39.3026), (5.78, 47.1974), (31.2859, 30.0771), (29.2811, 37.8031), (-48.8003, -22.5986), (121.3997, 31.0456), (-6.2, 54.7), (113.5325, 34.6836), (-100.6271, 46.6731), (115.275, 39.8897), (2.0495, 48.929), (-51.3167, -30.1111), (-58.3816, -34.6033), (-5.9761, 37.3824), (-3.6837999999999997, 40.4167), (12.8667, 41.4667), (9.1895, 45.4643), (3.2282, 49.0601), (54.0, 24.0), (10.5833, 45.3167), (13.9181, 37.2576), (23.7333, 37.9833), (77.0, 20.0), (153.0638, -27.4595), (-46.9, -23.5167), (-40.4, -18.7167), (21.0362, 52.2394), (88.3506, 22.8244), (-80.1842, 40.4998), (-56.1708, -34.8581), (5.3761, 43.2854), (14.3421, 40.9097), (32.8403, 39.9117), (34.0, -13.5), (15.5653, 41.8384), (24.0, 56.0), (-99.1386, 19.4342), (79.8478, 6.9319), (10.55, 43.6833), (-0.3297, 51.4454), (7.6868, 45.0705), (118.7778, 32.0617), (138.5986, -34.9287), (138.5986, -34.9287), (-0.1224, 51.4964), (18.2333, 40.0167), (12.1097, 43.1479), (-69.9, 18.4667), (18.35, 39.9167), (-67.95, -38.9417), (38.0, 35.0), (121.4966, 25.0418), (-8.5428, 40.9253), (13.3333, 38.2), (23.7333, 37.9833), (-2.1342, 53.4663), (-6.2595, 53.3389), (77.0, 20.0), (2.3387000000000002, 48.8582), (11.2368, 43.9993), (-71.6406, 10.6317), (20.9333, 52.4), (-58.3816, -34.6033), (19.0514, 47.4925), (-80.3666, 27.1188), (-76.7285, 39.051), (143.2104, -33.494), (54.3667, 24.4667), (-73.05, -36.8333), (-87.8371, 41.6163), (77.2167, 28.6667), (-66.5, 18.25), (-72.9447, -41.4698), (13.0167, 43.45), (4.8408, 52.4474), (77.0, 20.0), (115.8489, -31.9147), (-38.5167, -12.9833), (13.4625, 52.5311), (12.4833, 41.9), (-58.2567, -35.1942), (9.4449, 45.6788), (11.2667, 44.5667), (12.1097, 43.1479)]
for i in a :
    longitudes.append(i[0])
    latitudes.append(i[1])
airports = [dict(
    type='scattergeo',
    locationmode='USA-states',
    lat=latitudes,
    lon=longitudes,
    hoverinfo='text',
    text=df_airports['airport'],
    mode='markers',
    marker=dict(
        size=10,
        color='rgb(255, 0, 0)',
        line=dict(
            width=3,
            color='rgba(68, 68, 68, 0)'
        )
    ))]

flight_paths = []
# for i in range(len(df_flight_paths)):
#     flight_paths.append(
#         dict(
#             type='scattergeo',
#             locationmode='USA-states',
#             lon=[df_flight_paths['start_lon'][i], df_flight_paths['end_lon'][i]],
#             lat=[df_flight_paths['start_lat'][i], df_flight_paths['end_lat'][i]],
#             mode='lines',
#             line=dict(
#                 width=1,
#                 color='red',
#             ),
#             opacity=float(df_flight_paths['cnt'][i]) / float(df_flight_paths['cnt'].max()),
#         )
#     )

layout = dict(
    title='Feb. 2011 American Airline flight paths<br>(Hover for airport names)',
    showlegend=False,
    geo=dict(
        scope='global',
        projection=dict(type='azimuthal equal area'),
        showland=True,
        landcolor='rgb(243, 243, 243)',
        countrycolor='rgb(204, 204, 204)',
    ),
)

fig = dict(data=flight_paths + airports, layout=layout)
py.plot(fig, filename='d3-flight-paths')
