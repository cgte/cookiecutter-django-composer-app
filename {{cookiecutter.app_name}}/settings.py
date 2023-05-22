from project_composer.marker import EnabledApplicationMarker


class APPNAMESettings(EnabledApplicationMarker):
    SETTING_VARIABLE_NAME = True

    @classmethod
    def setup(cls):
        super().setup()

        cls.INSTALLED_APPS.extend(
            [
                "this_app_name",
            ]
        )
