#  * This file is part of me2u project.
#  * (c) Ochui Princewill Patrick <ochui.princewill@gmail.com>
#  * For the full copyright and license information, please view the "LICENSE.md"
#  * file that was distributed with this source code.

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ContactConfig(AppConfig):
    name = 'contact'
    verbose_name = _('contact')
