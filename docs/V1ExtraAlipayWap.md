# V1ExtraAlipayWap

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_token** | **str** | 授权码 | [optional] 
**business_params** | **str** | 业务扩展参数 | [optional] 
**disable_pay_channels** | **str** | 禁用渠道 | [optional] 
**enable_pay_channels** | **str** | 可用渠道 | [optional] 
**extend_params** | [**V1ExtraAlipayExtendParams**](V1ExtraAlipayExtendParams.md) | 业务扩展参数 | [optional] 
**fund_bill_list** | **list[str]** | 支付金额信息 | [optional] 
**goods_detail** | [**list[V1ExtraAlipayGoodsDetail]**](V1ExtraAlipayGoodsDetail.md) | 商品明细列表 | [optional] 
**goods_type** | **str** | 商品类型 | [optional] 
**merchant_trade_id** | **str** | [ONLY IN RESPONSE] 商户订单号 | [optional] 
**pay_url** | **str** | [ONLY IN RESPONSE] 支付链接 | [optional] 
**product_code** | **str** | 销售产品码 | [optional] 
**promo_params** | **str** | 优惠参数 | [optional] 
**quit_url** | **str** | 支付取消跳转的地址 | [optional] 
**return_url** | **str** | 支付成功跳转的地址 | [optional] 
**seller_id** | **str** | [ONLY IN RESPONSE] 收款支付宝用户ID | [optional] 
**store_id** | **str** | 商户门店编号 | [optional] 
**voucher_detail_list** | [**V1ExtraAlipayVoucherDetailList**](V1ExtraAlipayVoucherDetailList.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


