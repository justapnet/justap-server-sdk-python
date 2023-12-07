# coding: utf-8

"""
    Justap API

    欢迎阅读 Justap Api 文档  Justap 是为移动端应用和PC端应用打造的下一代聚合支付SAAS服务平台，通过一个 SDK 即可快速的支持各种形式的应用，并且一次接口完成多个不同支付渠道的接入。平台除了支持服务商子商户模式，同时还对商家自有商户（即自己前往微信、支付宝等机构开户）提供了完整的支持。  感谢您的支持，我们将不断探索，为您提供更优质的服务！如需技术支持可前往商户中心提交工单，支持工程师会尽快与您取得联系！  # 文档说明 采用 REST 风格设计。所有接口请求地址都是可预期的以及面向资源的。使用规范的 HTTP 响应代码来表示请求结果的正确或错误信息。使用 HTTP 内置的特性，如 HTTP Authentication 和 HTTP 请求方法让接口易于理解。  ## HTTP 状态码 HTTP 状态码可以用于表明服务的状态。服务器返回的 HTTP 状态码遵循 [RFC 7231](http://tools.ietf.org/html/rfc7231#section-6) 和 [IANA Status Code Registry](http://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml) 标准。  ## 认证 在调用 API 时，必须提供 API Key 作为每个请求的身份验证。你可以在管理平台内管理你的 API Key。API Key 是商户在系统中的身份标识，请安全存储，确保其不要被泄露。如需获取或更新 API Key ，也可以在商户中心内进行操作。 Api Key 在使用自定义的 HTTP Header 进行传递。  ``` X-Justap-Api-Key ```  API Key 分为 live 和 test 两种模式。分别对应真实交易环境和模拟测试交易环境并且可以实时切换。 测试模式下的 API Key 会模拟交易等请求，但是不会产生任何真实交易行为和费用，便于调试和接入。  **⚠️ 注意**：在使用 live 模式前，需要先前往 `商户中心 -> 应用设置 -> 开发参数` 开启 live 模式。  <SecurityDefinitions />  ## 请求类型 所有的 API 请求只支持 HTTPS 方式调用。  ## 路由参数 路由参数是指出现在 URL 路径中的可变变量。在本文档中，使用 `{}` 包裹的部分。 例如： `{charge_id}`，在实际使用是，需要将 `{charge_id}` 替换为实际值 `charge_8a8sdf888888`  ## MIME Type MIME 类型用于指示服务器返回的数据格式。服务器目前默认采用 `application/json`。  例如: ``` application/json ```  ## 错误 服务器使用 HTTP 状态码 (status code) 来表明一个 API 请求的成功或失败状态。返回 HTTP 2XX 表明 API 请求成功。返回 HTTP 4XX 表明在请求 API 时提供了错误信息，例如参数缺失、参数错误、支付渠道错误等。返回 HTTP 5XX 表明 API 请求时，服务器发生了错误。 在返回错误的状态码时，回同时返回一些错误信息提示出错原因。  具体的错误码我们正在整理当中。  ## 分页 所有的 Justap 资源都可以被 list API 方法支持，例如分页 charges 和 refunds。这些 list API 方法拥有相同的数据结构。Justap 是基于 cursor 的分页机制，使用参数 starting_after 来决定列表从何处开始，使用参数 ending_before 来决定列表从何处结束。  ## 参数说明 请求参数中包含的以下字段释义请参考：  - REQUIRED: 必填参数 - OPTIONAL: 可选参数，可以在请求当前接口时按需传入 - CONDITIONAL: 在某些条件下必传 - RESPONSE-ONLY: 标示该参数仅在接口返回参数中出现，调用 API 时无需传入  # 如何保证幂等性 如果发生请求超时或服务器内部错误，客户端可能会尝试重发请求。您可以在请求中设置 ClientToken 参数避免多次重试带来重复操作的问题。  ## 什么是幂等性 在数学计算或者计算机科学中，幂等性（idempotence）是指相同操作或资源在一次或多次请求中具有同样效果的作用。幂等性是在分布式系统设计中具有十分重要的地位。  ## 保证幂等性 通常情况下，客户端只需要在500（InternalErrorInternalError）或503（ServiceUnavailable）错误，或者无法获取响应结果时重试。充实时您可以从客户端生成一个参数值不超过64个的ASCII字符，并将值赋予 ClientToken，保证重试请求的幂等性。  ## ClientToken 详解 ClientToken参数的详细信息如下所示。  - ClientToken 是一个由客户端生成的唯一的、大小写敏感、不超过64个ASCII字符的字符串。例如，`ClientToken=123e4567-e89b-12d3-a456-426655440000`。 - 如果您提供了一个已经使用过的 ClientToken，但其他请求参数**有变化**，则服务器会返回 IdempotentParameterMismatch 的错误代码。 - 如果您提供了一个已经使用过的 ClientToken，且其他请求参数**不变**，则服务器会尝试返回 ClientToken 对应的记录。  ## API列表 以下为部分包含了 ClientToken 参数的API，供您参考。具体哪些API支持 ClientToken 参数请以各 API 文档为准，此处不一一列举。  - [申请退款接口](https://www.justap.cn/docs#operation/TradeService_Refunds)  # 签名 为保证安全，JUSTAP 所有接口均需要对请求进行签名。服务器收到请求后进行签名的验证。如果签名验证不通过，将会拒绝处理请求，并返回 401 Unauthorized。  签名算法：  ``` base64Encode(hamc-sha256(md5(请求 body + 请求时间戳 + 一次性随机字符串) + 一次性随机字符串)) ```  ## 准备 首先需要在 Justap 创建一个应用，商户需要生成一对 RSA 密钥对，并将公钥配置到 `商户中心 -> 开发配置`。 RSA 可以使用支付宝提供的 [密钥生成工具](https://opendocs.alipay.com/common/02kipl) 来生成。  商户在使用时，可以按照下述步骤生成请求的签名。   ## 算法描述: - 在请求发送前，取完整的**请求 body** - 生成一个随机的32位字符串，得到 **一次性随机字符串** - 获取当前时间的时间戳，得到 **请求时间戳** - 在请求字符串后面拼接上 **请求时间戳** 和 **一次性随机字符串**，得到 **待 Hash 字符串** - 对 **待 Hash 字符串** 转换为 utf8 编码并计算 md5，得到 **待签名字符串** - **待签名字符串** 后面拼接上 一次性随机字符串，得到完整的 **待签名字符串** - 使用商户 RSA 私钥，对 **待签名字符串** 计算签名，并对 结果 进行 base64 编码，即可得到 **签名**  ## 设置HTTP头 Justap 要求请求通过 自定义头部 来传递签名。具体定义如下:  ``` X-Justap-Signature: 签名 X-Justap-Request-Time: 请求时间戳 X-Justap-Nonce: 一次性随机字符串 X-Justap-Body-Hash: 待签名字符串 ```  具体的签名算法实现，可参考我们提供的各语言 SDK。  # WebHooks   # noqa: E501

    OpenAPI spec version: 1.0
    Contact: support@justap.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from justap_server_sdk_python.configuration import Configuration


class V1CreateChargeRequestExtra(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'alipay_app': 'V1ExtraAlipayApp',
        'alipay_face': 'V1ExtraAlipayFace',
        'alipay_lite': 'V1ExtraAlipayLite',
        'alipay_page': 'V1ExtraAlipayPage',
        'alipay_qr': 'V1ExtraAlipayQr',
        'alipay_scan': 'V1ExtraAlipayScan',
        'alipay_wap': 'V1ExtraAlipayWap',
        'wechatpay_app': 'V1ExtraWechatpayApp',
        'wechatpay_h5': 'V1ExtraWechatpayH5',
        'wechatpay_jsapi': 'V1ExtraWechatpayJsapi',
        'wechatpay_lite': 'V1ExtraWechatpayLite',
        'wechatpay_native': 'V1ExtraWechatpayNative',
        'wechatpay_scan': 'V1ExtraWechatpayScan'
    }

    attribute_map = {
        'alipay_app': 'alipay_app',
        'alipay_face': 'alipay_face',
        'alipay_lite': 'alipay_lite',
        'alipay_page': 'alipay_page',
        'alipay_qr': 'alipay_qr',
        'alipay_scan': 'alipay_scan',
        'alipay_wap': 'alipay_wap',
        'wechatpay_app': 'wechatpay_app',
        'wechatpay_h5': 'wechatpay_h5',
        'wechatpay_jsapi': 'wechatpay_jsapi',
        'wechatpay_lite': 'wechatpay_lite',
        'wechatpay_native': 'wechatpay_native',
        'wechatpay_scan': 'wechatpay_scan'
    }

    def __init__(self, alipay_app=None, alipay_face=None, alipay_lite=None, alipay_page=None, alipay_qr=None, alipay_scan=None, alipay_wap=None, wechatpay_app=None, wechatpay_h5=None, wechatpay_jsapi=None, wechatpay_lite=None, wechatpay_native=None, wechatpay_scan=None, _configuration=None):  # noqa: E501
        """V1CreateChargeRequestExtra - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._alipay_app = None
        self._alipay_face = None
        self._alipay_lite = None
        self._alipay_page = None
        self._alipay_qr = None
        self._alipay_scan = None
        self._alipay_wap = None
        self._wechatpay_app = None
        self._wechatpay_h5 = None
        self._wechatpay_jsapi = None
        self._wechatpay_lite = None
        self._wechatpay_native = None
        self._wechatpay_scan = None
        self.discriminator = None

        if alipay_app is not None:
            self.alipay_app = alipay_app
        if alipay_face is not None:
            self.alipay_face = alipay_face
        if alipay_lite is not None:
            self.alipay_lite = alipay_lite
        if alipay_page is not None:
            self.alipay_page = alipay_page
        if alipay_qr is not None:
            self.alipay_qr = alipay_qr
        if alipay_scan is not None:
            self.alipay_scan = alipay_scan
        if alipay_wap is not None:
            self.alipay_wap = alipay_wap
        if wechatpay_app is not None:
            self.wechatpay_app = wechatpay_app
        if wechatpay_h5 is not None:
            self.wechatpay_h5 = wechatpay_h5
        if wechatpay_jsapi is not None:
            self.wechatpay_jsapi = wechatpay_jsapi
        if wechatpay_lite is not None:
            self.wechatpay_lite = wechatpay_lite
        if wechatpay_native is not None:
            self.wechatpay_native = wechatpay_native
        if wechatpay_scan is not None:
            self.wechatpay_scan = wechatpay_scan

    @property
    def alipay_app(self):
        """Gets the alipay_app of this V1CreateChargeRequestExtra.  # noqa: E501

        支付宝 APP 支付元数据  # noqa: E501

        :return: The alipay_app of this V1CreateChargeRequestExtra.  # noqa: E501
        :rtype: V1ExtraAlipayApp
        """
        return self._alipay_app

    @alipay_app.setter
    def alipay_app(self, alipay_app):
        """Sets the alipay_app of this V1CreateChargeRequestExtra.

        支付宝 APP 支付元数据  # noqa: E501

        :param alipay_app: The alipay_app of this V1CreateChargeRequestExtra.  # noqa: E501
        :type: V1ExtraAlipayApp
        """

        self._alipay_app = alipay_app

    @property
    def alipay_face(self):
        """Gets the alipay_face of this V1CreateChargeRequestExtra.  # noqa: E501

        支付宝刷脸支付元数据  # noqa: E501

        :return: The alipay_face of this V1CreateChargeRequestExtra.  # noqa: E501
        :rtype: V1ExtraAlipayFace
        """
        return self._alipay_face

    @alipay_face.setter
    def alipay_face(self, alipay_face):
        """Sets the alipay_face of this V1CreateChargeRequestExtra.

        支付宝刷脸支付元数据  # noqa: E501

        :param alipay_face: The alipay_face of this V1CreateChargeRequestExtra.  # noqa: E501
        :type: V1ExtraAlipayFace
        """

        self._alipay_face = alipay_face

    @property
    def alipay_lite(self):
        """Gets the alipay_lite of this V1CreateChargeRequestExtra.  # noqa: E501

        支付宝小程序支付元数据  # noqa: E501

        :return: The alipay_lite of this V1CreateChargeRequestExtra.  # noqa: E501
        :rtype: V1ExtraAlipayLite
        """
        return self._alipay_lite

    @alipay_lite.setter
    def alipay_lite(self, alipay_lite):
        """Sets the alipay_lite of this V1CreateChargeRequestExtra.

        支付宝小程序支付元数据  # noqa: E501

        :param alipay_lite: The alipay_lite of this V1CreateChargeRequestExtra.  # noqa: E501
        :type: V1ExtraAlipayLite
        """

        self._alipay_lite = alipay_lite

    @property
    def alipay_page(self):
        """Gets the alipay_page of this V1CreateChargeRequestExtra.  # noqa: E501

        支付宝电脑网站支付元数据  # noqa: E501

        :return: The alipay_page of this V1CreateChargeRequestExtra.  # noqa: E501
        :rtype: V1ExtraAlipayPage
        """
        return self._alipay_page

    @alipay_page.setter
    def alipay_page(self, alipay_page):
        """Sets the alipay_page of this V1CreateChargeRequestExtra.

        支付宝电脑网站支付元数据  # noqa: E501

        :param alipay_page: The alipay_page of this V1CreateChargeRequestExtra.  # noqa: E501
        :type: V1ExtraAlipayPage
        """

        self._alipay_page = alipay_page

    @property
    def alipay_qr(self):
        """Gets the alipay_qr of this V1CreateChargeRequestExtra.  # noqa: E501

        支付宝二维码支付元数据  # noqa: E501

        :return: The alipay_qr of this V1CreateChargeRequestExtra.  # noqa: E501
        :rtype: V1ExtraAlipayQr
        """
        return self._alipay_qr

    @alipay_qr.setter
    def alipay_qr(self, alipay_qr):
        """Sets the alipay_qr of this V1CreateChargeRequestExtra.

        支付宝二维码支付元数据  # noqa: E501

        :param alipay_qr: The alipay_qr of this V1CreateChargeRequestExtra.  # noqa: E501
        :type: V1ExtraAlipayQr
        """

        self._alipay_qr = alipay_qr

    @property
    def alipay_scan(self):
        """Gets the alipay_scan of this V1CreateChargeRequestExtra.  # noqa: E501

        支付宝扫码（被扫）支付元数据  # noqa: E501

        :return: The alipay_scan of this V1CreateChargeRequestExtra.  # noqa: E501
        :rtype: V1ExtraAlipayScan
        """
        return self._alipay_scan

    @alipay_scan.setter
    def alipay_scan(self, alipay_scan):
        """Sets the alipay_scan of this V1CreateChargeRequestExtra.

        支付宝扫码（被扫）支付元数据  # noqa: E501

        :param alipay_scan: The alipay_scan of this V1CreateChargeRequestExtra.  # noqa: E501
        :type: V1ExtraAlipayScan
        """

        self._alipay_scan = alipay_scan

    @property
    def alipay_wap(self):
        """Gets the alipay_wap of this V1CreateChargeRequestExtra.  # noqa: E501

        支付宝手机网站支付元数据  # noqa: E501

        :return: The alipay_wap of this V1CreateChargeRequestExtra.  # noqa: E501
        :rtype: V1ExtraAlipayWap
        """
        return self._alipay_wap

    @alipay_wap.setter
    def alipay_wap(self, alipay_wap):
        """Sets the alipay_wap of this V1CreateChargeRequestExtra.

        支付宝手机网站支付元数据  # noqa: E501

        :param alipay_wap: The alipay_wap of this V1CreateChargeRequestExtra.  # noqa: E501
        :type: V1ExtraAlipayWap
        """

        self._alipay_wap = alipay_wap

    @property
    def wechatpay_app(self):
        """Gets the wechatpay_app of this V1CreateChargeRequestExtra.  # noqa: E501

        微信支付 APP 支付元数据  # noqa: E501

        :return: The wechatpay_app of this V1CreateChargeRequestExtra.  # noqa: E501
        :rtype: V1ExtraWechatpayApp
        """
        return self._wechatpay_app

    @wechatpay_app.setter
    def wechatpay_app(self, wechatpay_app):
        """Sets the wechatpay_app of this V1CreateChargeRequestExtra.

        微信支付 APP 支付元数据  # noqa: E501

        :param wechatpay_app: The wechatpay_app of this V1CreateChargeRequestExtra.  # noqa: E501
        :type: V1ExtraWechatpayApp
        """

        self._wechatpay_app = wechatpay_app

    @property
    def wechatpay_h5(self):
        """Gets the wechatpay_h5 of this V1CreateChargeRequestExtra.  # noqa: E501

        微信支付 H5 支付元数据  # noqa: E501

        :return: The wechatpay_h5 of this V1CreateChargeRequestExtra.  # noqa: E501
        :rtype: V1ExtraWechatpayH5
        """
        return self._wechatpay_h5

    @wechatpay_h5.setter
    def wechatpay_h5(self, wechatpay_h5):
        """Sets the wechatpay_h5 of this V1CreateChargeRequestExtra.

        微信支付 H5 支付元数据  # noqa: E501

        :param wechatpay_h5: The wechatpay_h5 of this V1CreateChargeRequestExtra.  # noqa: E501
        :type: V1ExtraWechatpayH5
        """

        self._wechatpay_h5 = wechatpay_h5

    @property
    def wechatpay_jsapi(self):
        """Gets the wechatpay_jsapi of this V1CreateChargeRequestExtra.  # noqa: E501

        微信支付 JSAPI 支付元数据  # noqa: E501

        :return: The wechatpay_jsapi of this V1CreateChargeRequestExtra.  # noqa: E501
        :rtype: V1ExtraWechatpayJsapi
        """
        return self._wechatpay_jsapi

    @wechatpay_jsapi.setter
    def wechatpay_jsapi(self, wechatpay_jsapi):
        """Sets the wechatpay_jsapi of this V1CreateChargeRequestExtra.

        微信支付 JSAPI 支付元数据  # noqa: E501

        :param wechatpay_jsapi: The wechatpay_jsapi of this V1CreateChargeRequestExtra.  # noqa: E501
        :type: V1ExtraWechatpayJsapi
        """

        self._wechatpay_jsapi = wechatpay_jsapi

    @property
    def wechatpay_lite(self):
        """Gets the wechatpay_lite of this V1CreateChargeRequestExtra.  # noqa: E501

        微信支付小程序支付元数据  # noqa: E501

        :return: The wechatpay_lite of this V1CreateChargeRequestExtra.  # noqa: E501
        :rtype: V1ExtraWechatpayLite
        """
        return self._wechatpay_lite

    @wechatpay_lite.setter
    def wechatpay_lite(self, wechatpay_lite):
        """Sets the wechatpay_lite of this V1CreateChargeRequestExtra.

        微信支付小程序支付元数据  # noqa: E501

        :param wechatpay_lite: The wechatpay_lite of this V1CreateChargeRequestExtra.  # noqa: E501
        :type: V1ExtraWechatpayLite
        """

        self._wechatpay_lite = wechatpay_lite

    @property
    def wechatpay_native(self):
        """Gets the wechatpay_native of this V1CreateChargeRequestExtra.  # noqa: E501

        微信支付二维码支付元数据  # noqa: E501

        :return: The wechatpay_native of this V1CreateChargeRequestExtra.  # noqa: E501
        :rtype: V1ExtraWechatpayNative
        """
        return self._wechatpay_native

    @wechatpay_native.setter
    def wechatpay_native(self, wechatpay_native):
        """Sets the wechatpay_native of this V1CreateChargeRequestExtra.

        微信支付二维码支付元数据  # noqa: E501

        :param wechatpay_native: The wechatpay_native of this V1CreateChargeRequestExtra.  # noqa: E501
        :type: V1ExtraWechatpayNative
        """

        self._wechatpay_native = wechatpay_native

    @property
    def wechatpay_scan(self):
        """Gets the wechatpay_scan of this V1CreateChargeRequestExtra.  # noqa: E501

        微信支付扫码（被扫）支付元数据  # noqa: E501

        :return: The wechatpay_scan of this V1CreateChargeRequestExtra.  # noqa: E501
        :rtype: V1ExtraWechatpayScan
        """
        return self._wechatpay_scan

    @wechatpay_scan.setter
    def wechatpay_scan(self, wechatpay_scan):
        """Sets the wechatpay_scan of this V1CreateChargeRequestExtra.

        微信支付扫码（被扫）支付元数据  # noqa: E501

        :param wechatpay_scan: The wechatpay_scan of this V1CreateChargeRequestExtra.  # noqa: E501
        :type: V1ExtraWechatpayScan
        """

        self._wechatpay_scan = wechatpay_scan

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(V1CreateChargeRequestExtra, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1CreateChargeRequestExtra):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1CreateChargeRequestExtra):
            return True

        return self.to_dict() != other.to_dict()
