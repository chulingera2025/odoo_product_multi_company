# Copyright 2015-2016 Pedro M. Baeza <pedro.baeza@tecnativa.com>
# Copyright 2017 LasLabs Inc.
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import SUPERUSER_ID, api


def fill_company_ids(cr, model_name):
    """Fill company_ids with company_id values for existing records."""
    env = api.Environment(cr, SUPERUSER_ID, {})
    # Copy company values from company_id to company_ids
    model = env[model_name]
    
    # Get the relation table information for company_ids field
    table_name = model._fields["company_ids"].relation
    column1 = model._fields["company_ids"].column1  # Usually the model's ID column
    column2 = model._fields["company_ids"].column2  # Usually the company ID column
    
    # SQL to migrate existing company_id values to company_ids
    SQL = """
        INSERT INTO {relation_table}
        ({model_column}, {company_column})
        SELECT id, company_id FROM {model_table} WHERE company_id IS NOT NULL
        ON CONFLICT DO NOTHING
    """.format(
        relation_table=table_name,
        model_column=column1,
        company_column=column2,
        model_table=model._table,
    )
    env.cr.execute(SQL)


def post_init_hook(env):
    """Initialize company_ids field with existing company_id values."""
    fill_company_ids(env.cr, "product.template")