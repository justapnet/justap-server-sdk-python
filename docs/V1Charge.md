# V1Charge

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | 订单金额 | [default to 0.0]
**amount_fee** | **float** | 下单金额 | 
**amount_refund** | **float** | 订单退款总金额 | 
**amount_royalty** | **float** | 分账金额 | 
**amount_settle** | **float** | 结算金额，不一定有，视支付通道情况返回 | 
**app_id** | **str** | 应用ID | 
**body** | **str** | 订单描述信息 | 
**channel** | [**Tradev1Channel**](Tradev1Channel.md) | 支付渠道 | 
**charge_id** | **str** | Charge 对象 id | 
**client_ip** | **str** | 顾客IP | 
**closed** | **bool** | 是否关闭 | [default to False]
**closed_at** | **datetime** | 关闭时间 | [optional] 
**closed_ts** | **str** | 关闭时间戳 | [optional] 
**created_at** | **datetime** | Charge 对象创建时间 | [optional] 
**credential** | [**ProtobufAny**](ProtobufAny.md) | 支付凭证 | [optional] 
**currency** | **str** | 货币单位，当前仅支持 CNY | 
**description** | **str** | 描述信息 | 
**expired_ts** | **str** | 订单过期时间戳 | [optional] 
**extra** | [**V1ChargeExtra**](V1ChargeExtra.md) | 支付渠道元数据 | [optional] 
**failure_code** | **str** | 收单机构错误码 | 
**failure_msg** | **str** | 收单机构错误描述信息 | 
**live_mode** | **bool** | 表明是否是沙箱环境 | [default to False]
**merchant_trade_id** | **str** | 商户系统订单号，APP下需唯一 | 
**metadata** | **dict(str, str)** | 订单元数据，原样返回 | [optional] 
**object** | **str** | 对象类型 | [default to 'Charge']
**paid** | **bool** | 表明是否已支付 | [default to False]
**paid_at** | **datetime** | 支付时间 | [optional] 
**paid_ts** | **str** | 支付时间戳 | [optional] 
**refunded** | **bool** | 表明是否包含退款，含退款失败的 | [default to False]
**refunds** | [**list[V1Refund]**](V1Refund.md) | Refund 对象列表 | [optional] 
**reversed** | **bool** | 表明是否已经撤销 | [default to False]
**reversed_at** | **datetime** | 冲正时间 | [optional] 
**subject** | **str** | 订单描述主题 | 
**time_expire** | **datetime** | 订单过期时间 | [optional] 
**transaction_no** | **str** | Charge 的支付单号 | 
**ttl** | **int** | 订单生存时间，单位秒 | [default to 0]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


