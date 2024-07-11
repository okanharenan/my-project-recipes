from unittest import TestCase
from utils.recipes.pagination import make_pagination_range 

class PaginationTest(TestCase):

    

    def test_make_pagination_range_returns_a_pagination_range(self):
         #current page = 1 qry pages = 1 midle page = 1

        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qty_pages=4,
            current_page=1,

        )['pagination']

        self.assertEqual([1,2,3,4], pagination)

        #current page = 2 qry pages = 2 midle page = 2
        pagination = make_pagination_range(
            page_range=list(range(1,21)),
            qty_pages=4,
            current_page=2
        )['pagination']

        self.assertEqual([1,2,3,4], pagination)

    

        #current page = 3 qry pages = 2 midle page = 2
        # Here range should change
        pagination = make_pagination_range(
            page_range=list(range(1,21)),
            qty_pages=4,
            current_page=3
        )['pagination']

        self.assertEqual([2,3,4,5], pagination)


    def test_make_sure_ranges_are_correct(self):

        #current page = 10 qty pages = 2 midle page = 2
        # Here range should change
        pagination = make_pagination_range(
                page_range=list(range(1,21)),
                qty_pages=4,
                current_page=10
            )['pagination']

        self.assertEqual([9,10,11,12], pagination)


    def test_make_pagination_range_is_static_when_last_page_is_next(self):

        pagination = make_pagination_range(
            page_range= list(range(1,21)),
            qty_pages=4,
            current_page=20,
        )['pagination']

        self.assertEqual([17,18,19,20], pagination)