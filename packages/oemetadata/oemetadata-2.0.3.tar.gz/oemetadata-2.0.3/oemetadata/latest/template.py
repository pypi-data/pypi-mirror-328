# SPDX-FileCopyrightText: 2024 Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: 2024 Jonas Huber <jh-RLI> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: oemetadata <https://github.com/OpenEnergyPlatform/oemetadata/>
# SPDX-License-Identifier: MIT

import json
import os


with open(os.path.join(os.path.dirname(__file__), "template.json"), "rb") as f:
    OEMETADATA_LATEST_TEMPLATE = json.loads(f.read())
