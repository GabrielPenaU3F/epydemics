from src.domain.models.model import ContagionModel, VeronicaSShapedModel
from src.domain.models.model import DelayedSShapedModel
from src.domain.models.model import GoelOkumotoModel


class ModelRepository:

    models = {
        'contagion': ContagionModel(),
        'goel_okumoto': GoelOkumotoModel(),
        'delayed_s_shaped': DelayedSShapedModel(),
        'veronica_s_shaped': VeronicaSShapedModel()
    }

    @classmethod
    def retrieve_model(cls, model_id):
        return cls.models.get(model_id)

    @classmethod
    def list_models(cls):
        return list(cls.models.keys())
