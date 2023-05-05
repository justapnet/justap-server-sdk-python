# justap_server_sdk_python.RoyaltyServiceApi

All URIs are relative to *http://127.0.0.1:21011*

Method | HTTP request | Description
------------- | ------------- | -------------
[**royalty_service_create_royalty**](RoyaltyServiceApi.md#royalty_service_create_royalty) | **POST** /v1/royalties | 创建 Royalty 对象


# **royalty_service_create_royalty**
> V1RoyaltyResponse royalty_service_create_royalty(body)

创建 Royalty 对象

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
api_instance = justap_server_sdk_python.RoyaltyServiceApi(justap_server_sdk_python.ApiClient(configuration))
body = justap_server_sdk_python.V1CreateRoyaltyRequest() # V1CreateRoyaltyRequest | 

try:
    # 创建 Royalty 对象
    api_response = api_instance.royalty_service_create_royalty(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoyaltyServiceApi->royalty_service_create_royalty: %s\n" % e)
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

