from ..base import Array, BaseObject, String, Integer


class BackendNode(BaseObject):

    node_type = Integer(source='nodeType')
    node_name = String(source='nodeName')
    backend_node_id = Integer(source='backendNodeId')


class Node(BaseObject):

    node_id = Integer(source='nodeId')
    backend_node_id = Integer(source='backendNodeId')
    node_type = Integer(source='nodeType')
    node_name = String(source='nodeName')
    local_name = String(source='localName')
    node_value = String(source='nodeValue')
    parent_id = Integer(source='nodeId', blank=True)
    child_node_count = Integer(source='childNodeCount', blank=True)
    children = Array(source='children', target='self', blank=True, default=())
    attributes = Array(source='attributes', target=String, blank=True)
    document_url = String(source='documentURL', blank=True)
    base_url = String(source='baseURL', blank=True)
    public_id = String(source='publicId', blank=True)


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
