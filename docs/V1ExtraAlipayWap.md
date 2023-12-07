# V1ExtraAlipayWap

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_token** | **str** | 授权码 | 
**business_params** | **str** | 业务扩展参数 | 
**disable_pay_channels** | **str** | 禁用渠道 | 
**enable_pay_channels** | **str** | 可用渠道 | 
**extend_params** | [**V1ExtraAlipayExtendParams**](V1ExtraAlipayExtendParams.md) | 业务扩展参数 | [optional] 
**fund_bill_list** | **list[str]** | 支付金额信息 | [optional] 
**goods_detail** | [**list[V1ExtraAlipayGoodsDetail]**](V1ExtraAlipayGoodsDetail.md) | 商品明细列表 | [optional] 
**goods_type** | **str** | 商品类型 | 
**merchant_trade_id** | **str** | [ONLY IN RESPONSE] 商户订单号 | 
**pay_url** | **str** | [ONLY IN RESPONSE] 支付链接 | 
**product_code** | **str** | 销售产品码 | 
**promo_params** | **str** | 优惠参数 | 
**quit_url** | **str** | 支付取消跳转的地址 | 
**return_url** | **str** | 支付成功跳转的地址 | 
**seller_id** | **str** | [ONLY IN RESPONSE] 收款支付宝用户ID | 
**store_id** | **str** | 商户门店编号 | 
**voucher_detail_list** | [**V1ExtraAlipayVoucherDetailList**](V1ExtraAlipayVoucherDetailList.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


