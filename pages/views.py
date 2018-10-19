#  * This file is part of me2u project.
#  * (c) Ochui Princewill Patrick <ochui.princewill@gmail.com>
#  * For the full copyright and license information, please view the "LICENSE.md"
#  * file that was distributed with this source code.
from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    
    template_name = 'landing/home.html'
