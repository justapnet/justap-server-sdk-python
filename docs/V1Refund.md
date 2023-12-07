# V1Refund

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**V1RefundExtra**](V1RefundExtra.md) | 支付渠道退款元参数 | [optional] 
**amount** | **float** | 退款金额 | 
**charge_id** | **str** | Charge 对象 id | 
**charge_merchant_trade_id** | **str** | 商户系统订单号 | 
**created** | **float** | 退款创建时间 | 
**created_at** | **datetime** | 退款创建时间 | [optional] 
**description** | **str** | 退款说明 | 
**failure_code** | **str** | 支付渠道失败错误码 | 
**failure_msg** | **str** | 支付渠道失败原因描述 | 
**is_success** | **bool** | 退款是否成功 | [default to False]
**metadata** | **dict(str, str)** | 元数据，原样返回 | [optional] 
**refund_id** | **str** | Refund 对象 ID | 
**refund_no** | **str** | 退款单号 | 
**status** | **str** | 退款状态 | 
**succeed_ts** | **float** | 退款成功时间 | 
**success_at** | **datetime** | 退款成功时间 | [optional] 
**transaction_no** | **str** | 交易号 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


