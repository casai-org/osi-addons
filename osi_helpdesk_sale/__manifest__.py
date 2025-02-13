# Copyright (C) 2022 - TODAY, Open Source Integrators
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "OSI Helpdesk Sale",
    "version": "15.0.1.0.0",
    "category": "Helpdesk",
    "license": "LGPL-3",
    "summary": """Adds the ability to create sales orders from tickets and
    tickets from sales orders without the need of Project/Timesheet modules.""",
    "author": "Open Source Integrators",
    "maintainers": ["opensourceintegrators"],
    "website": "https://github.com/OCA/partner-contact",
    "depends": [
        "helpdesk_sale",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/helpdesk_team_view.xml",
        "views/helpdesk_ticket_view.xml",
        "views/sale_order_view.xml",
    ],
    "installable": True,
}
