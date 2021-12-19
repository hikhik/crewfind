# CrewFind

- CrewFind runs under the Flask framework in Python.
- LaunchDarkly feature flags are used to control which features are exposed and to which users

---
# Configure Feature Flags
Login to your Launch Darkly account

### Create a new Project

### Create a new Feature Flag

### Copy SDK KEY


---
# Prerequisites
For detailed instructions on setting up a Flask environment, see the [Flask Install Documentation](https://flask.palletsprojects.com/en/2.0.x/installation/).

Otherwise, follow these brief instrcutions.

### Python
Install Python as described on the [Python website](https://www.python.org/downloads/)

### Flask module
Install the Flask Python module:

```
pip install Flask
```

### Launch Darkly module
Install the Launch Darkly Python module:

```
pip install ldclient
```


---
# CrewFind webapp
## Install webapp
1. Create a new directory to host CrewFind, and change into that directory
```
mkdir crewfind
cd crewfind
```
2. Download and unzip the CrewFind webapp from [this GitHub repository](https://github.com/hikhik/crewfind/tree/glitch)
```
wget http://github.com/hikhik/crewfind/archive/glitch.zip
unzip glitch.zip
cd crewfind-glitch
```

## Configure webapp
1. edit the file named `crewfind.py`
2. insert your SDK Key in line 10 in place of <SDK_KEY>
```
ldclient.set_config(Config("<SDK_KEY>"))
```


## Start webapp
1. Launch the builtin development server.
```
export FLASK_APP=crewfind
flask run --host=0.0.0.0
```
2. Access the webapp by browsing to the URL listed in the output above, typically http://<server_ip>:5000/


