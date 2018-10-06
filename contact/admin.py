#  * This file is part of me2u project.
#  * (c) Ochui Princewill Patrick <ochui.princewill@gmail.com>
#  * For the full copyright and license information, please view the "LICENSE.md"
#  * file that was distributed with this source code.

from django.contrib import admin
from . models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = ['user_from', 'user_to', 'created_at']
    list_filter = ['created_at']
