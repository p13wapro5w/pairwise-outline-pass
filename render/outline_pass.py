"""第 61 批：角色贴近亮墙，外描边忽粗忽细，转身到背影又整圈消失：描边宽度按世..."""

def screen_width(world_width, distance):
    """屏幕空间描边宽度。"""
    raise NotImplementedError("TODO: screen_width")

def depth_threshold(near, far):
    """深度阈值。"""
    raise NotImplementedError("TODO: depth_threshold")

def normal_threshold(nx, ny, nz):
    """法线阈值。"""
    raise NotImplementedError("TODO: normal_threshold")

def msaa_offset(sample, pixel):
    """MSAA 采样偏移。"""
    raise NotImplementedError("TODO: msaa_offset")

def scaled_width(width, scale):
    """角色缩放描边。"""
    raise NotImplementedError("TODO: scaled_width")

def transparent_occluded(depth, transparent_depth):
    """透明遮挡。"""
    raise NotImplementedError("TODO: transparent_occluded")

def stencil_order(write_pass, read_pass):
    """模板顺序。"""
    raise NotImplementedError("TODO: stencil_order")

def camera_key(camera_id, outline_id):
    """多相机描边键。"""
    raise NotImplementedError("TODO: camera_key")

def luma_threshold(color, threshold):
    """亮度阈值。"""
    raise NotImplementedError("TODO: luma_threshold")

def frame_normal(current, previous):
    """逐帧法线。"""
    raise NotImplementedError("TODO: frame_normal")

def resolution_offset(offset, width, base_width):
    """分辨率偏移。"""
    raise NotImplementedError("TODO: resolution_offset")

def tone_order(outline_pass, tonemap_pass):
    """色调映射顺序。"""
    raise NotImplementedError("TODO: tone_order")

def channel_mask(channel, used):
    """通道隔离。"""
    raise NotImplementedError("TODO: channel_mask")

def outline_color(r, g, b):
    """描边颜色。"""
    raise NotImplementedError("TODO: outline_color")

def fov_scale(fov, base_fov):
    """FOV 缩放。"""
    raise NotImplementedError("TODO: fov_scale")
