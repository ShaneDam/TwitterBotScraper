#http://127.0.0.1:8050/ to view the images

import dash
import dash_core_components as dcc
import dash_html_components as html

import flask
import glob
import os

image_directory = 'C:/Users/Cooki/OneDrive/Documents/concordia-bootcamps/final_project/TwitterBot/'
list_of_images = [os.path.basename(x) for x in glob.glob('{}*.png'.format(image_directory))]
static_image_route = '/static/'

app = dash.Dash()

app.layout = html.Div([
    dcc.Dropdown(
        id='image-dropdown',
        options=[{'label': i, 'value': i} for i in list_of_images],
        value=list_of_images[0]
    ),
    html.Img(id='image')
])

@app.callback(
    dash.dependencies.Output('image', 'src'),
    [dash.dependencies.Input('image-dropdown', 'value')])
def update_image_src(value):
    return static_image_route + value

#adding a static image route that serves images from the desktop of directory
@app.server.route('{}<image_path>.png'.format(static_image_route))
def serve_image(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory, image_name)

if __name__ == '__main__':
    app.run_server(debug=True)
