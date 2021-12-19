# CrewFind

- CrewFind runs under the Flask framework in Python.
- LaunchDarkly feature flags are used to control which features are exposed and to which users

---
# Prerequisites
For detailed instructions on setting up a Flask environment, see the [Flask Install Documentation](https://flask.palletsprojects.com/en/2.0.x/installation/).

Otherwise, follow these brief instrcutions.

### Python
Install Python as described on the [Python website](https://www.python.org/downloads/)

### Flask
Install the Flask Python module:

```
pip install Flask
```

### Launch Darkly
Install the Launch Darkly Python module:

```
pip install ldclient
```


---
# Install CrewFind webapp
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

## Start CrewFind webapp
export FLASK_APP=hello
