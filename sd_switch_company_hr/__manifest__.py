# -*- encoding: utf-8 -*-
##############################################################################
#
#    Web Easy Switch Company module for OpenERP
#    Copyright (C) 2014 GRAP (http://www.grap.coop)
#    @author Sylvain LE GAL (https://twitter.com/legalsylvain)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Multicompany - Switch Company modified',
    'version': '8.0.1.0.0',
    'category': 'web',
    'description': """
Add menu to allow user to switch to another company more easily
===============================================================
Modified the original module web_easy_switch_company (development by Sylvain LE GAL) for actualiced the analytic journal in HR users

Functionality:
--------------
    * Add a new menu in the top bar to switch to another company more easily;
    * Remove the old behaviour to switch company;
    * Change Analytic journal in RRHH for the actualy company

Documentations:
---------------
    * Video : http://www.youtube.com/watch?v=Cpm6dg-IEQQ

Technical information:
----------------------
    * Create a field function 'logo_topbar' in res_company to have a good"""
    """resized logo;

Limits:
-------
    * It would be interesting to show the structure of the companies;

Copyright, Author and Licence:
------------------------------
    * Copyright: 2014, Groupement Régional Alimentaire de Proximité;
    * Author: Sylvain LE GAL (https://twitter.com/legalsylvain);
    * Licence: AGPL-3 (http://www.gnu.org/licenses/)
    * Modified and rename by Sistemas de Datos S.L.""",
    'author': "GRAP,Odoo Community Association (OCA), modified SDatos",
    'website': 'http://www.grap.coop, http://www.sdatos.com',
    'license': 'AGPL-3',
    'depends': [
        'web',
        'account',
        'hr_timesheet'
    ],
    'data': [
        'view/res_users_view.xml',
    ],
    'qweb': [
        'static/src/xml/switch_company.xml',
    ],
    'installable': False,
    'auto_install': False,
}
