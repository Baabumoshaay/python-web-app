from flask import Flask, render_template, request
import logging

app = Flask(__name__)

# list of routes
routes = ['Route 01', 'Route 02']

# dictionary to store vehicle information
vehicles = {}

# dictionary to store security team information
teams = {}

# home page
# home page
@app.route('/')
def home():
    return render_template('home.html', routes=routes, vehicles=vehicles)

# add a route
@app.route('/add_route', methods=['POST'])
def add_route():
    route = request.form['route']
    routes.append(route)
    return render_template('home.html', routes=routes, vehicles=vehicles)

# remove a route
@app.route('/remove_route', methods=['POST'])
def remove_route():
    route = request.form['route']
    routes.remove(route)
    return render_template('home.html', routes=routes, vehicles=vehicles)

# track progress of a vehicle
@app.route('/vehicle_status/<vehicle>', methods=['GET', 'POST'])
def vehicle_status(vehicle):
    status = vehicles.get(vehicle, 'N/A')
    if request.method == 'POST':
        status = request.form['status']
        vehicles[vehicle] = status
    return render_template('vehicle_status.html', vehicle=vehicle, status=status)

# assign security team to a vehicle
@app.route('/vehicle_team/<vehicle>', methods=['GET', 'POST'])
def vehicle_team(vehicle):
    team = teams.get(vehicle, '')
    if request.method == 'POST':
        team = request.form['team']
        teams[vehicle] = team
    return render_template('vehicle_team.html', vehicle=vehicle, team=team)


if __name__ == '__main__':
    app.run(debug=True)
