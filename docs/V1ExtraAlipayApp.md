# V1ExtraAlipayApp

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credit_agreement_id** | **str** | [ONLY IN RESPONSE] 信用支付协议号 | 
**credit_biz_order_id** | **str** | [ONLY IN RESPONSE] 信用支付业务订单号 | 
**credit_pay_mode** | **str** | [ONLY IN RESPONSE] 信用支付模式 | 
**disable_pay_channels** | **str** | 禁用渠道 | 
**enable_pay_channels** | **str** | 可用渠道 | 
**ext_user_info** | [**V1ExtraAlipayExtUserInfo**](V1ExtraAlipayExtUserInfo.md) | 外部指定买家 | [optional] 
**extend_params** | [**V1ExtraAlipayExtendParams**](V1ExtraAlipayExtendParams.md) | 业务扩展参数 | [optional] 
**goods_detail** | [**list[V1ExtraAlipayGoodsDetail]**](V1ExtraAlipayGoodsDetail.md) | 商品明细列表 | [optional] 
**goods_type** | **str** | 商品类型 | 
**merchant_trade_id** | **str** | [ONLY IN RESPONSE] 商户订单号 | 
**pay_param** | **str** | [ONLY IN RESPONSE] App 用于拉起支付的请求字符串 | 
**product_code** | **str** | 销售产品码，商家和支付宝签约的产品码 | 
**seller_id** | **str** | [ONLY IN RESPONSE] 支付宝卖家支付宝用户ID | 
**store_id** | **str** | 商户门店编号 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


