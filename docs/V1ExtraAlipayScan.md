# V1ExtraAlipayScan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advance_payment_type** | **str** | 预授权类型 | 
**agreement_params** | [**V1ExtraAlipayAgreementParams**](V1ExtraAlipayAgreementParams.md) | 协议参数 | [optional] 
**auth_code** | **str** | 用户的条码 | 
**auth_confirm_mode** | **str** | 授权确认方式 | 
**auth_no** | **str** | 授权号 | 
**buyer_id** | **str** | 买家的支付宝用户id | 
**buyer_logon_id** | **str** | [ONLY IN RESPONSE] 买家支付宝账号 | 
**buyer_pay_amount** | **float** | [ONLY IN RESPONSE] 付款金额 | 
**buyer_user_id** | **str** | [ONLY IN RESPONSE] 买家在支付宝的用户id | 
**discount_amount** | **float** | [ONLY IN RESPONSE] 商家优惠金额 | 
**discount_goods_detail** | **str** | [ONLY IN RESPONSE] 商家优惠商品明细 | 
**discountable_amount** | **float** | 可打折金额 | 
**extend_params** | [**V1ExtraAlipayExtendParams**](V1ExtraAlipayExtendParams.md) | 业务扩展参数 | [optional] 
**fund_bill_list** | [**V1ExtraAlipayFundBillList**](V1ExtraAlipayFundBillList.md) | [ONLY IN RESPONSE] 支付金额信息 | [optional] 
**gmt_payment** | **str** | [ONLY IN RESPONSE] 支付时间 | 
**goods_detail** | [**list[V1ExtraAlipayGoodsDetail]**](V1ExtraAlipayGoodsDetail.md) | 商品明细列表 | [optional] 
**invoice_amount** | **float** | [ONLY IN RESPONSE] 开票金额 | 
**is_async_pay** | [**V1ExtraAlipayPayParams**](V1ExtraAlipayPayParams.md) | 是否异步支付 | [optional] 
**mdiscount_amount** | **float** | [ONLY IN RESPONSE] 平台优惠金额 | 
**operator_id** | **str** | 商户操作员编号 | 
**pay_params** | **str** | [ONLY IN RESPONSE] 支付宝返回的支付参数 | 
**point_amount** | **float** | [ONLY IN RESPONSE] 集分宝金额 | 
**product_code** | **str** | 销售产品码 | 
**query_options** | **str** | 商户授权查询类型 | 
**receipt_amount** | **float** | [ONLY IN RESPONSE] 实收金额 | 
**request_org_pid** | **str** | 请求方机构id | 
**scene** | **str** | 支付场景 | 
**settle_info** | [**V1ExtraAlipaySettleInfo**](V1ExtraAlipaySettleInfo.md) | 结算信息 | [optional] 
**store_id** | **str** | 商户门店编号 | 
**store_name** | **str** | [ONLY IN RESPONSE] 商户门店名称 | 
**sub_merchant** | [**V1ExtraAlipaySubMerchant**](V1ExtraAlipaySubMerchant.md) | 子商户信息 | [optional] 
**terminal_id** | **str** | 商户机具终端编号 | 
**total_amount** | **float** | [ONLY IN RESPONSE] 订单金额 | 
**undiscountable_amount** | **float** | 不可打折金额 | 
**voucher_detail_list** | [**V1ExtraAlipayVoucherDetailList**](V1ExtraAlipayVoucherDetailList.md) | [ONLY IN RESPONSE] 商家优惠明细列表 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


