---
layout: default
title: Resources
description: Workshop resources
---

- [Python v3.9 documentation](https://docs.python.org/3.9/)
- [pygame documentation](https://www.pygame.org/docs/)
- [repl.it Python (Online python interpreter)](https://repl.it/languages/python3)
- [repl.it PyGame](https://repl.it/languages/pygame)
- [Invent with Python's 'Making Games with Python and Pygame'](https://inventwithpython.com/pygame/)

# Example Code

<ul class="posts">
  {% assign posts_by_author = site.categories.examples | sort: "author" %}
  {% for post in posts_by_author %}
    <li>{{post.author}} » <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>

