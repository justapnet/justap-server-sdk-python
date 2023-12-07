# V1ExtraAlipayPage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_params** | **float** | 业务扩展参数 | 
**disable_pay_channels** | **str** | 禁用渠道 | 
**enable_pay_channels** | **str** | 可用渠道 | 
**extend_params** | [**V1ExtraAlipayExtendParams**](V1ExtraAlipayExtendParams.md) | 业务扩展参数 | [optional] 
**goods_detail** | [**list[V1ExtraAlipayGoodsDetail]**](V1ExtraAlipayGoodsDetail.md) | 商品明细列表 | [optional] 
**goods_type** | **str** | 商品类型 | 
**integration_type** | **float** | 支付宝用户ID | 
**invoice_info** | [**V1ExtraAlipayInvoiceInfo**](V1ExtraAlipayInvoiceInfo.md) | 发票信息 | [optional] 
**merchant_trade_id** | **str** | [ONLY IN RESPONSE] 商户订单号 | 
**pay_url** | **str** | [ONLY IN RESPONSE] 支付链接 | 
**promo_params** | **str** | 优惠参数 | 
**qr_pay_mode** | **str** | 扫码支付模式 | 
**qrcode_width** | **float** | 二维码宽度 | 
**request_from_url** | **float** | 请求来源地址 | 
**seller_id** | **str** | [ONLY IN RESPONSE] 收款支付宝用户ID | 
**store_id** | **str** | 商户门店编号 | 
**sub_merchant** | [**V1ExtraAlipaySubMerchant**](V1ExtraAlipaySubMerchant.md) | 二级商户信息 | [optional] 
**time_expire** | **int** | 订单失效时间 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


