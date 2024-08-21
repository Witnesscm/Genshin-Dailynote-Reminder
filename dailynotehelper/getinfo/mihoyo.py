from .client import Client
from .utils import *
from ..utils import log, _
from .parse_info import parse_info, parse_info_sr
from .model import BaseData, BaseData_SR

class Yuanshen(Client):
    def __init__(self, cookie: str = None):
        super().__init__(cookie)
        self.headers = get_headers(client_type='cn')
        self.client_type = 'cn'
        self.login_ticket: str = ''
        self.cookie_widget = {
            'stuid': self.cookie.get('ltuid') or self.cookie.get('account_id') or self.cookie.get('login_uid'),
            'stoken': self.cookie.get('stoken'),
            'mid': self.cookie.get('mid')
        }
        api_takumi = 'https://api-takumi.mihoyo.com'
        api_takumi_record = 'https://api-takumi-record.mihoyo.com'
        self.roles_api = api_takumi + '/binding/api/getUserGameRolesByCookie?game_biz=hk4e_cn'
        self.get_multitoken_api = api_takumi + '/auth/api/getMultiTokenByLoginTicket'
        self.dailynote_api = api_takumi_record + '/game_record/app/genshin/api/dailyNote'
        self.widget_api = api_takumi_record + '/game_record/app/genshin/aapi/widget/v2'

    def parse_widget_info(self, role):
        data = None
        try:
            r = request(
                'get',
                self.widget_api,
                headers=get_headers(ds=True, client_type='cn_widget'),
                cookies=self.cookie_widget
            )
            response = self.Response.parse_obj(r.json())
        except Exception as e:
            log.error(_('获取数据失败！'))
            log.error(e)
            message = e
            retcode = 999
        else:
            retcode = response.retcode
            if retcode == 0:
                data = BaseData.parse_obj(response.data)
                result = parse_info(data, role)
                message = "\n".join(result)
            else:
                message = f'Retcode: {retcode}\nMessage: {response.message}'

        return {
            'status': True if retcode == 0 else False,
            'retcode': retcode,
            'data': data,
            'message': message
        }


class StarRail(Client):
    def __init__(self, cookie: str = None):
        super().__init__(cookie)
        self.headers = get_headers(client_type='cn')
        self.client_type = 'cn'
        self.login_ticket: str = ''
        self.cookie_widget = {
            'stuid': self.cookie.get('ltuid') or self.cookie.get('account_id') or self.cookie.get('login_uid'),
            'stoken': self.cookie.get('stoken'),
            'mid': self.cookie.get('mid')
        }
        api_takumi = 'https://api-takumi.mihoyo.com'
        api_takumi_record = 'https://api-takumi-record.mihoyo.com'
        self.roles_api = api_takumi + '/binding/api/getUserGameRolesByCookie?game_biz=hkrpg_cn'
        self.dailynote_api = api_takumi_record + '/game_record/app/hkrpg/api/note'
        self.widget_api = api_takumi_record + '/game_record/app/hkrpg/aapi/widget'

    def parse_widget_info(self, role):
        data = None
        try:
            r = request(
                'get',
                self.widget_api,
                headers=get_headers(ds=True, client_type='cn_widget'),
                cookies=self.cookie_widget
            )
            response = self.Response.parse_obj(r.json())
        except Exception as e:
            log.error(_('获取数据失败！'))
            log.error(e)
            message = e
            retcode = 999
        else:
            retcode = response.retcode
            if retcode == 0:
                data = BaseData_SR.parse_obj(response.data)
                result = parse_info_sr(data, role)
                message = "\n".join(result)
            else:
                message = f'Retcode: {retcode}\nMessage: {response.message}'

        return {
            'status': True if retcode == 0 else False,
            'retcode': retcode,
            'data': data,
            'message': message
        }
