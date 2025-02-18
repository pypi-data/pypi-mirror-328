from nonebot import get_plugin_config
from pydantic import BaseModel, ConfigDict

class Config(BaseModel):
    model_config = ConfigDict(
        coerce_numbers_to_str=True
    )

    # 百度智能云文字审核API
    # 申请网址：https://cloud.baidu.com/doc/ANTIPORN/s/dkk6wyt3z
    nonebot_plugin_bottle_api_key: str = ""
    nonebot_plugin_bottle_secret_key: str = ""
    # 是否将图片保存在本地
    nonebot_plugin_bottle_local_storage: bool = True
    # 瓶子最大字符数量
    nonebot_plugin_bottle_max_length: int = 0
    # 最大换行数量
    nonebot_plugin_bottle_max_return: int = 0
    # 字符与换行的比率
    nonebot_plugin_bottle_rt_rate: int = 0
    # 漂流瓶被评论时将不提示
    nonebot_plugin_bottle_disable_comment_prompt: bool = False
    # 所有人都可查看漂流瓶
    nonebot_plugin_bottle_everyone_can_read: bool = False
    # 关闭转发发送（False为开启转发）
    nonebot_plugin_bottle_disable_forward: bool = False

    # 是否启用审批
    nonebot_plugin_bottle_enable_approve: bool = False
    # webui 管理员用户名
    nonebot_plugin_bottle_admin_user: str = "admin"
    # webui 如果空就每次启动随机生成一个
    nonebot_plugin_bottle_admin_password: str = ""
    # webui 是否发送待审批消息至管理员
    nonebot_plugin_bottle_notice_admin: bool = True
    # 是否允许待审批的漂流瓶被用户查看
    nonebot_plugin_bottle_allow_pending_approval_to_be_viewed: bool = False

config: Config = get_plugin_config(Config)
api_key = config.nonebot_plugin_bottle_api_key
secret_key = config.nonebot_plugin_bottle_secret_key
local_storage = config.nonebot_plugin_bottle_local_storage
maxlen = config.nonebot_plugin_bottle_max_length
maxrt = config.nonebot_plugin_bottle_max_return
rtrate = config.nonebot_plugin_bottle_rt_rate
disable_comment_prompt = config.nonebot_plugin_bottle_disable_comment_prompt
everyone_can_read = config.nonebot_plugin_bottle_everyone_can_read
disable_forward = config.nonebot_plugin_bottle_disable_forward
enable_approve = config.nonebot_plugin_bottle_enable_approve
approve_notice_admin = config.nonebot_plugin_bottle_notice_admin
allow_pending_approval_bottle_to_be_viewed = config.nonebot_plugin_bottle_allow_pending_approval_to_be_viewed