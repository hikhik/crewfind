# CrewFind

- CrewFind runs under the Flask framework in Python.
- LaunchDarkly feature flags are used to control which features are exposed and to which users

---
# Create Feature Flag
Login to your Launch Darkly account

### Create a new Project
1. Navigate to the [Account settings](https://app.launchdarkly.com/settings/projects) page.
2. Click **Create project**.
3. Give your project a human-readable **Name**, such as CrewFind.
4. Click **Save project**.
5. In the **Account Settings** page on the **Projects** tab, click to copy the new project's SDK key to your clipboard.

### Create a new Feature Flag
1. From the LaunchDarkly app, click **Feature flags**.
2. Click **Create flag**
3. Enter `selling_enabled` for the name.
4. Optionally, add a description of the flag.
5. Set the **Flag variations** to Boolean.
6. Save the new flag.


---
# Configure Flask Framework
For detailed instructions on setting up a Flask environment, see the [Flask Install Documentation](https://flask.palletsprojects.com/en/2.0.x/installation/).

Otherwise, follow these brief instrcutions.

### Python
Flask supports Python 3.6 and newer. Install Python as described on the [Python website](https://www.python.org/downloads/)

### Flask module
Install the Flask Python module:

```
pip3 install Flask
pip3 install python-dotenv
```

### Launch Darkly module
Install the Launch Darkly Python module:

```
pip3 install launchdarkly-server-sdk
```


---
# CrewFind webapp
## Install webapp
Download and unzip the CrewFind webapp from [this GitHub repository](https://github.com/hikhik/crewfind/tree/glitch)
```
wget http://github.com/hikhik/crewfind/archive/glitch.zip
unzip glitch.zip
cd crewfind-glitch
```

## Configure webapp
1. edit the file named `crewfind.py`
2. insert your SDK Key (copied above) in line 10 in place of <SDK_KEY>
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


# Testing

## Test with Feature Flag disabled
1. Access the webapp.
2. Login using any username (passwords are not required)
3. Notice that there is no section on the page named Sell Your Yacht

## Turning the Feature on
Turn on the feature flag to enable teh selling feature.
1. From the LaunchDarkly app, click **Feature flags**.
2. Navigate to the `selling_enabled` flag.
3. Click the Targeting toggle to toggle the flag to on.
4. Enter a comment.
5. Click Save changes.

## Test with Feature Flag enabled
1. Access the webapp.
2. Login using any username (passwords are not required)
3. Notice that the section named Sell Your Yacht now appears

## Target Individual Users
1. From the LaunchDarkly app, click **Feature flags**.
2. Navigate to the `selling_enabled` flag.
3. Navigate to the Target individual users **false** section.
4. Click on **Add users...**, and select one of the usernames.
5. Click Save changes.

## Test with Targetting
1. Access the webapp.
2. Login using the username configured in Target individual users above.
3. Notice that the section named Sell Your Yacht **does not** appear for this user.
4. Logout.
5. Login using a different username.
6. Notice that the section named Sell Your Yacht **does** appear for this user.




