# V1ExtraAlipayLite

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | 商品描述 | [optional] 
**business_params** | [**V1ExtraAlipayBusinessParams**](V1ExtraAlipayBusinessParams.md) | 业务扩展参数 | [optional] 
**buyer_id** | **str** | 买家的支付宝唯一用户号（2088开头的16位纯数字） | [optional] 
**discountable_amount** | **float** | 可打折金额. 参与优惠计算的金额，单位为元，精确到小数点后两位，取值范围[0.01,100000000] 如果该值未传入，但传入了【订单总金额】，【不可打折金额】则该值默认为【订单总金额】-【不可打折金额】 | [optional] 
**extend_params** | [**V1ExtraAlipayExtendParams**](V1ExtraAlipayExtendParams.md) | 业务扩展参数 | [optional] 
**logistics_detail** | [**V1ExtraAlipayLogisticsDetail**](V1ExtraAlipayLogisticsDetail.md) | 物流信息 | [optional] 
**operator_id** | **str** | 商户操作员编号 | [optional] 
**product_code** | **str** | 销售产品码，商家和支付宝签约的产品码，为固定值 FACE_TO_FACE_PAYMENT | [optional] 
**receiver_address_info** | [**V1ExtraAlipayReceiverAddressInfo**](V1ExtraAlipayReceiverAddressInfo.md) | 收货信息 | [optional] 
**seller_id** | **str** | 卖家支付宝用户号 | [optional] 
**settle_info** | [**V1ExtraAlipaySettleInfo**](V1ExtraAlipaySettleInfo.md) | 结算信息 | [optional] 
**store_id** | **str** | 商户门店编号 | [optional] 
**terminal_id** | **str** | 商户机具终端编号 | [optional] 
**time_expire** | **str** | 绝对超时时间，格式为yyyy-MM-dd HH:mm:ss | [optional] 
**timeout_express** | **str** | 订单有效时间，该时间段内订单可以进行支付，结束后订单将关闭，天数为0表示永久有效 | [optional] 
**trade_no** | **str** | [ONLY IN RESPONSE] 支付宝交易号 | [optional] 
**undiscountable_amount** | **float** | 不可打折金额. 不参与优惠计算的金额，单位为元，精确到小数点后两位，取值范围[0.01,100000000] 如果该值未传入，但传入了【订单总金额】,【可打折金额】，则该值默认为【订单总金额】-【可打折金额】 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


