{
    'name': 'Product Multi-Company',
    'version': '18.0.1.0.0',
    'category': 'Product',
    'summary': '允许产品属于多个公司',
    'description': """
        此模块将产品的公司字段从单选改为多选，允许产品属于多个公司。
        
        基于OCA (Odoo Community Association) 的base_multi_company和product_multi_company模块开发，
        针对Odoo18进行了优化。
        
        OCA是Odoo社区组织，致力于开发高质量的开源Odoo模块。
        链接: https://github.com/OCA/multi-company
        别问为什么不pr，
        - 支持产品模板跨多个公司使用
        - 提供多公司选择界面
        - 自动迁移现有单公司数据
        - 完全兼容Odoo多公司架构
    """,
    'author': 'chulingera2025, OCA',
    'website': 'https://github.com/chulingera2025',
    'depends': ['product', 'base'],
    'data': [
        'views/product_template_view.xml',
    ],
    'post_init_hook': 'post_init_hook',
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'AGPL-3',
    'maintainers': ['chulingera2025'],
    'external_dependencies': {},
}