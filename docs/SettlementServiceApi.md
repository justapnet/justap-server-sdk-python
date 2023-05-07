# justap_server_sdk_python.SettlementServiceApi

All URIs are relative to *http://127.0.0.1:21011*

Method | HTTP request | Description
------------- | ------------- | -------------
[**settlement_service_create_settlement_account**](SettlementServiceApi.md#settlement_service_create_settlement_account) | **POST** /v1/settlement_accounts | 创建 SettlementAccount 对象
[**settlement_service_delete_settlement_account**](SettlementServiceApi.md#settlement_service_delete_settlement_account) | **DELETE** /v1/settlement_accounts/{id} | 删除 SettlementAccount 对象
[**settlement_service_list_all_settlement_accounts**](SettlementServiceApi.md#settlement_service_list_all_settlement_accounts) | **GET** /v1/settlement_accounts | 查询 SettlementAccount 对象列表
[**settlement_service_retrieve_settlement_account**](SettlementServiceApi.md#settlement_service_retrieve_settlement_account) | **GET** /v1/settlement_accounts/{id} | 查询 SettlementAccount 对象
[**settlement_service_search_settlement_accounts**](SettlementServiceApi.md#settlement_service_search_settlement_accounts) | **GET** /v1/settlement_accounts/search | 搜索 SettlementAccount 对象
[**settlement_service_update_settlement_account**](SettlementServiceApi.md#settlement_service_update_settlement_account) | **POST** /v1/settlement_accounts/{id} | 更新 SettlementAccount 对象


# **settlement_service_create_settlement_account**
> V1SettlementAccountResponse settlement_service_create_settlement_account(app_id=app_id, user_id=user_id, customer_id=customer_id, channel=channel, recipient_wechatpay_channel_recipient_account=recipient_wechatpay_channel_recipient_account, recipient_wechatpay_channel_recipient_name=recipient_wechatpay_channel_recipient_name, recipient_wechatpay_channel_recipient_force_check=recipient_wechatpay_channel_recipient_force_check, recipient_wechatpay_channel_recipient_type=recipient_wechatpay_channel_recipient_type, recipient_wechatpay_channel_recipient_account_type=recipient_wechatpay_channel_recipient_account_type, recipient_wechatpay_channel_recipient_app_id=recipient_wechatpay_channel_recipient_app_id, recipient_alipay_channel_recipient_account=recipient_alipay_channel_recipient_account, recipient_alipay_channel_recipient_name=recipient_alipay_channel_recipient_name, recipient_alipay_channel_recipient_type=recipient_alipay_channel_recipient_type, recipient_alipay_channel_recipient_account_type=recipient_alipay_channel_recipient_account_type, recipient_bank_channel_recipient_account=recipient_bank_channel_recipient_account, recipient_bank_channel_recipient_name=recipient_bank_channel_recipient_name, recipient_bank_channel_recipient_type=recipient_bank_channel_recipient_type, recipient_bank_channel_recipient_bank_name=recipient_bank_channel_recipient_bank_name, recipient_bank_channel_recipient_bank_branch=recipient_bank_channel_recipient_bank_branch, recipient_bank_channel_recipient_bank_province=recipient_bank_channel_recipient_bank_province, recipient_bank_channel_recipient_bank_city=recipient_bank_channel_recipient_bank_city)

创建 SettlementAccount 对象

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
api_instance = justap_server_sdk_python.SettlementServiceApi(justap_server_sdk_python.ApiClient(configuration))
app_id = 'app_id_example' # str |  (optional)
user_id = 'user_id_example' # str |  (optional)
customer_id = 'customer_id_example' # str |  (optional)
channel = 'CHANNEL_UNKNOWN' # str |  - ALIPAY: 分账到支付宝  - WECHANTPAY: 分账到微信支付  - BANK: 分账到银行卡  - BALANCE: 分账到 justap 账户余额 (optional) (default to CHANNEL_UNKNOWN)
recipient_wechatpay_channel_recipient_account = 'recipient_wechatpay_channel_recipient_account_example' # str | openid 或者商户号，由类型决定  微信支付分账接收方账户，OPENID或者商户号 (optional)
recipient_wechatpay_channel_recipient_name = 'recipient_wechatpay_channel_recipient_name_example' # str | 微信支付分账接收方姓名或名称 (optional)
recipient_wechatpay_channel_recipient_force_check = false # bool | 是否强制校验收款人姓名 (optional) (default to false)
recipient_wechatpay_channel_recipient_type = 'TYPE_UNSET' # str | 微信支付分账接收方类型 (optional) (default to TYPE_UNSET)
recipient_wechatpay_channel_recipient_account_type = 'ACCOUNT_TYPE_UNSET' # str | 微信支付分账接收方账户类型   - ACCOUNT_TYPE_UNSET: 未设置  - MERCHANT_ID: 分账到微信商户号  - OPENID: 分账到个人微信号（父公众号的openid，或服务商的openid））  - SUB_OPENID: 分账到个人微信号，子账号的  - LOGIN_NAME: 分账到微信登录号 (optional) (default to ACCOUNT_TYPE_UNSET)
recipient_wechatpay_channel_recipient_app_id = 'recipient_wechatpay_channel_recipient_app_id_example' # str | 微信支付分账接收方 openid 所对应的公众号 ID (optional)
recipient_alipay_channel_recipient_account = 'recipient_alipay_channel_recipient_account_example' # str | 支付宝账号，账号ID或者登录邮箱 (optional)
recipient_alipay_channel_recipient_name = 'recipient_alipay_channel_recipient_name_example' # str | 支付宝账号真实姓名 (optional)
recipient_alipay_channel_recipient_type = 'TYPE_UNSET' # str | 支付宝账号类型 (optional) (default to TYPE_UNSET)
recipient_alipay_channel_recipient_account_type = 'ACCOUNT_TYPE_UNSET' # str | 支付宝账号类型   - ACCOUNT_TYPE_UNSET: 未设置  - MERCHANT_ID: 分账到微信商户号  - OPENID: 分账到个人微信号（父公众号的openid，或服务商的openid））  - SUB_OPENID: 分账到个人微信号，子账号的  - LOGIN_NAME: 分账到微信登录号 (optional) (default to ACCOUNT_TYPE_UNSET)
recipient_bank_channel_recipient_account = 'recipient_bank_channel_recipient_account_example' # str | 银行卡号 (optional)
recipient_bank_channel_recipient_name = 'recipient_bank_channel_recipient_name_example' # str | 银行卡开户名 (optional)
recipient_bank_channel_recipient_type = 'recipient_bank_channel_recipient_type_example' # str | 银行卡类型 (optional)
recipient_bank_channel_recipient_bank_name = 'recipient_bank_channel_recipient_bank_name_example' # str | 银行卡开户行编码 (optional)
recipient_bank_channel_recipient_bank_branch = 'recipient_bank_channel_recipient_bank_branch_example' # str | 银行卡开户支行 (optional)
recipient_bank_channel_recipient_bank_province = 'recipient_bank_channel_recipient_bank_province_example' # str | 银行卡开户省份 (optional)
recipient_bank_channel_recipient_bank_city = 'recipient_bank_channel_recipient_bank_city_example' # str | 银行卡开户城市 (optional)

try:
    # 创建 SettlementAccount 对象
    api_response = api_instance.settlement_service_create_settlement_account(app_id=app_id, user_id=user_id, customer_id=customer_id, channel=channel, recipient_wechatpay_channel_recipient_account=recipient_wechatpay_channel_recipient_account, recipient_wechatpay_channel_recipient_name=recipient_wechatpay_channel_recipient_name, recipient_wechatpay_channel_recipient_force_check=recipient_wechatpay_channel_recipient_force_check, recipient_wechatpay_channel_recipient_type=recipient_wechatpay_channel_recipient_type, recipient_wechatpay_channel_recipient_account_type=recipient_wechatpay_channel_recipient_account_type, recipient_wechatpay_channel_recipient_app_id=recipient_wechatpay_channel_recipient_app_id, recipient_alipay_channel_recipient_account=recipient_alipay_channel_recipient_account, recipient_alipay_channel_recipient_name=recipient_alipay_channel_recipient_name, recipient_alipay_channel_recipient_type=recipient_alipay_channel_recipient_type, recipient_alipay_channel_recipient_account_type=recipient_alipay_channel_recipient_account_type, recipient_bank_channel_recipient_account=recipient_bank_channel_recipient_account, recipient_bank_channel_recipient_name=recipient_bank_channel_recipient_name, recipient_bank_channel_recipient_type=recipient_bank_channel_recipient_type, recipient_bank_channel_recipient_bank_name=recipient_bank_channel_recipient_bank_name, recipient_bank_channel_recipient_bank_branch=recipient_bank_channel_recipient_bank_branch, recipient_bank_channel_recipient_bank_province=recipient_bank_channel_recipient_bank_province, recipient_bank_channel_recipient_bank_city=recipient_bank_channel_recipient_bank_city)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettlementServiceApi->settlement_service_create_settlement_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | [optional] 
 **user_id** | **str**|  | [optional] 
 **customer_id** | **str**|  | [optional] 
 **channel** | **str**|  - ALIPAY: 分账到支付宝  - WECHANTPAY: 分账到微信支付  - BANK: 分账到银行卡  - BALANCE: 分账到 justap 账户余额 | [optional] [default to CHANNEL_UNKNOWN]
 **recipient_wechatpay_channel_recipient_account** | **str**| openid 或者商户号，由类型决定  微信支付分账接收方账户，OPENID或者商户号 | [optional] 
 **recipient_wechatpay_channel_recipient_name** | **str**| 微信支付分账接收方姓名或名称 | [optional] 
 **recipient_wechatpay_channel_recipient_force_check** | **bool**| 是否强制校验收款人姓名 | [optional] [default to false]
 **recipient_wechatpay_channel_recipient_type** | **str**| 微信支付分账接收方类型 | [optional] [default to TYPE_UNSET]
 **recipient_wechatpay_channel_recipient_account_type** | **str**| 微信支付分账接收方账户类型   - ACCOUNT_TYPE_UNSET: 未设置  - MERCHANT_ID: 分账到微信商户号  - OPENID: 分账到个人微信号（父公众号的openid，或服务商的openid））  - SUB_OPENID: 分账到个人微信号，子账号的  - LOGIN_NAME: 分账到微信登录号 | [optional] [default to ACCOUNT_TYPE_UNSET]
 **recipient_wechatpay_channel_recipient_app_id** | **str**| 微信支付分账接收方 openid 所对应的公众号 ID | [optional] 
 **recipient_alipay_channel_recipient_account** | **str**| 支付宝账号，账号ID或者登录邮箱 | [optional] 
 **recipient_alipay_channel_recipient_name** | **str**| 支付宝账号真实姓名 | [optional] 
 **recipient_alipay_channel_recipient_type** | **str**| 支付宝账号类型 | [optional] [default to TYPE_UNSET]
 **recipient_alipay_channel_recipient_account_type** | **str**| 支付宝账号类型   - ACCOUNT_TYPE_UNSET: 未设置  - MERCHANT_ID: 分账到微信商户号  - OPENID: 分账到个人微信号（父公众号的openid，或服务商的openid））  - SUB_OPENID: 分账到个人微信号，子账号的  - LOGIN_NAME: 分账到微信登录号 | [optional] [default to ACCOUNT_TYPE_UNSET]
 **recipient_bank_channel_recipient_account** | **str**| 银行卡号 | [optional] 
 **recipient_bank_channel_recipient_name** | **str**| 银行卡开户名 | [optional] 
 **recipient_bank_channel_recipient_type** | **str**| 银行卡类型 | [optional] 
 **recipient_bank_channel_recipient_bank_name** | **str**| 银行卡开户行编码 | [optional] 
 **recipient_bank_channel_recipient_bank_branch** | **str**| 银行卡开户支行 | [optional] 
 **recipient_bank_channel_recipient_bank_province** | **str**| 银行卡开户省份 | [optional] 
 **recipient_bank_channel_recipient_bank_city** | **str**| 银行卡开户城市 | [optional] 

### Return type

[**V1SettlementAccountResponse**](V1SettlementAccountResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settlement_service_delete_settlement_account**
> V1DeleteSettlementAccountResponse settlement_service_delete_settlement_account(id, app_id=app_id)

删除 SettlementAccount 对象

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
api_instance = justap_server_sdk_python.SettlementServiceApi(justap_server_sdk_python.ApiClient(configuration))
id = 'id_example' # str | 
app_id = 'app_id_example' # str |  (optional)

try:
    # 删除 SettlementAccount 对象
    api_response = api_instance.settlement_service_delete_settlement_account(id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettlementServiceApi->settlement_service_delete_settlement_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **app_id** | **str**|  | [optional] 

### Return type

[**V1DeleteSettlementAccountResponse**](V1DeleteSettlementAccountResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settlement_service_list_all_settlement_accounts**
> V1SettlementAccountListResponse settlement_service_list_all_settlement_accounts(app_id=app_id, limit=limit, starting_after=starting_after, ending_before=ending_before, created_lt=created_lt, created_lte=created_lte, created_gt=created_gt, created_gte=created_gte, disabled=disabled, customer_id=customer_id, user_id=user_id)

查询 SettlementAccount 对象列表

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
api_instance = justap_server_sdk_python.SettlementServiceApi(justap_server_sdk_python.ApiClient(configuration))
app_id = 'app_id_example' # str |  (optional)
limit = 10 # int | [OPTIONAL] 限制有多少对象可以被返回，限制范围是从 1~100 项，默认是 10 项 (optional) (default to 10)
starting_after = 'starting_after_example' # str | [OPTIONAL] 在分页时使用的指针，决定了列表的第一项从何处开始。假设你的一次请求返回列表的最后一项的 id 是 obj_end，你可以使用 starting_after = obj_end 去获取下一页 (optional)
ending_before = 'ending_before_example' # str | [OPTIONAL] 在分页时使用的指针，决定了列表的最末项在何处结束。假设你的一次请求返回列表的第一项的 id 是 obj_start，你可以使用 ending_before = obj_start 去获取上一页 (optional)
created_lt = 0 # int | 大于 charge 对象的创建时间，用 Unix 时间戳表示 (optional) (default to 0)
created_lte = 0 # int | 大于或等于 charge 对象的创建时间，用 Unix 时间戳表示 (optional) (default to 0)
created_gt = 0 # int | 小于 charge 对象的创建时间，用 Unix 时间戳表示 (optional) (default to 0)
created_gte = 0 # int | 小于或等于 charge 对象的创建时间，用 Unix 时间戳表示 (optional) (default to 0)
disabled = true # bool | [OPTIONAL] 是否禁用，默认为 false (optional)
customer_id = 'customer_id_example' # str | [OPTIONAL] 客户 ID (optional)
user_id = 'user_id_example' # str | [OPTIONAL] 商户用户 ID (optional)

try:
    # 查询 SettlementAccount 对象列表
    api_response = api_instance.settlement_service_list_all_settlement_accounts(app_id=app_id, limit=limit, starting_after=starting_after, ending_before=ending_before, created_lt=created_lt, created_lte=created_lte, created_gt=created_gt, created_gte=created_gte, disabled=disabled, customer_id=customer_id, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettlementServiceApi->settlement_service_list_all_settlement_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | [optional] 
 **limit** | **int**| [OPTIONAL] 限制有多少对象可以被返回，限制范围是从 1~100 项，默认是 10 项 | [optional] [default to 10]
 **starting_after** | **str**| [OPTIONAL] 在分页时使用的指针，决定了列表的第一项从何处开始。假设你的一次请求返回列表的最后一项的 id 是 obj_end，你可以使用 starting_after &#x3D; obj_end 去获取下一页 | [optional] 
 **ending_before** | **str**| [OPTIONAL] 在分页时使用的指针，决定了列表的最末项在何处结束。假设你的一次请求返回列表的第一项的 id 是 obj_start，你可以使用 ending_before &#x3D; obj_start 去获取上一页 | [optional] 
 **created_lt** | **int**| 大于 charge 对象的创建时间，用 Unix 时间戳表示 | [optional] [default to 0]
 **created_lte** | **int**| 大于或等于 charge 对象的创建时间，用 Unix 时间戳表示 | [optional] [default to 0]
 **created_gt** | **int**| 小于 charge 对象的创建时间，用 Unix 时间戳表示 | [optional] [default to 0]
 **created_gte** | **int**| 小于或等于 charge 对象的创建时间，用 Unix 时间戳表示 | [optional] [default to 0]
 **disabled** | **bool**| [OPTIONAL] 是否禁用，默认为 false | [optional] 
 **customer_id** | **str**| [OPTIONAL] 客户 ID | [optional] 
 **user_id** | **str**| [OPTIONAL] 商户用户 ID | [optional] 

### Return type

[**V1SettlementAccountListResponse**](V1SettlementAccountListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settlement_service_retrieve_settlement_account**
> V1SettlementAccountResponse settlement_service_retrieve_settlement_account(id, app_id=app_id, object=object, data_id=data_id, data_app_id=data_app_id, data_user_id=data_user_id, data_channel=data_channel, data_recipient_wechatpay_channel_recipient_account=data_recipient_wechatpay_channel_recipient_account, data_recipient_wechatpay_channel_recipient_name=data_recipient_wechatpay_channel_recipient_name, data_recipient_wechatpay_channel_recipient_force_check=data_recipient_wechatpay_channel_recipient_force_check, data_recipient_wechatpay_channel_recipient_type=data_recipient_wechatpay_channel_recipient_type, data_recipient_wechatpay_channel_recipient_account_type=data_recipient_wechatpay_channel_recipient_account_type, data_recipient_wechatpay_channel_recipient_app_id=data_recipient_wechatpay_channel_recipient_app_id, data_recipient_alipay_channel_recipient_account=data_recipient_alipay_channel_recipient_account, data_recipient_alipay_channel_recipient_name=data_recipient_alipay_channel_recipient_name, data_recipient_alipay_channel_recipient_type=data_recipient_alipay_channel_recipient_type, data_recipient_alipay_channel_recipient_account_type=data_recipient_alipay_channel_recipient_account_type, data_recipient_bank_channel_recipient_account=data_recipient_bank_channel_recipient_account, data_recipient_bank_channel_recipient_name=data_recipient_bank_channel_recipient_name, data_recipient_bank_channel_recipient_type=data_recipient_bank_channel_recipient_type, data_recipient_bank_channel_recipient_bank_name=data_recipient_bank_channel_recipient_bank_name, data_recipient_bank_channel_recipient_bank_branch=data_recipient_bank_channel_recipient_bank_branch, data_recipient_bank_channel_recipient_bank_province=data_recipient_bank_channel_recipient_bank_province, data_recipient_bank_channel_recipient_bank_city=data_recipient_bank_channel_recipient_bank_city, data_created=data_created, data_updated=data_updated, data_object=data_object)

查询 SettlementAccount 对象

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
api_instance = justap_server_sdk_python.SettlementServiceApi(justap_server_sdk_python.ApiClient(configuration))
id = 'id_example' # str | 
app_id = 'app_id_example' # str |  (optional)
object = 'SettlementAccount' # str | 对象类型 (optional) (default to SettlementAccount)
data_id = '0' # str | 分账接收方的唯一标识 (optional) (default to 0)
data_app_id = '0' # str | 分账接收方所在的应用 ID (optional) (default to 0)
data_user_id = '0' # str | 分账接收方的用户 ID (optional) (default to 0)
data_channel = 'CHANNEL_UNKNOWN' # str | 分账接收方的账户类型   - ALIPAY: 分账到支付宝  - WECHANTPAY: 分账到微信支付  - BANK: 分账到银行卡  - BALANCE: 分账到 justap 账户余额 (optional) (default to CHANNEL_UNKNOWN)
data_recipient_wechatpay_channel_recipient_account = 'data_recipient_wechatpay_channel_recipient_account_example' # str | openid 或者商户号，由类型决定  微信支付分账接收方账户，OPENID或者商户号 (optional)
data_recipient_wechatpay_channel_recipient_name = 'data_recipient_wechatpay_channel_recipient_name_example' # str | 微信支付分账接收方姓名或名称 (optional)
data_recipient_wechatpay_channel_recipient_force_check = false # bool | 是否强制校验收款人姓名 (optional) (default to false)
data_recipient_wechatpay_channel_recipient_type = 'TYPE_UNSET' # str | 微信支付分账接收方类型 (optional) (default to TYPE_UNSET)
data_recipient_wechatpay_channel_recipient_account_type = 'ACCOUNT_TYPE_UNSET' # str | 微信支付分账接收方账户类型   - ACCOUNT_TYPE_UNSET: 未设置  - MERCHANT_ID: 分账到微信商户号  - OPENID: 分账到个人微信号（父公众号的openid，或服务商的openid））  - SUB_OPENID: 分账到个人微信号，子账号的  - LOGIN_NAME: 分账到微信登录号 (optional) (default to ACCOUNT_TYPE_UNSET)
data_recipient_wechatpay_channel_recipient_app_id = 'data_recipient_wechatpay_channel_recipient_app_id_example' # str | 微信支付分账接收方 openid 所对应的公众号 ID (optional)
data_recipient_alipay_channel_recipient_account = 'data_recipient_alipay_channel_recipient_account_example' # str | 支付宝账号，账号ID或者登录邮箱 (optional)
data_recipient_alipay_channel_recipient_name = 'data_recipient_alipay_channel_recipient_name_example' # str | 支付宝账号真实姓名 (optional)
data_recipient_alipay_channel_recipient_type = 'TYPE_UNSET' # str | 支付宝账号类型 (optional) (default to TYPE_UNSET)
data_recipient_alipay_channel_recipient_account_type = 'ACCOUNT_TYPE_UNSET' # str | 支付宝账号类型   - ACCOUNT_TYPE_UNSET: 未设置  - MERCHANT_ID: 分账到微信商户号  - OPENID: 分账到个人微信号（父公众号的openid，或服务商的openid））  - SUB_OPENID: 分账到个人微信号，子账号的  - LOGIN_NAME: 分账到微信登录号 (optional) (default to ACCOUNT_TYPE_UNSET)
data_recipient_bank_channel_recipient_account = 'data_recipient_bank_channel_recipient_account_example' # str | 银行卡号 (optional)
data_recipient_bank_channel_recipient_name = 'data_recipient_bank_channel_recipient_name_example' # str | 银行卡开户名 (optional)
data_recipient_bank_channel_recipient_type = 'data_recipient_bank_channel_recipient_type_example' # str | 银行卡类型 (optional)
data_recipient_bank_channel_recipient_bank_name = 'data_recipient_bank_channel_recipient_bank_name_example' # str | 银行卡开户行编码 (optional)
data_recipient_bank_channel_recipient_bank_branch = 'data_recipient_bank_channel_recipient_bank_branch_example' # str | 银行卡开户支行 (optional)
data_recipient_bank_channel_recipient_bank_province = 'data_recipient_bank_channel_recipient_bank_province_example' # str | 银行卡开户省份 (optional)
data_recipient_bank_channel_recipient_bank_city = 'data_recipient_bank_channel_recipient_bank_city_example' # str | 银行卡开户城市 (optional)
data_created = 0 # int | 分账接收方的创建时间 (optional) (default to 0)
data_updated = 0 # int | 分账接收方的更新时间 (optional) (default to 0)
data_object = 'Recipient' # str | 对象类型 (optional) (default to Recipient)

try:
    # 查询 SettlementAccount 对象
    api_response = api_instance.settlement_service_retrieve_settlement_account(id, app_id=app_id, object=object, data_id=data_id, data_app_id=data_app_id, data_user_id=data_user_id, data_channel=data_channel, data_recipient_wechatpay_channel_recipient_account=data_recipient_wechatpay_channel_recipient_account, data_recipient_wechatpay_channel_recipient_name=data_recipient_wechatpay_channel_recipient_name, data_recipient_wechatpay_channel_recipient_force_check=data_recipient_wechatpay_channel_recipient_force_check, data_recipient_wechatpay_channel_recipient_type=data_recipient_wechatpay_channel_recipient_type, data_recipient_wechatpay_channel_recipient_account_type=data_recipient_wechatpay_channel_recipient_account_type, data_recipient_wechatpay_channel_recipient_app_id=data_recipient_wechatpay_channel_recipient_app_id, data_recipient_alipay_channel_recipient_account=data_recipient_alipay_channel_recipient_account, data_recipient_alipay_channel_recipient_name=data_recipient_alipay_channel_recipient_name, data_recipient_alipay_channel_recipient_type=data_recipient_alipay_channel_recipient_type, data_recipient_alipay_channel_recipient_account_type=data_recipient_alipay_channel_recipient_account_type, data_recipient_bank_channel_recipient_account=data_recipient_bank_channel_recipient_account, data_recipient_bank_channel_recipient_name=data_recipient_bank_channel_recipient_name, data_recipient_bank_channel_recipient_type=data_recipient_bank_channel_recipient_type, data_recipient_bank_channel_recipient_bank_name=data_recipient_bank_channel_recipient_bank_name, data_recipient_bank_channel_recipient_bank_branch=data_recipient_bank_channel_recipient_bank_branch, data_recipient_bank_channel_recipient_bank_province=data_recipient_bank_channel_recipient_bank_province, data_recipient_bank_channel_recipient_bank_city=data_recipient_bank_channel_recipient_bank_city, data_created=data_created, data_updated=data_updated, data_object=data_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettlementServiceApi->settlement_service_retrieve_settlement_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **app_id** | **str**|  | [optional] 
 **object** | **str**| 对象类型 | [optional] [default to SettlementAccount]
 **data_id** | **str**| 分账接收方的唯一标识 | [optional] [default to 0]
 **data_app_id** | **str**| 分账接收方所在的应用 ID | [optional] [default to 0]
 **data_user_id** | **str**| 分账接收方的用户 ID | [optional] [default to 0]
 **data_channel** | **str**| 分账接收方的账户类型   - ALIPAY: 分账到支付宝  - WECHANTPAY: 分账到微信支付  - BANK: 分账到银行卡  - BALANCE: 分账到 justap 账户余额 | [optional] [default to CHANNEL_UNKNOWN]
 **data_recipient_wechatpay_channel_recipient_account** | **str**| openid 或者商户号，由类型决定  微信支付分账接收方账户，OPENID或者商户号 | [optional] 
 **data_recipient_wechatpay_channel_recipient_name** | **str**| 微信支付分账接收方姓名或名称 | [optional] 
 **data_recipient_wechatpay_channel_recipient_force_check** | **bool**| 是否强制校验收款人姓名 | [optional] [default to false]
 **data_recipient_wechatpay_channel_recipient_type** | **str**| 微信支付分账接收方类型 | [optional] [default to TYPE_UNSET]
 **data_recipient_wechatpay_channel_recipient_account_type** | **str**| 微信支付分账接收方账户类型   - ACCOUNT_TYPE_UNSET: 未设置  - MERCHANT_ID: 分账到微信商户号  - OPENID: 分账到个人微信号（父公众号的openid，或服务商的openid））  - SUB_OPENID: 分账到个人微信号，子账号的  - LOGIN_NAME: 分账到微信登录号 | [optional] [default to ACCOUNT_TYPE_UNSET]
 **data_recipient_wechatpay_channel_recipient_app_id** | **str**| 微信支付分账接收方 openid 所对应的公众号 ID | [optional] 
 **data_recipient_alipay_channel_recipient_account** | **str**| 支付宝账号，账号ID或者登录邮箱 | [optional] 
 **data_recipient_alipay_channel_recipient_name** | **str**| 支付宝账号真实姓名 | [optional] 
 **data_recipient_alipay_channel_recipient_type** | **str**| 支付宝账号类型 | [optional] [default to TYPE_UNSET]
 **data_recipient_alipay_channel_recipient_account_type** | **str**| 支付宝账号类型   - ACCOUNT_TYPE_UNSET: 未设置  - MERCHANT_ID: 分账到微信商户号  - OPENID: 分账到个人微信号（父公众号的openid，或服务商的openid））  - SUB_OPENID: 分账到个人微信号，子账号的  - LOGIN_NAME: 分账到微信登录号 | [optional] [default to ACCOUNT_TYPE_UNSET]
 **data_recipient_bank_channel_recipient_account** | **str**| 银行卡号 | [optional] 
 **data_recipient_bank_channel_recipient_name** | **str**| 银行卡开户名 | [optional] 
 **data_recipient_bank_channel_recipient_type** | **str**| 银行卡类型 | [optional] 
 **data_recipient_bank_channel_recipient_bank_name** | **str**| 银行卡开户行编码 | [optional] 
 **data_recipient_bank_channel_recipient_bank_branch** | **str**| 银行卡开户支行 | [optional] 
 **data_recipient_bank_channel_recipient_bank_province** | **str**| 银行卡开户省份 | [optional] 
 **data_recipient_bank_channel_recipient_bank_city** | **str**| 银行卡开户城市 | [optional] 
 **data_created** | **int**| 分账接收方的创建时间 | [optional] [default to 0]
 **data_updated** | **int**| 分账接收方的更新时间 | [optional] [default to 0]
 **data_object** | **str**| 对象类型 | [optional] [default to Recipient]

### Return type

[**V1SettlementAccountResponse**](V1SettlementAccountResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settlement_service_search_settlement_accounts**
> V1SettlementAccountListResponse settlement_service_search_settlement_accounts(user_id=user_id, app_id=app_id)

搜索 SettlementAccount 对象

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
api_instance = justap_server_sdk_python.SettlementServiceApi(justap_server_sdk_python.ApiClient(configuration))
user_id = 'user_id_example' # str |  (optional)
app_id = 'app_id_example' # str |  (optional)

try:
    # 搜索 SettlementAccount 对象
    api_response = api_instance.settlement_service_search_settlement_accounts(user_id=user_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettlementServiceApi->settlement_service_search_settlement_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | [optional] 
 **app_id** | **str**|  | [optional] 

### Return type

[**V1SettlementAccountListResponse**](V1SettlementAccountListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settlement_service_update_settlement_account**
> V1SettlementAccountResponse settlement_service_update_settlement_account(id, customer_id=customer_id, user_id=user_id, channel=channel, recipient_wechatpay_channel_recipient_account=recipient_wechatpay_channel_recipient_account, recipient_wechatpay_channel_recipient_name=recipient_wechatpay_channel_recipient_name, recipient_wechatpay_channel_recipient_force_check=recipient_wechatpay_channel_recipient_force_check, recipient_wechatpay_channel_recipient_type=recipient_wechatpay_channel_recipient_type, recipient_wechatpay_channel_recipient_account_type=recipient_wechatpay_channel_recipient_account_type, recipient_wechatpay_channel_recipient_app_id=recipient_wechatpay_channel_recipient_app_id, recipient_alipay_channel_recipient_account=recipient_alipay_channel_recipient_account, recipient_alipay_channel_recipient_name=recipient_alipay_channel_recipient_name, recipient_alipay_channel_recipient_type=recipient_alipay_channel_recipient_type, recipient_alipay_channel_recipient_account_type=recipient_alipay_channel_recipient_account_type, recipient_bank_channel_recipient_account=recipient_bank_channel_recipient_account, recipient_bank_channel_recipient_name=recipient_bank_channel_recipient_name, recipient_bank_channel_recipient_type=recipient_bank_channel_recipient_type, recipient_bank_channel_recipient_bank_name=recipient_bank_channel_recipient_bank_name, recipient_bank_channel_recipient_bank_branch=recipient_bank_channel_recipient_bank_branch, recipient_bank_channel_recipient_bank_province=recipient_bank_channel_recipient_bank_province, recipient_bank_channel_recipient_bank_city=recipient_bank_channel_recipient_bank_city)

更新 SettlementAccount 对象

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
api_instance = justap_server_sdk_python.SettlementServiceApi(justap_server_sdk_python.ApiClient(configuration))
id = 'id_example' # str | 
customer_id = 'customer_id_example' # str |  (optional)
user_id = 'user_id_example' # str |  (optional)
channel = 'CHANNEL_UNKNOWN' # str |  - ALIPAY: 分账到支付宝  - WECHANTPAY: 分账到微信支付  - BANK: 分账到银行卡  - BALANCE: 分账到 justap 账户余额 (optional) (default to CHANNEL_UNKNOWN)
recipient_wechatpay_channel_recipient_account = 'recipient_wechatpay_channel_recipient_account_example' # str | openid 或者商户号，由类型决定  微信支付分账接收方账户，OPENID或者商户号 (optional)
recipient_wechatpay_channel_recipient_name = 'recipient_wechatpay_channel_recipient_name_example' # str | 微信支付分账接收方姓名或名称 (optional)
recipient_wechatpay_channel_recipient_force_check = false # bool | 是否强制校验收款人姓名 (optional) (default to false)
recipient_wechatpay_channel_recipient_type = 'TYPE_UNSET' # str | 微信支付分账接收方类型 (optional) (default to TYPE_UNSET)
recipient_wechatpay_channel_recipient_account_type = 'ACCOUNT_TYPE_UNSET' # str | 微信支付分账接收方账户类型   - ACCOUNT_TYPE_UNSET: 未设置  - MERCHANT_ID: 分账到微信商户号  - OPENID: 分账到个人微信号（父公众号的openid，或服务商的openid））  - SUB_OPENID: 分账到个人微信号，子账号的  - LOGIN_NAME: 分账到微信登录号 (optional) (default to ACCOUNT_TYPE_UNSET)
recipient_wechatpay_channel_recipient_app_id = 'recipient_wechatpay_channel_recipient_app_id_example' # str | 微信支付分账接收方 openid 所对应的公众号 ID (optional)
recipient_alipay_channel_recipient_account = 'recipient_alipay_channel_recipient_account_example' # str | 支付宝账号，账号ID或者登录邮箱 (optional)
recipient_alipay_channel_recipient_name = 'recipient_alipay_channel_recipient_name_example' # str | 支付宝账号真实姓名 (optional)
recipient_alipay_channel_recipient_type = 'TYPE_UNSET' # str | 支付宝账号类型 (optional) (default to TYPE_UNSET)
recipient_alipay_channel_recipient_account_type = 'ACCOUNT_TYPE_UNSET' # str | 支付宝账号类型   - ACCOUNT_TYPE_UNSET: 未设置  - MERCHANT_ID: 分账到微信商户号  - OPENID: 分账到个人微信号（父公众号的openid，或服务商的openid））  - SUB_OPENID: 分账到个人微信号，子账号的  - LOGIN_NAME: 分账到微信登录号 (optional) (default to ACCOUNT_TYPE_UNSET)
recipient_bank_channel_recipient_account = 'recipient_bank_channel_recipient_account_example' # str | 银行卡号 (optional)
recipient_bank_channel_recipient_name = 'recipient_bank_channel_recipient_name_example' # str | 银行卡开户名 (optional)
recipient_bank_channel_recipient_type = 'recipient_bank_channel_recipient_type_example' # str | 银行卡类型 (optional)
recipient_bank_channel_recipient_bank_name = 'recipient_bank_channel_recipient_bank_name_example' # str | 银行卡开户行编码 (optional)
recipient_bank_channel_recipient_bank_branch = 'recipient_bank_channel_recipient_bank_branch_example' # str | 银行卡开户支行 (optional)
recipient_bank_channel_recipient_bank_province = 'recipient_bank_channel_recipient_bank_province_example' # str | 银行卡开户省份 (optional)
recipient_bank_channel_recipient_bank_city = 'recipient_bank_channel_recipient_bank_city_example' # str | 银行卡开户城市 (optional)

try:
    # 更新 SettlementAccount 对象
    api_response = api_instance.settlement_service_update_settlement_account(id, customer_id=customer_id, user_id=user_id, channel=channel, recipient_wechatpay_channel_recipient_account=recipient_wechatpay_channel_recipient_account, recipient_wechatpay_channel_recipient_name=recipient_wechatpay_channel_recipient_name, recipient_wechatpay_channel_recipient_force_check=recipient_wechatpay_channel_recipient_force_check, recipient_wechatpay_channel_recipient_type=recipient_wechatpay_channel_recipient_type, recipient_wechatpay_channel_recipient_account_type=recipient_wechatpay_channel_recipient_account_type, recipient_wechatpay_channel_recipient_app_id=recipient_wechatpay_channel_recipient_app_id, recipient_alipay_channel_recipient_account=recipient_alipay_channel_recipient_account, recipient_alipay_channel_recipient_name=recipient_alipay_channel_recipient_name, recipient_alipay_channel_recipient_type=recipient_alipay_channel_recipient_type, recipient_alipay_channel_recipient_account_type=recipient_alipay_channel_recipient_account_type, recipient_bank_channel_recipient_account=recipient_bank_channel_recipient_account, recipient_bank_channel_recipient_name=recipient_bank_channel_recipient_name, recipient_bank_channel_recipient_type=recipient_bank_channel_recipient_type, recipient_bank_channel_recipient_bank_name=recipient_bank_channel_recipient_bank_name, recipient_bank_channel_recipient_bank_branch=recipient_bank_channel_recipient_bank_branch, recipient_bank_channel_recipient_bank_province=recipient_bank_channel_recipient_bank_province, recipient_bank_channel_recipient_bank_city=recipient_bank_channel_recipient_bank_city)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettlementServiceApi->settlement_service_update_settlement_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **customer_id** | **str**|  | [optional] 
 **user_id** | **str**|  | [optional] 
 **channel** | **str**|  - ALIPAY: 分账到支付宝  - WECHANTPAY: 分账到微信支付  - BANK: 分账到银行卡  - BALANCE: 分账到 justap 账户余额 | [optional] [default to CHANNEL_UNKNOWN]
 **recipient_wechatpay_channel_recipient_account** | **str**| openid 或者商户号，由类型决定  微信支付分账接收方账户，OPENID或者商户号 | [optional] 
 **recipient_wechatpay_channel_recipient_name** | **str**| 微信支付分账接收方姓名或名称 | [optional] 
 **recipient_wechatpay_channel_recipient_force_check** | **bool**| 是否强制校验收款人姓名 | [optional] [default to false]
 **recipient_wechatpay_channel_recipient_type** | **str**| 微信支付分账接收方类型 | [optional] [default to TYPE_UNSET]
 **recipient_wechatpay_channel_recipient_account_type** | **str**| 微信支付分账接收方账户类型   - ACCOUNT_TYPE_UNSET: 未设置  - MERCHANT_ID: 分账到微信商户号  - OPENID: 分账到个人微信号（父公众号的openid，或服务商的openid））  - SUB_OPENID: 分账到个人微信号，子账号的  - LOGIN_NAME: 分账到微信登录号 | [optional] [default to ACCOUNT_TYPE_UNSET]
 **recipient_wechatpay_channel_recipient_app_id** | **str**| 微信支付分账接收方 openid 所对应的公众号 ID | [optional] 
 **recipient_alipay_channel_recipient_account** | **str**| 支付宝账号，账号ID或者登录邮箱 | [optional] 
 **recipient_alipay_channel_recipient_name** | **str**| 支付宝账号真实姓名 | [optional] 
 **recipient_alipay_channel_recipient_type** | **str**| 支付宝账号类型 | [optional] [default to TYPE_UNSET]
 **recipient_alipay_channel_recipient_account_type** | **str**| 支付宝账号类型   - ACCOUNT_TYPE_UNSET: 未设置  - MERCHANT_ID: 分账到微信商户号  - OPENID: 分账到个人微信号（父公众号的openid，或服务商的openid））  - SUB_OPENID: 分账到个人微信号，子账号的  - LOGIN_NAME: 分账到微信登录号 | [optional] [default to ACCOUNT_TYPE_UNSET]
 **recipient_bank_channel_recipient_account** | **str**| 银行卡号 | [optional] 
 **recipient_bank_channel_recipient_name** | **str**| 银行卡开户名 | [optional] 
 **recipient_bank_channel_recipient_type** | **str**| 银行卡类型 | [optional] 
 **recipient_bank_channel_recipient_bank_name** | **str**| 银行卡开户行编码 | [optional] 
 **recipient_bank_channel_recipient_bank_branch** | **str**| 银行卡开户支行 | [optional] 
 **recipient_bank_channel_recipient_bank_province** | **str**| 银行卡开户省份 | [optional] 
 **recipient_bank_channel_recipient_bank_city** | **str**| 银行卡开户城市 | [optional] 

### Return type

[**V1SettlementAccountResponse**](V1SettlementAccountResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

