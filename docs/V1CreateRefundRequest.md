# V1CreateRefundRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | [OPTIONAL] 退款金额大于 0, 单位为对应币种的最小货币单位，例如：人民币为分（如退款金额为 1 元，此处请填 100）。必须小于等于可退款金额，默认为全额退款。 | 
**app_id** | **str** | [REQUIRED] 应用 id | 
**charge_id** | **str** | [REQUIRED] 支付 Charge Id | 
**description** | **str** | [REQUIRED] 退款原因，最多 255 个 Unicode 字符。 | 
**extra** | [**ProtobufAny**](ProtobufAny.md) | [OPTIONAL] 退款 extra 参数。 | [optional] 
**merchant_refund_id** | **str** | [REQUIRED] 商户系统的退款单号，必须保证唯一。由于 charge 支持多次退款，对于失败重试动作确保使用相同的订单号，以避免重复退款造成损失。 | 
**metadata** | **dict(str, str)** | [OPTIONAL] 参考元数据。 | [optional] 
**notification_area** | **str** | [OPTIONAL] 接受通知服务器所在区域，为确保消息能够送达，请选择服务器所在国家的国家码。如不填默认为 CN | [default to 'CN']
**notify_url** | **str** | [OPTIONAL] 退款成功后的异步通知地址。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


