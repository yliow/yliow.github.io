def ul(htmls):
    """ returns ul of lists """
    return r'''<ul>
%(lis)s
</ul>
''' % {'lis':''.join(('<li>' + _) for _ in htmls)}
