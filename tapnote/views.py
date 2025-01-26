import markdown
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from .models import Note
import re

def process_markdown_links(html_content):
    # Add target="_blank" and rel="noopener noreferrer" to all links
    pattern = r'<a(.*?)href="(.*?)"(.*?)>'
    replacement = r'<a\1href="\2"\3 target="_blank" rel="noopener noreferrer">'
    return re.sub(pattern, replacement, html_content)

def home(request):
    return render(request, 'tapnote/editor.html')

@csrf_exempt
def publish(request):
    if request.method == 'POST':
        content = request.POST.get('content', '').strip()
        if content:
            note = Note.objects.create(content=content)
            response = redirect('view_note', hashcode=note.hashcode)
            response.set_cookie(f'edit_token_{note.hashcode}', note.edit_token, max_age=31536000)
            return response
    return redirect('home')

def view_note(request, hashcode):
    note = get_object_or_404(Note, hashcode=hashcode)
    md = markdown.Markdown(extensions=['fenced_code', 'tables'])
    html_content = md.convert(note.content)
    html_content = process_markdown_links(html_content)
    
    can_edit = (
        request.COOKIES.get(f'edit_token_{note.hashcode}') == note.edit_token or
        request.GET.get('token') == note.edit_token
    )
    
    return render(request, 'tapnote/view_note.html', {
        'note': note,
        'content': html_content,
        'can_edit': can_edit,
    })

def edit_note(request, hashcode):
    note = get_object_or_404(Note, hashcode=hashcode)
    edit_token = request.COOKIES.get(f'edit_token_{note.hashcode}')
    url_token = request.GET.get('token')
    
    if edit_token != note.edit_token and url_token != note.edit_token:
        raise Http404()
    
    if request.method == 'POST':
        content = request.POST.get('content', '').strip()
        if content:
            note.content = content
            note.save()
            return redirect('view_note', hashcode=note.hashcode)
    
    return render(request, 'tapnote/editor.html', {'note': note})

def handler404(request, exception):
    return render(request, 'tapnote/404.html', status=404) 