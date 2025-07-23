**Language**: [English](README.md) | [中文](README_CN.md)

# Product Multi-Company Module

This module provides multi-company support for product templates in Odoo 18.

## Features

- Allows product templates to be visible in multiple companies
- Replaces the single `company_id` field with a `company_ids` Many2many field
- Provides seamless integration with existing Odoo multi-company functionality
- Includes data migration hooks for upgrading from single-company setups

## Installation

1. Copy the module to your Odoo addons directory
2. Update the module list in Odoo
3. Install the "Product Multi-Company" module

## Usage

After installation:

1. Go to Products > Product Templates
2. Edit any product template
3. In the General Information tab, you'll see a "Companies" field
4. Select which companies should have access to this product

## Technical Details

### Models

- `multi.company.abstract`: Abstract model providing multi-company functionality
- `product.template`: Extended with multi-company support

### Key Features

- Automatic migration of existing `company_id` values to `company_ids`
- Context-aware company computation
- Proper search domain handling for multi-company scenarios

## Compatibility

- Odoo 18.0+
- Requires `product` module

## License

AGPL-3

## About OCA

The Odoo Community Association (OCA) is a nonprofit organization whose mission is to promote the widespread use of Odoo and to support the collaborative development of Odoo features.

OCA, or the [Odoo Community Association](http://odoo-community.org/), is a nonprofit organization whose mission is to support the collaborative development of Odoo features and promote its widespread use.

This module is maintained by the OCA.

OCA maintains and develops Odoo addons and provides a framework for collaborative development. For more information about OCA and its projects, visit:

- [OCA Website](https://odoo-community.org/)
- [OCA GitHub](https://github.com/OCA)
- [OCA Runbot](https://runbot.odoo-community.org/)