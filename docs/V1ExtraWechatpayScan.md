# V1ExtraWechatpayScan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attach** | **str** | 元数据 | [optional] 
**auth_code** | **str** | 授权码 | [optional] 
**bank_type** | **str** | 付款银行 | [optional] 
**cash_fee** | **str** | 现金支付金额 | [optional] 
**cash_fee_type** | **str** | 现金支付币种 | [optional] 
**detail** | [**V1ExtraWechatpayDetail**](V1ExtraWechatpayDetail.md) | 商品详情 | [optional] 
**fee_type** | **str** | 货币种类 | [optional] 
**goods_tag** | **str** | 订单优惠标记 | [optional] 
**is_subscribe** | **bool** | 是否关注公众账号 | [optional] [default to False]
**payer** | [**V1ExtraWechatpayPayer**](V1ExtraWechatpayPayer.md) | 付款人信息 | [optional] 
**scene_info** | [**V1ExtraWechatpaySceneInfo**](V1ExtraWechatpaySceneInfo.md) | 场景信息 | [optional] 
**settle_info** | [**V1ExtraWechatpaySettleInfo**](V1ExtraWechatpaySettleInfo.md) | 结算信息 | [optional] 
**settlement_total_fee** | **float** | 应结订单金额 | [optional] 
**spbill_create_ip** | **str** | 终端IP | [optional] 
**sub_is_subscribe** | **bool** | 子商户是否关注公众账号 | [optional] [default to False]
**sub_openid** | **str** | 子商户openid | [optional] 
**time_end** | **str** | 支付完成时间 | [optional] 
**time_expire** | **str** | 交易结束时间 | [optional] 
**time_start** | **str** | 交易起始时间 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


