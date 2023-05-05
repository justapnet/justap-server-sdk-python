# V1ExtraAlipayQr

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buyer_id** | **str** | 买家的支付宝唯一用户号（2088开头的16位纯数字） | [optional] 
**discountable_amount** | **str** | 可打折金额. 参与优惠计算的金额，单位为元，精确到小数点后两位，取值范围[0.01,100000000] 如果该值未传入，但传入了【订单总金额】，【不可打折金额】则该值默认为【订单总金额】-【不可打折金额】 | [optional] 
**goods_detail** | [**list[V1ExtraAlipayGoodsDetail]**](V1ExtraAlipayGoodsDetail.md) | 商品明细列表 | [optional] 
**operator_id** | **str** | 商户操作员编号 | [optional] 
**product_code** | **str** | 销售产品码，商家和支付宝签约的产品码，为固定值QUICK_MSECURITY_PAY | [optional] 
**qr_code** | **str** | [ONLY IN RESPONSE] 二维码 | [optional] 
**qr_code_timeout_express** | **str** | 支付场景。 条码支付，取值：bar_code； 声波支付，取值：wave_code | [optional] 
**qr_link** | **str** | [ONLY IN RESPONSE] 二维码图片的URL地址 | [optional] 
**store_id** | **str** | 商户门店编号 | [optional] 
**terminal_id** | **str** | 商户机具终端编号 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


