# Copyright 2024 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This file stores input parameters for the app."""

import json

# Sets Dash debug which hides and shows Dash debug menu.
# Set to True if developing and False if demoing.
# App should be restarted to see change.
DEBUG = False

# THEME_COLOR is used for the button, text, and banner and should be dark
# and pass accessibility checks with white: https://webaim.org/resources/contrastchecker/
# THEME_COLOR_SECONDARY can be light or dark and is used for sliders, loading icon, and tabs
THEME_COLOR = "#1d232f"
THEME_COLOR_SECONDARY = "#1d232f"

THUMBNAIL = "assets/logo.svg"

APP_TITLE = "Dynex | FSS Demo"
MAIN_HEADER = "Flow Shop Scheduling"
DESCRIPTION = "Run the cargo-loading themed flow shop scheduling (FSS) problem for several different scenarios. \
Each job must execute, in order, all operations listed on the right."
DESCRIPTION2 = "Heavy Compute - Subscription Recommended"

CLASSICAL_TAB_LABEL = "Classical Results"
DWAVE_TAB_LABEL = "Dynex n.quantum"

SHOW_CQM = True

# The list of scenarios (sorted by jobs, then operations) that the user
# can choose from in the app. These can be found in the 'input' directory.
# Only the first Taillard instance for each size is loaded directly.
SCENARIOS = {
    "Carlier 7x7": "car7",
    "Carlier 8x8": "car8",
    "Carlier 8x9": "car6",
    "Carlier 10x6": "car5",
}

OR_INSTANCES = "flowshop1.txt"

# solver time limits in seconds (value means default)
SOLVER_TIME = {
    "min": 5,
    "max": 300,
    "step": 5,
    "value": 10,
}

# The list of resources that the user can choose from in the app
RESOURCE_NAMES = json.load(open("./src/data/resource_names.json", "r"))
