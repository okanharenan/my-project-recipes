from django.core.paginator import Paginator
import math

def make_pagination_range( page_range, qty_pages, current_page):
    midle_range = math.ceil(qty_pages / 2)
    start_range = current_page - midle_range
    stop_range= current_page + midle_range
    start_range_ofset = abs(start_range) if start_range < 0 else 0
    total_pages = len(page_range)
  
    if start_range <0:
        start_range = 0
        stop_range += start_range_ofset
    
    if stop_range > total_pages:
        start_range -= abs(total_pages - stop_range)

    pagination = page_range[start_range:stop_range]
    return {
        'pagination':pagination,
        'current_page':current_page,
        'qty_pages':qty_pages,
        'page_range':page_range,
        'total_pages':total_pages,
        'start_range': start_range,
        'stop_range': stop_range,
        'first_page_out_of_range': current_page > midle_range,
        'last_page_out_of_range': stop_range < total_pages,
    }

def make_pagination(request, queryset, per_page, qty_page=4):
   
    
    try:
        current_page = int(request.GET.get('page', 1))
    except ValueError:
        current_page = 1
    paginator = Paginator(queryset, per_page )
    page_objt = paginator.get_page(current_page)
    pagination_range = make_pagination_range(
        paginator.page_range,
        qty_page,
        current_page
    )

    return page_objt, pagination_range