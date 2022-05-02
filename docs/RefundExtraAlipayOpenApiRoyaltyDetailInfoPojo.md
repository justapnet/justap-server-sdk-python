# RefundExtraAlipayOpenApiRoyaltyDetailInfoPojo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | 分账的金额，单位为元 | 
**buyer_logon_id** | **str** | 买家支付宝账号 | 
**buyer_user_id** | **str** | 买家在支付宝的用户id | 
**desc** | **str** | 分账描述 | 
**fund_change** | **str** | 分账变更消息 | 
**refund_detail_item_list** | [**list[OpenApiRoyaltyDetailInfoPojoTradeFundBillItem]**](OpenApiRoyaltyDetailInfoPojoTradeFundBillItem.md) | 退款使用的资金渠道 | [optional] 
**refund_fee** | **float** | 总退款金额 | 
**royalty_scene** | **str** | 可选值：达人佣金、平台服务费、技术服务费、其他 | 
**royalty_type** | **str** | 分账类型 | 
**send_back_fee** | **str** | 买家实际退款金额 | 
**store_name** | **str** | 交易场景 | 
**trans_in** | **str** | 收入方账户 | 
**trans_in_name** | **str** | 分账收款方姓名 | 
**trans_in_type** | **str** | 收入方账户类型 | 
**trans_out** | **str** | 支出方账户 | 
**trans_out_type** | **str** | 支出方账户类型 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


