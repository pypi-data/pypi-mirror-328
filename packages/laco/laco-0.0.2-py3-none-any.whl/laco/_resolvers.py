import math

import omegaconf

omegaconf.OmegaConf.register_new_resolver("sum", lambda *numbers: sum(numbers))
omegaconf.OmegaConf.register_new_resolver("min", lambda *numbers: min(numbers))
omegaconf.OmegaConf.register_new_resolver("max", lambda *numbers: max(numbers))
omegaconf.OmegaConf.register_new_resolver("div", lambda a, b: a / b)
omegaconf.OmegaConf.register_new_resolver("pow", lambda a, b: a**b)
omegaconf.OmegaConf.register_new_resolver("mod", lambda a, b: a % b)
omegaconf.OmegaConf.register_new_resolver("neg", lambda a: -a)
omegaconf.OmegaConf.register_new_resolver("reciprocal", lambda a: 1 / a)
omegaconf.OmegaConf.register_new_resolver("abs", lambda a: abs(a))
omegaconf.OmegaConf.register_new_resolver("round", lambda a, b: round(a, b))
omegaconf.OmegaConf.register_new_resolver(
    "math", lambda name, *args: getattr(math, name)(args)
)
