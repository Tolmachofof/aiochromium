from .base import Domain, DomainMethod


class Page(Domain):

    _ENABLE = DomainMethod('Page.enable', None)
    _DISABLE = DomainMethod('Page.disable', None)
    _NAVIGATE = DomainMethod('Page.navigate', None)
    _RELOAD = DomainMethod('Page.reload', None)
    _SET_GEOLOCATION_OVERRIDE = 'Page.setGeolocationOverride'
    _CLEAR_GEOLOCATION_OVERRIDE = 'Page.clearGeolocationOverride'
    _HANDLE_JAVASCRIPT_DIALOG = 'Page.handleJavaScriptDialog'
    _SCREENSHOT = 'Page.captureScreenshot'
    _FRAME_STOPPED_LOADING = 'Page.frameStoppedLoading'

    @classmethod
    def enable(cls):
        return cls.create_frame(cls._ENABLE)

    @classmethod
    def disable(cls):
        return cls.create_frame(cls._DISABLE)

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
    def set_geolocation_override(cls, latitude, longitude, accuracy):
        return cls.create_frame(
            cls._SET_GEOLOCATION_OVERRIDE,
            {
                'latitude': latitude,
                'longitude': longitude,
                'accuracy': accuracy
            }
        )

    @classmethod
    def clear_geolocation_override(cls):
        return cls.create_frame(cls._CLEAR_GEOLOCATION_OVERRIDE)

    @classmethod
    def handle_javascript_dialog(cls, accept, prompt_text=None):
        return cls.create_frame(
            cls._HANDLE_JAVASCRIPT_DIALOG,
            {
                'accept': accept,
                'prompttext': prompt_text
            }
        )

    @classmethod
    def frame_stopped_loading(cls, frame_id):
        return cls.create_frame(
            cls._FRAME_STOPPED_LOADING, {'frameId': frame_id}
        )
