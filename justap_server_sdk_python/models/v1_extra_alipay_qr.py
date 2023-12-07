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


class V1ExtraAlipayQr(object):
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
        'buyer_id': 'str',
        'discountable_amount': 'str',
        'goods_detail': 'list[V1ExtraAlipayGoodsDetail]',
        'operator_id': 'str',
        'product_code': 'str',
        'qr_code': 'str',
        'qr_code_timeout_express': 'str',
        'qr_link': 'str',
        'store_id': 'str',
        'terminal_id': 'str'
    }

    attribute_map = {
        'buyer_id': 'buyer_id',
        'discountable_amount': 'discountable_amount',
        'goods_detail': 'goods_detail',
        'operator_id': 'operator_id',
        'product_code': 'product_code',
        'qr_code': 'qr_code',
        'qr_code_timeout_express': 'qr_code_timeout_express',
        'qr_link': 'qr_link',
        'store_id': 'store_id',
        'terminal_id': 'terminal_id'
    }

    def __init__(self, buyer_id=None, discountable_amount=None, goods_detail=None, operator_id=None, product_code=None, qr_code=None, qr_code_timeout_express=None, qr_link=None, store_id=None, terminal_id=None, _configuration=None):  # noqa: E501
        """V1ExtraAlipayQr - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._buyer_id = None
        self._discountable_amount = None
        self._goods_detail = None
        self._operator_id = None
        self._product_code = None
        self._qr_code = None
        self._qr_code_timeout_express = None
        self._qr_link = None
        self._store_id = None
        self._terminal_id = None
        self.discriminator = None

        self.buyer_id = buyer_id
        if discountable_amount is not None:
            self.discountable_amount = discountable_amount
        if goods_detail is not None:
            self.goods_detail = goods_detail
        self.operator_id = operator_id
        self.product_code = product_code
        self.qr_code = qr_code
        self.qr_code_timeout_express = qr_code_timeout_express
        self.qr_link = qr_link
        self.store_id = store_id
        self.terminal_id = terminal_id

    @property
    def buyer_id(self):
        """Gets the buyer_id of this V1ExtraAlipayQr.  # noqa: E501

        买家的支付宝唯一用户号（2088开头的16位纯数字）  # noqa: E501

        :return: The buyer_id of this V1ExtraAlipayQr.  # noqa: E501
        :rtype: str
        """
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, buyer_id):
        """Sets the buyer_id of this V1ExtraAlipayQr.

        买家的支付宝唯一用户号（2088开头的16位纯数字）  # noqa: E501

        :param buyer_id: The buyer_id of this V1ExtraAlipayQr.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and buyer_id is None:
            raise ValueError("Invalid value for `buyer_id`, must not be `None`")  # noqa: E501

        self._buyer_id = buyer_id

    @property
    def discountable_amount(self):
        """Gets the discountable_amount of this V1ExtraAlipayQr.  # noqa: E501

        可打折金额. 参与优惠计算的金额，单位为元，精确到小数点后两位，取值范围[0.01,100000000] 如果该值未传入，但传入了【订单总金额】，【不可打折金额】则该值默认为【订单总金额】-【不可打折金额】  # noqa: E501

        :return: The discountable_amount of this V1ExtraAlipayQr.  # noqa: E501
        :rtype: str
        """
        return self._discountable_amount

    @discountable_amount.setter
    def discountable_amount(self, discountable_amount):
        """Sets the discountable_amount of this V1ExtraAlipayQr.

        可打折金额. 参与优惠计算的金额，单位为元，精确到小数点后两位，取值范围[0.01,100000000] 如果该值未传入，但传入了【订单总金额】，【不可打折金额】则该值默认为【订单总金额】-【不可打折金额】  # noqa: E501

        :param discountable_amount: The discountable_amount of this V1ExtraAlipayQr.  # noqa: E501
        :type: str
        """

        self._discountable_amount = discountable_amount

    @property
    def goods_detail(self):
        """Gets the goods_detail of this V1ExtraAlipayQr.  # noqa: E501

        商品明细列表  # noqa: E501

        :return: The goods_detail of this V1ExtraAlipayQr.  # noqa: E501
        :rtype: list[V1ExtraAlipayGoodsDetail]
        """
        return self._goods_detail

    @goods_detail.setter
    def goods_detail(self, goods_detail):
        """Sets the goods_detail of this V1ExtraAlipayQr.

        商品明细列表  # noqa: E501

        :param goods_detail: The goods_detail of this V1ExtraAlipayQr.  # noqa: E501
        :type: list[V1ExtraAlipayGoodsDetail]
        """

        self._goods_detail = goods_detail

    @property
    def operator_id(self):
        """Gets the operator_id of this V1ExtraAlipayQr.  # noqa: E501

        商户操作员编号  # noqa: E501

        :return: The operator_id of this V1ExtraAlipayQr.  # noqa: E501
        :rtype: str
        """
        return self._operator_id

    @operator_id.setter
    def operator_id(self, operator_id):
        """Sets the operator_id of this V1ExtraAlipayQr.

        商户操作员编号  # noqa: E501

        :param operator_id: The operator_id of this V1ExtraAlipayQr.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and operator_id is None:
            raise ValueError("Invalid value for `operator_id`, must not be `None`")  # noqa: E501

        self._operator_id = operator_id

    @property
    def product_code(self):
        """Gets the product_code of this V1ExtraAlipayQr.  # noqa: E501

        销售产品码，商家和支付宝签约的产品码，为固定值QUICK_MSECURITY_PAY  # noqa: E501

        :return: The product_code of this V1ExtraAlipayQr.  # noqa: E501
        :rtype: str
        """
        return self._product_code

    @product_code.setter
    def product_code(self, product_code):
        """Sets the product_code of this V1ExtraAlipayQr.

        销售产品码，商家和支付宝签约的产品码，为固定值QUICK_MSECURITY_PAY  # noqa: E501

        :param product_code: The product_code of this V1ExtraAlipayQr.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and product_code is None:
            raise ValueError("Invalid value for `product_code`, must not be `None`")  # noqa: E501

        self._product_code = product_code

    @property
    def qr_code(self):
        """Gets the qr_code of this V1ExtraAlipayQr.  # noqa: E501

        [ONLY IN RESPONSE] 二维码  # noqa: E501

        :return: The qr_code of this V1ExtraAlipayQr.  # noqa: E501
        :rtype: str
        """
        return self._qr_code

    @qr_code.setter
    def qr_code(self, qr_code):
        """Sets the qr_code of this V1ExtraAlipayQr.

        [ONLY IN RESPONSE] 二维码  # noqa: E501

        :param qr_code: The qr_code of this V1ExtraAlipayQr.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and qr_code is None:
            raise ValueError("Invalid value for `qr_code`, must not be `None`")  # noqa: E501

        self._qr_code = qr_code

    @property
    def qr_code_timeout_express(self):
        """Gets the qr_code_timeout_express of this V1ExtraAlipayQr.  # noqa: E501

        支付场景。 条码支付，取值：bar_code； 声波支付，取值：wave_code  # noqa: E501

        :return: The qr_code_timeout_express of this V1ExtraAlipayQr.  # noqa: E501
        :rtype: str
        """
        return self._qr_code_timeout_express

    @qr_code_timeout_express.setter
    def qr_code_timeout_express(self, qr_code_timeout_express):
        """Sets the qr_code_timeout_express of this V1ExtraAlipayQr.

        支付场景。 条码支付，取值：bar_code； 声波支付，取值：wave_code  # noqa: E501

        :param qr_code_timeout_express: The qr_code_timeout_express of this V1ExtraAlipayQr.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and qr_code_timeout_express is None:
            raise ValueError("Invalid value for `qr_code_timeout_express`, must not be `None`")  # noqa: E501

        self._qr_code_timeout_express = qr_code_timeout_express

    @property
    def qr_link(self):
        """Gets the qr_link of this V1ExtraAlipayQr.  # noqa: E501

        [ONLY IN RESPONSE] 二维码图片的URL地址  # noqa: E501

        :return: The qr_link of this V1ExtraAlipayQr.  # noqa: E501
        :rtype: str
        """
        return self._qr_link

    @qr_link.setter
    def qr_link(self, qr_link):
        """Sets the qr_link of this V1ExtraAlipayQr.

        [ONLY IN RESPONSE] 二维码图片的URL地址  # noqa: E501

        :param qr_link: The qr_link of this V1ExtraAlipayQr.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and qr_link is None:
            raise ValueError("Invalid value for `qr_link`, must not be `None`")  # noqa: E501

        self._qr_link = qr_link

    @property
    def store_id(self):
        """Gets the store_id of this V1ExtraAlipayQr.  # noqa: E501

        商户门店编号  # noqa: E501

        :return: The store_id of this V1ExtraAlipayQr.  # noqa: E501
        :rtype: str
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id):
        """Sets the store_id of this V1ExtraAlipayQr.

        商户门店编号  # noqa: E501

        :param store_id: The store_id of this V1ExtraAlipayQr.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and store_id is None:
            raise ValueError("Invalid value for `store_id`, must not be `None`")  # noqa: E501

        self._store_id = store_id

    @property
    def terminal_id(self):
        """Gets the terminal_id of this V1ExtraAlipayQr.  # noqa: E501

        商户机具终端编号  # noqa: E501

        :return: The terminal_id of this V1ExtraAlipayQr.  # noqa: E501
        :rtype: str
        """
        return self._terminal_id

    @terminal_id.setter
    def terminal_id(self, terminal_id):
        """Sets the terminal_id of this V1ExtraAlipayQr.

        商户机具终端编号  # noqa: E501

        :param terminal_id: The terminal_id of this V1ExtraAlipayQr.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and terminal_id is None:
            raise ValueError("Invalid value for `terminal_id`, must not be `None`")  # noqa: E501

        self._terminal_id = terminal_id

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
        if issubclass(V1ExtraAlipayQr, dict):
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
        if not isinstance(other, V1ExtraAlipayQr):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1ExtraAlipayQr):
            return True

        return self.to_dict() != other.to_dict()
