from kinder.controllers import (
    dict_controller,
)

import concentrator.changes.app_meta
from concentrator.changes.actions import (
    ChangesDetailPack,
    ChangesPack,
)
from concentrator.dict import (
    signals,
)
from concentrator.dict.actions import (
    ServicesPack,
)
from concentrator.update_conf.actions import (
    UpdateConfigPack,
)


def register_actions():
    """
    Метод регистрации Action'ов для приложения в котором описан
    """

    dict_controller.packs.extend([UpdateConfigPack(), ChangesDetailPack(), ChangesPack(), ServicesPack()])
