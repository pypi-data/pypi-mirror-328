# SPDX-FileCopyrightText: 2021 Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: 2021 Jonas Huber <jh-RLI> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: oemetadata <https://github.com/OpenEnergyPlatform/oemetadata/>
# SPDX-License-Identifier: MIT

import json
import os


with open(os.path.join(os.path.dirname(__file__), "schema.json"), "rb") as f:
    OEMETADATA_V150_SCHEMA = json.loads(f.read())
