# coding: utf-8

"""
    Justap API

    欢迎阅读 Justap Api 文档  Justap 是为移动端应用和PC端应用打造的下一代聚合支付SAAS服务平台，通过一个 SDK 即可快速的支持各种形式的应用，并且一次接口完成多个不同支付渠道的接入。平台除了支持服务商子商户模式，同时还对商家自有商户（即自己前往微信、支付宝等机构开户）提供了完整的支持。  感谢您的支持，我们将不断探索，为您提供更优质的服务！如需技术支持可前往商户中心提交工单，支持工程师会尽快与您取得联系！  # 文档说明 采用 REST 风格设计。所有接口请求地址都是可预期的以及面向资源的。使用规范的 HTTP 响应代码来表示请求结果的正确或错误信息。使用 HTTP 内置的特性，如 HTTP Authentication 和 HTTP 请求方法让接口易于理解。  ## HTTP 状态码 HTTP 状态码可以用于表明服务的状态。服务器返回的 HTTP 状态码遵循 [RFC 7231](http://tools.ietf.org/html/rfc7231#section-6) 和 [IANA Status Code Registry](http://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml) 标准。  ## 认证 在调用 API 时，必须提供 API Key 作为每个请求的身份验证。你可以在管理平台内管理你的 API Key。API Key 是商户在系统中的身份标识，请安全存储，确保其不要被泄露。如需获取或更新 API Key ，也可以在商户中心内进行操作。 Api Key 在使用自定义的 HTTP Header 进行传递。  ``` X-Justap-Api-Key ```  API Key 分为 live 和 test 两种模式。分别对应真实交易环境和模拟测试交易环境并且可以实时切换。 测试模式下的 API Key 会模拟交易等请求，但是不会产生任何真实交易行为和费用，便于调试和接入。  **⚠️ 注意**：在使用 live 模式前，需要先前往 `商户中心 -> 应用设置 -> 开发参数` 开启 live 模式。  <SecurityDefinitions />  ## 请求类型 所有的 API 请求只支持 HTTPS 方式调用。  ## 路由参数 路由参数是指出现在 URL 路径中的可变变量。在本文档中，使用 `{}` 包裹的部分。 例如： `{charge_id}`，在实际使用是，需要将 `{charge_id}` 替换为实际值 `charge_8a8sdf888888`  ## MIME Type MIME 类型用于指示服务器返回的数据格式。服务器目前默认采用 `application/json`。  例如: ``` application/json ```  ## 错误 服务器使用 HTTP 状态码 (status code) 来表明一个 API 请求的成功或失败状态。返回 HTTP 2XX 表明 API 请求成功。返回 HTTP 4XX 表明在请求 API 时提供了错误信息，例如参数缺失、参数错误、支付渠道错误等。返回 HTTP 5XX 表明 API 请求时，服务器发生了错误。 在返回错误的状态码时，回同时返回一些错误信息提示出错原因。  具体的错误码我们正在整理当中。  ## 分页 所有的 Justap 资源都可以被 list API 方法支持，例如分页 charges 和 refunds。这些 list API 方法拥有相同的数据结构。Justap 是基于 cursor 的分页机制，使用参数 starting_after 来决定列表从何处开始，使用参数 ending_before 来决定列表从何处结束。  ## 参数说明 请求参数中包含的以下字段释义请参考：  - REQUIRED: 必填参数 - OPTIONAL: 可选参数，可以在请求当前接口时按需传入 - CONDITIONAL: 在某些条件下必传 - RESPONSE-ONLY: 标示该参数仅在接口返回参数中出现，调用 API 时无需传入  # 如何保证幂等性 如果发生请求超时或服务器内部错误，客户端可能会尝试重发请求。您可以在请求中设置 ClientToken 参数避免多次重试带来重复操作的问题。  ## 什么是幂等性 在数学计算或者计算机科学中，幂等性（idempotence）是指相同操作或资源在一次或多次请求中具有同样效果的作用。幂等性是在分布式系统设计中具有十分重要的地位。  ## 保证幂等性 通常情况下，客户端只需要在500（InternalErrorInternalError）或503（ServiceUnavailable）错误，或者无法获取响应结果时重试。充实时您可以从客户端生成一个参数值不超过64个的ASCII字符，并将值赋予 ClientToken，保证重试请求的幂等性。  ## ClientToken 详解 ClientToken参数的详细信息如下所示。  - ClientToken 是一个由客户端生成的唯一的、大小写敏感、不超过64个ASCII字符的字符串。例如，`ClientToken=123e4567-e89b-12d3-a456-426655440000`。 - 如果您提供了一个已经使用过的 ClientToken，但其他请求参数**有变化**，则服务器会返回 IdempotentParameterMismatch 的错误代码。 - 如果您提供了一个已经使用过的 ClientToken，且其他请求参数**不变**，则服务器会尝试返回 ClientToken 对应的记录。  ## API列表 以下为部分包含了 ClientToken 参数的API，供您参考。具体哪些API支持 ClientToken 参数请以各 API 文档为准，此处不一一列举。  - [申请退款接口](https://www.justap.cn/docs#operation/TradeService_Refunds)  # 签名 为保证安全，JUSTAP 所有接口均需要对请求进行签名。服务器收到请求后进行签名的验证。如果签名验证不通过，将会拒绝处理请求，并返回 401 Unauthorized。  签名算法：  ``` base64Encode(hamc-sha256(md5(请求 body + 请求时间戳 + 一次性随机字符串) + 一次性随机字符串)) ```  ## 准备 首先需要在 Justap 创建一个应用，商户需要生成一对 RSA 密钥对，并将公钥配置到 `商户中心 -> 开发配置`。 RSA 可以使用支付宝提供的 [密钥生成工具](https://opendocs.alipay.com/common/02kipl) 来生成。  商户在使用时，可以按照下述步骤生成请求的签名。   ## 算法描述: - 在请求发送前，取完整的**请求 body** - 生成一个随机的32位字符串，得到 **一次性随机字符串** - 获取当前时间的时间戳，得到 **请求时间戳** - 在请求字符串后面拼接上 **请求时间戳** 和 **一次性随机字符串**，得到 **待 Hash 字符串** - 对 **待 Hash 字符串** 计算 md5，得到 **待签名字符串** - **待签名字符串** 后面拼接上 一次性随机字符串，得到完整的 **待签名字符串** - 使用商户 RSA 私钥，对 **待签名字符串** 计算签名，并对 结果 进行 base64 编码，即可得到 **签名**  ## 设置HTTP头 Justap 要求请求通过 自定义头部 来传递签名。具体定义如下:  ``` X-Justap-Signature: 签名 X-Justap-Request-Time: 请求时间戳 X-Justap-Nonce: 一次性随机字符串 X-Justap-Body-Hash: 待签名字符串 ```  具体的签名算法实现，可参考我们提供的各语言 SDK。  # WebHooks   # noqa: E501

    OpenAPI spec version: 1.0
    Contact: support@justap.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from justap_server_sdk_python.configuration import Configuration


class V1Charge(object):
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
        'amount': 'float',
        'amount_fee': 'float',
        'amount_refund': 'float',
        'amount_royalty': 'float',
        'amount_settle': 'float',
        'app_id': 'str',
        'body': 'str',
        'channel': 'V1Channel',
        'charge_id': 'str',
        'client_ip': 'str',
        'closed': 'bool',
        'closed_at': 'datetime',
        'created_at': 'datetime',
        'credential': 'ProtobufAny',
        'currency': 'str',
        'description': 'str',
        'extra': 'V1ChargeExtra',
        'failure_code': 'str',
        'failure_msg': 'str',
        'live_mode': 'bool',
        'merchant_trade_id': 'str',
        'metadata': 'dict(str, str)',
        'paid': 'bool',
        'paid_at': 'datetime',
        'refunded': 'bool',
        'refunds': 'list[V1Refund]',
        'reversed': 'bool',
        'reversed_at': 'datetime',
        'subject': 'str',
        'time_expire': 'datetime',
        'transaction_no': 'str',
        'ttl': 'int'
    }

    attribute_map = {
        'amount': 'amount',
        'amount_fee': 'amount_fee',
        'amount_refund': 'amount_refund',
        'amount_royalty': 'amount_royalty',
        'amount_settle': 'amount_settle',
        'app_id': 'app_id',
        'body': 'body',
        'channel': 'channel',
        'charge_id': 'charge_id',
        'client_ip': 'client_ip',
        'closed': 'closed',
        'closed_at': 'closed_at',
        'created_at': 'created_at',
        'credential': 'credential',
        'currency': 'currency',
        'description': 'description',
        'extra': 'extra',
        'failure_code': 'failure_code',
        'failure_msg': 'failure_msg',
        'live_mode': 'live_mode',
        'merchant_trade_id': 'merchant_trade_id',
        'metadata': 'metadata',
        'paid': 'paid',
        'paid_at': 'paid_at',
        'refunded': 'refunded',
        'refunds': 'refunds',
        'reversed': 'reversed',
        'reversed_at': 'reversed_at',
        'subject': 'subject',
        'time_expire': 'time_expire',
        'transaction_no': 'transaction_no',
        'ttl': 'ttl'
    }

    def __init__(self, amount=0.0, amount_fee=None, amount_refund=None, amount_royalty=None, amount_settle=None, app_id=None, body=None, channel=None, charge_id=None, client_ip=None, closed=False, closed_at=None, created_at=None, credential=None, currency=None, description=None, extra=None, failure_code=None, failure_msg=None, live_mode=False, merchant_trade_id=None, metadata=None, paid=False, paid_at=None, refunded=False, refunds=None, reversed=False, reversed_at=None, subject=None, time_expire=None, transaction_no=None, ttl=0, _configuration=None):  # noqa: E501
        """V1Charge - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._amount = None
        self._amount_fee = None
        self._amount_refund = None
        self._amount_royalty = None
        self._amount_settle = None
        self._app_id = None
        self._body = None
        self._channel = None
        self._charge_id = None
        self._client_ip = None
        self._closed = None
        self._closed_at = None
        self._created_at = None
        self._credential = None
        self._currency = None
        self._description = None
        self._extra = None
        self._failure_code = None
        self._failure_msg = None
        self._live_mode = None
        self._merchant_trade_id = None
        self._metadata = None
        self._paid = None
        self._paid_at = None
        self._refunded = None
        self._refunds = None
        self._reversed = None
        self._reversed_at = None
        self._subject = None
        self._time_expire = None
        self._transaction_no = None
        self._ttl = None
        self.discriminator = None

        self.amount = amount
        self.amount_fee = amount_fee
        self.amount_refund = amount_refund
        self.amount_royalty = amount_royalty
        self.amount_settle = amount_settle
        self.app_id = app_id
        self.body = body
        self.channel = channel
        self.charge_id = charge_id
        self.client_ip = client_ip
        self.closed = closed
        if closed_at is not None:
            self.closed_at = closed_at
        if created_at is not None:
            self.created_at = created_at
        if credential is not None:
            self.credential = credential
        self.currency = currency
        self.description = description
        if extra is not None:
            self.extra = extra
        self.failure_code = failure_code
        self.failure_msg = failure_msg
        self.live_mode = live_mode
        self.merchant_trade_id = merchant_trade_id
        if metadata is not None:
            self.metadata = metadata
        self.paid = paid
        if paid_at is not None:
            self.paid_at = paid_at
        self.refunded = refunded
        if refunds is not None:
            self.refunds = refunds
        self.reversed = reversed
        if reversed_at is not None:
            self.reversed_at = reversed_at
        self.subject = subject
        if time_expire is not None:
            self.time_expire = time_expire
        self.transaction_no = transaction_no
        self.ttl = ttl

    @property
    def amount(self):
        """Gets the amount of this V1Charge.  # noqa: E501

        订单金额  # noqa: E501

        :return: The amount of this V1Charge.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this V1Charge.

        订单金额  # noqa: E501

        :param amount: The amount of this V1Charge.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def amount_fee(self):
        """Gets the amount_fee of this V1Charge.  # noqa: E501

        下单金额  # noqa: E501

        :return: The amount_fee of this V1Charge.  # noqa: E501
        :rtype: float
        """
        return self._amount_fee

    @amount_fee.setter
    def amount_fee(self, amount_fee):
        """Sets the amount_fee of this V1Charge.

        下单金额  # noqa: E501

        :param amount_fee: The amount_fee of this V1Charge.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and amount_fee is None:
            raise ValueError("Invalid value for `amount_fee`, must not be `None`")  # noqa: E501

        self._amount_fee = amount_fee

    @property
    def amount_refund(self):
        """Gets the amount_refund of this V1Charge.  # noqa: E501

        订单退款总金额  # noqa: E501

        :return: The amount_refund of this V1Charge.  # noqa: E501
        :rtype: float
        """
        return self._amount_refund

    @amount_refund.setter
    def amount_refund(self, amount_refund):
        """Sets the amount_refund of this V1Charge.

        订单退款总金额  # noqa: E501

        :param amount_refund: The amount_refund of this V1Charge.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and amount_refund is None:
            raise ValueError("Invalid value for `amount_refund`, must not be `None`")  # noqa: E501

        self._amount_refund = amount_refund

    @property
    def amount_royalty(self):
        """Gets the amount_royalty of this V1Charge.  # noqa: E501

        分账金额  # noqa: E501

        :return: The amount_royalty of this V1Charge.  # noqa: E501
        :rtype: float
        """
        return self._amount_royalty

    @amount_royalty.setter
    def amount_royalty(self, amount_royalty):
        """Sets the amount_royalty of this V1Charge.

        分账金额  # noqa: E501

        :param amount_royalty: The amount_royalty of this V1Charge.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and amount_royalty is None:
            raise ValueError("Invalid value for `amount_royalty`, must not be `None`")  # noqa: E501

        self._amount_royalty = amount_royalty

    @property
    def amount_settle(self):
        """Gets the amount_settle of this V1Charge.  # noqa: E501

        结算金额，不一定有，视支付通道情况返回  # noqa: E501

        :return: The amount_settle of this V1Charge.  # noqa: E501
        :rtype: float
        """
        return self._amount_settle

    @amount_settle.setter
    def amount_settle(self, amount_settle):
        """Sets the amount_settle of this V1Charge.

        结算金额，不一定有，视支付通道情况返回  # noqa: E501

        :param amount_settle: The amount_settle of this V1Charge.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and amount_settle is None:
            raise ValueError("Invalid value for `amount_settle`, must not be `None`")  # noqa: E501

        self._amount_settle = amount_settle

    @property
    def app_id(self):
        """Gets the app_id of this V1Charge.  # noqa: E501

        应用ID  # noqa: E501

        :return: The app_id of this V1Charge.  # noqa: E501
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this V1Charge.

        应用ID  # noqa: E501

        :param app_id: The app_id of this V1Charge.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and app_id is None:
            raise ValueError("Invalid value for `app_id`, must not be `None`")  # noqa: E501

        self._app_id = app_id

    @property
    def body(self):
        """Gets the body of this V1Charge.  # noqa: E501

        订单描述信息  # noqa: E501

        :return: The body of this V1Charge.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this V1Charge.

        订单描述信息  # noqa: E501

        :param body: The body of this V1Charge.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and body is None:
            raise ValueError("Invalid value for `body`, must not be `None`")  # noqa: E501

        self._body = body

    @property
    def channel(self):
        """Gets the channel of this V1Charge.  # noqa: E501

        支付渠道  # noqa: E501

        :return: The channel of this V1Charge.  # noqa: E501
        :rtype: V1Channel
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this V1Charge.

        支付渠道  # noqa: E501

        :param channel: The channel of this V1Charge.  # noqa: E501
        :type: V1Channel
        """
        if self._configuration.client_side_validation and channel is None:
            raise ValueError("Invalid value for `channel`, must not be `None`")  # noqa: E501

        self._channel = channel

    @property
    def charge_id(self):
        """Gets the charge_id of this V1Charge.  # noqa: E501

        Charge 对象 id  # noqa: E501

        :return: The charge_id of this V1Charge.  # noqa: E501
        :rtype: str
        """
        return self._charge_id

    @charge_id.setter
    def charge_id(self, charge_id):
        """Sets the charge_id of this V1Charge.

        Charge 对象 id  # noqa: E501

        :param charge_id: The charge_id of this V1Charge.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and charge_id is None:
            raise ValueError("Invalid value for `charge_id`, must not be `None`")  # noqa: E501

        self._charge_id = charge_id

    @property
    def client_ip(self):
        """Gets the client_ip of this V1Charge.  # noqa: E501

        顾客IP  # noqa: E501

        :return: The client_ip of this V1Charge.  # noqa: E501
        :rtype: str
        """
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        """Sets the client_ip of this V1Charge.

        顾客IP  # noqa: E501

        :param client_ip: The client_ip of this V1Charge.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and client_ip is None:
            raise ValueError("Invalid value for `client_ip`, must not be `None`")  # noqa: E501

        self._client_ip = client_ip

    @property
    def closed(self):
        """Gets the closed of this V1Charge.  # noqa: E501

        是否关闭  # noqa: E501

        :return: The closed of this V1Charge.  # noqa: E501
        :rtype: bool
        """
        return self._closed

    @closed.setter
    def closed(self, closed):
        """Sets the closed of this V1Charge.

        是否关闭  # noqa: E501

        :param closed: The closed of this V1Charge.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and closed is None:
            raise ValueError("Invalid value for `closed`, must not be `None`")  # noqa: E501

        self._closed = closed

    @property
    def closed_at(self):
        """Gets the closed_at of this V1Charge.  # noqa: E501

        关闭时间  # noqa: E501

        :return: The closed_at of this V1Charge.  # noqa: E501
        :rtype: datetime
        """
        return self._closed_at

    @closed_at.setter
    def closed_at(self, closed_at):
        """Sets the closed_at of this V1Charge.

        关闭时间  # noqa: E501

        :param closed_at: The closed_at of this V1Charge.  # noqa: E501
        :type: datetime
        """

        self._closed_at = closed_at

    @property
    def created_at(self):
        """Gets the created_at of this V1Charge.  # noqa: E501

        Charge 对象创建时间  # noqa: E501

        :return: The created_at of this V1Charge.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this V1Charge.

        Charge 对象创建时间  # noqa: E501

        :param created_at: The created_at of this V1Charge.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def credential(self):
        """Gets the credential of this V1Charge.  # noqa: E501

        支付凭证  # noqa: E501

        :return: The credential of this V1Charge.  # noqa: E501
        :rtype: ProtobufAny
        """
        return self._credential

    @credential.setter
    def credential(self, credential):
        """Sets the credential of this V1Charge.

        支付凭证  # noqa: E501

        :param credential: The credential of this V1Charge.  # noqa: E501
        :type: ProtobufAny
        """

        self._credential = credential

    @property
    def currency(self):
        """Gets the currency of this V1Charge.  # noqa: E501

        货币单位，当前仅支持 CNY  # noqa: E501

        :return: The currency of this V1Charge.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this V1Charge.

        货币单位，当前仅支持 CNY  # noqa: E501

        :param currency: The currency of this V1Charge.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def description(self):
        """Gets the description of this V1Charge.  # noqa: E501

        描述信息  # noqa: E501

        :return: The description of this V1Charge.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1Charge.

        描述信息  # noqa: E501

        :param description: The description of this V1Charge.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def extra(self):
        """Gets the extra of this V1Charge.  # noqa: E501

        支付渠道元数据  # noqa: E501

        :return: The extra of this V1Charge.  # noqa: E501
        :rtype: V1ChargeExtra
        """
        return self._extra

    @extra.setter
    def extra(self, extra):
        """Sets the extra of this V1Charge.

        支付渠道元数据  # noqa: E501

        :param extra: The extra of this V1Charge.  # noqa: E501
        :type: V1ChargeExtra
        """

        self._extra = extra

    @property
    def failure_code(self):
        """Gets the failure_code of this V1Charge.  # noqa: E501

        收单机构错误码  # noqa: E501

        :return: The failure_code of this V1Charge.  # noqa: E501
        :rtype: str
        """
        return self._failure_code

    @failure_code.setter
    def failure_code(self, failure_code):
        """Sets the failure_code of this V1Charge.

        收单机构错误码  # noqa: E501

        :param failure_code: The failure_code of this V1Charge.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and failure_code is None:
            raise ValueError("Invalid value for `failure_code`, must not be `None`")  # noqa: E501

        self._failure_code = failure_code

    @property
    def failure_msg(self):
        """Gets the failure_msg of this V1Charge.  # noqa: E501

        收单机构错误描述信息  # noqa: E501

        :return: The failure_msg of this V1Charge.  # noqa: E501
        :rtype: str
        """
        return self._failure_msg

    @failure_msg.setter
    def failure_msg(self, failure_msg):
        """Sets the failure_msg of this V1Charge.

        收单机构错误描述信息  # noqa: E501

        :param failure_msg: The failure_msg of this V1Charge.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and failure_msg is None:
            raise ValueError("Invalid value for `failure_msg`, must not be `None`")  # noqa: E501

        self._failure_msg = failure_msg

    @property
    def live_mode(self):
        """Gets the live_mode of this V1Charge.  # noqa: E501

        表明是否是沙箱环境  # noqa: E501

        :return: The live_mode of this V1Charge.  # noqa: E501
        :rtype: bool
        """
        return self._live_mode

    @live_mode.setter
    def live_mode(self, live_mode):
        """Sets the live_mode of this V1Charge.

        表明是否是沙箱环境  # noqa: E501

        :param live_mode: The live_mode of this V1Charge.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and live_mode is None:
            raise ValueError("Invalid value for `live_mode`, must not be `None`")  # noqa: E501

        self._live_mode = live_mode

    @property
    def merchant_trade_id(self):
        """Gets the merchant_trade_id of this V1Charge.  # noqa: E501

        商户系统订单号，APP下需唯一  # noqa: E501

        :return: The merchant_trade_id of this V1Charge.  # noqa: E501
        :rtype: str
        """
        return self._merchant_trade_id

    @merchant_trade_id.setter
    def merchant_trade_id(self, merchant_trade_id):
        """Sets the merchant_trade_id of this V1Charge.

        商户系统订单号，APP下需唯一  # noqa: E501

        :param merchant_trade_id: The merchant_trade_id of this V1Charge.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and merchant_trade_id is None:
            raise ValueError("Invalid value for `merchant_trade_id`, must not be `None`")  # noqa: E501

        self._merchant_trade_id = merchant_trade_id

    @property
    def metadata(self):
        """Gets the metadata of this V1Charge.  # noqa: E501

        订单元数据，原样返回  # noqa: E501

        :return: The metadata of this V1Charge.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this V1Charge.

        订单元数据，原样返回  # noqa: E501

        :param metadata: The metadata of this V1Charge.  # noqa: E501
        :type: dict(str, str)
        """

        self._metadata = metadata

    @property
    def paid(self):
        """Gets the paid of this V1Charge.  # noqa: E501

        表明是否已支付  # noqa: E501

        :return: The paid of this V1Charge.  # noqa: E501
        :rtype: bool
        """
        return self._paid

    @paid.setter
    def paid(self, paid):
        """Sets the paid of this V1Charge.

        表明是否已支付  # noqa: E501

        :param paid: The paid of this V1Charge.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and paid is None:
            raise ValueError("Invalid value for `paid`, must not be `None`")  # noqa: E501

        self._paid = paid

    @property
    def paid_at(self):
        """Gets the paid_at of this V1Charge.  # noqa: E501

        支付时间  # noqa: E501

        :return: The paid_at of this V1Charge.  # noqa: E501
        :rtype: datetime
        """
        return self._paid_at

    @paid_at.setter
    def paid_at(self, paid_at):
        """Sets the paid_at of this V1Charge.

        支付时间  # noqa: E501

        :param paid_at: The paid_at of this V1Charge.  # noqa: E501
        :type: datetime
        """

        self._paid_at = paid_at

    @property
    def refunded(self):
        """Gets the refunded of this V1Charge.  # noqa: E501

        表明是否包含退款，含退款失败的  # noqa: E501

        :return: The refunded of this V1Charge.  # noqa: E501
        :rtype: bool
        """
        return self._refunded

    @refunded.setter
    def refunded(self, refunded):
        """Sets the refunded of this V1Charge.

        表明是否包含退款，含退款失败的  # noqa: E501

        :param refunded: The refunded of this V1Charge.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and refunded is None:
            raise ValueError("Invalid value for `refunded`, must not be `None`")  # noqa: E501

        self._refunded = refunded

    @property
    def refunds(self):
        """Gets the refunds of this V1Charge.  # noqa: E501

        Refund 对象列表  # noqa: E501

        :return: The refunds of this V1Charge.  # noqa: E501
        :rtype: list[V1Refund]
        """
        return self._refunds

    @refunds.setter
    def refunds(self, refunds):
        """Sets the refunds of this V1Charge.

        Refund 对象列表  # noqa: E501

        :param refunds: The refunds of this V1Charge.  # noqa: E501
        :type: list[V1Refund]
        """

        self._refunds = refunds

    @property
    def reversed(self):
        """Gets the reversed of this V1Charge.  # noqa: E501

        表明是否已经撤销  # noqa: E501

        :return: The reversed of this V1Charge.  # noqa: E501
        :rtype: bool
        """
        return self._reversed

    @reversed.setter
    def reversed(self, reversed):
        """Sets the reversed of this V1Charge.

        表明是否已经撤销  # noqa: E501

        :param reversed: The reversed of this V1Charge.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and reversed is None:
            raise ValueError("Invalid value for `reversed`, must not be `None`")  # noqa: E501

        self._reversed = reversed

    @property
    def reversed_at(self):
        """Gets the reversed_at of this V1Charge.  # noqa: E501

        冲正时间  # noqa: E501

        :return: The reversed_at of this V1Charge.  # noqa: E501
        :rtype: datetime
        """
        return self._reversed_at

    @reversed_at.setter
    def reversed_at(self, reversed_at):
        """Sets the reversed_at of this V1Charge.

        冲正时间  # noqa: E501

        :param reversed_at: The reversed_at of this V1Charge.  # noqa: E501
        :type: datetime
        """

        self._reversed_at = reversed_at

    @property
    def subject(self):
        """Gets the subject of this V1Charge.  # noqa: E501

        订单描述主题  # noqa: E501

        :return: The subject of this V1Charge.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this V1Charge.

        订单描述主题  # noqa: E501

        :param subject: The subject of this V1Charge.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and subject is None:
            raise ValueError("Invalid value for `subject`, must not be `None`")  # noqa: E501

        self._subject = subject

    @property
    def time_expire(self):
        """Gets the time_expire of this V1Charge.  # noqa: E501

        订单过期时间  # noqa: E501

        :return: The time_expire of this V1Charge.  # noqa: E501
        :rtype: datetime
        """
        return self._time_expire

    @time_expire.setter
    def time_expire(self, time_expire):
        """Sets the time_expire of this V1Charge.

        订单过期时间  # noqa: E501

        :param time_expire: The time_expire of this V1Charge.  # noqa: E501
        :type: datetime
        """

        self._time_expire = time_expire

    @property
    def transaction_no(self):
        """Gets the transaction_no of this V1Charge.  # noqa: E501

        Charge 的支付单号  # noqa: E501

        :return: The transaction_no of this V1Charge.  # noqa: E501
        :rtype: str
        """
        return self._transaction_no

    @transaction_no.setter
    def transaction_no(self, transaction_no):
        """Sets the transaction_no of this V1Charge.

        Charge 的支付单号  # noqa: E501

        :param transaction_no: The transaction_no of this V1Charge.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and transaction_no is None:
            raise ValueError("Invalid value for `transaction_no`, must not be `None`")  # noqa: E501

        self._transaction_no = transaction_no

    @property
    def ttl(self):
        """Gets the ttl of this V1Charge.  # noqa: E501

        订单生存时间，单位秒  # noqa: E501

        :return: The ttl of this V1Charge.  # noqa: E501
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this V1Charge.

        订单生存时间，单位秒  # noqa: E501

        :param ttl: The ttl of this V1Charge.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and ttl is None:
            raise ValueError("Invalid value for `ttl`, must not be `None`")  # noqa: E501

        self._ttl = ttl

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
        if issubclass(V1Charge, dict):
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
        if not isinstance(other, V1Charge):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1Charge):
            return True

        return self.to_dict() != other.to_dict()
