from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context, loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from django.core.context_processors import csrf

from django.contrib.auth import authenticate, login   
from django.db.models import Q

from dclog.forms import *
from dclog.models import *

import pprint

def newLog(request): 
    # If the form has been submitted...
    if request.method == 'POST': 
        # A form bound to the POST data 
        #pprint.pprint(globals())
        form = NewLogForm(request.user, request.POST)
        # All validation rules pass
        if form.is_valid(): 
            form.save()
            # Redirect after POST
            return HttpResponseRedirect('/') 
    else:
        # An unbound form
        form = NewLogForm(request.user)
        form.created_by = request.user
        
	# display either the form
    return render_to_response('log_new.html', { 'form': form,}, context_instance=RequestContext(request))
 
def editLog(request, log_id):
    # Which Log will this form show?
    log = get_object_or_404(Log, pk=log_id)
    
    # If the form has been submitted...
    if request.method == 'POST': 
        # A form bound to the POST data
        form = EditLogForm(request.POST, instance=log)
        # All validation rules pass
        if form.is_valid(): 
            form.save()
            # Redirect after POST (to guard from accidentally reposting)
            return HttpResponseRedirect('/')
             
    # The form has not been submitted, it's a GET request 
    else:
        # A form that is bound to Log data
        form = EditLogForm(instance=log) 
    return render_to_response('log_edit.html', {'form': form, 'log_id':log.id}, context_instance=RequestContext(request))   

def newAlarm(request): 
    # If the form has been submitted...
    if request.method == 'POST': 
        # A form bound to the POST data
        form = NewAlarmForm(request.POST)
        # All validation rules pass
        if form.is_valid(): 
            form.save()
            # Redirect after POST
            return HttpResponseRedirect('/') 
    else:
        # An unbound form
        form = NewAlarmForm()
	# display either the form
    return render_to_response('alarm_new.html', { 'form': form,}, context_instance=RequestContext(request)) 

def newArea(request):
    # If the form has been submitted...
    if request.method == 'POST': 
        # A form bound to the POST data
        form = NewAreaForm(request.POST)
        # All validation rules pass
        if form.is_valid(): 
            form.save()
            # Redirect after POST
            return HttpResponseRedirect('/') 
    else:
        # An unbound form
        form = NewAreaForm()
	# display either the form
    return render_to_response('area_new.html', { 'form': form,}, context_instance=RequestContext(request)) 

def newFacilityType(request): 
    # If the form has been submitted...
    if request.method == 'POST': 
        # A form bound to the POST data
        form = NewFacilityTypeForm(request.POST)
        # All validation rules pass
        if form.is_valid(): 
            form.save()
            # Redirect after POST
            return HttpResponseRedirect('/') 
    else:
        # An unbound form
        form = NewFacilityTypeForm()
	# display either the form
    return render_to_response('facility_type_new.html', { 'form': form,}, context_instance=RequestContext(request)) 

def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(title__icontains=query) |
            Q(alarm__name__icontains=query) |
            Q(created_by__username__icontains=query) |
            Q(notes__icontains=query)
        )
        results = Log.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response( "search.html", { "results": results, "query": query }, context_instance=RequestContext(request))