from .base import Domain, RequestFrame


class Page(Domain):

    _ENABLE = 'Page.enable'
    _DISABLE = 'Page.disable'
    _NAVIGATE = 'Page.navigate'
    _RELOAD = 'Page.reload'
    _SCREENSHOT = 'Page.captureScreenshot'
    _FRAME_STOPPED_LOADING = 'Page.frameStoppedLoading'

    def enable(self):
        return RequestFrame(self._ENABLE)

    def disable(self):
        return RequestFrame(self._DISABLE)

    @classmethod
    def navigate(
        cls, url, refferer=None, transition_type=None, frame_id=None
    ):
        return cls.create_frame(
            cls._NAVIGATE, {
                'url': url,
                'refferer': refferer,
                'transitionType': transition_type,
                'frameId': frame_id
            }
        )

    @classmethod
    def reload(cls, ignore_cache=None, script_to_eval_on_load=None):
        return cls.create_frame(
            cls._RELOAD,
            {
                'ignoreCache': ignore_cache,
                'scriptToEvaluateOnLoad': script_to_eval_on_load
            }
        )

    @classmethod
    def frame_stopped_loading(cls, frame_id):
        return cls.create_frame(
            cls._FRAME_STOPPED_LOADING, {'frameId': frame_id}
        )

