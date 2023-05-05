# justap_server_sdk_python.BusinessUserServiceApi

All URIs are relative to *http://127.0.0.1:21011*

Method | HTTP request | Description
------------- | ------------- | -------------
[**business_user_service_create_user**](BusinessUserServiceApi.md#business_user_service_create_user) | **POST** /v1/business_users | 创建 BusinessUser 对象
[**business_user_service_delete_user**](BusinessUserServiceApi.md#business_user_service_delete_user) | **DELETE** /v1/business_users/{id} | 删除 BusinessUser 对象
[**business_user_service_list_all_users**](BusinessUserServiceApi.md#business_user_service_list_all_users) | **GET** /v1/business_users | 查询 BusinessUser 对象列表
[**business_user_service_retrieve_user**](BusinessUserServiceApi.md#business_user_service_retrieve_user) | **GET** /v1/business_users/{id} | 查询 BusinessUser 对象
[**business_user_service_search_users**](BusinessUserServiceApi.md#business_user_service_search_users) | **GET** /v1/business_users/search | 搜索 BusinessUser 对象
[**business_user_service_update_user**](BusinessUserServiceApi.md#business_user_service_update_user) | **POST** /v1/business_users/{id} | 更新 BusinessUser 对象


# **business_user_service_create_user**
> V1UserResponse business_user_service_create_user(body)

创建 BusinessUser 对象

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
api_instance = justap_server_sdk_python.BusinessUserServiceApi(justap_server_sdk_python.ApiClient(configuration))
body = justap_server_sdk_python.V1CreateUserRequest() # V1CreateUserRequest | 

try:
    # 创建 BusinessUser 对象
    api_response = api_instance.business_user_service_create_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessUserServiceApi->business_user_service_create_user: %s\n" % e)
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

删除 BusinessUser 对象

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
api_instance = justap_server_sdk_python.BusinessUserServiceApi(justap_server_sdk_python.ApiClient(configuration))
id = 'id_example' # str | 
app_id = 'app_id_example' # str |  (optional)

try:
    # 删除 BusinessUser 对象
    api_response = api_instance.business_user_service_delete_user(id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessUserServiceApi->business_user_service_delete_user: %s\n" % e)
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

查询 BusinessUser 对象列表

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
api_instance = justap_server_sdk_python.BusinessUserServiceApi(justap_server_sdk_python.ApiClient(configuration))
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
    # 查询 BusinessUser 对象列表
    api_response = api_instance.business_user_service_list_all_users(app_id=app_id, limit=limit, starting_after=starting_after, ending_before=ending_before, created_lt=created_lt, created_lte=created_lte, created_gt=created_gt, created_gte=created_gte, disabled=disabled)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessUserServiceApi->business_user_service_list_all_users: %s\n" % e)
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

查询 BusinessUser 对象

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
api_instance = justap_server_sdk_python.BusinessUserServiceApi(justap_server_sdk_python.ApiClient(configuration))
id = 'id_example' # str | 
app_id = 'app_id_example' # str |  (optional)

try:
    # 查询 BusinessUser 对象
    api_response = api_instance.business_user_service_retrieve_user(id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessUserServiceApi->business_user_service_retrieve_user: %s\n" % e)
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

搜索 BusinessUser 对象

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
api_instance = justap_server_sdk_python.BusinessUserServiceApi(justap_server_sdk_python.ApiClient(configuration))
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
    # 搜索 BusinessUser 对象
    api_response = api_instance.business_user_service_search_users(app_id=app_id, limit=limit, created_lt=created_lt, created_lte=created_lte, created_gt=created_gt, created_gte=created_gte, email=email, name=name, phone=phone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessUserServiceApi->business_user_service_search_users: %s\n" % e)
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
> V1UserResponse business_user_service_update_user(id, app_id=app_id, address=address, currency=currency, description=description, email=email, name=name, phone=phone, avatar=avatar, disabled=disabled, gender=gender, parent_user_id=parent_user_id)

更新 BusinessUser 对象

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
api_instance = justap_server_sdk_python.BusinessUserServiceApi(justap_server_sdk_python.ApiClient(configuration))
id = 'id_example' # str | 
app_id = 'app_id_example' # str |  (optional)
address = 'address_example' # str |  (optional)
currency = 'currency_example' # str |  (optional)
description = 'description_example' # str |  (optional)
email = 'email_example' # str |  (optional)
name = 'name_example' # str |  (optional)
phone = 'phone_example' # str |  (optional)
avatar = 'avatar_example' # str |  (optional)
disabled = true # bool |  (optional)
gender = 'GENDER_UNKNOWN' # str |  - GENDER_UNKNOWN: 未设置  - MALE: 男  - FE_MALE: 女  - PRIVACY: 保密  - ThirdGender: 第三性别 (optional) (default to GENDER_UNKNOWN)
parent_user_id = 'parent_user_id_example' # str |  (optional)

try:
    # 更新 BusinessUser 对象
    api_response = api_instance.business_user_service_update_user(id, app_id=app_id, address=address, currency=currency, description=description, email=email, name=name, phone=phone, avatar=avatar, disabled=disabled, gender=gender, parent_user_id=parent_user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessUserServiceApi->business_user_service_update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **app_id** | **str**|  | [optional] 
 **address** | **str**|  | [optional] 
 **currency** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **email** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **phone** | **str**|  | [optional] 
 **avatar** | **str**|  | [optional] 
 **disabled** | **bool**|  | [optional] 
 **gender** | **str**|  - GENDER_UNKNOWN: 未设置  - MALE: 男  - FE_MALE: 女  - PRIVACY: 保密  - ThirdGender: 第三性别 | [optional] [default to GENDER_UNKNOWN]
 **parent_user_id** | **str**|  | [optional] 

### Return type

[**V1UserResponse**](V1UserResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

