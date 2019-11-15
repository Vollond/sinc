from datetime import datetime
import random
from django.http import HttpResponse


def index(request):
    now = datetime.now()
    rand=random.randint(1,10)
    html = f'''
    <html>
        <body>
            <h1>Hello from Zeit Now! SICN</h1>
            <h1>Hello from Zeit Now! {rand}.</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)
