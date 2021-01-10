from django.shortcuts import render
import markdown2
from . import util
from markdown2 import Markdown



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def display_entry(request, entry):
        markdowner = Markdown()
        entryPage = util.get_entry(entry)
 
        if entryPage is None:
            return render(request, "encyclopedia/entryNil.html",
            {"entry": entry} )

        else:
            markdowner = Markdown()
            return render(request, "encyclopedia/entry.html", 
            { "entry": markdowner.convert(entryPage)
            })

def search(request, entry):
        return render(request, "encyclopedia/search.html", {         
        "entries": util.list_entries()
        })