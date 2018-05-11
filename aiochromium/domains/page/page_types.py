from ..base import Array, BooleanField, BaseObject, Integer, String


class Frame(BaseObject):

    id = String(source='id')
    loader_id = String(source='loaderId')
    url = String(source='url')
    security_origin = String(source='securityOrigin')
    mime_type = String(source='mimeType')
    parent_id = String(source='parentId', blank=True)
    name = String(source='name', blank=True)
    unreachable_url = String(source='unreachableUrl', blank=True)


class FrameTree(BaseObject):

    frame = Frame(source='frame')
    child_frames = Array(source='childFrames', target=Frame, blank=True)


class NavigationEntry(BaseObject):

    id = Integer(source='id')
    url = String(source='url')
    user_typed_url = String(source='userTypedUrl')
    title = String(source='title')
    transition_type = String(source='transitionType')
