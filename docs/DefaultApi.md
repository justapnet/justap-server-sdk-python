# justap_server_sdk_python.DefaultApi

All URIs are relative to *http://127.0.0.1:21011*

Method | HTTP request | Description
------------- | ------------- | -------------
[**business_user_service_create_user**](DefaultApi.md#business_user_service_create_user) | **POST** /v1/business_users | 创建 Business User 对象
[**business_user_service_delete_user**](DefaultApi.md#business_user_service_delete_user) | **DELETE** /v1/business_users/{id} | 删除 Business User 对象
[**business_user_service_list_all_users**](DefaultApi.md#business_user_service_list_all_users) | **GET** /v1/business_users | 查询 Business User 对象列表
[**business_user_service_retrieve_user**](DefaultApi.md#business_user_service_retrieve_user) | **GET** /v1/business_users/{id} | 查询 Business User 对象
[**business_user_service_search_users**](DefaultApi.md#business_user_service_search_users) | **GET** /v1/business_users/search | 查询 Business User 对象列表
[**business_user_service_update_user**](DefaultApi.md#business_user_service_update_user) | **PUT** /v1/business_users/{user.id} | 更新 Business User 对象
[**business_user_service_update_user2**](DefaultApi.md#business_user_service_update_user2) | **PATCH** /v1/business_users/{user.id} | 更新 Business User 对象
[**charge_service_charges**](DefaultApi.md#charge_service_charges) | **POST** /transaction/v1/charges | 创建 Charge 对象
[**charge_service_charges2**](DefaultApi.md#charge_service_charges2) | **POST** /v1/charges | 创建 Charge 对象
[**charge_service_query_charge**](DefaultApi.md#charge_service_query_charge) | **GET** /transaction/v1/charges/{charge_id} | 查询 Charge 对象
[**charge_service_query_charge2**](DefaultApi.md#charge_service_query_charge2) | **GET** /v1/charges/{charge_id} | 查询 Charge 对象
[**charge_service_query_charge3**](DefaultApi.md#charge_service_query_charge3) | **GET** /v1/charges/merchant_trade_id/{merchant_trade_id} | 查询 Charge 对象
[**charge_service_query_charge_list**](DefaultApi.md#charge_service_query_charge_list) | **GET** /transaction/v1/charges | 查询 Charge 对象列表
[**charge_service_query_charge_list2**](DefaultApi.md#charge_service_query_charge_list2) | **GET** /v1/charges | 查询 Charge 对象列表
[**charge_service_reverse_charge**](DefaultApi.md#charge_service_reverse_charge) | **POST** /transaction/v1/charges/{charge_id}/reverse | 撤销 Charge 对象
[**charge_service_reverse_charge2**](DefaultApi.md#charge_service_reverse_charge2) | **POST** /v1/charges/{charge_id}/reverse | 撤销 Charge 对象
[**refund_service_query_refund**](DefaultApi.md#refund_service_query_refund) | **GET** /transaction/v1/charges/{charge_id}/refunds/{refund_id} | 查询 Refund 对象
[**refund_service_query_refund2**](DefaultApi.md#refund_service_query_refund2) | **GET** /v1/refunds/{refund_id} | 查询 Refund 对象
[**refund_service_query_refund_list**](DefaultApi.md#refund_service_query_refund_list) | **GET** /transaction/v1/charges/{charge_id}/refunds | 查询 Refund 对象列表
[**refund_service_query_refund_list2**](DefaultApi.md#refund_service_query_refund_list2) | **GET** /v1/refunds | 查询 Refund 对象列表
[**refund_service_refunds**](DefaultApi.md#refund_service_refunds) | **POST** /transaction/v1/refunds | 创建 Refund 对象
[**refund_service_refunds2**](DefaultApi.md#refund_service_refunds2) | **POST** /v1/refunds | 创建 Refund 对象
[**royalty_service_create_royalty**](DefaultApi.md#royalty_service_create_royalty) | **POST** /v1/royalties | 创建 Royalty 对象
[**royalty_service_list_all_royalties**](DefaultApi.md#royalty_service_list_all_royalties) | **GET** /v1/royalties | 查询 Royalty 对象列表
[**royalty_service_retrieve_royalty**](DefaultApi.md#royalty_service_retrieve_royalty) | **GET** /v1/royalties/{id} | 查询 Royalty 对象
[**settlement_service_create_settlement_account**](DefaultApi.md#settlement_service_create_settlement_account) | **POST** /v1/settlement_accounts | 创建结算账户
[**settlement_service_delete_settlement_account**](DefaultApi.md#settlement_service_delete_settlement_account) | **DELETE** /v1/settlement_accounts/{id} | 删除结算账户
[**settlement_service_list_all_settlement_accounts**](DefaultApi.md#settlement_service_list_all_settlement_accounts) | **GET** /v1/settlement_accounts | 查询结算账户列表
[**settlement_service_retrieve_settlement_account**](DefaultApi.md#settlement_service_retrieve_settlement_account) | **GET** /v1/settlement_accounts/{id} | 查询结算账户
[**settlement_service_search_settlement_accounts**](DefaultApi.md#settlement_service_search_settlement_accounts) | **GET** /v1/settlement_accounts/search | 查询结算账户列表
[**settlement_service_update_settlement_account**](DefaultApi.md#settlement_service_update_settlement_account) | **PUT** /v1/settlement_accounts/{settlementAccount.id} | 更新结算账户
[**settlement_service_update_settlement_account2**](DefaultApi.md#settlement_service_update_settlement_account2) | **PATCH** /v1/settlement_accounts/{settlementAccount.id} | 更新结算账户


# **business_user_service_create_user**
> V1UserResponse business_user_service_create_user(body)

创建 Business User 对象

创建 Business User 对象。商业用户是本系统中的一种账户类型，在交易完成之后可以对该类型的账户进行分账等操作。

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
body = justap_server_sdk_python.V1CreateUserRequest() # V1CreateUserRequest | 

try:
    # 创建 Business User 对象
    api_response = api_instance.business_user_service_create_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->business_user_service_create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreateUserRequest**](V1CreateUserRequest.md)|  | 

### Return type

[**V1UserResponse**](V1UserResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **business_user_service_delete_user**
> V1DeleteUserResponse business_user_service_delete_user(id, app_id=app_id)

删除 Business User 对象

删除 Business User 对象

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
id = 'id_example' # str | 
app_id = 'app_id_example' # str |  (optional)

try:
    # 删除 Business User 对象
    api_response = api_instance.business_user_service_delete_user(id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->business_user_service_delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **app_id** | **str**|  | [optional] 

### Return type

[**V1DeleteUserResponse**](V1DeleteUserResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **business_user_service_list_all_users**
> V1UserListResponse business_user_service_list_all_users(app_id=app_id, limit=limit, starting_after=starting_after, ending_before=ending_before, created_lt=created_lt, created_lte=created_lte, created_gt=created_gt, created_gte=created_gte, disabled=disabled)

查询 Business User 对象列表

查询 Business User 对象列表

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
app_id = 'app_id_example' # str |  (optional)
limit = 10 # int | [OPTIONAL] 限制有多少对象可以被返回，限制范围是从 1~100 项，默认是 10 项 (optional) (default to 10)
starting_after = 'starting_after_example' # str | [OPTIONAL] 在分页时使用的指针，决定了列表的第一项从何处开始。假设你的一次请求返回列表的最后一项的 id 是 obj_end，你可以使用 starting_after = obj_end 去获取下一页 (optional)
ending_before = 'ending_before_example' # str | [OPTIONAL] 在分页时使用的指针，决定了列表的最末项在何处结束。假设你的一次请求返回列表的第一项的 id 是 obj_start，你可以使用 ending_before = obj_start 去获取上一页 (optional)
created_lt = 0 # int | 大于 charge 对象的创建时间，用 Unix 时间戳表示 (optional) (default to 0)
created_lte = 0 # int | 大于或等于 charge 对象的创建时间，用 Unix 时间戳表示 (optional) (default to 0)
created_gt = 0 # int | 小于 charge 对象的创建时间，用 Unix 时间戳表示 (optional) (default to 0)
created_gte = 0 # int | 小于或等于 charge 对象的创建时间，用 Unix 时间戳表示 (optional) (default to 0)
disabled = true # bool | [OPTIONAL] 是否禁用，默认为 false (optional)

try:
    # 查询 Business User 对象列表
    api_response = api_instance.business_user_service_list_all_users(app_id=app_id, limit=limit, starting_after=starting_after, ending_before=ending_before, created_lt=created_lt, created_lte=created_lte, created_gt=created_gt, created_gte=created_gte, disabled=disabled)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->business_user_service_list_all_users: %s\n" % e)
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

### Return type

[**V1UserListResponse**](V1UserListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **business_user_service_retrieve_user**
> V1UserResponse business_user_service_retrieve_user(id, app_id=app_id)

查询 Business User 对象

查询 Business User 对象

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
id = 'id_example' # str | 
app_id = 'app_id_example' # str |  (optional)

try:
    # 查询 Business User 对象
    api_response = api_instance.business_user_service_retrieve_user(id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->business_user_service_retrieve_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **app_id** | **str**|  | [optional] 

### Return type

[**V1UserResponse**](V1UserResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **business_user_service_search_users**
> V1UserListResponse business_user_service_search_users(app_id=app_id, limit=limit, created_lt=created_lt, created_lte=created_lte, created_gt=created_gt, created_gte=created_gte, email=email, name=name, phone=phone)

查询 Business User 对象列表

查询 Business User 对象列表

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
app_id = 'app_id_example' # str |  (optional)
limit = 10 # int | [OPTIONAL] 限制有多少对象可以被返回，限制范围是从 1~100 项，默认是 10 项 (optional) (default to 10)
created_lt = 0 # int | 大于 BusinessUser 对象的创建时间，用 Unix 时间戳表示 (optional) (default to 0)
created_lte = 0 # int | 大于或等于 BusinessUser 对象的创建时间，用 Unix 时间戳表示 (optional) (default to 0)
created_gt = 0 # int | 小于 BusinessUser 对象的创建时间，用 Unix 时间戳表示 (optional) (default to 0)
created_gte = 0 # int | 小于或等于 BusinessUser 对象的创建时间，用 Unix 时间戳表示 (optional) (default to 0)
email = 'email_example' # str | [OPTIONAL] BusinessUser 对象的邮箱地址。支持模糊匹配 (optional)
name = 'name_example' # str | [OPTIONAL] BusinessUser 对象的用户名。支持模糊匹配 (optional)
phone = 'phone_example' # str | [OPTIONAL] BusinessUser 对象的手机号码 (optional)

try:
    # 查询 Business User 对象列表
    api_response = api_instance.business_user_service_search_users(app_id=app_id, limit=limit, created_lt=created_lt, created_lte=created_lte, created_gt=created_gt, created_gte=created_gte, email=email, name=name, phone=phone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->business_user_service_search_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | [optional] 
 **limit** | **int**| [OPTIONAL] 限制有多少对象可以被返回，限制范围是从 1~100 项，默认是 10 项 | [optional] [default to 10]
 **created_lt** | **int**| 大于 BusinessUser 对象的创建时间，用 Unix 时间戳表示 | [optional] [default to 0]
 **created_lte** | **int**| 大于或等于 BusinessUser 对象的创建时间，用 Unix 时间戳表示 | [optional] [default to 0]
 **created_gt** | **int**| 小于 BusinessUser 对象的创建时间，用 Unix 时间戳表示 | [optional] [default to 0]
 **created_gte** | **int**| 小于或等于 BusinessUser 对象的创建时间，用 Unix 时间戳表示 | [optional] [default to 0]
 **email** | **str**| [OPTIONAL] BusinessUser 对象的邮箱地址。支持模糊匹配 | [optional] 
 **name** | **str**| [OPTIONAL] BusinessUser 对象的用户名。支持模糊匹配 | [optional] 
 **phone** | **str**| [OPTIONAL] BusinessUser 对象的手机号码 | [optional] 

### Return type

[**V1UserListResponse**](V1UserListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **business_user_service_update_user**
> V1UserResponse business_user_service_update_user(user_id, body, update_mask=update_mask)

更新 Business User 对象

更新 Business User 对象

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
user_id = 'user_id_example' # str | 
body = justap_server_sdk_python.V1BusinessUser() # V1BusinessUser | 
update_mask = 'update_mask_example' # str |  (optional)

try:
    # 更新 Business User 对象
    api_response = api_instance.business_user_service_update_user(user_id, body, update_mask=update_mask)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->business_user_service_update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **body** | [**V1BusinessUser**](V1BusinessUser.md)|  | 
 **update_mask** | **str**|  | [optional] 

### Return type

[**V1UserResponse**](V1UserResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **business_user_service_update_user2**
> V1UserResponse business_user_service_update_user2(user_id, body, update_mask=update_mask)

更新 Business User 对象

更新 Business User 对象

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
user_id = 'user_id_example' # str | 
body = justap_server_sdk_python.V1BusinessUser() # V1BusinessUser | 
update_mask = 'update_mask_example' # str |  (optional)

try:
    # 更新 Business User 对象
    api_response = api_instance.business_user_service_update_user2(user_id, body, update_mask=update_mask)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->business_user_service_update_user2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **body** | [**V1BusinessUser**](V1BusinessUser.md)|  | 
 **update_mask** | **str**|  | [optional] 

### Return type

[**V1UserResponse**](V1UserResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **charge_service_charges**
> V1ChargeResponse charge_service_charges(body)

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
    api_response = api_instance.charge_service_charges(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->charge_service_charges: %s\n" % e)
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

# **charge_service_charges2**
> V1ChargeResponse charge_service_charges2(body)

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
    api_response = api_instance.charge_service_charges2(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->charge_service_charges2: %s\n" % e)
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

# **charge_service_query_charge**
> V1ChargeResponse charge_service_query_charge(charge_id, app_id=app_id, merchant_trade_id=merchant_trade_id)

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
merchant_trade_id = 'merchant_trade_id_example' # str | [OPTIONAL] 商户订单号 (optional)

try:
    # 查询 Charge 对象
    api_response = api_instance.charge_service_query_charge(charge_id, app_id=app_id, merchant_trade_id=merchant_trade_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->charge_service_query_charge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **charge_id** | **str**| [REQUIRED] Charge 对象 id | 
 **app_id** | **str**| [REQUIRED] 应用 id | [optional] 
 **merchant_trade_id** | **str**| [OPTIONAL] 商户订单号 | [optional] 

### Return type

[**V1ChargeResponse**](V1ChargeResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **charge_service_query_charge2**
> V1ChargeResponse charge_service_query_charge2(charge_id, app_id=app_id, merchant_trade_id=merchant_trade_id)

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
merchant_trade_id = 'merchant_trade_id_example' # str | [OPTIONAL] 商户订单号 (optional)

try:
    # 查询 Charge 对象
    api_response = api_instance.charge_service_query_charge2(charge_id, app_id=app_id, merchant_trade_id=merchant_trade_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->charge_service_query_charge2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **charge_id** | **str**| [REQUIRED] Charge 对象 id | 
 **app_id** | **str**| [REQUIRED] 应用 id | [optional] 
 **merchant_trade_id** | **str**| [OPTIONAL] 商户订单号 | [optional] 

### Return type

[**V1ChargeResponse**](V1ChargeResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **charge_service_query_charge3**
> V1ChargeResponse charge_service_query_charge3(merchant_trade_id, charge_id=charge_id, app_id=app_id)

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
merchant_trade_id = 'merchant_trade_id_example' # str | [OPTIONAL] 商户订单号
charge_id = 'charge_id_example' # str | [REQUIRED] Charge 对象 id (optional)
app_id = 'app_id_example' # str | [REQUIRED] 应用 id (optional)

try:
    # 查询 Charge 对象
    api_response = api_instance.charge_service_query_charge3(merchant_trade_id, charge_id=charge_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->charge_service_query_charge3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_trade_id** | **str**| [OPTIONAL] 商户订单号 | 
 **charge_id** | **str**| [REQUIRED] Charge 对象 id | [optional] 
 **app_id** | **str**| [REQUIRED] 应用 id | [optional] 

### Return type

[**V1ChargeResponse**](V1ChargeResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **charge_service_query_charge_list**
> V1ChargeListResponse charge_service_query_charge_list(app_id=app_id, limit=limit, starting_after=starting_after, ending_before=ending_before, merchant_trade_id=merchant_trade_id, created_lt=created_lt, created_lte=created_lte, created_gt=created_gt, created_gte=created_gte, channel=channel, paid=paid, refunded=refunded, reversed=reversed, closed=closed, expired=expired)

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
channel = 'CHANNEL_INVALID_UNSPECIFIED' # str | [OPTIONAL] 渠道名称   - BALANCE: 余额支付  - AlipayQR: 支付宝扫码支付  - AlipayScan: 支付宝条码支付  - AlipayApp: 支付宝 App 支付  - AlipayWap: 支付宝手机网站支付  - AlipayPage: 支付宝电脑网站支付  - AlipayFace: 支付宝刷脸支付  - AlipayLite: 支付宝小程序支付  - AlipayJSAPI: 支付宝 JSAPI 支付  - WechatpayApp: 微信 App 支付  - WechatpayJSAPI: 微信 JSAPI 支付  - WechatpayH5: 微信 H5 支付  - WechatpayNative: 微信 Native 支付  - WechatpayLite: 微信小程序支付  - WechatpayFace: 刷脸支付  - WechatpayScan: 微信付款码支付  - UnionPayQr: 银联二维码支付（云闪付扫码） (optional) (default to CHANNEL_INVALID_UNSPECIFIED)
paid = false # bool | [OPTIONAL] 是否已付款 (optional) (default to false)
refunded = false # bool | [OPTIONAL] 是否存在退款信息，无论退款是否成功。 (optional) (default to false)
reversed = false # bool | [OPTIONAL] 是否已撤销 (optional) (default to false)
closed = false # bool | [OPTIONAL] 是否已关闭 (optional) (default to false)
expired = false # bool | [OPTIONAL] 是否已过期 (optional) (default to false)

try:
    # 查询 Charge 对象列表
    api_response = api_instance.charge_service_query_charge_list(app_id=app_id, limit=limit, starting_after=starting_after, ending_before=ending_before, merchant_trade_id=merchant_trade_id, created_lt=created_lt, created_lte=created_lte, created_gt=created_gt, created_gte=created_gte, channel=channel, paid=paid, refunded=refunded, reversed=reversed, closed=closed, expired=expired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->charge_service_query_charge_list: %s\n" % e)
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
 **channel** | **str**| [OPTIONAL] 渠道名称   - BALANCE: 余额支付  - AlipayQR: 支付宝扫码支付  - AlipayScan: 支付宝条码支付  - AlipayApp: 支付宝 App 支付  - AlipayWap: 支付宝手机网站支付  - AlipayPage: 支付宝电脑网站支付  - AlipayFace: 支付宝刷脸支付  - AlipayLite: 支付宝小程序支付  - AlipayJSAPI: 支付宝 JSAPI 支付  - WechatpayApp: 微信 App 支付  - WechatpayJSAPI: 微信 JSAPI 支付  - WechatpayH5: 微信 H5 支付  - WechatpayNative: 微信 Native 支付  - WechatpayLite: 微信小程序支付  - WechatpayFace: 刷脸支付  - WechatpayScan: 微信付款码支付  - UnionPayQr: 银联二维码支付（云闪付扫码） | [optional] [default to CHANNEL_INVALID_UNSPECIFIED]
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

# **charge_service_query_charge_list2**
> V1ChargeListResponse charge_service_query_charge_list2(app_id=app_id, limit=limit, starting_after=starting_after, ending_before=ending_before, merchant_trade_id=merchant_trade_id, created_lt=created_lt, created_lte=created_lte, created_gt=created_gt, created_gte=created_gte, channel=channel, paid=paid, refunded=refunded, reversed=reversed, closed=closed, expired=expired)

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
channel = 'CHANNEL_INVALID_UNSPECIFIED' # str | [OPTIONAL] 渠道名称   - BALANCE: 余额支付  - AlipayQR: 支付宝扫码支付  - AlipayScan: 支付宝条码支付  - AlipayApp: 支付宝 App 支付  - AlipayWap: 支付宝手机网站支付  - AlipayPage: 支付宝电脑网站支付  - AlipayFace: 支付宝刷脸支付  - AlipayLite: 支付宝小程序支付  - AlipayJSAPI: 支付宝 JSAPI 支付  - WechatpayApp: 微信 App 支付  - WechatpayJSAPI: 微信 JSAPI 支付  - WechatpayH5: 微信 H5 支付  - WechatpayNative: 微信 Native 支付  - WechatpayLite: 微信小程序支付  - WechatpayFace: 刷脸支付  - WechatpayScan: 微信付款码支付  - UnionPayQr: 银联二维码支付（云闪付扫码） (optional) (default to CHANNEL_INVALID_UNSPECIFIED)
paid = false # bool | [OPTIONAL] 是否已付款 (optional) (default to false)
refunded = false # bool | [OPTIONAL] 是否存在退款信息，无论退款是否成功。 (optional) (default to false)
reversed = false # bool | [OPTIONAL] 是否已撤销 (optional) (default to false)
closed = false # bool | [OPTIONAL] 是否已关闭 (optional) (default to false)
expired = false # bool | [OPTIONAL] 是否已过期 (optional) (default to false)

try:
    # 查询 Charge 对象列表
    api_response = api_instance.charge_service_query_charge_list2(app_id=app_id, limit=limit, starting_after=starting_after, ending_before=ending_before, merchant_trade_id=merchant_trade_id, created_lt=created_lt, created_lte=created_lte, created_gt=created_gt, created_gte=created_gte, channel=channel, paid=paid, refunded=refunded, reversed=reversed, closed=closed, expired=expired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->charge_service_query_charge_list2: %s\n" % e)
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
 **channel** | **str**| [OPTIONAL] 渠道名称   - BALANCE: 余额支付  - AlipayQR: 支付宝扫码支付  - AlipayScan: 支付宝条码支付  - AlipayApp: 支付宝 App 支付  - AlipayWap: 支付宝手机网站支付  - AlipayPage: 支付宝电脑网站支付  - AlipayFace: 支付宝刷脸支付  - AlipayLite: 支付宝小程序支付  - AlipayJSAPI: 支付宝 JSAPI 支付  - WechatpayApp: 微信 App 支付  - WechatpayJSAPI: 微信 JSAPI 支付  - WechatpayH5: 微信 H5 支付  - WechatpayNative: 微信 Native 支付  - WechatpayLite: 微信小程序支付  - WechatpayFace: 刷脸支付  - WechatpayScan: 微信付款码支付  - UnionPayQr: 银联二维码支付（云闪付扫码） | [optional] [default to CHANNEL_INVALID_UNSPECIFIED]
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

# **charge_service_reverse_charge**
> V1ChargeResponse charge_service_reverse_charge(charge_id)

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

try:
    # 撤销 Charge 对象
    api_response = api_instance.charge_service_reverse_charge(charge_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->charge_service_reverse_charge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **charge_id** | **str**| Charge 对象 id | 

### Return type

[**V1ChargeResponse**](V1ChargeResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **charge_service_reverse_charge2**
> V1ChargeResponse charge_service_reverse_charge2(charge_id)

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

try:
    # 撤销 Charge 对象
    api_response = api_instance.charge_service_reverse_charge2(charge_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->charge_service_reverse_charge2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **charge_id** | **str**| Charge 对象 id | 

### Return type

[**V1ChargeResponse**](V1ChargeResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund_service_query_refund**
> V1RefundResponse refund_service_query_refund(charge_id, refund_id, app_id=app_id)

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
    api_response = api_instance.refund_service_query_refund(charge_id, refund_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->refund_service_query_refund: %s\n" % e)
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

# **refund_service_query_refund2**
> V1RefundResponse refund_service_query_refund2(refund_id, charge_id=charge_id, app_id=app_id)

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
refund_id = 'refund_id_example' # str | [REQUIRED] Refund 对象 id
charge_id = 'charge_id_example' # str | [REQUIRED] 支付 Charge Id (optional)
app_id = 'app_id_example' # str | [REQUIRED] 应用 id (optional)

try:
    # 查询 Refund 对象
    api_response = api_instance.refund_service_query_refund2(refund_id, charge_id=charge_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->refund_service_query_refund2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refund_id** | **str**| [REQUIRED] Refund 对象 id | 
 **charge_id** | **str**| [REQUIRED] 支付 Charge Id | [optional] 
 **app_id** | **str**| [REQUIRED] 应用 id | [optional] 

### Return type

[**V1RefundResponse**](V1RefundResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund_service_query_refund_list**
> V1RefundListResponse refund_service_query_refund_list(charge_id, app_id=app_id, limit=limit, starting_after=starting_after, ending_before=ending_before)

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
    api_response = api_instance.refund_service_query_refund_list(charge_id, app_id=app_id, limit=limit, starting_after=starting_after, ending_before=ending_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->refund_service_query_refund_list: %s\n" % e)
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

# **refund_service_query_refund_list2**
> V1RefundListResponse refund_service_query_refund_list2(charge_id=charge_id, app_id=app_id, limit=limit, starting_after=starting_after, ending_before=ending_before)

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
charge_id = 'charge_id_example' # str | [REQUIRED] 支付 Charge Id (optional)
app_id = 'app_id_example' # str | [REQUIRED] 应用 id (optional)
limit = 10 # int | [OPTIONAL] 限制有多少对象可以被返回，限制范围是从 1~100 项，默认是 10 项 (optional) (default to 10)
starting_after = 'starting_after_example' # str | [OPTIONAL] 在分页时使用的指针，决定了列表的第一项从何处开始。假设你的一次请求返回列表的最后一项的 id 是 obj_end，你可以使用 starting_after = obj_end 去获取下一页 (optional)
ending_before = 'ending_before_example' # str | [OPTIONAL] 在分页时使用的指针，决定了列表的最末项在何处结束。假设你的一次请求返回列表的第一项的 id 是 obj_start，你可以使用 ending_before = obj_start 去获取上一页 (optional)

try:
    # 查询 Refund 对象列表
    api_response = api_instance.refund_service_query_refund_list2(charge_id=charge_id, app_id=app_id, limit=limit, starting_after=starting_after, ending_before=ending_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->refund_service_query_refund_list2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **charge_id** | **str**| [REQUIRED] 支付 Charge Id | [optional] 
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

# **refund_service_refunds**
> V1RefundResponse refund_service_refunds(body)

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
    api_response = api_instance.refund_service_refunds(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->refund_service_refunds: %s\n" % e)
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

# **refund_service_refunds2**
> V1RefundResponse refund_service_refunds2(body)

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
    api_response = api_instance.refund_service_refunds2(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->refund_service_refunds2: %s\n" % e)
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

# **royalty_service_create_royalty**
> V1RoyaltyResponse royalty_service_create_royalty(body)

创建 Royalty 对象

对一个 Charge 对象进行分账，分账的金额和分账接收方由 Royalty 对象指定。Royalty 创建仅代表本系统成功接收分账申请，尚未提交到支付机构清分，更不代表分账立即成功，相关结果信息请调用查询接口确认

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
body = justap_server_sdk_python.V1CreateRoyaltyRequest() # V1CreateRoyaltyRequest | 

try:
    # 创建 Royalty 对象
    api_response = api_instance.royalty_service_create_royalty(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->royalty_service_create_royalty: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreateRoyaltyRequest**](V1CreateRoyaltyRequest.md)|  | 

### Return type

[**V1RoyaltyResponse**](V1RoyaltyResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **royalty_service_list_all_royalties**
> V1ListAllRoyaltiesResponse royalty_service_list_all_royalties(limit=limit, starting_after=starting_after, ending_before=ending_before, merchant_trade_id=merchant_trade_id, created_lt=created_lt, created_lte=created_lte, created_gt=created_gt, created_gte=created_gte, app_id=app_id, settle_account_id=settle_account_id, royalty_settlement_id=royalty_settlement_id)

查询 Royalty 对象列表

查询 Royalty 对象的列表信息

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
limit = 10 # int | [OPTIONAL] 限制有多少对象可以被返回，限制范围是从 1~100 项，默认是 10 项 (optional) (default to 10)
starting_after = 'starting_after_example' # str | [OPTIONAL] 在分页时使用的指针，决定了列表的第一项从何处开始。假设你的一次请求返回列表的最后一项的 id 是 obj_end，你可以使用 starting_after = obj_end 去获取下一页 (optional)
ending_before = 'ending_before_example' # str | [OPTIONAL] 在分页时使用的指针，决定了列表的最末项在何处结束。假设你的一次请求返回列表的第一项的 id 是 obj_start，你可以使用 ending_before = obj_start 去获取上一页 (optional)
merchant_trade_id = 'merchant_trade_id_example' # str | [OPTIONAL] 客户系统订单号 (optional)
created_lt = 0 # int | 大于 charge 对象的创建时间，用 Unix 时间戳表示 (optional) (default to 0)
created_lte = 0 # int | 大于或等于 charge 对象的创建时间，用 Unix 时间戳表示 (optional) (default to 0)
created_gt = 0 # int | 小于 charge 对象的创建时间，用 Unix 时间戳表示 (optional) (default to 0)
created_gte = 0 # int | 小于或等于 charge 对象的创建时间，用 Unix 时间戳表示 (optional) (default to 0)
app_id = 'app_id_example' # str |  (optional)
settle_account_id = 'settle_account_id_example' # str |  (optional)
royalty_settlement_id = 'royalty_settlement_id_example' # str |  (optional)

try:
    # 查询 Royalty 对象列表
    api_response = api_instance.royalty_service_list_all_royalties(limit=limit, starting_after=starting_after, ending_before=ending_before, merchant_trade_id=merchant_trade_id, created_lt=created_lt, created_lte=created_lte, created_gt=created_gt, created_gte=created_gte, app_id=app_id, settle_account_id=settle_account_id, royalty_settlement_id=royalty_settlement_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->royalty_service_list_all_royalties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| [OPTIONAL] 限制有多少对象可以被返回，限制范围是从 1~100 项，默认是 10 项 | [optional] [default to 10]
 **starting_after** | **str**| [OPTIONAL] 在分页时使用的指针，决定了列表的第一项从何处开始。假设你的一次请求返回列表的最后一项的 id 是 obj_end，你可以使用 starting_after &#x3D; obj_end 去获取下一页 | [optional] 
 **ending_before** | **str**| [OPTIONAL] 在分页时使用的指针，决定了列表的最末项在何处结束。假设你的一次请求返回列表的第一项的 id 是 obj_start，你可以使用 ending_before &#x3D; obj_start 去获取上一页 | [optional] 
 **merchant_trade_id** | **str**| [OPTIONAL] 客户系统订单号 | [optional] 
 **created_lt** | **int**| 大于 charge 对象的创建时间，用 Unix 时间戳表示 | [optional] [default to 0]
 **created_lte** | **int**| 大于或等于 charge 对象的创建时间，用 Unix 时间戳表示 | [optional] [default to 0]
 **created_gt** | **int**| 小于 charge 对象的创建时间，用 Unix 时间戳表示 | [optional] [default to 0]
 **created_gte** | **int**| 小于或等于 charge 对象的创建时间，用 Unix 时间戳表示 | [optional] [default to 0]
 **app_id** | **str**|  | [optional] 
 **settle_account_id** | **str**|  | [optional] 
 **royalty_settlement_id** | **str**|  | [optional] 

### Return type

[**V1ListAllRoyaltiesResponse**](V1ListAllRoyaltiesResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **royalty_service_retrieve_royalty**
> V1RoyaltyResponse royalty_service_retrieve_royalty(id)

查询 Royalty 对象

查询 Royalty 对象的信息

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
id = 'id_example' # str | 

try:
    # 查询 Royalty 对象
    api_response = api_instance.royalty_service_retrieve_royalty(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->royalty_service_retrieve_royalty: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**V1RoyaltyResponse**](V1RoyaltyResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settlement_service_create_settlement_account**
> V1SettlementAccountResponse settlement_service_create_settlement_account(body)

创建结算账户

为用户创建一个结算账户。添加结算账户信息后方可对该用进行分账、余额充值、转账等操作。

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
body = justap_server_sdk_python.V1CreateSettlementAccountRequest() # V1CreateSettlementAccountRequest | 

try:
    # 创建结算账户
    api_response = api_instance.settlement_service_create_settlement_account(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->settlement_service_create_settlement_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreateSettlementAccountRequest**](V1CreateSettlementAccountRequest.md)|  | 

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

删除结算账户

删除结算账户

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
id = 'id_example' # str | 
app_id = 'app_id_example' # str |  (optional)

try:
    # 删除结算账户
    api_response = api_instance.settlement_service_delete_settlement_account(id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->settlement_service_delete_settlement_account: %s\n" % e)
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
> V1SettlementAccountListResponse settlement_service_list_all_settlement_accounts(app_id=app_id, limit=limit, starting_after=starting_after, ending_before=ending_before, created_lt=created_lt, created_lte=created_lte, created_gt=created_gt, created_gte=created_gte, disabled=disabled, customer_id=customer_id, business_user_id=business_user_id)

查询结算账户列表

查询结算账户列表

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
business_user_id = 'business_user_id_example' # str | [OPTIONAL] 商户用户 ID (optional)

try:
    # 查询结算账户列表
    api_response = api_instance.settlement_service_list_all_settlement_accounts(app_id=app_id, limit=limit, starting_after=starting_after, ending_before=ending_before, created_lt=created_lt, created_lte=created_lte, created_gt=created_gt, created_gte=created_gte, disabled=disabled, customer_id=customer_id, business_user_id=business_user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->settlement_service_list_all_settlement_accounts: %s\n" % e)
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
 **business_user_id** | **str**| [OPTIONAL] 商户用户 ID | [optional] 

### Return type

[**V1SettlementAccountListResponse**](V1SettlementAccountListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settlement_service_retrieve_settlement_account**
> V1SettlementAccountResponse settlement_service_retrieve_settlement_account(id, app_id=app_id, object=object, data_id=data_id, data_app_id=data_app_id, data_business_user_id=data_business_user_id, data_customer_id=data_customer_id, data_channel=data_channel, data_recipient_wechatpay_account=data_recipient_wechatpay_account, data_recipient_wechatpay_name=data_recipient_wechatpay_name, data_recipient_wechatpay_force_check=data_recipient_wechatpay_force_check, data_recipient_wechatpay_type=data_recipient_wechatpay_type, data_recipient_wechatpay_account_type=data_recipient_wechatpay_account_type, data_recipient_wechatpay_app_id=data_recipient_wechatpay_app_id, data_recipient_wechatpay_sub_app_id=data_recipient_wechatpay_sub_app_id, data_recipient_payment_alipay_account=data_recipient_payment_alipay_account, data_recipient_payment_alipay_name=data_recipient_payment_alipay_name, data_recipient_payment_alipay_type=data_recipient_payment_alipay_type, data_recipient_payment_alipay_account_type=data_recipient_payment_alipay_account_type, data_recipient_bank_account=data_recipient_bank_account, data_recipient_bank_name=data_recipient_bank_name, data_recipient_bank_type=data_recipient_bank_type, data_recipient_bank_bank_name=data_recipient_bank_bank_name, data_recipient_bank_bank_branch=data_recipient_bank_bank_branch, data_recipient_bank_bank_province=data_recipient_bank_bank_province, data_recipient_bank_bank_city=data_recipient_bank_bank_city, data_recipient_ysepay_merchant_division_mer_usercode=data_recipient_ysepay_merchant_division_mer_usercode, data_created=data_created, data_updated=data_updated, data_object=data_object)

查询结算账户

查询结算账户

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
id = 'id_example' # str | 
app_id = 'app_id_example' # str |  (optional)
object = 'SettlementAccount' # str | 对象类型 (optional) (default to SettlementAccount)
data_id = '0' # str | 分账接收方的唯一标识 (optional) (default to 0)
data_app_id = '0' # str | 分账接收方所在的应用 ID (optional) (default to 0)
data_business_user_id = '0' # str | 分账接收方的用户 ID (optional) (default to 0)
data_customer_id = '0' # str | 分账接收方的用户 ID (optional) (default to 0)
data_channel = 'CHANNEL_UNKNOWN' # str | 分账接收方的账户类型 (optional) (default to CHANNEL_UNKNOWN)
data_recipient_wechatpay_account = 'data_recipient_wechatpay_account_example' # str | openid 或者商户号，由类型决定. 微信支付分账接收方账户，OPENID或者商户号 (optional)
data_recipient_wechatpay_name = 'data_recipient_wechatpay_name_example' # str | 微信支付分账接收方姓名或名称 (optional)
data_recipient_wechatpay_force_check = false # bool | 是否强制校验收款人姓名 (optional) (default to false)
data_recipient_wechatpay_type = 'TYPE_UNSET' # str | 微信支付分账接收方类型 (optional) (default to TYPE_UNSET)
data_recipient_wechatpay_account_type = 'ACCOUNT_TYPE_UNSET' # str | 微信支付分账接收方账户类型 (optional) (default to ACCOUNT_TYPE_UNSET)
data_recipient_wechatpay_app_id = 'data_recipient_wechatpay_app_id_example' # str | 微信支付分账接收方 openid 所对应的服务商公众号 ID (optional)
data_recipient_wechatpay_sub_app_id = 'data_recipient_wechatpay_sub_app_id_example' # str | 微信支付分账接收方 openid 所对应的商户公众号 ID (optional)
data_recipient_payment_alipay_account = 'data_recipient_payment_alipay_account_example' # str | 支付宝账号，账号ID或者登录邮箱 (optional)
data_recipient_payment_alipay_name = 'data_recipient_payment_alipay_name_example' # str | 支付宝账号真实姓名 (optional)
data_recipient_payment_alipay_type = 'TYPE_UNSET' # str | 支付宝账号类型 (optional) (default to TYPE_UNSET)
data_recipient_payment_alipay_account_type = 'ACCOUNT_TYPE_UNSET' # str | 支付宝账号类型 (optional) (default to ACCOUNT_TYPE_UNSET)
data_recipient_bank_account = 'data_recipient_bank_account_example' # str | 银行卡号 (optional)
data_recipient_bank_name = 'data_recipient_bank_name_example' # str | 银行卡开户名 (optional)
data_recipient_bank_type = 'data_recipient_bank_type_example' # str | 银行卡类型 (optional)
data_recipient_bank_bank_name = 'data_recipient_bank_bank_name_example' # str | 银行卡开户行编码 (optional)
data_recipient_bank_bank_branch = 'data_recipient_bank_bank_branch_example' # str | 银行卡开户支行 (optional)
data_recipient_bank_bank_province = 'data_recipient_bank_bank_province_example' # str | 银行卡开户省份 (optional)
data_recipient_bank_bank_city = 'data_recipient_bank_bank_city_example' # str | 银行卡开户城市 (optional)
data_recipient_ysepay_merchant_division_mer_usercode = 'data_recipient_ysepay_merchant_division_mer_usercode_example' # str | 银盛商户号 (optional)
data_created = 0 # int | 分账接收方的创建时间 (optional) (default to 0)
data_updated = 0 # int | 分账接收方的更新时间 (optional) (default to 0)
data_object = 'Recipient' # str | 对象类型 (optional) (default to Recipient)

try:
    # 查询结算账户
    api_response = api_instance.settlement_service_retrieve_settlement_account(id, app_id=app_id, object=object, data_id=data_id, data_app_id=data_app_id, data_business_user_id=data_business_user_id, data_customer_id=data_customer_id, data_channel=data_channel, data_recipient_wechatpay_account=data_recipient_wechatpay_account, data_recipient_wechatpay_name=data_recipient_wechatpay_name, data_recipient_wechatpay_force_check=data_recipient_wechatpay_force_check, data_recipient_wechatpay_type=data_recipient_wechatpay_type, data_recipient_wechatpay_account_type=data_recipient_wechatpay_account_type, data_recipient_wechatpay_app_id=data_recipient_wechatpay_app_id, data_recipient_wechatpay_sub_app_id=data_recipient_wechatpay_sub_app_id, data_recipient_payment_alipay_account=data_recipient_payment_alipay_account, data_recipient_payment_alipay_name=data_recipient_payment_alipay_name, data_recipient_payment_alipay_type=data_recipient_payment_alipay_type, data_recipient_payment_alipay_account_type=data_recipient_payment_alipay_account_type, data_recipient_bank_account=data_recipient_bank_account, data_recipient_bank_name=data_recipient_bank_name, data_recipient_bank_type=data_recipient_bank_type, data_recipient_bank_bank_name=data_recipient_bank_bank_name, data_recipient_bank_bank_branch=data_recipient_bank_bank_branch, data_recipient_bank_bank_province=data_recipient_bank_bank_province, data_recipient_bank_bank_city=data_recipient_bank_bank_city, data_recipient_ysepay_merchant_division_mer_usercode=data_recipient_ysepay_merchant_division_mer_usercode, data_created=data_created, data_updated=data_updated, data_object=data_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->settlement_service_retrieve_settlement_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **app_id** | **str**|  | [optional] 
 **object** | **str**| 对象类型 | [optional] [default to SettlementAccount]
 **data_id** | **str**| 分账接收方的唯一标识 | [optional] [default to 0]
 **data_app_id** | **str**| 分账接收方所在的应用 ID | [optional] [default to 0]
 **data_business_user_id** | **str**| 分账接收方的用户 ID | [optional] [default to 0]
 **data_customer_id** | **str**| 分账接收方的用户 ID | [optional] [default to 0]
 **data_channel** | **str**| 分账接收方的账户类型 | [optional] [default to CHANNEL_UNKNOWN]
 **data_recipient_wechatpay_account** | **str**| openid 或者商户号，由类型决定. 微信支付分账接收方账户，OPENID或者商户号 | [optional] 
 **data_recipient_wechatpay_name** | **str**| 微信支付分账接收方姓名或名称 | [optional] 
 **data_recipient_wechatpay_force_check** | **bool**| 是否强制校验收款人姓名 | [optional] [default to false]
 **data_recipient_wechatpay_type** | **str**| 微信支付分账接收方类型 | [optional] [default to TYPE_UNSET]
 **data_recipient_wechatpay_account_type** | **str**| 微信支付分账接收方账户类型 | [optional] [default to ACCOUNT_TYPE_UNSET]
 **data_recipient_wechatpay_app_id** | **str**| 微信支付分账接收方 openid 所对应的服务商公众号 ID | [optional] 
 **data_recipient_wechatpay_sub_app_id** | **str**| 微信支付分账接收方 openid 所对应的商户公众号 ID | [optional] 
 **data_recipient_payment_alipay_account** | **str**| 支付宝账号，账号ID或者登录邮箱 | [optional] 
 **data_recipient_payment_alipay_name** | **str**| 支付宝账号真实姓名 | [optional] 
 **data_recipient_payment_alipay_type** | **str**| 支付宝账号类型 | [optional] [default to TYPE_UNSET]
 **data_recipient_payment_alipay_account_type** | **str**| 支付宝账号类型 | [optional] [default to ACCOUNT_TYPE_UNSET]
 **data_recipient_bank_account** | **str**| 银行卡号 | [optional] 
 **data_recipient_bank_name** | **str**| 银行卡开户名 | [optional] 
 **data_recipient_bank_type** | **str**| 银行卡类型 | [optional] 
 **data_recipient_bank_bank_name** | **str**| 银行卡开户行编码 | [optional] 
 **data_recipient_bank_bank_branch** | **str**| 银行卡开户支行 | [optional] 
 **data_recipient_bank_bank_province** | **str**| 银行卡开户省份 | [optional] 
 **data_recipient_bank_bank_city** | **str**| 银行卡开户城市 | [optional] 
 **data_recipient_ysepay_merchant_division_mer_usercode** | **str**| 银盛商户号 | [optional] 
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

查询结算账户列表

查询结算账户列表

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
user_id = 'user_id_example' # str |  (optional)
app_id = 'app_id_example' # str |  (optional)

try:
    # 查询结算账户列表
    api_response = api_instance.settlement_service_search_settlement_accounts(user_id=user_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->settlement_service_search_settlement_accounts: %s\n" % e)
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
> V1SettlementAccountResponse settlement_service_update_settlement_account(settlement_account_id, body, update_mask=update_mask)

更新结算账户

更新结算账户

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
settlement_account_id = 'settlement_account_id_example' # str | 
body = justap_server_sdk_python.V1UpdateAndPatchRequestBody() # V1UpdateAndPatchRequestBody | 
update_mask = 'update_mask_example' # str |  (optional)

try:
    # 更新结算账户
    api_response = api_instance.settlement_service_update_settlement_account(settlement_account_id, body, update_mask=update_mask)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->settlement_service_update_settlement_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_account_id** | **str**|  | 
 **body** | [**V1UpdateAndPatchRequestBody**](V1UpdateAndPatchRequestBody.md)|  | 
 **update_mask** | **str**|  | [optional] 

### Return type

[**V1SettlementAccountResponse**](V1SettlementAccountResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settlement_service_update_settlement_account2**
> V1SettlementAccountResponse settlement_service_update_settlement_account2(settlement_account_id, body, update_mask=update_mask)

更新结算账户

更新结算账户

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
settlement_account_id = 'settlement_account_id_example' # str | 
body = justap_server_sdk_python.V1UpdateAndPatchRequestBody() # V1UpdateAndPatchRequestBody | 
update_mask = 'update_mask_example' # str |  (optional)

try:
    # 更新结算账户
    api_response = api_instance.settlement_service_update_settlement_account2(settlement_account_id, body, update_mask=update_mask)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->settlement_service_update_settlement_account2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_account_id** | **str**|  | 
 **body** | [**V1UpdateAndPatchRequestBody**](V1UpdateAndPatchRequestBody.md)|  | 
 **update_mask** | **str**|  | [optional] 

### Return type

[**V1SettlementAccountResponse**](V1SettlementAccountResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

