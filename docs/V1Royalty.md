# V1Royalty

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge_id** | **str** | Charge ID | 
**created** | **int** | 创建时间 | [default to 0]
**description** | **str** | 分账的原因描述，分账账单中需要体现，不超过 80 个字符 | 
**id** | **str** | 分账 ID | 
**livemode** | **bool** |  | [optional] 
**metadata** | **dict(str, str)** | 元数据 | 
**method** | [**Tradev1RoyaltyMethod**](Tradev1RoyaltyMethod.md) | 分账方式 | 
**object** | **str** | 对象类型 | [default to 'Royalty']
**order_id** | **str** | 订单 ID | 
**payer_app_id** | **str** | 付款方 App ID | 
**payer_settle_account_id** | **str** | 付款方结算账户 ID | 
**payer_user_id** | **str** | 付款方用户 ID | 
**royalty_settlement_id** | **str** | 分账结算单 ID | 
**status** | [**V1RoyaltyStatus**](V1RoyaltyStatus.md) | 分账状态 | 
**time_settled** | **int** | 分账完成时间 | [default to 0]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


