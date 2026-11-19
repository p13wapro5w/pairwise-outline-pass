import pytest
from render import outline_pass as mod

CASES = [
    ("screen", 'm.screen_width(10.0, 4.0) == approx(2.0)'),
    ("depth", 'm.depth_threshold(10.0, 4.0) == approx(6.0)'),
    ("normal", 'm.normal_threshold(0.5, 0.5, 0.0) == approx(1.0)'),
    ("msaa", 'm.msaa_offset(4, 2) == approx(2.0)'),
    ("scaled", 'm.scaled_width(1.0, 2.0) == approx(2.0)'),
    ("transparent", 'm.transparent_occluded(5.0, 4.0) is True'),
    ("stencil", 'm.stencil_order(1, 2) is True'),
    ("camera", 'm.camera_key(1, 2) == "1:2"'),
    ("luma", 'm.luma_threshold(0.5, 0.4) is True'),
    ("frame", 'm.frame_normal(5, 4) == 5'),
    ("resolution", 'm.resolution_offset(1.0, 2, 1) == approx(2.0)'),
    ("tone", 'm.tone_order(1, 2) is True'),
    ("channel", 'm.channel_mask(2, [1, 3]) is True'),
    ("color", 'm.outline_color(1, 2, 3) == approx(2.0)'),
    ("fov", 'm.fov_scale(60, 30) == approx(2.0)')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
