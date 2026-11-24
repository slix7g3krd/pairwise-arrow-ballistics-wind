import pytest
import gameplay.arrow_ballistics_wind as mod

CASES = [
    ("wind_each_frame", (1,)),
    ("tag_sample_lag", (1,)),
    ("sweep_by_distance", (1,)),
    ("trail_with_arrow", (1,)),
    ("predict_per_shooter", (1,)),
    ("integrate_fixed_step", (1,)),
    ("aim", (1,)),
    ("launch", (1,)),
    ("sweep", (1,)),
    ("hit", (1,)),
    ("validate_ballistic", (1,)),
    ("metrics", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("determinism", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
