# justap_server_sdk_python.CustomerServiceApi

All URIs are relative to *http://127.0.0.1:21011*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customer_service_create_customer**](CustomerServiceApi.md#customer_service_create_customer) | **POST** /v1/customers | 
[**customer_service_delete_customer**](CustomerServiceApi.md#customer_service_delete_customer) | **DELETE** /v1/customers/{id} | 
[**customer_service_list_all_customers**](CustomerServiceApi.md#customer_service_list_all_customers) | **GET** /v1/customers | 
[**customer_service_retrieve_customer**](CustomerServiceApi.md#customer_service_retrieve_customer) | **GET** /v1/customers/{id} | 
[**customer_service_search_customers**](CustomerServiceApi.md#customer_service_search_customers) | **GET** /v1/customers/search | 
[**customer_service_update_customer**](CustomerServiceApi.md#customer_service_update_customer) | **POST** /v1/customers/{id} | 


# **customer_service_create_customer**
> V1CustomerResponse customer_service_create_customer(body)



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
api_instance = justap_server_sdk_python.CustomerServiceApi(justap_server_sdk_python.ApiClient(configuration))
body = justap_server_sdk_python.V1CreateCustomerRequest() # V1CreateCustomerRequest | 

try:
    api_response = api_instance.customer_service_create_customer(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerServiceApi->customer_service_create_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreateCustomerRequest**](V1CreateCustomerRequest.md)|  | 

### Return type

[**V1CustomerResponse**](V1CustomerResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_service_delete_customer**
> V1DeleteCustomerResponse customer_service_delete_customer(id, app_id=app_id)



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
api_instance = justap_server_sdk_python.CustomerServiceApi(justap_server_sdk_python.ApiClient(configuration))
id = 'id_example' # str | 
app_id = 'app_id_example' # str |  (optional)

try:
    api_response = api_instance.customer_service_delete_customer(id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerServiceApi->customer_service_delete_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **app_id** | **str**|  | [optional] 

### Return type

[**V1DeleteCustomerResponse**](V1DeleteCustomerResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_service_list_all_customers**
> V1CustomerListResponse customer_service_list_all_customers(app_id=app_id, limit=limit, starting_after=starting_after, ending_before=ending_before, created_lt=created_lt, created_lte=created_lte, created_gt=created_gt, created_gte=created_gte, disabled=disabled)



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
api_instance = justap_server_sdk_python.CustomerServiceApi(justap_server_sdk_python.ApiClient(configuration))
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
    api_response = api_instance.customer_service_list_all_customers(app_id=app_id, limit=limit, starting_after=starting_after, ending_before=ending_before, created_lt=created_lt, created_lte=created_lte, created_gt=created_gt, created_gte=created_gte, disabled=disabled)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerServiceApi->customer_service_list_all_customers: %s\n" % e)
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

[**V1CustomerListResponse**](V1CustomerListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_service_retrieve_customer**
> V1CustomerResponse customer_service_retrieve_customer(id, app_id=app_id)



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
api_instance = justap_server_sdk_python.CustomerServiceApi(justap_server_sdk_python.ApiClient(configuration))
id = 'id_example' # str | 
app_id = 'app_id_example' # str |  (optional)

try:
    api_response = api_instance.customer_service_retrieve_customer(id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerServiceApi->customer_service_retrieve_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **app_id** | **str**|  | [optional] 

### Return type

[**V1CustomerResponse**](V1CustomerResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_service_search_customers**
> V1CustomerListResponse customer_service_search_customers(app_id=app_id, limit=limit, created_lt=created_lt, created_lte=created_lte, created_gt=created_gt, created_gte=created_gte, email=email, name=name, phone=phone)



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
api_instance = justap_server_sdk_python.CustomerServiceApi(justap_server_sdk_python.ApiClient(configuration))
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
    api_response = api_instance.customer_service_search_customers(app_id=app_id, limit=limit, created_lt=created_lt, created_lte=created_lte, created_gt=created_gt, created_gte=created_gte, email=email, name=name, phone=phone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerServiceApi->customer_service_search_customers: %s\n" % e)
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

[**V1CustomerListResponse**](V1CustomerListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_service_update_customer**
> V1CustomerResponse customer_service_update_customer(id, app_id=app_id, address=address, currency=currency, description=description, email=email, name=name, phone=phone, avatar=avatar, disabled=disabled, gender=gender, parent_customer_id=parent_customer_id, out_customer_id=out_customer_id)



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
api_instance = justap_server_sdk_python.CustomerServiceApi(justap_server_sdk_python.ApiClient(configuration))
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
parent_customer_id = 'parent_customer_id_example' # str |  (optional)
out_customer_id = 'out_customer_id_example' # str |  (optional)

try:
    api_response = api_instance.customer_service_update_customer(id, app_id=app_id, address=address, currency=currency, description=description, email=email, name=name, phone=phone, avatar=avatar, disabled=disabled, gender=gender, parent_customer_id=parent_customer_id, out_customer_id=out_customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerServiceApi->customer_service_update_customer: %s\n" % e)
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
 **parent_customer_id** | **str**|  | [optional] 
 **out_customer_id** | **str**|  | [optional] 

### Return type

[**V1CustomerResponse**](V1CustomerResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

