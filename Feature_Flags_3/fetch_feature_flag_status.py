
import os
import ldclient
from ldclient import Context
from ldclient.config import Config
from threading import Lock, Event

def fetch_feature_flag_status():
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

    flag_value = ldclient.get().variation(feature_flag_key, context, False)

    # Print the flag value
    print("Feature flag 'Status_Flag' status:", flag_value)

if __name__ == "__main__":
    fetch_feature_flag_status()
