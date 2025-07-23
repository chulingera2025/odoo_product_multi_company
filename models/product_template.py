# Copyright 2015-2016 Pedro M. Baeza <pedro.baeza@tecnativa.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models


class ProductTemplate(models.Model):
    """Product template with multi-company support."""
    
    _inherit = ["multi.company.abstract", "product.template"]
    _name = "product.template"