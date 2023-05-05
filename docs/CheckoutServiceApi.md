# justap_server_sdk_python.CheckoutServiceApi

All URIs are relative to *http://127.0.0.1:21011*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkout_service_create_union_qr_checkout**](CheckoutServiceApi.md#checkout_service_create_union_qr_checkout) | **POST** /v1/checkout/union_qr | 通过聚合收款码创建订单


# **checkout_service_create_union_qr_checkout**
> V1UnionQrRequest checkout_service_create_union_qr_checkout(body)

通过聚合收款码创建订单

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
api_instance = justap_server_sdk_python.CheckoutServiceApi(justap_server_sdk_python.ApiClient(configuration))
body = justap_server_sdk_python.V1UnionQrRequest() # V1UnionQrRequest | 

try:
    # 通过聚合收款码创建订单
    api_response = api_instance.checkout_service_create_union_qr_checkout(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckoutServiceApi->checkout_service_create_union_qr_checkout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1UnionQrRequest**](V1UnionQrRequest.md)|  | 

### Return type

[**V1UnionQrRequest**](V1UnionQrRequest.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

