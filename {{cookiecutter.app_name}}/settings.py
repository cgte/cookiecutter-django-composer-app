from project_composer.marker import EnabledApplicationMarker


class {{cookiecutter.settings_name}}Settings(EnabledApplicationMarker):
    SETTING_VARIABLE_NAME = True

    @classmethod
    def setup(cls):
        super().setup()

        cls.INSTALLED_APPS.extend(
            [
                "{{cookiecutter.app_name}}",
            ]
        )
