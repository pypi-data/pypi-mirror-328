# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import logging

"""
Functions to process and deploy Semantic Model item.
"""

logger = logging.getLogger(__name__)


def publish_semanticmodels(fabric_workspace_obj):
    """Publishes all semantic model items from the repository."""
    item_type = "SemanticModel"

    for item_name in fabric_workspace_obj.repository_items.get(item_type, {}):
        fabric_workspace_obj._publish_item(item_name=item_name, item_type=item_type, excluded_directories={".pbi"})
