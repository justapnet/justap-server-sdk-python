# coding: utf-8

"""
    Justap API

    欢迎阅读 Justap Api 文档  Justap 是为移动端应用和PC端应用打造的下一代聚合支付SAAS服务平台，通过一个 SDK 即可快速的支持各种形式的应用，并且一次接口完成多个不同支付渠道的接入。平台除了支持服务商子商户模式，同时还对商家自有商户（即自己前往微信、支付宝等机构开户）提供了完整的支持。  感谢您的支持，我们将不断探索，为您提供更优质的服务！如需技术支持可前往商户中心提交工单，支持工程师会尽快与您取得联系！  # 文档说明 采用 REST 风格设计。所有接口请求地址都是可预期的以及面向资源的。使用规范的 HTTP 响应代码来表示请求结果的正确或错误信息。使用 HTTP 内置的特性，如 HTTP Authentication 和 HTTP 请求方法让接口易于理解。  ## HTTP 状态码 HTTP 状态码可以用于表明服务的状态。服务器返回的 HTTP 状态码遵循 [RFC 7231](http://tools.ietf.org/html/rfc7231#section-6) 和 [IANA Status Code Registry](http://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml) 标准。  ## 认证 在调用 API 时，必须提供 API Key 作为每个请求的身份验证。你可以在管理平台内管理你的 API Key。API Key 是商户在系统中的身份标识，请安全存储，确保其不要被泄露。如需获取或更新 API Key ，也可以在商户中心内进行操作。 Api Key 在使用自定义的 HTTP Header 进行传递。  ``` X-Justap-Api-Key ```  API Key 分为 live 和 test 两种模式。分别对应真实交易环境和模拟测试交易环境并且可以实时切换。 测试模式下的 API Key 会模拟交易等请求，但是不会产生任何真实交易行为和费用，便于调试和接入。  **⚠️ 注意**：在使用 live 模式前，需要先前往 `商户中心 -> 应用设置 -> 开发参数` 开启 live 模式。  <SecurityDefinitions />  ## 请求类型 所有的 API 请求只支持 HTTPS 方式调用。  ## 路由参数 路由参数是指出现在 URL 路径中的可变变量。在本文档中，使用 `{}` 包裹的部分。 例如： `{charge_id}`，在实际使用是，需要将 `{charge_id}` 替换为实际值 `charge_8a8sdf888888`  ## MIME Type MIME 类型用于指示服务器返回的数据格式。服务器目前默认采用 `application/json`。  例如: ``` application/json ```  ## 错误 服务器使用 HTTP 状态码 (status code) 来表明一个 API 请求的成功或失败状态。返回 HTTP 2XX 表明 API 请求成功。返回 HTTP 4XX 表明在请求 API 时提供了错误信息，例如参数缺失、参数错误、支付渠道错误等。返回 HTTP 5XX 表明 API 请求时，服务器发生了错误。 在返回错误的状态码时，回同时返回一些错误信息提示出错原因。  具体的错误码我们正在整理当中。  ## 分页 所有的 Justap 资源都可以被 list API 方法支持，例如分页 charges 和 refunds。这些 list API 方法拥有相同的数据结构。Justap 是基于 cursor 的分页机制，使用参数 starting_after 来决定列表从何处开始，使用参数 ending_before 来决定列表从何处结束。  ## 参数说明 请求参数中包含的以下字段释义请参考：  - REQUIRED: 必填参数 - OPTIONAL: 可选参数，可以在请求当前接口时按需传入 - CONDITIONAL: 在某些条件下必传 - RESPONSE-ONLY: 标示该参数仅在接口返回参数中出现，调用 API 时无需传入  # 如何保证幂等性 如果发生请求超时或服务器内部错误，客户端可能会尝试重发请求。您可以在请求中设置 ClientToken 参数避免多次重试带来重复操作的问题。  ## 什么是幂等性 在数学计算或者计算机科学中，幂等性（idempotence）是指相同操作或资源在一次或多次请求中具有同样效果的作用。幂等性是在分布式系统设计中具有十分重要的地位。  ## 保证幂等性 通常情况下，客户端只需要在500（InternalErrorInternalError）或503（ServiceUnavailable）错误，或者无法获取响应结果时重试。充实时您可以从客户端生成一个参数值不超过64个的ASCII字符，并将值赋予 ClientToken，保证重试请求的幂等性。  ## ClientToken 详解 ClientToken参数的详细信息如下所示。  - ClientToken 是一个由客户端生成的唯一的、大小写敏感、不超过64个ASCII字符的字符串。例如，`ClientToken=123e4567-e89b-12d3-a456-426655440000`。 - 如果您提供了一个已经使用过的 ClientToken，但其他请求参数**有变化**，则服务器会返回 IdempotentParameterMismatch 的错误代码。 - 如果您提供了一个已经使用过的 ClientToken，且其他请求参数**不变**，则服务器会尝试返回 ClientToken 对应的记录。  ## API列表 以下为部分包含了 ClientToken 参数的API，供您参考。具体哪些API支持 ClientToken 参数请以各 API 文档为准，此处不一一列举。  - [申请退款接口](https://www.justap.cn/docs#operation/TradeService_Refunds)  # 签名 为保证安全，JUSTAP 所有接口均需要对请求进行签名。服务器收到请求后进行签名的验证。如果签名验证不通过，将会拒绝处理请求，并返回 401 Unauthorized。  签名算法：  ``` base64Encode(hamc-sha256(md5(请求 body + 请求时间戳 + 一次性随机字符串) + 一次性随机字符串)) ```  ## 准备 首先需要在 Justap 创建一个应用，商户需要生成一对 RSA 密钥对，并将公钥配置到 `商户中心 -> 开发配置`。 RSA 可以使用支付宝提供的 [密钥生成工具](https://opendocs.alipay.com/common/02kipl) 来生成。  商户在使用时，可以按照下述步骤生成请求的签名。   ## 算法描述: - 在请求发送前，取完整的**请求 body** - 生成一个随机的32位字符串，得到 **一次性随机字符串** - 获取当前时间的时间戳，得到 **请求时间戳** - 在请求字符串后面拼接上 **请求时间戳** 和 **一次性随机字符串**，得到 **待 Hash 字符串** - 对 **待 Hash 字符串** 转换为 utf8 编码并计算 md5，得到 **待签名字符串** - **待签名字符串** 后面拼接上 一次性随机字符串，得到完整的 **待签名字符串** - 使用商户 RSA 私钥，对 **待签名字符串** 计算签名，并对 结果 进行 base64 编码，即可得到 **签名**  ## 设置HTTP头 Justap 要求请求通过 自定义头部 来传递签名。具体定义如下:  ``` X-Justap-Signature: 签名 X-Justap-Request-Time: 请求时间戳 X-Justap-Nonce: 一次性随机字符串 X-Justap-Body-Hash: 待签名字符串 ```  具体的签名算法实现，可参考我们提供的各语言 SDK。  # WebHooks   # noqa: E501

    OpenAPI spec version: 1.0
    Contact: support@justap.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from justap_server_sdk_python.api_client import ApiClient


class CheckoutServiceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def checkout_service_create_union_qr_checkout(self, body, **kwargs):  # noqa: E501
        """通过聚合收款码创建订单  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.checkout_service_create_union_qr_checkout(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1UnionQrRequest body: (required)
        :return: V1UnionQrRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.checkout_service_create_union_qr_checkout_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.checkout_service_create_union_qr_checkout_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def checkout_service_create_union_qr_checkout_with_http_info(self, body, **kwargs):  # noqa: E501
        """通过聚合收款码创建订单  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.checkout_service_create_union_qr_checkout_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1UnionQrRequest body: (required)
        :return: V1UnionQrRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method checkout_service_create_union_qr_checkout" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `checkout_service_create_union_qr_checkout`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/checkout/union_qr', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1UnionQrRequest',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
