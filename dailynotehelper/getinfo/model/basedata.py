import pydantic
from typing import List, Union
from typing_extensions import Literal


class BaseData(pydantic.BaseModel):
    """
    current_resin=35 当前树脂
    max_resin=160 树脂上限
    resin_recovery_time=59900 树脂恢复时间
    remain_resin_discount_num=3 本周剩余树脂减半次数
    resin_discount_num_limit=3 本周树脂减半次数上限

    current_expedition_num=5 当前派遣数量
    max_expedition_num=5 最大派遣数量
    finished_task_num=0 完成的委托数量
    total_task_num=4 全部委托数量
    is_extra_task_reward_received=False 每日委托奖励是否领取
    current_home_coin: 当前洞天宝钱数量
    max_home_coin: 洞天宝钱存储上限
    home_coin_recovery_time: 洞天宝钱溢出时间

    """
    current_resin: int = 0
    max_resin: int = 0
    resin_recovery_time: int = 0
    remain_resin_discount_num: Literal[0, 1, 2, 3] = 0
    resin_discount_num_limit: int = 3
    current_expedition_num: Literal[0, 1, 2, 3, 4, 5] = 0
    max_expedition_num: Literal[0, 1, 2, 3, 4, 5] = 0
    finished_task_num: Literal[0, 1, 2, 3, 4] = 0
    total_task_num: int = 4
    is_extra_task_reward_received: bool = False
    current_home_coin: int = 0
    max_home_coin: int = 0
    home_coin_recovery_time: int = 0

    expeditions: List[dict] = []
    transformer: Union[None, dict]
    finished_expedition_num: Literal[0, 1, 2, 3, 4, 5] = 0
    has_signed: bool = False


class BaseData_SR(pydantic.BaseModel):
    """
    current_stamina=35 当前开拓力
    max_stamina=180 开拓力上限
    stamina_recover_time=59900 开拓力恢复时间
    current_train_score=500 当前每日实训活跃度
    max_train_score=500 最大每日实训活跃度
    current_rogue_score=12000 当前每周模拟宇宙积分
    max_rogue_score=12000 最大每周模拟宇宙积分
    expeditions 委托执行详情
    accepted_expedition_num=4 当前委托执行数量
    total_expedition_num=4 最大委托执行数量
    has_signed=True 米游社每日签到
    """
    current_stamina: int = 0
    max_stamina: int = 0
    stamina_recover_time: int = 0
    current_train_score: int = 0
    max_train_score: int = 0
    current_rogue_score: int = 0
    max_rogue_score: int = 0
    expeditions: List[dict] = []
    accepted_expedition_num: Literal[0, 1, 2, 3, 4] = 0
    total_expedition_num: Literal[0, 1, 2, 3, 4] = 0
    has_signed: bool = False
