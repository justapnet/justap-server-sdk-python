# V1CreateUserRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | [OPTIONAL] 用户地址 | 
**app_id** | **str** | App ID | 
**available_balance** | **float** | [OPTIONAL] 用户可用余额 | 
**avatar** | **str** | [OPTIONAL] 用户头像 | 
**created** | **int** | [OPTIONAL] 用户创建时间 | [default to 0]
**currency** | **str** | [OPTIONAL] 用户货币 | 
**description** | **str** | [OPTIONAL] 用户描述 | 
**disabled** | **bool** | [OPTIONAL] 是否禁用，默认为 false | [default to False]
**email** | **str** | [OPTIONAL] 用户邮箱 | 
**gender** | [**V1Gender**](V1Gender.md) | [OPTIONAL] 用户性别 | 
**metadata** | **dict(str, str)** | [OPTIONAL] 用户元数据 | 
**name** | **str** | [OPTIONAL] 用户名 | 
**nickname** | **str** | [OPTIONAL] 用户昵称 | 
**out_user_id** | **str** | [REQUIRED] 商户系统用户 ID | 
**parent_user_id** | **str** | [OPTIONAL] 父用户 ID | 
**phone** | **str** | [OPTIONAL] 用户手机号 | 
**withdrawable_balance** | **float** | [OPTIONAL] 用户可提现余额 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


