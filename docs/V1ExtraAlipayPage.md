# V1ExtraAlipayPage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_params** | **float** | 业务扩展参数 | [optional] 
**disable_pay_channels** | **str** | 禁用渠道 | [optional] 
**enable_pay_channels** | **str** | 可用渠道 | [optional] 
**extend_params** | [**V1ExtraAlipayExtendParams**](V1ExtraAlipayExtendParams.md) | 业务扩展参数 | [optional] 
**goods_detail** | [**list[V1ExtraAlipayGoodsDetail]**](V1ExtraAlipayGoodsDetail.md) | 商品明细列表 | [optional] 
**goods_type** | **str** | 商品类型 | [optional] 
**integration_type** | **float** | 支付宝用户ID | [optional] 
**invoice_info** | [**V1ExtraAlipayInvoiceInfo**](V1ExtraAlipayInvoiceInfo.md) | 发票信息 | [optional] 
**merchant_trade_id** | **str** | [ONLY IN RESPONSE] 商户订单号 | [optional] 
**pay_url** | **str** | [ONLY IN RESPONSE] 支付链接 | [optional] 
**promo_params** | **str** | 优惠参数 | [optional] 
**qr_pay_mode** | **str** | 扫码支付模式 | [optional] 
**qrcode_width** | **float** | 二维码宽度 | [optional] 
**request_from_url** | **float** | 请求来源地址 | [optional] 
**seller_id** | **str** | [ONLY IN RESPONSE] 收款支付宝用户ID | [optional] 
**store_id** | **str** | 商户门店编号 | [optional] 
**sub_merchant** | [**V1ExtraAlipaySubMerchant**](V1ExtraAlipaySubMerchant.md) | 二级商户信息 | [optional] 
**time_expire** | **int** | 订单失效时间 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


