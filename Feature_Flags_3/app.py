from flask import Flask, render_template
import os
import ldclient
from ldclient import Context
from ldclient.config import Config
from threading import Lock, Event

app = Flask(__name__)

# Set sdk_key to your LaunchDarkly SDK key.
sdk_key = "sdk-79037d1d-f7c5-4380-ba2a-9f0611717500"

# Set feature_flag_key to the feature flag key you want to evaluate.
feature_flag_key = "Status_Flag"

# Initialize LaunchDarkly client
ldclient.set_config(Config(sdk_key))

if not ldclient.get().is_initialized():
    print("*** SDK failed to initialize. Please check your internet connection and SDK credential for any typo.")
    exit()

print("*** SDK successfully initialized")

# Set up the evaluation context.
context = Context.builder('Status_Flag').kind('user').name('Sandy').build()

# Function to fetch the latest value of the feature flag
def get_flag_value():
    return ldclient.get().variation(feature_flag_key, context, False)

@app.route('/')
def index():
    flag_value = get_flag_value()
    return render_template('index.html', flag_value=flag_value)

if __name__ == '__main__':
    app.run(debug=True)
