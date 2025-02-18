# SPDX-FileCopyrightText: 2019 Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: 2019 Jonas Huber <jh-RLI> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: oemetadata <https://github.com/OpenEnergyPlatform/oemetadata/>
# SPDX-License-Identifier: MIT

import json
import os


with open(os.path.join(os.path.dirname(__file__), "schema.json"), "rb") as f:
    OEMETADATA_V130_SCHEMA = json.loads(f.read())
