# Copyright 2015-2016 Pedro M. Baeza <pedro.baeza@tecnativa.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo.tests.common import TransactionCase


class TestProductMultiCompany(TransactionCase):
    """Test cases for product multi-company functionality."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        
        # Create test companies
        cls.company_1 = cls.env["res.company"].create({
            "name": "Test Company 1",
        })
        cls.company_2 = cls.env["res.company"].create({
            "name": "Test Company 2", 
        })
        
        # Create test product template
        cls.product_template = cls.env["product.template"].create({
            "name": "Test Product",
            "company_ids": [(6, 0, [cls.company_1.id, cls.company_2.id])],
        })

    def test_company_id_compute(self):
        """Test that company_id is computed correctly based on company_ids."""
        # Test with company_1 in context
        product = self.product_template.with_company(self.company_1)
        self.assertEqual(product.company_id, self.company_1)
        
        # Test with company_2 in context
        product = self.product_template.with_company(self.company_2)
        self.assertEqual(product.company_id, self.company_2)

    def test_company_id_inverse(self):
        """Test that setting company_id updates company_ids."""
        product = self.product_template.copy({
            "name": "Test Product Copy",
            "company_ids": [(6, 0, [])],
        })
        
        # Set company_id and check company_ids is updated
        product.company_id = self.company_1
        self.assertEqual(product.company_ids, self.company_1)

    def test_company_ids_search(self):
        """Test searching by company_id works correctly."""
        # Search for products in company_1
        products = self.env["product.template"].search([
            ("company_id", "=", self.company_1.id)
        ])
        self.assertIn(self.product_template, products)
        
        # Create product only for company_2
        product_2 = self.env["product.template"].create({
            "name": "Company 2 Product",
            "company_ids": [(6, 0, [self.company_2.id])],
        })
        
        # Search should not find company_2 product when searching for company_1
        products = self.env["product.template"].search([
            ("company_id", "=", self.company_1.id)
        ])
        self.assertNotIn(product_2, products)

    def test_multicompany_patch_vals(self):
        """Test that vals are patched correctly when both company_id and company_ids are provided."""
        vals = {
            "name": "Test Product Patch",
            "company_id": self.company_1.id,
            "company_ids": [(6, 0, [self.company_2.id])],
        }
        
        product = self.env["product.template"].create(vals)
        
        # company_ids should contain both companies
        self.assertIn(self.company_1, product.company_ids)
        self.assertIn(self.company_2, product.company_ids)