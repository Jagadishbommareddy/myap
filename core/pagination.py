PAGE_LIMIT = 20

def get_offset(request):
        offset = request.Post.get('offset')
        limit = offset+PAGE_LIMIT
        return offset,limit