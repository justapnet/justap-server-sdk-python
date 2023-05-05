# V1CreateChargeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | [REQUIRED] 订单金额，单位元， 如 0.01 | [optional] 
**app_id** | **str** | [REQUIRED] 应用 id | [optional] 
**body** | **str** | [REQUIRED] 服务明细 | [optional] 
**callback_url** | **str** | [OPTIONAL] 回调地址，如不传则使用 APP 设置中的回调地址。若都为空，则无法跳回原页面 | [optional] 
**channel** | [**Tradev1Channel**](Tradev1Channel.md) | [REQUIRED] 渠道名称 | [optional] 
**client_ip** | **str** | [REQUIRED] 客户端机器 IP | [optional] 
**currency** | **str** | 货币单位。国内收单机构仅支持 CNY | [optional] [default to 'CNY']
**description** | **str** | [OPTIONAL] 交易描述 | [optional] 
**extra** | [**V1CreateChargeRequestExtra**](V1CreateChargeRequestExtra.md) | [OPTIONAL] 各支付渠道元数据 | [optional] 
**merchant_trade_id** | **str** | [REQUIRED] 客户系统的交易单号（订单号），必须在应用下唯一。长度不超过30个字符 | [optional] 
**metadata** | **dict(str, str)** | [OPTIONAL] 订单元数据，原样返回 | [optional] 
**notification_area** | **str** | [OPTIONAL] 接受通知服务器所在区域，为确保消息能够送达，请选择服务器所在国家的国家码。如不填默认为 CN | [optional] [default to 'CN']
**notify_url** | **str** | [OPTIONAL] 通知地址，如不传则使用 APP 设置中的通知地址。若都为空，则不发送通知 | [optional] 
**subject** | **str** | [REQUIRED] 物品或服务名称（交易标题） | [optional] 
**ttl** | **int** | [OPTIONAL] 订单超时时间，单位秒 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


