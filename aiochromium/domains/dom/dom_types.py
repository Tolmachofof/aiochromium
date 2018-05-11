from ..base import BooleanField, Array, BaseObject, String, Integer, Self


class BackendNode(BaseObject):

    node_type = Integer(source='nodeType')
    node_name = String(source='nodeName')
    backend_node_id = Integer(source='backendNodeId')


class Node(BaseObject):
    """
    The mirror object that represents the actual DOM node.
    """

    node_id = Integer(source='nodeId')
    backend_node_id = Integer(source='backendNodeId')
    node_type = Integer(source='nodeType')
    node_name = String(source='nodeName')
    local_name = String(source='localName')
    node_value = String(source='nodeValue')
    parent_id = Integer(source='nodeId', blank=True)
    child_node_count = Integer(source='childNodeCount', blank=True)
    children = Array(source='children', target=Self, blank=True, default=())
    attributes = Array(source='attributes', target=String, blank=True)
    document_url = String(source='documentURL', blank=True)
    base_url = String(source='baseURL', blank=True)
    public_id = String(source='publicId', blank=True)
    system_id = String(source='systemId', blank=True)
    internal_subset = String(source='internalSubset', blank=True)
    xml_version = String(source='xmlVersion', blank=True)
    name = String(source='name', blank=True)
    value = String(source='value', blank=True)
    pseudo_type = String(source='pseudoType', blank=True)
    shadow_root_type = String(source='shadowRootType', blank=True)
    frame_id = String(source='frameId', blank=True)
    content_document = Self(source='contentDocument', blank=True)
    shadow_roots = Array(source='shadowRoots', target=Self, blank=True)
    template_content = Self(source='templateContent', blank=True)
    pseudo_elements = Array(source='pseudoElements', target=Self, blank=True)
    imported_document = Self(source='importedDocument', blank=True)
    distributed_nodes = Array(
        source='distributedNodes', target=BackendNode(), blank=True
    )
    is_svg = BooleanField(source='isSVG', blank=True)


class RGBA(BaseObject):

    r = Integer(source='r')
    g = Integer(source='g')
    b = Integer(source='b')
    a = Integer(source='a', blank=True, default=1)


class ShapeOutsideInfo(BaseObject):

    bounds = Array(source='bounds', target=Integer)
    shape = Array(source='shape')
    margin_shape = Array(source='marginShape')


class BoxModel(BaseObject):

    content = Array(source='content', target=Integer)
    padding = Array(source='padding', target=Integer)
    border = Array(source='border', target=Integer)
    margin = Array(source='margin', target=Integer)
    width = Integer(source='width')
    height = Integer(source='height')
    shape_outside = ShapeOutsideInfo(source='shapeOutside', blank=True)


class Rect(BaseObject):

    x = Integer(source='x')
    y = Integer(source='y')
    width = Integer(source='width')
    height = Integer(source='height')
