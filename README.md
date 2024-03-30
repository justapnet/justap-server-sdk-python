# justap-server-sdk-python

- API version: 1.0
- Package version: 
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Document

[https://www.justap.cn/docs](https://www.justap.cn/docs)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import justap_server_sdk_python 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import justap_server_sdk_python
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *http://127.0.0.1:21011*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**business_user_service_create_user**](docs/DefaultApi.md#business_user_service_create_user) | **POST** /v1/business_users | 创建 Business User 对象
*DefaultApi* | [**business_user_service_delete_user**](docs/DefaultApi.md#business_user_service_delete_user) | **DELETE** /v1/business_users/{id} | 删除 Business User 对象
*DefaultApi* | [**business_user_service_list_all_users**](docs/DefaultApi.md#business_user_service_list_all_users) | **GET** /v1/business_users | 查询 Business User 对象列表
*DefaultApi* | [**business_user_service_retrieve_user**](docs/DefaultApi.md#business_user_service_retrieve_user) | **GET** /v1/business_users/{id} | 查询 Business User 对象
*DefaultApi* | [**business_user_service_search_users**](docs/DefaultApi.md#business_user_service_search_users) | **GET** /v1/business_users/search | 查询 Business User 对象列表
*DefaultApi* | [**business_user_service_update_user**](docs/DefaultApi.md#business_user_service_update_user) | **PUT** /v1/business_users/{user.id} | 更新 Business User 对象
*DefaultApi* | [**business_user_service_update_user2**](docs/DefaultApi.md#business_user_service_update_user2) | **PATCH** /v1/business_users/{user.id} | 更新 Business User 对象
*DefaultApi* | [**charge_service_charges**](docs/DefaultApi.md#charge_service_charges) | **POST** /transaction/v1/charges | 创建 Charge 对象
*DefaultApi* | [**charge_service_charges2**](docs/DefaultApi.md#charge_service_charges2) | **POST** /v1/charges | 创建 Charge 对象
*DefaultApi* | [**charge_service_query_charge**](docs/DefaultApi.md#charge_service_query_charge) | **GET** /transaction/v1/charges/{charge_id} | 查询 Charge 对象
*DefaultApi* | [**charge_service_query_charge2**](docs/DefaultApi.md#charge_service_query_charge2) | **GET** /v1/charges/{charge_id} | 查询 Charge 对象
*DefaultApi* | [**charge_service_query_charge3**](docs/DefaultApi.md#charge_service_query_charge3) | **GET** /v1/charges/merchant_trade_id/{merchant_trade_id} | 查询 Charge 对象
*DefaultApi* | [**charge_service_query_charge_list**](docs/DefaultApi.md#charge_service_query_charge_list) | **GET** /transaction/v1/charges | 查询 Charge 对象列表
*DefaultApi* | [**charge_service_query_charge_list2**](docs/DefaultApi.md#charge_service_query_charge_list2) | **GET** /v1/charges | 查询 Charge 对象列表
*DefaultApi* | [**charge_service_reverse_charge**](docs/DefaultApi.md#charge_service_reverse_charge) | **POST** /transaction/v1/charges/{charge_id}/reverse | 撤销 Charge 对象
*DefaultApi* | [**charge_service_reverse_charge2**](docs/DefaultApi.md#charge_service_reverse_charge2) | **POST** /v1/charges/{charge_id}/reverse | 撤销 Charge 对象
*DefaultApi* | [**refund_service_query_refund**](docs/DefaultApi.md#refund_service_query_refund) | **GET** /transaction/v1/charges/{charge_id}/refunds/{refund_id} | 查询 Refund 对象
*DefaultApi* | [**refund_service_query_refund2**](docs/DefaultApi.md#refund_service_query_refund2) | **GET** /v1/refunds/{refund_id} | 查询 Refund 对象
*DefaultApi* | [**refund_service_query_refund_list**](docs/DefaultApi.md#refund_service_query_refund_list) | **GET** /transaction/v1/charges/{charge_id}/refunds | 查询 Refund 对象列表
*DefaultApi* | [**refund_service_query_refund_list2**](docs/DefaultApi.md#refund_service_query_refund_list2) | **GET** /v1/refunds | 查询 Refund 对象列表
*DefaultApi* | [**refund_service_refunds**](docs/DefaultApi.md#refund_service_refunds) | **POST** /transaction/v1/refunds | 创建 Refund 对象
*DefaultApi* | [**refund_service_refunds2**](docs/DefaultApi.md#refund_service_refunds2) | **POST** /v1/refunds | 创建 Refund 对象
*DefaultApi* | [**royalty_service_create_royalty**](docs/DefaultApi.md#royalty_service_create_royalty) | **POST** /v1/royalties | 创建 Royalty 对象
*DefaultApi* | [**royalty_service_list_all_royalties**](docs/DefaultApi.md#royalty_service_list_all_royalties) | **GET** /v1/royalties | 查询 Royalty 对象列表
*DefaultApi* | [**royalty_service_retrieve_royalty**](docs/DefaultApi.md#royalty_service_retrieve_royalty) | **GET** /v1/royalties/{id} | 查询 Royalty 对象
*DefaultApi* | [**settlement_service_create_settlement_account**](docs/DefaultApi.md#settlement_service_create_settlement_account) | **POST** /v1/settlement_accounts | 创建结算账户
*DefaultApi* | [**settlement_service_delete_settlement_account**](docs/DefaultApi.md#settlement_service_delete_settlement_account) | **DELETE** /v1/settlement_accounts/{id} | 删除结算账户
*DefaultApi* | [**settlement_service_list_all_settlement_accounts**](docs/DefaultApi.md#settlement_service_list_all_settlement_accounts) | **GET** /v1/settlement_accounts | 查询结算账户列表
*DefaultApi* | [**settlement_service_retrieve_settlement_account**](docs/DefaultApi.md#settlement_service_retrieve_settlement_account) | **GET** /v1/settlement_accounts/{id} | 查询结算账户
*DefaultApi* | [**settlement_service_search_settlement_accounts**](docs/DefaultApi.md#settlement_service_search_settlement_accounts) | **GET** /v1/settlement_accounts/search | 查询结算账户列表
*DefaultApi* | [**settlement_service_update_settlement_account**](docs/DefaultApi.md#settlement_service_update_settlement_account) | **PUT** /v1/settlement_accounts/{settlementAccount.id} | 更新结算账户
*DefaultApi* | [**settlement_service_update_settlement_account2**](docs/DefaultApi.md#settlement_service_update_settlement_account2) | **PATCH** /v1/settlement_accounts/{settlementAccount.id} | 更新结算账户
*CheckoutServiceApi* | [**checkout_service_create_union_qr_checkout**](docs/CheckoutServiceApi.md#checkout_service_create_union_qr_checkout) | **POST** /v1/checkout/union_qr | 通过聚合收款码创建订单
*CustomerServiceApi* | [**customer_service_create_customer**](docs/CustomerServiceApi.md#customer_service_create_customer) | **POST** /v1/customers | 
*CustomerServiceApi* | [**customer_service_delete_customer**](docs/CustomerServiceApi.md#customer_service_delete_customer) | **DELETE** /v1/customers/{id} | 
*CustomerServiceApi* | [**customer_service_list_all_customers**](docs/CustomerServiceApi.md#customer_service_list_all_customers) | **GET** /v1/customers | 
*CustomerServiceApi* | [**customer_service_retrieve_customer**](docs/CustomerServiceApi.md#customer_service_retrieve_customer) | **GET** /v1/customers/{id} | 
*CustomerServiceApi* | [**customer_service_search_customers**](docs/CustomerServiceApi.md#customer_service_search_customers) | **GET** /v1/customers/search | 
*CustomerServiceApi* | [**customer_service_update_customer**](docs/CustomerServiceApi.md#customer_service_update_customer) | **POST** /v1/customers/{id} | 


## Documentation For Models

 - [ChargeRoutingRequestChargeMethod](docs/ChargeRoutingRequestChargeMethod.md)
 - [CreateRoyaltyRequestRoyaltyMode](docs/CreateRoyaltyRequestRoyaltyMode.md)
 - [CreateRoyaltyRequestRoyaltyReceiver](docs/CreateRoyaltyRequestRoyaltyReceiver.md)
 - [ExtraAlipayInvoiceInfoKeyInfo](docs/ExtraAlipayInvoiceInfoKeyInfo.md)
 - [ExtraAlipayJSAPIPayer](docs/ExtraAlipayJSAPIPayer.md)
 - [ExtraAlipaySettleInfoSettleDetailInfos](docs/ExtraAlipaySettleInfoSettleDetailInfos.md)
 - [ExtraWechatpayDetailGoodsDetail](docs/ExtraWechatpayDetailGoodsDetail.md)
 - [ExtraWechatpaySceneInfoH5Info](docs/ExtraWechatpaySceneInfoH5Info.md)
 - [ExtraWechatpaySceneInfoStoreInfo](docs/ExtraWechatpaySceneInfoStoreInfo.md)
 - [GooglerpcStatus](docs/GooglerpcStatus.md)
 - [OpenApiRoyaltyDetailInfoPojoTradeFundBillItem](docs/OpenApiRoyaltyDetailInfoPojoTradeFundBillItem.md)
 - [ProtobufAny](docs/ProtobufAny.md)
 - [RefundExtraAlipayOpenApiRoyaltyDetailInfoPojo](docs/RefundExtraAlipayOpenApiRoyaltyDetailInfoPojo.md)
 - [RefundExtraWechatPayAccount](docs/RefundExtraWechatPayAccount.md)
 - [RefundExtraWechatPayGoodsDetailItem](docs/RefundExtraWechatPayGoodsDetailItem.md)
 - [RefundRoutingRequestRefundMethod](docs/RefundRoutingRequestRefundMethod.md)
 - [RoyaltyReceiverRoyaltyFeeMode](docs/RoyaltyReceiverRoyaltyFeeMode.md)
 - [RoyaltySettlementRoyaltySettlementStatus](docs/RoyaltySettlementRoyaltySettlementStatus.md)
 - [RoyaltySettlementTransactionRoyaltyTransactionStatus](docs/RoyaltySettlementTransactionRoyaltyTransactionStatus.md)
 - [SettlementAccountRecipientAccountType](docs/SettlementAccountRecipientAccountType.md)
 - [SettlementAccountRecipientAlipayChannelRecipient](docs/SettlementAccountRecipientAlipayChannelRecipient.md)
 - [SettlementAccountRecipientBalanceChannelRecipient](docs/SettlementAccountRecipientBalanceChannelRecipient.md)
 - [SettlementAccountRecipientBankChannelRecipient](docs/SettlementAccountRecipientBankChannelRecipient.md)
 - [SettlementAccountRecipientRecipientType](docs/SettlementAccountRecipientRecipientType.md)
 - [SettlementAccountRecipientWechatpayChannelRecipient](docs/SettlementAccountRecipientWechatpayChannelRecipient.md)
 - [SettlementAccountRecipientYsepayMerchantRecipient](docs/SettlementAccountRecipientYsepayMerchantRecipient.md)
 - [Tradev1Channel](docs/Tradev1Channel.md)
 - [Tradev1RoyaltyMethod](docs/Tradev1RoyaltyMethod.md)
 - [V1AcquirerCloseTransactionResponse](docs/V1AcquirerCloseTransactionResponse.md)
 - [V1AcquirerCreateRefundResponse](docs/V1AcquirerCreateRefundResponse.md)
 - [V1AcquirerCreateRoyaltyResponse](docs/V1AcquirerCreateRoyaltyResponse.md)
 - [V1AcquirerCreateTransactionResponse](docs/V1AcquirerCreateTransactionResponse.md)
 - [V1AcquirerPaymentNotifyResponse](docs/V1AcquirerPaymentNotifyResponse.md)
 - [V1AcquirerQueryRefundResponse](docs/V1AcquirerQueryRefundResponse.md)
 - [V1AcquirerQueryRoyaltyResponse](docs/V1AcquirerQueryRoyaltyResponse.md)
 - [V1AcquirerQueryTransactionResponse](docs/V1AcquirerQueryTransactionResponse.md)
 - [V1AcquirerRefundNotifyResponse](docs/V1AcquirerRefundNotifyResponse.md)
 - [V1AcquirerRoyaltyNotifyResponse](docs/V1AcquirerRoyaltyNotifyResponse.md)
 - [V1AlipayCallbackResponse](docs/V1AlipayCallbackResponse.md)
 - [V1AlipayNotifyResponse](docs/V1AlipayNotifyResponse.md)
 - [V1BusinessUser](docs/V1BusinessUser.md)
 - [V1CallbackRoutingResponse](docs/V1CallbackRoutingResponse.md)
 - [V1Charge](docs/V1Charge.md)
 - [V1ChargeExtra](docs/V1ChargeExtra.md)
 - [V1ChargeListResponse](docs/V1ChargeListResponse.md)
 - [V1ChargeResponse](docs/V1ChargeResponse.md)
 - [V1ChargeRoutingResponse](docs/V1ChargeRoutingResponse.md)
 - [V1CreateChargeRequest](docs/V1CreateChargeRequest.md)
 - [V1CreateChargeRequestExtra](docs/V1CreateChargeRequestExtra.md)
 - [V1CreateCustomerRequest](docs/V1CreateCustomerRequest.md)
 - [V1CreateRefundRequest](docs/V1CreateRefundRequest.md)
 - [V1CreateRoyaltyRequest](docs/V1CreateRoyaltyRequest.md)
 - [V1CreateSettlementAccountRequest](docs/V1CreateSettlementAccountRequest.md)
 - [V1CreateUserRequest](docs/V1CreateUserRequest.md)
 - [V1Customer](docs/V1Customer.md)
 - [V1CustomerListResponse](docs/V1CustomerListResponse.md)
 - [V1CustomerResponse](docs/V1CustomerResponse.md)
 - [V1DeleteCustomerResponse](docs/V1DeleteCustomerResponse.md)
 - [V1DeleteProductResponse](docs/V1DeleteProductResponse.md)
 - [V1DeleteSettlementAccountResponse](docs/V1DeleteSettlementAccountResponse.md)
 - [V1DeleteUserResponse](docs/V1DeleteUserResponse.md)
 - [V1ExtraAlipayApp](docs/V1ExtraAlipayApp.md)
 - [V1ExtraAlipayBusinessParams](docs/V1ExtraAlipayBusinessParams.md)
 - [V1ExtraAlipayExtUserInfo](docs/V1ExtraAlipayExtUserInfo.md)
 - [V1ExtraAlipayExtendParams](docs/V1ExtraAlipayExtendParams.md)
 - [V1ExtraAlipayFace](docs/V1ExtraAlipayFace.md)
 - [V1ExtraAlipayFundBillList](docs/V1ExtraAlipayFundBillList.md)
 - [V1ExtraAlipayGoodsDetail](docs/V1ExtraAlipayGoodsDetail.md)
 - [V1ExtraAlipayInvoiceInfo](docs/V1ExtraAlipayInvoiceInfo.md)
 - [V1ExtraAlipayJSAPI](docs/V1ExtraAlipayJSAPI.md)
 - [V1ExtraAlipayLite](docs/V1ExtraAlipayLite.md)
 - [V1ExtraAlipayLogisticsDetail](docs/V1ExtraAlipayLogisticsDetail.md)
 - [V1ExtraAlipayPage](docs/V1ExtraAlipayPage.md)
 - [V1ExtraAlipayPayParams](docs/V1ExtraAlipayPayParams.md)
 - [V1ExtraAlipayQr](docs/V1ExtraAlipayQr.md)
 - [V1ExtraAlipayReceiverAddressInfo](docs/V1ExtraAlipayReceiverAddressInfo.md)
 - [V1ExtraAlipayScan](docs/V1ExtraAlipayScan.md)
 - [V1ExtraAlipaySettleInfo](docs/V1ExtraAlipaySettleInfo.md)
 - [V1ExtraAlipaySubMerchant](docs/V1ExtraAlipaySubMerchant.md)
 - [V1ExtraAlipayVoucherDetailList](docs/V1ExtraAlipayVoucherDetailList.md)
 - [V1ExtraAlipayWap](docs/V1ExtraAlipayWap.md)
 - [V1ExtraWechatpayApp](docs/V1ExtraWechatpayApp.md)
 - [V1ExtraWechatpayAppConfig](docs/V1ExtraWechatpayAppConfig.md)
 - [V1ExtraWechatpayAppletConfig](docs/V1ExtraWechatpayAppletConfig.md)
 - [V1ExtraWechatpayDetail](docs/V1ExtraWechatpayDetail.md)
 - [V1ExtraWechatpayH5](docs/V1ExtraWechatpayH5.md)
 - [V1ExtraWechatpayJsapi](docs/V1ExtraWechatpayJsapi.md)
 - [V1ExtraWechatpayJsapiConfig](docs/V1ExtraWechatpayJsapiConfig.md)
 - [V1ExtraWechatpayLite](docs/V1ExtraWechatpayLite.md)
 - [V1ExtraWechatpayNative](docs/V1ExtraWechatpayNative.md)
 - [V1ExtraWechatpayPayer](docs/V1ExtraWechatpayPayer.md)
 - [V1ExtraWechatpayScan](docs/V1ExtraWechatpayScan.md)
 - [V1ExtraWechatpaySceneInfo](docs/V1ExtraWechatpaySceneInfo.md)
 - [V1ExtraWechatpaySettleInfo](docs/V1ExtraWechatpaySettleInfo.md)
 - [V1FinishRoyaltyResponse](docs/V1FinishRoyaltyResponse.md)
 - [V1Gender](docs/V1Gender.md)
 - [V1ListAllCustomersRequestCreated](docs/V1ListAllCustomersRequestCreated.md)
 - [V1ListAllRoyaltiesRequestCreated](docs/V1ListAllRoyaltiesRequestCreated.md)
 - [V1ListAllRoyaltiesResponse](docs/V1ListAllRoyaltiesResponse.md)
 - [V1ListAllSettlementAccountsRequestCreated](docs/V1ListAllSettlementAccountsRequestCreated.md)
 - [V1ListAllUsersRequestCreated](docs/V1ListAllUsersRequestCreated.md)
 - [V1NotifyRoutingResponse](docs/V1NotifyRoutingResponse.md)
 - [V1ProductListResponse](docs/V1ProductListResponse.md)
 - [V1ProductResponse](docs/V1ProductResponse.md)
 - [V1QueryChargeListRequestCreated](docs/V1QueryChargeListRequestCreated.md)
 - [V1Refund](docs/V1Refund.md)
 - [V1RefundExtra](docs/V1RefundExtra.md)
 - [V1RefundExtraAlipay](docs/V1RefundExtraAlipay.md)
 - [V1RefundExtraWechatPay](docs/V1RefundExtraWechatPay.md)
 - [V1RefundListResponse](docs/V1RefundListResponse.md)
 - [V1RefundResponse](docs/V1RefundResponse.md)
 - [V1RefundRoutingResponse](docs/V1RefundRoutingResponse.md)
 - [V1Royalty](docs/V1Royalty.md)
 - [V1RoyaltyResponse](docs/V1RoyaltyResponse.md)
 - [V1RoyaltyRoutingRequestRoyaltyMethod](docs/V1RoyaltyRoutingRequestRoyaltyMethod.md)
 - [V1RoyaltyRoutingResponse](docs/V1RoyaltyRoutingResponse.md)
 - [V1RoyaltySettlement](docs/V1RoyaltySettlement.md)
 - [V1RoyaltySettlementListResponse](docs/V1RoyaltySettlementListResponse.md)
 - [V1RoyaltySettlementResponse](docs/V1RoyaltySettlementResponse.md)
 - [V1RoyaltySettlementSource](docs/V1RoyaltySettlementSource.md)
 - [V1RoyaltySettlementSourceType](docs/V1RoyaltySettlementSourceType.md)
 - [V1RoyaltySettlementTransaction](docs/V1RoyaltySettlementTransaction.md)
 - [V1RoyaltySettlementTransactionListResponse](docs/V1RoyaltySettlementTransactionListResponse.md)
 - [V1RoyaltySettlementTransactionResponse](docs/V1RoyaltySettlementTransactionResponse.md)
 - [V1RoyaltyStatus](docs/V1RoyaltyStatus.md)
 - [V1SearchCustomersRequestCreated](docs/V1SearchCustomersRequestCreated.md)
 - [V1SearchRoyaltiesResponse](docs/V1SearchRoyaltiesResponse.md)
 - [V1SearchUsersRequestCreated](docs/V1SearchUsersRequestCreated.md)
 - [V1ServiceError](docs/V1ServiceError.md)
 - [V1SettlementAccount](docs/V1SettlementAccount.md)
 - [V1SettlementAccountChannel](docs/V1SettlementAccountChannel.md)
 - [V1SettlementAccountListResponse](docs/V1SettlementAccountListResponse.md)
 - [V1SettlementAccountRecipient](docs/V1SettlementAccountRecipient.md)
 - [V1SettlementAccountResponse](docs/V1SettlementAccountResponse.md)
 - [V1TransferRoutingResponse](docs/V1TransferRoutingResponse.md)
 - [V1UnionQrRequest](docs/V1UnionQrRequest.md)
 - [V1UpdateAndPatchRequestBody](docs/V1UpdateAndPatchRequestBody.md)
 - [V1User](docs/V1User.md)
 - [V1UserListResponse](docs/V1UserListResponse.md)
 - [V1UserResponse](docs/V1UserResponse.md)
 - [V1WechatpayCallbackResponse](docs/V1WechatpayCallbackResponse.md)
 - [V1WechatpayNotifyResponse](docs/V1WechatpayNotifyResponse.md)


## Documentation For Authorization


## ApiKeyAuth

- **Type**: API key
- **API key parameter name**: X-JUSTAP-API-KEY
- **Location**: HTTP header


## Author

support@justap.net

