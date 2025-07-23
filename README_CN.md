**语言**: [English](README.md) | [中文](README_CN.md)

# 产品多公司模块

此模块为 Odoo 18 中的产品模板提供多公司支持。

## 功能特性

- 允许产品模板在多个公司中可见
- 将单一的 `company_id` 字段替换为 `company_ids` Many2many 字段
- 与现有的 Odoo 多公司功能无缝集成
- 包含数据迁移钩子，用于从单公司设置升级

## 安装

1. 将模块复制到您的 Odoo 插件目录
2. 在 Odoo 中更新模块列表
3. 安装"产品多公司"模块

## 使用方法

安装后：

1. 转到 产品 > 产品模板
2. 编辑任何产品模板
3. 在常规信息选项卡中，您将看到"公司"字段
4. 选择哪些公司应该有权访问此产品

## 技术详情

### 模型

- `multi.company.abstract`: 提供多公司功能的抽象模型
- `product.template`: 扩展了多公司支持

### 主要功能

- 自动将现有的 `company_id` 值迁移到 `company_ids`
- 上下文感知的公司计算
- 多公司场景的适当搜索域处理

## 兼容性

- Odoo 18.0+
- 需要 `product` 模块

## 许可证

AGPL-3

## 关于 OCA

Odoo 社区协会（OCA）是一个非营利组织，其使命是促进 Odoo 的广泛使用并支持 Odoo 功能的协作开发。

OCA，即 [Odoo 社区协会](http://odoo-community.org/)，是一个非营利组织，其使命是支持 Odoo 功能的协作开发并促进其广泛使用。

此模块由 OCA 维护。

OCA 维护和开发 Odoo 插件，并为协作开发提供框架。有关 OCA 及其项目的更多信息，请访问：

- [OCA 官网](https://odoo-community.org/)
- [OCA GitHub](https://github.com/OCA)
- [OCA Runbot](https://runbot.odoo-community.org/)