# justap_server_sdk_python.DefaultApi

All URIs are relative to *http://127.0.0.1:21011*

Method | HTTP request | Description
------------- | ------------- | -------------
[**trade_service_charges**](DefaultApi.md#trade_service_charges) | **POST** /transaction/v1/charges | 创建 Charge 对象
[**trade_service_query_charge**](DefaultApi.md#trade_service_query_charge) | **GET** /transaction/v1/charges/{charge_id} | 查询 Charge 对象
[**trade_service_query_charge_list**](DefaultApi.md#trade_service_query_charge_list) | **GET** /transaction/v1/charges | 查询 Charge 对象列表
[**trade_service_query_refund**](DefaultApi.md#trade_service_query_refund) | **GET** /transaction/v1/charges/{charge_id}/refunds/{refund_id} | 查询 Refund 对象
[**trade_service_query_refund_list**](DefaultApi.md#trade_service_query_refund_list) | **GET** /transaction/v1/charges/{charge_id}/refunds | 查询 Refund 对象列表
[**trade_service_refunds**](DefaultApi.md#trade_service_refunds) | **POST** /transaction/v1/refunds | 创建 Refund 对象
[**trade_service_reverse_charge**](DefaultApi.md#trade_service_reverse_charge) | **POST** /transaction/v1/charges/{charge_id}/reverse | 撤销 Charge 对象


# **trade_service_charges**
> V1ChargeResponse trade_service_charges(body)

创建 Charge 对象

发起一次支付请求时需要创建一个新的 charge 对象，获取一个可用的支付凭据用于客户端向第三方渠道发起支付请求。如果使用测试模式的 API Key，则不会发生真实交易。当支付成功后，会发送 Webhooks 通知。

### Example
```python
from __future__ import print_function
import time
import justap_server_sdk_python
from justap_server_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = justap_server_sdk_python.Configuration()
configuration.api_key['X-JUSTAP-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-JUSTAP-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = justap_server_sdk_python.DefaultApi(justap_server_sdk_python.ApiClient(configuration))
body = justap_server_sdk_python.V1CreateChargeRequest() # V1CreateChargeRequest | 

try:
    # 创建 Charge 对象
    api_response = api_instance.trade_service_charges(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->trade_service_charges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreateChargeRequest**](V1CreateChargeRequest.md)|  | 

### Return type

[**V1ChargeResponse**](V1ChargeResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trade_service_query_charge**
> V1ChargeResponse trade_service_query_charge(charge_id, app_id=app_id)

查询 Charge 对象

你可以在后台异步通知之前，通过查询接口确认支付状态。通过charge对象的id查询一个已创建的charge对象。

### Example
```python
from __future__ import print_function
import time
import justap_server_sdk_python
from justap_server_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = justap_server_sdk_python.Configuration()
configuration.api_key['X-JUSTAP-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-JUSTAP-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = justap_server_sdk_python.DefaultApi(justap_server_sdk_python.ApiClient(configuration))
charge_id = 'charge_id_example' # str | [REQUIRED] Charge 对象 id
app_id = 'app_id_example' # str | [REQUIRED] 应用 id (optional)

try:
    # 查询 Charge 对象
    api_response = api_instance.trade_service_query_charge(charge_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->trade_service_query_charge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **charge_id** | **str**| [REQUIRED] Charge 对象 id | 
 **app_id** | **str**| [REQUIRED] 应用 id | [optional] 

### Return type

[**V1ChargeResponse**](V1ChargeResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trade_service_query_charge_list**
> V1ChargeListResponse trade_service_query_charge_list(app_id=app_id, limit=limit, starting_after=starting_after, ending_before=ending_before, merchant_trade_id=merchant_trade_id, created_lt=created_lt, created_lte=created_lte, created_gt=created_gt, created_gte=created_gte, channel=channel, paid=paid, refunded=refunded, reversed=reversed, closed=closed, expired=expired)

查询 Charge 对象列表

返回之前创建过 charge 对象的一个列表。列表是按创建时间进行排序，总是将最新的 charge 对象显示在最前。如果不设置 created 参数，默认查询近一个月的数据；设置了 created 参数，会按照对应的时间段查询。

### Example
```python
from __future__ import print_function
import time
import justap_server_sdk_python
from justap_server_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = justap_server_sdk_python.Configuration()
configuration.api_key['X-JUSTAP-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-JUSTAP-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = justap_server_sdk_python.DefaultApi(justap_server_sdk_python.ApiClient(configuration))
app_id = 'app_id_example' # str | [REQUIRED] 应用 id (optional)
limit = 10 # int | [OPTIONAL] 限制有多少对象可以被返回，限制范围是从 1~100 项，默认是 10 项 (optional) (default to 10)
starting_after = 'starting_after_example' # str | [OPTIONAL] 在分页时使用的指针，决定了列表的第一项从何处开始。假设你的一次请求返回列表的最后一项的 id 是 obj_end，你可以使用 starting_after = obj_end 去获取下一页 (optional)
ending_before = 'ending_before_example' # str | [OPTIONAL] 在分页时使用的指针，决定了列表的最末项在何处结束。假设你的一次请求返回列表的第一项的 id 是 obj_start，你可以使用 ending_before = obj_start 去获取上一页 (optional)
merchant_trade_id = 'merchant_trade_id_example' # str | [OPTIONAL] 客户系统订单号 (optional)
created_lt = 0 # int | 大于 charge 对象的创建时间，用 Unix 时间戳表示 (optional) (default to 0)
created_lte = 0 # int | 大于或等于 charge 对象的创建时间，用 Unix 时间戳表示 (optional) (default to 0)
created_gt = 0 # int | 小于 charge 对象的创建时间，用 Unix 时间戳表示 (optional) (default to 0)
created_gte = 0 # int | 小于或等于 charge 对象的创建时间，用 Unix 时间戳表示 (optional) (default to 0)
channel = 'CHANNEL_INVALID_UNSPECIFIED' # str | [OPTIONAL] 渠道名称   - BALANCE: 余额支付  - AlipayQR: 支付宝扫码支付  - AlipayScan: 支付宝条码支付  - AlipayApp: 支付宝 App 支付  - AlipayWap: 支付宝手机网站支付  - AlipayPage: 支付宝电脑网站支付  - AlipayFace: 支付宝刷脸支付  - AlipayLite: 支付宝小程序支付  - WechatpayApp: 微信 App 支付  - WechatpayJSAPI: 微信 JSAPI 支付  - WechatpayH5: 微信 H5 支付  - WechatpayNative: 微信 Native 支付  - WechatpayLite: 微信小程序支付  - WechatpayFace: 刷脸支付  - WechatpayScan: 微信付款码支付 (optional) (default to CHANNEL_INVALID_UNSPECIFIED)
paid = false # bool | [OPTIONAL] 是否已付款 (optional) (default to false)
refunded = false # bool | [OPTIONAL] 是否存在退款信息，无论退款是否成功。 (optional) (default to false)
reversed = false # bool | [OPTIONAL] 是否已撤销 (optional) (default to false)
closed = false # bool | [OPTIONAL] 是否已关闭 (optional) (default to false)
expired = false # bool | [OPTIONAL] 是否已过期 (optional) (default to false)

try:
    # 查询 Charge 对象列表
    api_response = api_instance.trade_service_query_charge_list(app_id=app_id, limit=limit, starting_after=starting_after, ending_before=ending_before, merchant_trade_id=merchant_trade_id, created_lt=created_lt, created_lte=created_lte, created_gt=created_gt, created_gte=created_gte, channel=channel, paid=paid, refunded=refunded, reversed=reversed, closed=closed, expired=expired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->trade_service_query_charge_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| [REQUIRED] 应用 id | [optional] 
 **limit** | **int**| [OPTIONAL] 限制有多少对象可以被返回，限制范围是从 1~100 项，默认是 10 项 | [optional] [default to 10]
 **starting_after** | **str**| [OPTIONAL] 在分页时使用的指针，决定了列表的第一项从何处开始。假设你的一次请求返回列表的最后一项的 id 是 obj_end，你可以使用 starting_after &#x3D; obj_end 去获取下一页 | [optional] 
 **ending_before** | **str**| [OPTIONAL] 在分页时使用的指针，决定了列表的最末项在何处结束。假设你的一次请求返回列表的第一项的 id 是 obj_start，你可以使用 ending_before &#x3D; obj_start 去获取上一页 | [optional] 
 **merchant_trade_id** | **str**| [OPTIONAL] 客户系统订单号 | [optional] 
 **created_lt** | **int**| 大于 charge 对象的创建时间，用 Unix 时间戳表示 | [optional] [default to 0]
 **created_lte** | **int**| 大于或等于 charge 对象的创建时间，用 Unix 时间戳表示 | [optional] [default to 0]
 **created_gt** | **int**| 小于 charge 对象的创建时间，用 Unix 时间戳表示 | [optional] [default to 0]
 **created_gte** | **int**| 小于或等于 charge 对象的创建时间，用 Unix 时间戳表示 | [optional] [default to 0]
 **channel** | **str**| [OPTIONAL] 渠道名称   - BALANCE: 余额支付  - AlipayQR: 支付宝扫码支付  - AlipayScan: 支付宝条码支付  - AlipayApp: 支付宝 App 支付  - AlipayWap: 支付宝手机网站支付  - AlipayPage: 支付宝电脑网站支付  - AlipayFace: 支付宝刷脸支付  - AlipayLite: 支付宝小程序支付  - WechatpayApp: 微信 App 支付  - WechatpayJSAPI: 微信 JSAPI 支付  - WechatpayH5: 微信 H5 支付  - WechatpayNative: 微信 Native 支付  - WechatpayLite: 微信小程序支付  - WechatpayFace: 刷脸支付  - WechatpayScan: 微信付款码支付 | [optional] [default to CHANNEL_INVALID_UNSPECIFIED]
 **paid** | **bool**| [OPTIONAL] 是否已付款 | [optional] [default to false]
 **refunded** | **bool**| [OPTIONAL] 是否存在退款信息，无论退款是否成功。 | [optional] [default to false]
 **reversed** | **bool**| [OPTIONAL] 是否已撤销 | [optional] [default to false]
 **closed** | **bool**| [OPTIONAL] 是否已关闭 | [optional] [default to false]
 **expired** | **bool**| [OPTIONAL] 是否已过期 | [optional] [default to false]

### Return type

[**V1ChargeListResponse**](V1ChargeListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trade_service_query_refund**
> V1RefundResponse trade_service_query_refund(charge_id, refund_id, app_id=app_id)

查询 Refund 对象

可以通过 charge 对象的查询接口查询某一个 charge 对象的退款列表，也可以通过 refund 对象的 id 查询一个已创建的 refund 对象。可以在 Webhooks 通知之前，通过查询接口确认退款状态。

### Example
```python
from __future__ import print_function
import time
import justap_server_sdk_python
from justap_server_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = justap_server_sdk_python.Configuration()
configuration.api_key['X-JUSTAP-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-JUSTAP-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = justap_server_sdk_python.DefaultApi(justap_server_sdk_python.ApiClient(configuration))
charge_id = 'charge_id_example' # str | [REQUIRED] 支付 Charge Id
refund_id = 'refund_id_example' # str | [REQUIRED] Refund 对象 id
app_id = 'app_id_example' # str | [REQUIRED] 应用 id (optional)

try:
    # 查询 Refund 对象
    api_response = api_instance.trade_service_query_refund(charge_id, refund_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->trade_service_query_refund: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **charge_id** | **str**| [REQUIRED] 支付 Charge Id | 
 **refund_id** | **str**| [REQUIRED] Refund 对象 id | 
 **app_id** | **str**| [REQUIRED] 应用 id | [optional] 

### Return type

[**V1RefundResponse**](V1RefundResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trade_service_query_refund_list**
> V1RefundListResponse trade_service_query_refund_list(charge_id, app_id=app_id, limit=limit, starting_after=starting_after, ending_before=ending_before)

查询 Refund 对象列表

返回之前创建 charge 对象的一个 refund 对象列表。列表是按创建时间进行排序，总是将最新的 refund 对象显示在最前。

### Example
```python
from __future__ import print_function
import time
import justap_server_sdk_python
from justap_server_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = justap_server_sdk_python.Configuration()
configuration.api_key['X-JUSTAP-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-JUSTAP-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = justap_server_sdk_python.DefaultApi(justap_server_sdk_python.ApiClient(configuration))
charge_id = 'charge_id_example' # str | [REQUIRED] 支付 Charge Id
app_id = 'app_id_example' # str | [REQUIRED] 应用 id (optional)
limit = 10 # int | [OPTIONAL] 限制有多少对象可以被返回，限制范围是从 1~100 项，默认是 10 项 (optional) (default to 10)
starting_after = 'starting_after_example' # str | [OPTIONAL] 在分页时使用的指针，决定了列表的第一项从何处开始。假设你的一次请求返回列表的最后一项的 id 是 obj_end，你可以使用 starting_after = obj_end 去获取下一页 (optional)
ending_before = 'ending_before_example' # str | [OPTIONAL] 在分页时使用的指针，决定了列表的最末项在何处结束。假设你的一次请求返回列表的第一项的 id 是 obj_start，你可以使用 ending_before = obj_start 去获取上一页 (optional)

try:
    # 查询 Refund 对象列表
    api_response = api_instance.trade_service_query_refund_list(charge_id, app_id=app_id, limit=limit, starting_after=starting_after, ending_before=ending_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->trade_service_query_refund_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **charge_id** | **str**| [REQUIRED] 支付 Charge Id | 
 **app_id** | **str**| [REQUIRED] 应用 id | [optional] 
 **limit** | **int**| [OPTIONAL] 限制有多少对象可以被返回，限制范围是从 1~100 项，默认是 10 项 | [optional] [default to 10]
 **starting_after** | **str**| [OPTIONAL] 在分页时使用的指针，决定了列表的第一项从何处开始。假设你的一次请求返回列表的最后一项的 id 是 obj_end，你可以使用 starting_after &#x3D; obj_end 去获取下一页 | [optional] 
 **ending_before** | **str**| [OPTIONAL] 在分页时使用的指针，决定了列表的最末项在何处结束。假设你的一次请求返回列表的第一项的 id 是 obj_start，你可以使用 ending_before &#x3D; obj_start 去获取上一页 | [optional] 

### Return type

[**V1RefundListResponse**](V1RefundListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trade_service_refunds**
> V1RefundResponse trade_service_refunds(body)

创建 Refund 对象

通过发起一次退款请求创建一个新的 refund 对象，只能对已经发生交易并且没有全额退款的 charge 对象发起退款。当进行全额退款之前，可以进行多次退款，直至全额退款。当一次退款成功后，会发送 Webhooks 通知。

### Example
```python
from __future__ import print_function
import time
import justap_server_sdk_python
from justap_server_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = justap_server_sdk_python.Configuration()
configuration.api_key['X-JUSTAP-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-JUSTAP-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = justap_server_sdk_python.DefaultApi(justap_server_sdk_python.ApiClient(configuration))
body = justap_server_sdk_python.V1CreateRefundRequest() # V1CreateRefundRequest | 

try:
    # 创建 Refund 对象
    api_response = api_instance.trade_service_refunds(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->trade_service_refunds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreateRefundRequest**](V1CreateRefundRequest.md)|  | 

### Return type

[**V1RefundResponse**](V1RefundResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trade_service_reverse_charge**
> V1ChargeResponse trade_service_reverse_charge(charge_id, app_id=app_id)

撤销 Charge 对象

针对已经创建的 Charge，你可以调用撤销接口进行交易的关闭。接口支持对于未成功付款的订单进行撤销，则关闭交易。调用此接口后用户后期不能支付成功。  注：撤销订单在不同收单机构会有不同的行为。对于成功付款的订单请使用 退款 接口进行退款处理。只有针对未支付的订单，我们建议你调用撤销接口。  - 微信支付：如果此订单用户支付失败，微信支付系统会将此订单关闭；如果用户支付成功，微信支付系统会将此订单资金退还给用户。(7天以内的交易单可调用撤销) - 支付宝：如果此订单用户支付失败，支付宝系统会将此订单关闭；如果用户支付成功，支付宝系统会将此订单资金退还给用户。

### Example
```python
from __future__ import print_function
import time
import justap_server_sdk_python
from justap_server_sdk_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = justap_server_sdk_python.Configuration()
configuration.api_key['X-JUSTAP-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-JUSTAP-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = justap_server_sdk_python.DefaultApi(justap_server_sdk_python.ApiClient(configuration))
charge_id = 'charge_id_example' # str | Charge 对象 id
app_id = 'app_id_example' # str | [REQUIRED] 应用 id (optional)

try:
    # 撤销 Charge 对象
    api_response = api_instance.trade_service_reverse_charge(charge_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->trade_service_reverse_charge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **charge_id** | **str**| Charge 对象 id | 
 **app_id** | **str**| [REQUIRED] 应用 id | [optional] 

### Return type

[**V1ChargeResponse**](V1ChargeResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

