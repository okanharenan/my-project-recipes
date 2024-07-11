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