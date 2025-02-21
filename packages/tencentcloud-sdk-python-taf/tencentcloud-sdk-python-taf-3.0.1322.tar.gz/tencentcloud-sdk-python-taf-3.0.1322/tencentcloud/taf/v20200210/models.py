# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class Device(AbstractModel):
    """业务入参

    """

    def __init__(self):
        r"""
        :param _DeviceId: 业务入参id
        :type DeviceId: str
        :param _DeviceType: 业务入参类型
        :type DeviceType: int
        """
        self._DeviceId = None
        self._DeviceType = None

    @property
    def DeviceId(self):
        """业务入参id
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def DeviceType(self):
        """业务入参类型
        :rtype: int
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._DeviceType = params.get("DeviceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputBusinessEncryptData(AbstractModel):
    """业务入参

    """

    def __init__(self):
        r"""
        :param _EncryptMethod: 加密方式；0：AES;1:DES
        :type EncryptMethod: int
        :param _EncryptData: 业务数据加密字符串
        :type EncryptData: str
        :param _EncryptMode: 加密模式；0：ECB,1:CBC;2:CTR;3:CFB;4:OFB
        :type EncryptMode: int
        :param _PaddingType: 填充模式;0:ZERO ;1:PKCS5;3:PKCS7
        :type PaddingType: int
        """
        self._EncryptMethod = None
        self._EncryptData = None
        self._EncryptMode = None
        self._PaddingType = None

    @property
    def EncryptMethod(self):
        """加密方式；0：AES;1:DES
        :rtype: int
        """
        return self._EncryptMethod

    @EncryptMethod.setter
    def EncryptMethod(self, EncryptMethod):
        self._EncryptMethod = EncryptMethod

    @property
    def EncryptData(self):
        """业务数据加密字符串
        :rtype: str
        """
        return self._EncryptData

    @EncryptData.setter
    def EncryptData(self, EncryptData):
        self._EncryptData = EncryptData

    @property
    def EncryptMode(self):
        """加密模式；0：ECB,1:CBC;2:CTR;3:CFB;4:OFB
        :rtype: int
        """
        return self._EncryptMode

    @EncryptMode.setter
    def EncryptMode(self, EncryptMode):
        self._EncryptMode = EncryptMode

    @property
    def PaddingType(self):
        """填充模式;0:ZERO ;1:PKCS5;3:PKCS7
        :rtype: int
        """
        return self._PaddingType

    @PaddingType.setter
    def PaddingType(self, PaddingType):
        self._PaddingType = PaddingType


    def _deserialize(self, params):
        self._EncryptMethod = params.get("EncryptMethod")
        self._EncryptData = params.get("EncryptData")
        self._EncryptMode = params.get("EncryptMode")
        self._PaddingType = params.get("PaddingType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputRecognizeTargetAudience(AbstractModel):
    """流量反欺诈-验准入参

    """

    def __init__(self):
        r"""
        :param _ModelIdList: 模型ID列表
        :type ModelIdList: list of int
        :param _Uid: 设备ID，AccountType指定的类型
        :type Uid: str
        :param _AccountType: 设备号类型，1.imei 2.imeiMd5（小写后转MD5转小写）3.idfa， 4.idfaMd5（大写后转MD5转小写），5.手机号,256.其它
        :type AccountType: int
        :param _Ip: 用户IP
        :type Ip: str
        :param _Os: 操作系统类型(unknown，android，ios，windows)
        :type Os: str
        :param _Osv: 操作系统版本
        :type Osv: str
        :param _Lat: 纬度
        :type Lat: str
        :param _Lon: 经度
        :type Lon: str
        :param _DeviceModel: 设备型号(MI 6)
        :type DeviceModel: str
        :param _BidFloor: 竞价底价
        :type BidFloor: int
        :param _Age: 年龄
        :type Age: int
        :param _Gender: 性别(1.MALE 2.FEMALE)
        :type Gender: int
        :param _Location: 用户地址
        :type Location: str
        :param _DeliveryMode: 投放模式（0=PDB，1=PD，2=RTB，10=其他）
        :type DeliveryMode: int
        :param _AdvertisingType: 广告位类型<br />（0=前贴片，1=开屏广告，2=网页头部广告、3=网页中部广告、4=网页底部广告、5=悬浮广告、10=其它）
        :type AdvertisingType: int
        :param _Mac: mac地址，建议提供
        :type Mac: str
        :param _Phone: 电话号码
        :type Phone: str
        :param _Ua: 浏览器类型
        :type Ua: str
        :param _App: 客户端应用
        :type App: str
        :param _Package: 应用包名
        :type Package: str
        :param _Maker: 设备制造商
        :type Maker: str
        :param _DeviceType: 设备类型（PHONE,TABLET）
        :type DeviceType: str
        :param _AccessMode: 入网方式(wifi,4g,3g,2g)
        :type AccessMode: str
        :param _Sp: 运营商(1.移动 2.联通 3.电信等)
        :type Sp: int
        :param _DeviceW: 设备屏幕分辨率宽度像素数
        :type DeviceW: int
        :param _DeviceH: 设备屏幕分辨率高度像素数
        :type DeviceH: int
        :param _FullScreen: 是否全屏插广告(0-否，1-是)
        :type FullScreen: int
        :param _ImpBannerW: 广告位宽度
        :type ImpBannerW: int
        :param _ImpBannerH: 广告位高度
        :type ImpBannerH: int
        :param _Url: 网址
        :type Url: str
        :param _Context: 上下文信息
        :type Context: str
        :param _Channel: 渠道
        :type Channel: str
        :param _ReqId: 请求ID
        :type ReqId: str
        :param _ReqMd5: 请求ID的md5值
        :type ReqMd5: str
        :param _AdType: ad_type
        :type AdType: int
        :param _AppName: app名称
        :type AppName: str
        :param _AppVer: app版本描述
        :type AppVer: str
        :param _ReqType: 竞价模式1：rtb 2:pd
        :type ReqType: int
        :param _IsAuthorized: 用户是否授权,1为授权，0为未授权
        :type IsAuthorized: int
        :param _DeviceList: 设备信息
        :type DeviceList: list of Device
        """
        self._ModelIdList = None
        self._Uid = None
        self._AccountType = None
        self._Ip = None
        self._Os = None
        self._Osv = None
        self._Lat = None
        self._Lon = None
        self._DeviceModel = None
        self._BidFloor = None
        self._Age = None
        self._Gender = None
        self._Location = None
        self._DeliveryMode = None
        self._AdvertisingType = None
        self._Mac = None
        self._Phone = None
        self._Ua = None
        self._App = None
        self._Package = None
        self._Maker = None
        self._DeviceType = None
        self._AccessMode = None
        self._Sp = None
        self._DeviceW = None
        self._DeviceH = None
        self._FullScreen = None
        self._ImpBannerW = None
        self._ImpBannerH = None
        self._Url = None
        self._Context = None
        self._Channel = None
        self._ReqId = None
        self._ReqMd5 = None
        self._AdType = None
        self._AppName = None
        self._AppVer = None
        self._ReqType = None
        self._IsAuthorized = None
        self._DeviceList = None

    @property
    def ModelIdList(self):
        """模型ID列表
        :rtype: list of int
        """
        return self._ModelIdList

    @ModelIdList.setter
    def ModelIdList(self, ModelIdList):
        self._ModelIdList = ModelIdList

    @property
    def Uid(self):
        """设备ID，AccountType指定的类型
        :rtype: str
        """
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid

    @property
    def AccountType(self):
        """设备号类型，1.imei 2.imeiMd5（小写后转MD5转小写）3.idfa， 4.idfaMd5（大写后转MD5转小写），5.手机号,256.其它
        :rtype: int
        """
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType

    @property
    def Ip(self):
        """用户IP
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Os(self):
        """操作系统类型(unknown，android，ios，windows)
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Osv(self):
        """操作系统版本
        :rtype: str
        """
        return self._Osv

    @Osv.setter
    def Osv(self, Osv):
        self._Osv = Osv

    @property
    def Lat(self):
        """纬度
        :rtype: str
        """
        return self._Lat

    @Lat.setter
    def Lat(self, Lat):
        self._Lat = Lat

    @property
    def Lon(self):
        """经度
        :rtype: str
        """
        return self._Lon

    @Lon.setter
    def Lon(self, Lon):
        self._Lon = Lon

    @property
    def DeviceModel(self):
        """设备型号(MI 6)
        :rtype: str
        """
        return self._DeviceModel

    @DeviceModel.setter
    def DeviceModel(self, DeviceModel):
        self._DeviceModel = DeviceModel

    @property
    def BidFloor(self):
        """竞价底价
        :rtype: int
        """
        return self._BidFloor

    @BidFloor.setter
    def BidFloor(self, BidFloor):
        self._BidFloor = BidFloor

    @property
    def Age(self):
        """年龄
        :rtype: int
        """
        return self._Age

    @Age.setter
    def Age(self, Age):
        self._Age = Age

    @property
    def Gender(self):
        """性别(1.MALE 2.FEMALE)
        :rtype: int
        """
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender

    @property
    def Location(self):
        """用户地址
        :rtype: str
        """
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def DeliveryMode(self):
        """投放模式（0=PDB，1=PD，2=RTB，10=其他）
        :rtype: int
        """
        return self._DeliveryMode

    @DeliveryMode.setter
    def DeliveryMode(self, DeliveryMode):
        self._DeliveryMode = DeliveryMode

    @property
    def AdvertisingType(self):
        """广告位类型<br />（0=前贴片，1=开屏广告，2=网页头部广告、3=网页中部广告、4=网页底部广告、5=悬浮广告、10=其它）
        :rtype: int
        """
        return self._AdvertisingType

    @AdvertisingType.setter
    def AdvertisingType(self, AdvertisingType):
        self._AdvertisingType = AdvertisingType

    @property
    def Mac(self):
        """mac地址，建议提供
        :rtype: str
        """
        return self._Mac

    @Mac.setter
    def Mac(self, Mac):
        self._Mac = Mac

    @property
    def Phone(self):
        """电话号码
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Ua(self):
        """浏览器类型
        :rtype: str
        """
        return self._Ua

    @Ua.setter
    def Ua(self, Ua):
        self._Ua = Ua

    @property
    def App(self):
        """客户端应用
        :rtype: str
        """
        return self._App

    @App.setter
    def App(self, App):
        self._App = App

    @property
    def Package(self):
        """应用包名
        :rtype: str
        """
        return self._Package

    @Package.setter
    def Package(self, Package):
        self._Package = Package

    @property
    def Maker(self):
        """设备制造商
        :rtype: str
        """
        return self._Maker

    @Maker.setter
    def Maker(self, Maker):
        self._Maker = Maker

    @property
    def DeviceType(self):
        """设备类型（PHONE,TABLET）
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def AccessMode(self):
        """入网方式(wifi,4g,3g,2g)
        :rtype: str
        """
        return self._AccessMode

    @AccessMode.setter
    def AccessMode(self, AccessMode):
        self._AccessMode = AccessMode

    @property
    def Sp(self):
        """运营商(1.移动 2.联通 3.电信等)
        :rtype: int
        """
        return self._Sp

    @Sp.setter
    def Sp(self, Sp):
        self._Sp = Sp

    @property
    def DeviceW(self):
        """设备屏幕分辨率宽度像素数
        :rtype: int
        """
        return self._DeviceW

    @DeviceW.setter
    def DeviceW(self, DeviceW):
        self._DeviceW = DeviceW

    @property
    def DeviceH(self):
        """设备屏幕分辨率高度像素数
        :rtype: int
        """
        return self._DeviceH

    @DeviceH.setter
    def DeviceH(self, DeviceH):
        self._DeviceH = DeviceH

    @property
    def FullScreen(self):
        """是否全屏插广告(0-否，1-是)
        :rtype: int
        """
        return self._FullScreen

    @FullScreen.setter
    def FullScreen(self, FullScreen):
        self._FullScreen = FullScreen

    @property
    def ImpBannerW(self):
        """广告位宽度
        :rtype: int
        """
        return self._ImpBannerW

    @ImpBannerW.setter
    def ImpBannerW(self, ImpBannerW):
        self._ImpBannerW = ImpBannerW

    @property
    def ImpBannerH(self):
        """广告位高度
        :rtype: int
        """
        return self._ImpBannerH

    @ImpBannerH.setter
    def ImpBannerH(self, ImpBannerH):
        self._ImpBannerH = ImpBannerH

    @property
    def Url(self):
        """网址
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Context(self):
        """上下文信息
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Channel(self):
        """渠道
        :rtype: str
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def ReqId(self):
        """请求ID
        :rtype: str
        """
        return self._ReqId

    @ReqId.setter
    def ReqId(self, ReqId):
        self._ReqId = ReqId

    @property
    def ReqMd5(self):
        """请求ID的md5值
        :rtype: str
        """
        return self._ReqMd5

    @ReqMd5.setter
    def ReqMd5(self, ReqMd5):
        self._ReqMd5 = ReqMd5

    @property
    def AdType(self):
        """ad_type
        :rtype: int
        """
        return self._AdType

    @AdType.setter
    def AdType(self, AdType):
        self._AdType = AdType

    @property
    def AppName(self):
        """app名称
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def AppVer(self):
        """app版本描述
        :rtype: str
        """
        return self._AppVer

    @AppVer.setter
    def AppVer(self, AppVer):
        self._AppVer = AppVer

    @property
    def ReqType(self):
        """竞价模式1：rtb 2:pd
        :rtype: int
        """
        return self._ReqType

    @ReqType.setter
    def ReqType(self, ReqType):
        self._ReqType = ReqType

    @property
    def IsAuthorized(self):
        """用户是否授权,1为授权，0为未授权
        :rtype: int
        """
        return self._IsAuthorized

    @IsAuthorized.setter
    def IsAuthorized(self, IsAuthorized):
        self._IsAuthorized = IsAuthorized

    @property
    def DeviceList(self):
        """设备信息
        :rtype: list of Device
        """
        return self._DeviceList

    @DeviceList.setter
    def DeviceList(self, DeviceList):
        self._DeviceList = DeviceList


    def _deserialize(self, params):
        self._ModelIdList = params.get("ModelIdList")
        self._Uid = params.get("Uid")
        self._AccountType = params.get("AccountType")
        self._Ip = params.get("Ip")
        self._Os = params.get("Os")
        self._Osv = params.get("Osv")
        self._Lat = params.get("Lat")
        self._Lon = params.get("Lon")
        self._DeviceModel = params.get("DeviceModel")
        self._BidFloor = params.get("BidFloor")
        self._Age = params.get("Age")
        self._Gender = params.get("Gender")
        self._Location = params.get("Location")
        self._DeliveryMode = params.get("DeliveryMode")
        self._AdvertisingType = params.get("AdvertisingType")
        self._Mac = params.get("Mac")
        self._Phone = params.get("Phone")
        self._Ua = params.get("Ua")
        self._App = params.get("App")
        self._Package = params.get("Package")
        self._Maker = params.get("Maker")
        self._DeviceType = params.get("DeviceType")
        self._AccessMode = params.get("AccessMode")
        self._Sp = params.get("Sp")
        self._DeviceW = params.get("DeviceW")
        self._DeviceH = params.get("DeviceH")
        self._FullScreen = params.get("FullScreen")
        self._ImpBannerW = params.get("ImpBannerW")
        self._ImpBannerH = params.get("ImpBannerH")
        self._Url = params.get("Url")
        self._Context = params.get("Context")
        self._Channel = params.get("Channel")
        self._ReqId = params.get("ReqId")
        self._ReqMd5 = params.get("ReqMd5")
        self._AdType = params.get("AdType")
        self._AppName = params.get("AppName")
        self._AppVer = params.get("AppVer")
        self._ReqType = params.get("ReqType")
        self._IsAuthorized = params.get("IsAuthorized")
        if params.get("DeviceList") is not None:
            self._DeviceList = []
            for item in params.get("DeviceList"):
                obj = Device()
                obj._deserialize(item)
                self._DeviceList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManagePortraitRiskInput(AbstractModel):
    """业务入参

    """

    def __init__(self):
        r"""
        :param _PostTime: 请求时间戳秒
        :type PostTime: int
        :param _UserIp: 用户公网ip（仅支持IPv4）
        :type UserIp: str
        :param _Channel: 渠道号
        :type Channel: int
        """
        self._PostTime = None
        self._UserIp = None
        self._Channel = None

    @property
    def PostTime(self):
        """请求时间戳秒
        :rtype: int
        """
        return self._PostTime

    @PostTime.setter
    def PostTime(self, PostTime):
        self._PostTime = PostTime

    @property
    def UserIp(self):
        """用户公网ip（仅支持IPv4）
        :rtype: str
        """
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp

    @property
    def Channel(self):
        """渠道号
        :rtype: int
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel


    def _deserialize(self, params):
        self._PostTime = params.get("PostTime")
        self._UserIp = params.get("UserIp")
        self._Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManagePortraitRiskOutput(AbstractModel):
    """业务出参

    """

    def __init__(self):
        r"""
        :param _Code: 返回码（0，成功，其他失败）
        :type Code: int
        :param _Message: 返回码对应的信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _Value: 结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: :class:`tencentcloud.taf.v20200210.models.ManagePortraitRiskValueOutput`
        """
        self._Code = None
        self._Message = None
        self._Value = None

    @property
    def Code(self):
        """返回码（0，成功，其他失败）
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        """返回码对应的信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Value(self):
        """结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.taf.v20200210.models.ManagePortraitRiskValueOutput`
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        if params.get("Value") is not None:
            self._Value = ManagePortraitRiskValueOutput()
            self._Value._deserialize(params.get("Value"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManagePortraitRiskRequest(AbstractModel):
    """ManagePortraitRisk请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BusinessSecurityData: 业务入参
        :type BusinessSecurityData: :class:`tencentcloud.taf.v20200210.models.ManagePortraitRiskInput`
        """
        self._BusinessSecurityData = None

    @property
    def BusinessSecurityData(self):
        """业务入参
        :rtype: :class:`tencentcloud.taf.v20200210.models.ManagePortraitRiskInput`
        """
        return self._BusinessSecurityData

    @BusinessSecurityData.setter
    def BusinessSecurityData(self, BusinessSecurityData):
        self._BusinessSecurityData = BusinessSecurityData


    def _deserialize(self, params):
        if params.get("BusinessSecurityData") is not None:
            self._BusinessSecurityData = ManagePortraitRiskInput()
            self._BusinessSecurityData._deserialize(params.get("BusinessSecurityData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManagePortraitRiskResponse(AbstractModel):
    """ManagePortraitRisk返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 业务出参
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.taf.v20200210.models.ManagePortraitRiskOutput`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """业务出参
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.taf.v20200210.models.ManagePortraitRiskOutput`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = ManagePortraitRiskOutput()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ManagePortraitRiskValueOutput(AbstractModel):
    """业务出参

    """

    def __init__(self):
        r"""
        :param _UserIp: 对应的IP
        :type UserIp: str
        :param _Level: 返回风险等级, 0 - 4，0代表无风险，数值越大，风险越高
        :type Level: int
        """
        self._UserIp = None
        self._Level = None

    @property
    def UserIp(self):
        """对应的IP
        :rtype: str
        """
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp

    @property
    def Level(self):
        """返回风险等级, 0 - 4，0代表无风险，数值越大，风险越高
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level


    def _deserialize(self, params):
        self._UserIp = params.get("UserIp")
        self._Level = params.get("Level")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputRecognizeTargetAudience(AbstractModel):
    """流量反欺诈-验准返回值

    """

    def __init__(self):
        r"""
        :param _Code: 返回码（0，成功，其他失败）
        :type Code: int
        :param _Message: 返回码对应的信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _Value: 返回模型结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: list of OutputRecognizeTargetAudienceValue
        """
        self._Code = None
        self._Message = None
        self._Value = None

    @property
    def Code(self):
        """返回码（0，成功，其他失败）
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        """返回码对应的信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Value(self):
        """返回模型结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of OutputRecognizeTargetAudienceValue
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        if params.get("Value") is not None:
            self._Value = []
            for item in params.get("Value"):
                obj = OutputRecognizeTargetAudienceValue()
                obj._deserialize(item)
                self._Value.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputRecognizeTargetAudienceValue(AbstractModel):
    """流量反欺诈-验准返回的查询分值

    """

    def __init__(self):
        r"""
        :param _ModelId: 模型ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelId: int
        :param _IsFound: 是否正常返回结果
注意：此字段可能返回 null，表示取不到有效值。
        :type IsFound: int
        :param _Score: 返回分值
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: float
        :param _ModelType: 模型类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelType: int
        :param _Uid: 入参Uid
注意：此字段可能返回 null，表示取不到有效值。
        :type Uid: str
        """
        self._ModelId = None
        self._IsFound = None
        self._Score = None
        self._ModelType = None
        self._Uid = None

    @property
    def ModelId(self):
        """模型ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def IsFound(self):
        """是否正常返回结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsFound

    @IsFound.setter
    def IsFound(self, IsFound):
        self._IsFound = IsFound

    @property
    def Score(self):
        """返回分值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def ModelType(self):
        """模型类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ModelType

    @ModelType.setter
    def ModelType(self, ModelType):
        self._ModelType = ModelType

    @property
    def Uid(self):
        """入参Uid
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid


    def _deserialize(self, params):
        self._ModelId = params.get("ModelId")
        self._IsFound = params.get("IsFound")
        self._Score = params.get("Score")
        self._ModelType = params.get("ModelType")
        self._Uid = params.get("Uid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeCustomizedAudienceRequest(AbstractModel):
    """RecognizeCustomizedAudience请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BspData: 业务入参
        :type BspData: :class:`tencentcloud.taf.v20200210.models.InputRecognizeTargetAudience`
        """
        self._BspData = None

    @property
    def BspData(self):
        """业务入参
        :rtype: :class:`tencentcloud.taf.v20200210.models.InputRecognizeTargetAudience`
        """
        return self._BspData

    @BspData.setter
    def BspData(self, BspData):
        self._BspData = BspData


    def _deserialize(self, params):
        if params.get("BspData") is not None:
            self._BspData = InputRecognizeTargetAudience()
            self._BspData._deserialize(params.get("BspData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeCustomizedAudienceResponse(AbstractModel):
    """RecognizeCustomizedAudience返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 业务出参
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.taf.v20200210.models.OutputRecognizeTargetAudience`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """业务出参
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.taf.v20200210.models.OutputRecognizeTargetAudience`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = OutputRecognizeTargetAudience()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class RecognizePreciseTargetAudienceRequest(AbstractModel):
    """RecognizePreciseTargetAudience请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BspData: 业务数据
        :type BspData: :class:`tencentcloud.taf.v20200210.models.InputRecognizeTargetAudience`
        """
        self._BspData = None

    @property
    def BspData(self):
        """业务数据
        :rtype: :class:`tencentcloud.taf.v20200210.models.InputRecognizeTargetAudience`
        """
        return self._BspData

    @BspData.setter
    def BspData(self, BspData):
        self._BspData = BspData


    def _deserialize(self, params):
        if params.get("BspData") is not None:
            self._BspData = InputRecognizeTargetAudience()
            self._BspData._deserialize(params.get("BspData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizePreciseTargetAudienceResponse(AbstractModel):
    """RecognizePreciseTargetAudience返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 回包数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.taf.v20200210.models.OutputRecognizeTargetAudience`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """回包数据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.taf.v20200210.models.OutputRecognizeTargetAudience`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = OutputRecognizeTargetAudience()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class RecognizeTargetAudienceRequest(AbstractModel):
    """RecognizeTargetAudience请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BspData: 业务数据
        :type BspData: :class:`tencentcloud.taf.v20200210.models.InputRecognizeTargetAudience`
        :param _BusinessEncryptData: 业务加密数据
        :type BusinessEncryptData: :class:`tencentcloud.taf.v20200210.models.InputBusinessEncryptData`
        """
        self._BspData = None
        self._BusinessEncryptData = None

    @property
    def BspData(self):
        """业务数据
        :rtype: :class:`tencentcloud.taf.v20200210.models.InputRecognizeTargetAudience`
        """
        return self._BspData

    @BspData.setter
    def BspData(self, BspData):
        self._BspData = BspData

    @property
    def BusinessEncryptData(self):
        """业务加密数据
        :rtype: :class:`tencentcloud.taf.v20200210.models.InputBusinessEncryptData`
        """
        return self._BusinessEncryptData

    @BusinessEncryptData.setter
    def BusinessEncryptData(self, BusinessEncryptData):
        self._BusinessEncryptData = BusinessEncryptData


    def _deserialize(self, params):
        if params.get("BspData") is not None:
            self._BspData = InputRecognizeTargetAudience()
            self._BspData._deserialize(params.get("BspData"))
        if params.get("BusinessEncryptData") is not None:
            self._BusinessEncryptData = InputBusinessEncryptData()
            self._BusinessEncryptData._deserialize(params.get("BusinessEncryptData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeTargetAudienceResponse(AbstractModel):
    """RecognizeTargetAudience返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 回包数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.taf.v20200210.models.OutputRecognizeTargetAudience`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """回包数据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.taf.v20200210.models.OutputRecognizeTargetAudience`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = OutputRecognizeTargetAudience()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")