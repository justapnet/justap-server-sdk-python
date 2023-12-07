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


class V1Refund(object):
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
        'account': 'V1RefundExtra',
        'amount': 'float',
        'charge_id': 'str',
        'charge_merchant_trade_id': 'str',
        'created': 'float',
        'created_at': 'datetime',
        'description': 'str',
        'failure_code': 'str',
        'failure_msg': 'str',
        'is_success': 'bool',
        'metadata': 'dict(str, str)',
        'refund_id': 'str',
        'refund_no': 'str',
        'status': 'str',
        'succeed_ts': 'float',
        'success_at': 'datetime',
        'transaction_no': 'str'
    }

    attribute_map = {
        'account': 'account',
        'amount': 'amount',
        'charge_id': 'charge_id',
        'charge_merchant_trade_id': 'charge_merchant_trade_id',
        'created': 'created',
        'created_at': 'created_at',
        'description': 'description',
        'failure_code': 'failure_code',
        'failure_msg': 'failure_msg',
        'is_success': 'is_success',
        'metadata': 'metadata',
        'refund_id': 'refund_id',
        'refund_no': 'refund_no',
        'status': 'status',
        'succeed_ts': 'succeed_ts',
        'success_at': 'success_at',
        'transaction_no': 'transaction_no'
    }

    def __init__(self, account=None, amount=None, charge_id=None, charge_merchant_trade_id=None, created=None, created_at=None, description=None, failure_code=None, failure_msg=None, is_success=False, metadata=None, refund_id=None, refund_no=None, status=None, succeed_ts=None, success_at=None, transaction_no=None, _configuration=None):  # noqa: E501
        """V1Refund - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account = None
        self._amount = None
        self._charge_id = None
        self._charge_merchant_trade_id = None
        self._created = None
        self._created_at = None
        self._description = None
        self._failure_code = None
        self._failure_msg = None
        self._is_success = None
        self._metadata = None
        self._refund_id = None
        self._refund_no = None
        self._status = None
        self._succeed_ts = None
        self._success_at = None
        self._transaction_no = None
        self.discriminator = None

        if account is not None:
            self.account = account
        self.amount = amount
        self.charge_id = charge_id
        self.charge_merchant_trade_id = charge_merchant_trade_id
        self.created = created
        if created_at is not None:
            self.created_at = created_at
        self.description = description
        self.failure_code = failure_code
        self.failure_msg = failure_msg
        self.is_success = is_success
        if metadata is not None:
            self.metadata = metadata
        self.refund_id = refund_id
        self.refund_no = refund_no
        self.status = status
        self.succeed_ts = succeed_ts
        if success_at is not None:
            self.success_at = success_at
        self.transaction_no = transaction_no

    @property
    def account(self):
        """Gets the account of this V1Refund.  # noqa: E501

        支付渠道退款元参数  # noqa: E501

        :return: The account of this V1Refund.  # noqa: E501
        :rtype: V1RefundExtra
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this V1Refund.

        支付渠道退款元参数  # noqa: E501

        :param account: The account of this V1Refund.  # noqa: E501
        :type: V1RefundExtra
        """

        self._account = account

    @property
    def amount(self):
        """Gets the amount of this V1Refund.  # noqa: E501

        退款金额  # noqa: E501

        :return: The amount of this V1Refund.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this V1Refund.

        退款金额  # noqa: E501

        :param amount: The amount of this V1Refund.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def charge_id(self):
        """Gets the charge_id of this V1Refund.  # noqa: E501

        Charge 对象 id  # noqa: E501

        :return: The charge_id of this V1Refund.  # noqa: E501
        :rtype: str
        """
        return self._charge_id

    @charge_id.setter
    def charge_id(self, charge_id):
        """Sets the charge_id of this V1Refund.

        Charge 对象 id  # noqa: E501

        :param charge_id: The charge_id of this V1Refund.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and charge_id is None:
            raise ValueError("Invalid value for `charge_id`, must not be `None`")  # noqa: E501

        self._charge_id = charge_id

    @property
    def charge_merchant_trade_id(self):
        """Gets the charge_merchant_trade_id of this V1Refund.  # noqa: E501

        商户系统订单号  # noqa: E501

        :return: The charge_merchant_trade_id of this V1Refund.  # noqa: E501
        :rtype: str
        """
        return self._charge_merchant_trade_id

    @charge_merchant_trade_id.setter
    def charge_merchant_trade_id(self, charge_merchant_trade_id):
        """Sets the charge_merchant_trade_id of this V1Refund.

        商户系统订单号  # noqa: E501

        :param charge_merchant_trade_id: The charge_merchant_trade_id of this V1Refund.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and charge_merchant_trade_id is None:
            raise ValueError("Invalid value for `charge_merchant_trade_id`, must not be `None`")  # noqa: E501

        self._charge_merchant_trade_id = charge_merchant_trade_id

    @property
    def created(self):
        """Gets the created of this V1Refund.  # noqa: E501

        退款创建时间  # noqa: E501

        :return: The created of this V1Refund.  # noqa: E501
        :rtype: float
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this V1Refund.

        退款创建时间  # noqa: E501

        :param created: The created of this V1Refund.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def created_at(self):
        """Gets the created_at of this V1Refund.  # noqa: E501

        退款创建时间  # noqa: E501

        :return: The created_at of this V1Refund.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this V1Refund.

        退款创建时间  # noqa: E501

        :param created_at: The created_at of this V1Refund.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this V1Refund.  # noqa: E501

        退款说明  # noqa: E501

        :return: The description of this V1Refund.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1Refund.

        退款说明  # noqa: E501

        :param description: The description of this V1Refund.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def failure_code(self):
        """Gets the failure_code of this V1Refund.  # noqa: E501

        支付渠道失败错误码  # noqa: E501

        :return: The failure_code of this V1Refund.  # noqa: E501
        :rtype: str
        """
        return self._failure_code

    @failure_code.setter
    def failure_code(self, failure_code):
        """Sets the failure_code of this V1Refund.

        支付渠道失败错误码  # noqa: E501

        :param failure_code: The failure_code of this V1Refund.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and failure_code is None:
            raise ValueError("Invalid value for `failure_code`, must not be `None`")  # noqa: E501

        self._failure_code = failure_code

    @property
    def failure_msg(self):
        """Gets the failure_msg of this V1Refund.  # noqa: E501

        支付渠道失败原因描述  # noqa: E501

        :return: The failure_msg of this V1Refund.  # noqa: E501
        :rtype: str
        """
        return self._failure_msg

    @failure_msg.setter
    def failure_msg(self, failure_msg):
        """Sets the failure_msg of this V1Refund.

        支付渠道失败原因描述  # noqa: E501

        :param failure_msg: The failure_msg of this V1Refund.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and failure_msg is None:
            raise ValueError("Invalid value for `failure_msg`, must not be `None`")  # noqa: E501

        self._failure_msg = failure_msg

    @property
    def is_success(self):
        """Gets the is_success of this V1Refund.  # noqa: E501

        退款是否成功  # noqa: E501

        :return: The is_success of this V1Refund.  # noqa: E501
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        """Sets the is_success of this V1Refund.

        退款是否成功  # noqa: E501

        :param is_success: The is_success of this V1Refund.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and is_success is None:
            raise ValueError("Invalid value for `is_success`, must not be `None`")  # noqa: E501

        self._is_success = is_success

    @property
    def metadata(self):
        """Gets the metadata of this V1Refund.  # noqa: E501

        元数据，原样返回  # noqa: E501

        :return: The metadata of this V1Refund.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this V1Refund.

        元数据，原样返回  # noqa: E501

        :param metadata: The metadata of this V1Refund.  # noqa: E501
        :type: dict(str, str)
        """

        self._metadata = metadata

    @property
    def refund_id(self):
        """Gets the refund_id of this V1Refund.  # noqa: E501

        Refund 对象 ID  # noqa: E501

        :return: The refund_id of this V1Refund.  # noqa: E501
        :rtype: str
        """
        return self._refund_id

    @refund_id.setter
    def refund_id(self, refund_id):
        """Sets the refund_id of this V1Refund.

        Refund 对象 ID  # noqa: E501

        :param refund_id: The refund_id of this V1Refund.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and refund_id is None:
            raise ValueError("Invalid value for `refund_id`, must not be `None`")  # noqa: E501

        self._refund_id = refund_id

    @property
    def refund_no(self):
        """Gets the refund_no of this V1Refund.  # noqa: E501

        退款单号  # noqa: E501

        :return: The refund_no of this V1Refund.  # noqa: E501
        :rtype: str
        """
        return self._refund_no

    @refund_no.setter
    def refund_no(self, refund_no):
        """Sets the refund_no of this V1Refund.

        退款单号  # noqa: E501

        :param refund_no: The refund_no of this V1Refund.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and refund_no is None:
            raise ValueError("Invalid value for `refund_no`, must not be `None`")  # noqa: E501

        self._refund_no = refund_no

    @property
    def status(self):
        """Gets the status of this V1Refund.  # noqa: E501

        退款状态  # noqa: E501

        :return: The status of this V1Refund.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this V1Refund.

        退款状态  # noqa: E501

        :param status: The status of this V1Refund.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def succeed_ts(self):
        """Gets the succeed_ts of this V1Refund.  # noqa: E501

        退款成功时间  # noqa: E501

        :return: The succeed_ts of this V1Refund.  # noqa: E501
        :rtype: float
        """
        return self._succeed_ts

    @succeed_ts.setter
    def succeed_ts(self, succeed_ts):
        """Sets the succeed_ts of this V1Refund.

        退款成功时间  # noqa: E501

        :param succeed_ts: The succeed_ts of this V1Refund.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and succeed_ts is None:
            raise ValueError("Invalid value for `succeed_ts`, must not be `None`")  # noqa: E501

        self._succeed_ts = succeed_ts

    @property
    def success_at(self):
        """Gets the success_at of this V1Refund.  # noqa: E501

        退款成功时间  # noqa: E501

        :return: The success_at of this V1Refund.  # noqa: E501
        :rtype: datetime
        """
        return self._success_at

    @success_at.setter
    def success_at(self, success_at):
        """Sets the success_at of this V1Refund.

        退款成功时间  # noqa: E501

        :param success_at: The success_at of this V1Refund.  # noqa: E501
        :type: datetime
        """

        self._success_at = success_at

    @property
    def transaction_no(self):
        """Gets the transaction_no of this V1Refund.  # noqa: E501

        交易号  # noqa: E501

        :return: The transaction_no of this V1Refund.  # noqa: E501
        :rtype: str
        """
        return self._transaction_no

    @transaction_no.setter
    def transaction_no(self, transaction_no):
        """Sets the transaction_no of this V1Refund.

        交易号  # noqa: E501

        :param transaction_no: The transaction_no of this V1Refund.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and transaction_no is None:
            raise ValueError("Invalid value for `transaction_no`, must not be `None`")  # noqa: E501

        self._transaction_no = transaction_no

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
        if issubclass(V1Refund, dict):
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
        if not isinstance(other, V1Refund):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1Refund):
            return True

        return self.to_dict() != other.to_dict()
