node_store = None
"""
The node store for SDoc2 nodes.

:type: sdoc.sdoc2.NodeStore.NodeStore|None
"""


# ----------------------------------------------------------------------------------------------------------------------
def in_scope(node_id: int):
    """
    Retrieves a node based on its ID.

    :param node_id: The node ID.
    """
    return node_store.nodes[node_id]


# ----------------------------------------------------------------------------------------------------------------------
def out_scope(node) -> None:
    """
    Marks a node as no longer in scope.

    :param node: The node.
    """
    node_store.out_scope(node)

# ----------------------------------------------------------------------------------------------------------------------
