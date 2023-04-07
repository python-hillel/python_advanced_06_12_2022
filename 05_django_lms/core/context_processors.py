from copy import copy


def get_params(request):
    params = request.GET
    if 'page' in params:
        params = copy(params)
        del params['page']

    return {'params': f'&{params.urlencode()}' if params else ''}
