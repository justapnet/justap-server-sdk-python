# V1SettlementAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | 分账接收方所在的应用 ID | [default to '0']
**business_user_id** | **str** | 分账接收方的用户 ID | [default to '0']
**channel** | [**V1SettlementAccountChannel**](V1SettlementAccountChannel.md) | 分账接收方的账户类型 | [optional] 
**created** | **int** | 分账接收方的创建时间 | [default to 0]
**customer_id** | **str** | 分账接收方的用户 ID | [default to '0']
**id** | **str** | 分账接收方的唯一标识 | [default to '0']
**object** | **str** | 对象类型 | [default to 'Recipient']
**recipient** | [**V1SettlementAccountRecipient**](V1SettlementAccountRecipient.md) | 分账接收方的账户信息 | [optional] 
**updated** | **int** | 分账接收方的更新时间 | [default to 0]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


