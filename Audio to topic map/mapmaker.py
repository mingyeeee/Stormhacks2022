import plotly.graph_objects as go
import igraph
from igraph import Graph, EdgeSeq
import json
import math

# open json file
# open json file
with open('nodemap.json') as json_file:
    data = json.load(json_file)

nr_vertices = 13
v_label = data['nodemap']
G = Graph.Tree(nr_vertices, 3) # 2 stands for children number
lay = G.layout('rt')

position = {k: lay[k] for k in range(nr_vertices)}
Y = [lay[k][1] for k in range(nr_vertices)]
M = max(Y)

es = EdgeSeq(G) # sequence of edges
E = [e.tuple for e in G.es] # list of edges

L = len(position)
Xn = [position[k][0] for k in range(L)]
Yn = [2*M-position[k][1] for k in range(L)]
Xe = []
Ye = []
counter = 0
counter2 = 0
for edge in E:
    Xe+=[position[edge[0]][0],position[edge[1]][0], None]
    if counter == 3:
        counter2 = 1
    elif counter == 6:
        counter2 = 2
    elif counter == 9:
        counter2 = 3

    
    Ye+=[2*M-position[edge[0]][1]-10*counter2,2*M-position[edge[1]][1]-1*counter*10.5, None]
    counter +=1


labels = v_label


def make_annotations(pos, text, font_size=10, font_color='rgb(0,0,250)'):
    L=len(pos)
    if len(text)!=L:
        raise ValueError('The lists pos and text must have the same len')
    annotations = []
    for k in range(L):
        annotations.append(
            dict(
                text=labels[k], # or replace labels with a different list for the text within the circle
                x=pos[k][0], y=2*M-position[k][1]+k*-1*10,
                xref='x1', yref='y1',
                font=dict(color=font_color, size=font_size),
                showarrow=False)
        )
    return annotations

fig = go.Figure()
fig.add_trace(go.Scatter(x=Xe,
                   y=Ye,
                   mode='lines',
                   line=dict(color='rgb(210,210,210)', width=1),
                   hoverinfo='none'
                   ))
fig.add_trace(go.Scatter(x=Xn,
                  y=Yn,
                  mode='markers',
                  name='bla',
                  
                  text=labels,
                  hoverinfo='text',
                  opacity=0
                  ))

axis = dict(showline=False, # hide axis line, grid, ticklabels and  title
            zeroline=False,
            showgrid=False,
            showticklabels=False,
            )

fig.update_layout(title= f'Topic Map for {v_label[0]}',
              annotations=make_annotations(position, v_label),
              font_size=12,
              showlegend=False,
              xaxis=axis,
              yaxis=axis,
              margin=dict(l=40, r=40, b=85, t=100),
              hovermode='closest',
              plot_bgcolor='rgb(248,248,248)'
              )
fig.write_image(f"{v_label[0]}.png")