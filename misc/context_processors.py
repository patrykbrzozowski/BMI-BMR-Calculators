def add_custom_context(request):
    return {
        'app_name': request.resolver_match.app_name,
        'page_path': request.path,
    }