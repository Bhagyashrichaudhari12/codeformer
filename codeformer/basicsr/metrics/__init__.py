from copy import deepcopy

from codeformer.basicsr.metrics.psnr_ssim import calculate_psnr, calculate_ssim
from codeformer.basicsr.utils.registry import METRIC_REGISTRY

__all__ = ["calculate_psnr", "calculate_ssim"]


def calculate_metric(data, opt):
    """Calculate metric from data and options.

    Args:
        opt (dict): Configuration. It must constain:
            type (str): Model type.
    """
    opt = deepcopy(opt)
    metric_type = opt.pop("type")
    metric = METRIC_REGISTRY.get(metric_type)(**data, **opt)
    return metric
